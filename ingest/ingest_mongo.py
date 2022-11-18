import pymongo
from pymongo import MongoClient, errors
import json
import os

CONNECTIONSTRING = 'mongodb://root:root@localhost:27017'
CURRENTPATH = os.getcwd()

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(CONNECTIONSTRING)

    #create or set current DB to __THE__ DB
    db = client.mongoDB

    #first connection to work with
    connection = db.courses
    
    #retrieve data
    with open(CURRENTPATH + '\data_generation\MongoDB_Data\MongoDB-course-info.json') as file:
      courseInfoData = json.load(file)
    with open(CURRENTPATH + '\data_generation\MongoDB_Data\MongoDB-course-restrictions.json') as file:
      courseReqData = json.load(file)
    #TODO: GET CLASSES-INFO-DATA

    
except errors.ServerSelectionTimeoutError as err:
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)