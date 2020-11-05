import requests
import json
from .mytoken import token


def getCoordinate(DATA_STREAM='GPS'):
    PRODUCT_ID = '293928'
    ACCESS_KEY = 'ekLpu0QDwN3SFBJ8kxvO3uvYEsiO09L7NEQWQ1FXslE='
    DEVICE_ID = "587179118"

    url = 'https://api.heclouds.com/devices/'+DEVICE_ID+'/datapoints'
    token_str = token(PRODUCT_ID, ACCESS_KEY)
    headers = {"Authorization" : token_str}
    parameter = {"datastream_id" : DATA_STREAM} # 设置URL参数， 可多个

    res = requests.get(url, headers=headers, params=parameter)
    data = json.loads(res.text) #读取json数据
    print(res.text)
    longitude = data['data']['datastreams'][0]['datapoints'][0]['value']['lon']
    latitude = data['data']['datastreams'][0]['datapoints'][0]['value']['lat']
    # lo2 = data['data']['datastreams'][0]['datapoints'][1]['value']['lon']
    # print(lo2)
    return longitude, latitude

if __name__ == '__main__':
    print(getCoordinate())
