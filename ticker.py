import pymysql
import requests

def coinset(market, x) :
    url = f"https://api.upbit.com/v1/ticker?markets={market}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res_json = response.json()
    price = res_json[0]['trade_price']
    conn = pymysql.connect(host='caixi-db.ctcinfc6ligu.ap-northeast-2.rds.amazonaws.com',user='admin',password='',db='coinDB',charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE coinprice SET 현재가=%s WHERE 종목번호=%s"
    cur.execute(sql, (price, x))
    conn.commit()
    conn.close()

coinset("KRW-BTC", 1)
coinset("KRW-ETH", 2)
coinset("KRW-AAVE", 3)
coinset("KRW-SOL", 4)
coinset("KRW-NEO", 5)
coinset("KRW-EGLD", 6)
coinset("KRW-AVAX", 7)
coinset("KRW-LINK", 8)
coinset("KRW-STRK", 9)
coinset("KRW-ATOM", 10)
    