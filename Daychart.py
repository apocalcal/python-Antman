import pymysql
import requests
import json

def coinset(market, x, str) :
    url = f"https://api.upbit.com/v1/candles/days?market={market}&count=32"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res_json = response.json()
    conn = pymysql.connect(host='caixi-db.ctcinfc6ligu.ap-northeast-2.rds.amazonaws.com',user='admin',password='',db='coinDB',charset='utf8')
    cur = conn.cursor()
    for i in range (0, 32) :
        date = res_json[i]['candle_date_time_kst']
        open = res_json[i]['opening_price']
        low = res_json[i]['low_price']
        high = res_json[i]['high_price']
        trade = res_json[i]['trade_price']
        vol = res_json[i]['candle_acc_trade_volume']
        sql = "INSERT INTO Daycoin VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (x, str, date, open, low, high, trade, vol))
    conn.commit()
    conn.close()
    
coinset("KRW-BTC", 1, "비트코인")
coinset("KRW-ETH", 2, "이더리움")
coinset("KRW-AAVE", 3, "에이브")
coinset("KRW-SOL", 4, "솔라나")
coinset("KRW-NEO", 5, "네오")
coinset("KRW-EGLD", 6, "멀티버스엑스")
coinset("KRW-AVAX", 7, "아발란체")
coinset("KRW-LINK", 8, "체인링크")
coinset("KRW-STRK", 9, "스트라이크")
coinset("KRW-ATOM", 10, "코스모스")

   

'''
sql = "CREATE TABLE Daycoin (종목번호 int, 종목이름 char(10), 기준날짜 char(30), 시가 int, 최고가 int, 최저가 int, 종가 int, 거래량 int);"
cur.execute(sql)
'''

