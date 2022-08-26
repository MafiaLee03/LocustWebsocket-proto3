from locust import task
from Core.WebSocketIO import SocketIOUser
import time

class testuser(SocketIOUser):

    @task(3)
    def get_shop_info(self):
        body = {'type':['Shop99'],'opt':0}
        cmd = 'game.RequestGetShopInfo'
        msg = {'cmd':cmd,'body':body}
        # time.sleep(1000000)
        self.send(msg,'获取商店')

    @task(2)
    def use_item_overstep(self):
        body = {'item_id':2032,'item_count':1001}
        cmd = 'game.RequestUseItem'
        msg = {'cmd':cmd,'body':body}
        # time.sleep(1000000)
        self.send(msg,'超出使用道具')
