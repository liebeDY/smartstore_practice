import os
import sys
import urllib.request
import pandas as pd
import json
import re

client_id = "5Nk_Ci8z0DciOuhueii_"
client_secret = "4YOE6MffqF"
search = input('검색할 단어를 입력하세요 : ')
encText = urllib.parse.quote(search)

idx = 1
display = 100
start = 1
end = 300

web_df = pd.DataFrame(columns=("상품명", "최저가","최고가","쇼핑몰", "제조사", "브랜드"))

for start_index in range(start, end, display):

    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&start=" + str(start_index)
    # print(url)


    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for item_index in range(0, len(items)) :
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, "", items[item_index]['title'])
            lprice = items[item_index]['lprice']
            hprice = items[item_index]['hprice']
            mallName = items[item_index]['mallName']
            maker = items[item_index]['maker']
            brand = items[item_index]['brand']
            web_df.loc[idx] = [title, lprice, hprice,mallName,maker,brand]
            idx += 1
    else:
        print("Error Code:" + rescode)
web_df.to_csv(f'{search}.csv', encoding='utf-8-sig')
print('저장이 완료되었습니다.')