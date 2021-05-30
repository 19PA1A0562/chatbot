import pymongo

client = pymongo.MongoClient("mongodb+srv://MounikaDS143:MounikaDS143@cluster0.d2jfb.mongodb.net/personal?retryWrites=true&w=majority")

database = client["personal"]
collection = database["details"]

class data:
    @classmethod
    def getdata(cls,intent:str) -> str:
        return collection.find_one({f"{intent}" : {'$exists' : 1}})[intent]

