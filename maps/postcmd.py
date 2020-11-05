import requests
import json
from .mytoken import token

def sendCmd(payload):
    PRODUCT_ID = '293928'
    ACCESS_KEY = 'ekLpu0QDwN3SFBJ8kxvO3uvYEsiO09L7NEQWQ1FXslE='
    DEVICE_ID = "587179118"
    token_str = token(PRODUCT_ID, ACCESS_KEY)

    url = "http://api.heclouds.com/v1/synccmds?device_id=587179118&timeout=30"
    headers = {"Authorization" : token_str}
    parameter = {"device_id" : DEVICE_ID, "timeout" : "5"}


    res = requests.post(url, data=payload, headers = headers)
    print(res.text)


if __name__ == '__main__':
    sendCmd(payload = "beep:0")

