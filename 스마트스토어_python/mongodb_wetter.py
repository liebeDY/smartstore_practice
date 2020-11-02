from pymongo import MongoClient 
from pymongo.cursor import CursorType



class MongodbSetting():
    def __init__(self):
        self.host = "localhost" 
        self.port = "27017" 
        self.mongo = MongoClient(self.host, int(self.port)) 
        print()
        print(self.mongo)
        print()


class WetterMongodb(MongodbSetting):
    def __init__(self):
        MongodbSetting.__init__(self)
        self.db = self.mongo['weather_database']
        self.weather_collection = self.db['weather']
        print(self.db)
        print(self.weather_collection)
        print()

    def alldatafind(self):
        self.data_list = []
        for self.data in self.weather_collection.find():
            # print(self.data)
            self.data_list.append(self.data)
        return self.data_list

    def wetterlistsave(self, city, info, temp, temp_min, temp_max):
        
        self.city = city
        self.info = info
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.weather_save_template = {
            "도시":self.city,
            "날씨":self.info,
            "온도":self.temp,
            "최저온도":self.temp_min,
            "최고온도":self.temp_max
        }
        return self.weather_save_template


    def datasave(self, time, data):
        self.time = time
        self.data = data
        self.weather_collection.save({
            "날짜":self.time,
            "일기예보":self.data
        })



a = WetterMongodb()

b = a.alldatafind()
# # weather_collection.save(b)
# # print("b : ", b)
# print()
for idx, result in enumerate(b):
    print(f"{idx}: ",result)
    # print(result['날씨'])
    




