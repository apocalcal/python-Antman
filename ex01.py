import requests
import json

def BTC() : 
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res_json = response.json()
    print(res_json[0]['korean_name'],"의 현재가는", res_json[0]['trade_price'])

def ETH() : 
    url = "https://api.upbit.com/v1/ticker?markets=KRW-ETH"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res_json = response.json()
    print(res_json[0]['market'],"의 현재가는", res_json[0]['trade_price'])

BTC()

