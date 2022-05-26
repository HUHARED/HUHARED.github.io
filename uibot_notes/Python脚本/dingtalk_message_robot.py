import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import requests


def send_signed_text_messages(sign, webhook, dingMessage):
    """ 加签方式发送消息 """
    timestamp = str(round(time.time() * 1000))
    UTF8Encodesign = sign.encode('utf-8')
    temp = '{}\n{}'.format(
        timestamp, sign)  # timestamp +换行+sign
    UTF8EncodeTemp = temp.encode('utf-8')
    hmac_code = hmac.new(UTF8Encodesign, UTF8EncodeTemp,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # print(timestamp)
    # print(sign)
    URL = webhook+"&timestamp="+timestamp + "&sign="+sign
    # print(URL)
    dingMessage = json.dumps(dingMessage)
    r = requests.post(URL, data=dingMessage, headers={
                      "Content-Type": "application/json"})
    # print(r.text)
    return r.text


def send_general_text_messages(webhook, dingMessage):
    """ 自定义关键词方式发送消息 """
    URL = webhook
    # print(URL)
    dingMessage = json.dumps(dingMessage)
    r = requests.post(URL, data=dingMessage, headers={
                      "Content-Type": "application/json"})
    # print(r.text)
    return r.text
