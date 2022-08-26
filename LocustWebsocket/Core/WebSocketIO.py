from http import server
import json
import logging
from multiprocessing import Event
import re
import time
import gevent
import websocket
from locust import User
from google.protobuf import json_format
from proto.kgs.gateway.v1 import client_pb2
from Core.HttpManager import getToken
import random
import string
import importlib
import _thread

url = 'ws://10.96.0.54:9000/conn'

CMD_TRANSLATE = {
    'game.ResponseUserLogin':'登录 回包',
    'game.ResponseGetShopInfo':'获取商店 回包',
    '心跳':'心跳'
}
def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

def pb_to_jsonDict(pbStringRequest):
    """将pbstring转化为json格式的dict Response返回"""
    jsonStringRequest=json_format.MessageToDict(pbStringRequest)
    return jsonStringRequest

def jsonDict_to_pb(jsonStringResponse : dict,ProtoBufMessage = client_pb2.RequestForward):
    """将json格式的dict Response转化为pbString返回"""
    pbStringResponse = json_format.ParseDict(jsonStringResponse, ProtoBufMessage())
    return pbStringResponse

def get_path_from_pbMsg(pbPathMsg):
    pbPath = '.'.join(pbPathMsg.split('.')[:-1])
    return pbPath
REGISTER_NAME_LEN = 7 # 随机生成的注册的账号名字长度
REGISTER_PASSWORD = 'a123456' # 注册密码
HTTPURL = ''
# CMD：客户端请求的message路径
CMDPROTOREQ = {
    'game.RequestUserLogin':'proto.game.user_profile_pb2.RequestUserLogin',
    'game.RequestGetShopInfo':'proto.game.user_profile_pb2.RequestGetShopInfo',
    'game.RequestUseItem':'proto.game.user_profile_pb2.RequestUseItem'


}
# CMD：服务器返回的message路径
CMDPROTORSP = {
    'game.ResponseUserLogin':'proto.game.user_profile_pb2.ResponseUserLogin',
    'game.ResponseGetShopInfo':'proto.game.user_profile_pb2.ResponseGetShopInfo',
    'game.NoticeResourceChange':'proto.game.user_profile_pb2.NoticeResourceChange',
    'game.NoticeHeroChange':'proto.game.user_profile_pb2.NoticeHeroChange',
    'game.ResponseUseItem':'proto.game.user_profile_pb2.ResponseUseItem'


}
# 储存请求的CMD和服务器返回的CMD之间的对应关系
REQ_RSP_CMD_MAPPING = {
    'game.RequestUserLogin':'game.ResponseUserLogin',
    'game.RequestGetShopInfo':'game.ResponseGetShopInfo',
    'game.RequestUseItem':'game.ResponseUseItem'
}

def pb_translate(msg):
    current_cmd = msg['cmd']
    current_body = msg['body']
    # current_session = msg['session']
    pb_path_msg = CMDPROTOREQ[current_cmd]
    pb_path = get_path_from_pbMsg(pb_path_msg)
    pb_msg = pb_path_msg.split('.')[-1]
    module = importlib.import_module(pb_path)
    current_body_pb = jsonDict_to_pb(current_body,module.__dict__[pb_msg])
    current_body_byte =current_body_pb.SerializeToString()
    msg_dict = {
        'cmd':current_cmd,
        'body':current_body_byte,
    }
    # session = client_pb2.Session(uid = msg_dict['session']['uid'],ip = msg_dict['session']['ip'],info = msg_dict['session']['info'])
    msg_pb = client_pb2.RequestForward(cmd = msg_dict['cmd'],body = current_body_byte)
    gateway_msg_pb = client_pb2.Request(forward = msg_pb)
    msg_byte = gateway_msg_pb.SerializeToString()
    return msg_byte

class SocketIOUser(User):
    """
    A locust that includes a socket io websocket connection.
    You could easily use this a template for plain WebSockets,
    socket.io just happens to be my use case. You can use multiple
    inheritance to combine this with an HttpUser
    (class MyUser(HttpUser, SocketIOUser)
    """

    abstract = True
    message_regex = re.compile(r"(\d*)(.*)")
    description_regex = re.compile(r"<([0-9]+)>$")

    def __init__(self, environment):
        super().__init__(environment)
        self.host = url
        self.req_cmd = ''
        self.received = False
        self.sent_timestamp = 0
        self.e = Event()
        self.token = ''
        self.count = 0

    def connect(self, host: str, header=[]):
        self.ws = websocket.create_connection(host, header=header)
        gevent.spawn(self.receive_loop)

    def on_message(self, message):  # override this method in your subclass for custom handling
        current_timestamp = time.time()
        messagepb = client_pb2.Response()
        try:
            messagepb.ParseFromString(message)
            msg_dict = pb_to_jsonDict(messagepb)
            print(msg_dict)
        except Exception as e:
            raise Exception('接收消息格式错误:{1}，ParseFromString失败 错误消息：{0}'.format(message,e))
        if msg_dict.get('login') != None:
            if msg_dict.get('login') == {}:
                print('登录gateway成功')
            else:
                print('登录gateway失败!!!错误消息：{}'.format(msg_dict))
                self.ws.close()
        else:
            response_time = 0  # unknown
            # if m is None:
            #     # uh oh...
            #     raise Exception(f"got no matches for {self.message_regex} in {message}")
            cmd = messagepb.forward.cmd
            if cmd == REQ_RSP_CMD_MAPPING[self.req_cmd]:
                body = messagepb.forward.body
                pb_path_msg = CMDPROTORSP[cmd]
                pb_path = get_path_from_pbMsg(pb_path_msg)
                pb_msg = pb_path_msg.split('.')[-1]
                try:
                    module = importlib.import_module(pb_path)
                except Exception as e:
                    raise Exception(e)
                body_pb = module.__dict__[pb_msg]()
                try:
                    body_pb.ParseFromString(body)
                except Exception as e:
                    raise Exception('接收消息中body格式错误:{},ParseFromString失败 错误消息:{}'.format(e,body))
                body_dict = pb_to_jsonDict(body_pb)
                code = body_dict.get('code')
                if cmd in CMD_TRANSLATE.keys():
                    name = CMD_TRANSLATE[cmd]
                else:
                    name = cmd
                if code != None and code != 'SUCCESS': #code 为SUCCESS或者None都视为success
                    self.environment.runner.stats.log_error('response',name,code)
                if cmd != '心跳': # 去掉心跳消息
                    response_time = current_timestamp - self.sent_timestamp
                # print('recv change received True!!!')
                self.received = True
                self.environment.events.request.fire(
                    request_type="response",
                    name=name,
                    response_time=response_time*10000,
                    response_length=len(message),
                    exception=None,
                    context=self.context(),
            )

    def receive_loop(self):
        while True:
            message = self.ws.recv()
            logging.debug(f"response: {message}")
            self.on_message(message)

    def send(self, msg, name=None, context={}):
        # print('received False now!!!')
        self.received = False
        if not name:
            if msg['cmd'] == 30000:
                name = '心跳'
            else:
                name = msg['cmd']
        self.req_cmd = msg['cmd']
        msg_byte = pb_translate(msg) # 把写的json格式dict转pb_byte发出去
        self.environment.events.request.fire(
            request_type="request",
            name=name,
            response_time=None,
            response_length=len(msg),
            exception=None,
            context={**self.context(), **context},
        )
        logging.debug(f"request: {msg}")
        self.sent_timestamp = time.time()
        self.ws.send(msg_byte,opcode = 0x2)
        while not self.received:
            gevent.sleep(0)

    def sleep_with_heartbeat(self, seconds):
        body = {
            'server_id':30000,
            'request':'',
            'uid':time.time(),
            'code':200
            }
        while seconds >= 0:
            gevent.sleep(min(15, seconds))
            seconds -= 15
            self.send(body)

    def gateway_login(self):
        self.connect(self.host)
        sendToken = create_string_number(6)
        self.token = getToken(data = {'token':sendToken,'sdkProvider':''})
        print(self.token)
        RequestLogin = client_pb2.RequestLogin()
        RequestLogin.token = self.token
        Requestmsg = client_pb2.Request(login = RequestLogin)
        self.ws.send(Requestmsg.SerializeToString(),opcode = 0x2)



    def on_start(self):
        # gevent.spawn(self.gateway_login())
        self.gateway_login()