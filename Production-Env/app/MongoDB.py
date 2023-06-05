# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import variables and packages.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pymongo 
from datetime import datetime, timedelta
from keys_app.Keys import Mongodb_Connection

# 
class MongoDB:
    def __init__(self, cryptocurrency_information):
        self.cryptocurrency_information = cryptocurrency_information

# MongoDB Conection.
    def connect_to_mongodb(self):
        client = pymongo.MongoClient(Mongodb_Connection)
        db = client["My_Currencys_Collection"]
        collection = db["user_search"]
        return collection
    
# Insert data into mongodb collection.
    def insert_currency_data_to_mongodb(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data_upload = {
            'timestamp': current_time,
            'name': self.cryptocurrency_information['name'],
            'price': self.cryptocurrency_information['price'],
            'price_1h' : self.cryptocurrency_information['price_change_1h_percent']
        }

        MongoDB.connect_to_mongodb.insert_one(data_upload)