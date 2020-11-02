from pymongo import MongoClient 
from pymongo.cursor import CursorType


host = "localhost" 
port = "27017" 
mongo = MongoClient(host, int(port)) 
db = mongo['weather_database']
weather_collection = db['weather']



for result in weather_collection.find():
    # print(result['도시'])
    # print(result['온도'])
    # print(result['날씨'])
    print()
    print(result)
# weather_collection.delete_many({})   #모두 삭제 (조건지정x)