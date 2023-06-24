import os
import pymongo
import json

with open("env.json")as file:
    myDetails=json.load(file)

passw = myDetails["PASSWORD"]
user = myDetails["USERNAME"]

client = pymongo.MongoClient(f'mongodb+srv://{user}:{passw}@cluster0.b8d55ly.mongodb.net/?retryWrites=true&w=majority')
