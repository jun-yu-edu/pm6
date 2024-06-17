import requests
from pprint import pprint

# 단, 보안의 문제로 https 가 불가능하니 http 로 변경해서 사용
URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
response = requests.get(URL)

data = response.json()

# pprint(data.get('response').get('body').get('items'))
data = data.get('response').get('body').get('items')

# pprint(data)

for datum in data:
    if datum.get('stationName') == '강변북로':
        print(datum)


for datum in data:
    if datum.get('stationName') == '성북구':
        print(datum)