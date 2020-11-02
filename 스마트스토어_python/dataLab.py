import os
import sys
import urllib.request
import json
import pandas as pd 

search_df = pd.DataFrame(columns=('날짜','검색수'))

def startdateSetting():
    startDate = input('시작 날짜를 입력하세요(YYYY.MM.DD) : ')
    startDate = startDate.split('.')
    startDate = '-'.join(startDate)
    return startDate 

def enddateSetting():
    endDate = input('마지막 날짜를 입력하세요(YYYY.MM.DD) : ')
    endDate = endDate.split('.')
    endDate = '-'.join(endDate)
    return endDate 

def timeUnitSetting():
    timeUnit = input('구간 단위를 입력하세요(date : 일간, week : 주간, month : 월간) : ')
    
    try :
        if timeUnit == "d" :
            timeUnit = "date"
            return timeUnit
        elif timeUnit == "w" :
            timeUnit = "week"
            return timeUnit
        elif timeUnit == "m" :
            timeUnit = "month"
            return timeUnit
    
    except :
        print('다시 입력해 주세요')

def groupNameSetting():
    groupName = input('주제어를 입력하세요(groupName) : ')
    return groupName 

def keywordsSetting(number):
    number = int(number)
    keywords = []
    for idx, keyword in enumerate(range(1, number+1)) :
        keyword = input(f'{str(idx+1)} 번째 키워드를 입력하세요 : ')
        keyword = f'\"{keyword}\"'
        keywords.append(keyword)
    text = ','.join(keywords)
    return text 

client_id = "5Nk_Ci8z0DciOuhueii_"
client_secret = "4YOE6MffqF"
url = "https://openapi.naver.com/v1/datalab/search"

idx = 1
startDate = startdateSetting()
endDate = enddateSetting()
timeUnit = timeUnitSetting()
groupName = groupNameSetting()
number = int(input('키워드 갯수를 입력해주세요 : '))
keywords = keywordsSetting(number)


body = f'{{"startDate":"{startDate}","endDate":"{endDate}","timeUnit":"{timeUnit}","keywordGroups":['+f'{{"groupName":"{groupName}","keywords":[{keywords}]}}]'+',"device":"pc","ages":["1","2"],"gender":"f"}'
# print("출력\n",body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_dict = json.loads(response_body.decode('utf-8'))
    results = response_dict['results']
    results_data = results[0]['data']
    results_title = results[0]['title']
    results_keywords = results[0]['keywords']
    for result_data_idx in range(0, len(results_data)) :
        result_data_period = results_data[result_data_idx]['period']
        result_data_ratio = results_data[result_data_idx]['ratio']
        search_df.loc[idx] = [result_data_period, result_data_ratio]
        idx += 1
        print()
        print('검색 주제어 :',results_title)
        print('검색 키워드 :',results_keywords)
        print('날짜 :',result_data_period)
        print('조회수 :',result_data_ratio)
        print()
    print('완료되었습니다.')


else:
    print("Error Code:" + rescode)

print()
search_df.to_csv(f'{results_title}{results_keywords}.csv', encoding='utf-8-sig')
print('저장이 완료되었습니다.')