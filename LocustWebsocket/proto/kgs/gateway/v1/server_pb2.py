# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x0ekgs.gateway.v1\"&\n\x16QueryUserStatusRequest\x12\x0c\n\x04uids\x18\x01 \x03(\t\"\xbc\x01\n\x17QueryUserStatusResponse\x12P\n\ruser_statuses\x18\x01 \x03(\x0b\x32\x39.kgs.gateway.v1.QueryUserStatusResponse.UserStatusesEntry\x1aO\n\x11UserStatusesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.kgs.gateway.v1.UserStatus:\x02\x38\x01\"\xd1\x01\n\nUserStatus\x12\x0e\n\x06online\x18\x01 \x01(\x08\x12\x14\n\x0conline_milli\x18\x02 \x01(\x03\x12\x15\n\roffline_milli\x18\x03 \x01(\x03\x12\x12\n\ngateway_id\x18\x04 \x01(\t\x12?\n\x0bservice_ids\x18\x05 \x03(\x0b\x32*.kgs.gateway.v1.UserStatus.ServiceIdsEntry\x1a\x31\n\x0fServiceIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"@\n\x16\x46orwardToClientRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x63md\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\x0c\")\n\x17\x46orwardToClientResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\"\xc3\x01\n\x1b\x42\x61tchForwardToClientRequest\x12K\n\x08requests\x18\x01 \x03(\x0b\x32\x39.kgs.gateway.v1.BatchForwardToClientRequest.RequestsEntry\x1aW\n\rRequestsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.kgs.gateway.v1.ForwardToClientRequest:\x02\x38\x01\"\xa0\x01\n\x1c\x42\x61tchForwardToClientResponse\x12N\n\tresponses\x18\x01 \x03(\x0b\x32;.kgs.gateway.v1.BatchForwardToClientResponse.ResponsesEntry\x1a\x30\n\x0eResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xbe\x01\n\x19SetUserIdleTimeoutRequest\x12\x64\n\x17user_idle_timeout_milli\x18\x01 \x03(\x0b\x32\x43.kgs.gateway.v1.SetUserIdleTimeoutRequest.UserIdleTimeoutMilliEntry\x1a;\n\x19UserIdleTimeoutMilliEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x96\x01\n\x1aSetUserIdleTimeoutResponse\x12H\n\x07results\x18\x01 \x03(\x0b\x32\x37.kgs.gateway.v1.SetUserIdleTimeoutResponse.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xb9\x01\n\x15SetUserServiceRequest\x12N\n\ruser_services\x18\x01 \x03(\x0b\x32\x37.kgs.gateway.v1.SetUserServiceRequest.UserServicesEntry\x1aP\n\x11UserServicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.kgs.gateway.v1.UserService:\x02\x38\x01\"\x8e\x01\n\x16SetUserServiceResponse\x12\x44\n\x07results\x18\x01 \x03(\x0b\x32\x33.kgs.gateway.v1.SetUserServiceResponse.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"S\n\x0bUserService\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x12\n\nservice_id\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\"\x1c\n\x1aQueryConcurrentUserRequest\"1\n\x1bQueryConcurrentUserResponse\x12\x12\n\nuser_count\x18\x01 \x01(\r\";\n\x11\x43\x61llClientRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x63md\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\x0c\"/\n\x12\x43\x61llClientResponse\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x32\xe8\x05\n\nHubService\x12\x64\n\x0fQueryUserStatus\x12&.kgs.gateway.v1.QueryUserStatusRequest\x1a\'.kgs.gateway.v1.QueryUserStatusResponse\"\x00\x12\x64\n\x0f\x46orwardToClient\x12&.kgs.gateway.v1.ForwardToClientRequest\x1a\'.kgs.gateway.v1.ForwardToClientResponse\"\x00\x12s\n\x14\x42\x61tchForwardToClient\x12+.kgs.gateway.v1.BatchForwardToClientRequest\x1a,.kgs.gateway.v1.BatchForwardToClientResponse\"\x00\x12m\n\x12SetUserIdleTimeout\x12).kgs.gateway.v1.SetUserIdleTimeoutRequest\x1a*.kgs.gateway.v1.SetUserIdleTimeoutResponse\"\x00\x12\x61\n\x0eSetUserService\x12%.kgs.gateway.v1.SetUserServiceRequest\x1a&.kgs.gateway.v1.SetUserServiceResponse\"\x00\x12p\n\x13QueryConcurrentUser\x12*.kgs.gateway.v1.QueryConcurrentUserRequest\x1a+.kgs.gateway.v1.QueryConcurrentUserResponse\"\x00\x12U\n\nCallClient\x12!.kgs.gateway.v1.CallClientRequest\x1a\".kgs.gateway.v1.CallClientResponse\"\x00\x42v\n\"com.kingsoft.shiyou.kgs.gateway.v1B\x0bServerProtoP\x01ZAgit.shiyou.kingsoft.com/server/kgs-apis/go/kgs/gateway/v1;gatewayb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.kingsoft.shiyou.kgs.gateway.v1B\013ServerProtoP\001ZAgit.shiyou.kingsoft.com/server/kgs-apis/go/kgs/gateway/v1;gateway'
  _QUERYUSERSTATUSRESPONSE_USERSTATUSESENTRY._options = None
  _QUERYUSERSTATUSRESPONSE_USERSTATUSESENTRY._serialized_options = b'8\001'
  _USERSTATUS_SERVICEIDSENTRY._options = None
  _USERSTATUS_SERVICEIDSENTRY._serialized_options = b'8\001'
  _BATCHFORWARDTOCLIENTREQUEST_REQUESTSENTRY._options = None
  _BATCHFORWARDTOCLIENTREQUEST_REQUESTSENTRY._serialized_options = b'8\001'
  _BATCHFORWARDTOCLIENTRESPONSE_RESPONSESENTRY._options = None
  _BATCHFORWARDTOCLIENTRESPONSE_RESPONSESENTRY._serialized_options = b'8\001'
  _SETUSERIDLETIMEOUTREQUEST_USERIDLETIMEOUTMILLIENTRY._options = None
  _SETUSERIDLETIMEOUTREQUEST_USERIDLETIMEOUTMILLIENTRY._serialized_options = b'8\001'
  _SETUSERIDLETIMEOUTRESPONSE_RESULTSENTRY._options = None
  _SETUSERIDLETIMEOUTRESPONSE_RESULTSENTRY._serialized_options = b'8\001'
  _SETUSERSERVICEREQUEST_USERSERVICESENTRY._options = None
  _SETUSERSERVICEREQUEST_USERSERVICESENTRY._serialized_options = b'8\001'
  _SETUSERSERVICERESPONSE_RESULTSENTRY._options = None
  _SETUSERSERVICERESPONSE_RESULTSENTRY._serialized_options = b'8\001'
  _QUERYUSERSTATUSREQUEST._serialized_start=32
  _QUERYUSERSTATUSREQUEST._serialized_end=70
  _QUERYUSERSTATUSRESPONSE._serialized_start=73
  _QUERYUSERSTATUSRESPONSE._serialized_end=261
  _QUERYUSERSTATUSRESPONSE_USERSTATUSESENTRY._serialized_start=182
  _QUERYUSERSTATUSRESPONSE_USERSTATUSESENTRY._serialized_end=261
  _USERSTATUS._serialized_start=264
  _USERSTATUS._serialized_end=473
  _USERSTATUS_SERVICEIDSENTRY._serialized_start=424
  _USERSTATUS_SERVICEIDSENTRY._serialized_end=473
  _FORWARDTOCLIENTREQUEST._serialized_start=475
  _FORWARDTOCLIENTREQUEST._serialized_end=539
  _FORWARDTOCLIENTRESPONSE._serialized_start=541
  _FORWARDTOCLIENTRESPONSE._serialized_end=582
  _BATCHFORWARDTOCLIENTREQUEST._serialized_start=585
  _BATCHFORWARDTOCLIENTREQUEST._serialized_end=780
  _BATCHFORWARDTOCLIENTREQUEST_REQUESTSENTRY._serialized_start=693
  _BATCHFORWARDTOCLIENTREQUEST_REQUESTSENTRY._serialized_end=780
  _BATCHFORWARDTOCLIENTRESPONSE._serialized_start=783
  _BATCHFORWARDTOCLIENTRESPONSE._serialized_end=943
  _BATCHFORWARDTOCLIENTRESPONSE_RESPONSESENTRY._serialized_start=895
  _BATCHFORWARDTOCLIENTRESPONSE_RESPONSESENTRY._serialized_end=943
  _SETUSERIDLETIMEOUTREQUEST._serialized_start=946
  _SETUSERIDLETIMEOUTREQUEST._serialized_end=1136
  _SETUSERIDLETIMEOUTREQUEST_USERIDLETIMEOUTMILLIENTRY._serialized_start=1077
  _SETUSERIDLETIMEOUTREQUEST_USERIDLETIMEOUTMILLIENTRY._serialized_end=1136
  _SETUSERIDLETIMEOUTRESPONSE._serialized_start=1139
  _SETUSERIDLETIMEOUTRESPONSE._serialized_end=1289
  _SETUSERIDLETIMEOUTRESPONSE_RESULTSENTRY._serialized_start=1243
  _SETUSERIDLETIMEOUTRESPONSE_RESULTSENTRY._serialized_end=1289
  _SETUSERSERVICEREQUEST._serialized_start=1292
  _SETUSERSERVICEREQUEST._serialized_end=1477
  _SETUSERSERVICEREQUEST_USERSERVICESENTRY._serialized_start=1397
  _SETUSERSERVICEREQUEST_USERSERVICESENTRY._serialized_end=1477
  _SETUSERSERVICERESPONSE._serialized_start=1480
  _SETUSERSERVICERESPONSE._serialized_end=1622
  _SETUSERSERVICERESPONSE_RESULTSENTRY._serialized_start=1576
  _SETUSERSERVICERESPONSE_RESULTSENTRY._serialized_end=1622
  _USERSERVICE._serialized_start=1624
  _USERSERVICE._serialized_end=1707
  _QUERYCONCURRENTUSERREQUEST._serialized_start=1709
  _QUERYCONCURRENTUSERREQUEST._serialized_end=1737
  _QUERYCONCURRENTUSERRESPONSE._serialized_start=1739
  _QUERYCONCURRENTUSERRESPONSE._serialized_end=1788
  _CALLCLIENTREQUEST._serialized_start=1790
  _CALLCLIENTREQUEST._serialized_end=1849
  _CALLCLIENTRESPONSE._serialized_start=1851
  _CALLCLIENTRESPONSE._serialized_end=1898
  _HUBSERVICE._serialized_start=1901
  _HUBSERVICE._serialized_end=2645
# @@protoc_insertion_point(module_scope)
