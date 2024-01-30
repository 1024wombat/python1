import requests
import json
import pprint

url = 'https://zipcloud.ibsnet.co.jp/api/search'

num = input("郵便番号を入力：")

params = {'zipcode':num}

res = requests.get(url, params=params)

data = json.loads(res.text)

pprint.pprint(data['results'][0])
