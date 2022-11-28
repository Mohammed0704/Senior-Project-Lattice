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

  #drop databases, ensures no duplicate data entry
  dbList = client.list_database_names()
  if 'courses' in dbList:
    client.drop_database('courses')
  if 'classes' in dbList:
    client.drop_database('classes')

  #set up DBs ('AKA schemas in the req doc')
  coursesDB = client.courses
  classesDB = client.classes

  #set up collections ('tables')
  coursesInfoColl = coursesDB.courses_info
  coursesReqsColl = coursesDB.courses_requirements
  classesInfoColl = classesDB.classes_info
  classesInstrInfoColl = classesDB.classes_instruction_info
  classesSoftwareColl = classesDB.software
  
  #retrieve data
  with open(CURRENTPATH + '\data_generation\MongoDB_Data\MongoDB-course-info.json') as file:
    courseInfoData = json.load(file)
  with open(CURRENTPATH + '\data_generation\MongoDB_Data\MongoDB-course-restrictions.json') as file:
    courseReqData = json.load(file)
  #TODO: GET CLASSES-INFO-DATA
  #TODO: GET CLASSES-INSTRUCTION-INFO-DATA 
  with open(CURRENTPATH + '\data_generation\MongoDB_Data\MongoDB-software.json') as file:
    softwareData = json.load(file) 

  coursesInfoColl.insert_many(courseInfoData)
  coursesReqsColl.insert_many(courseReqData)
  #TODO: INSERT CLASSES-INFO-DATA
  #TODO: INSERT CLASSES-INSTRUCTION-INFO-DATA
  classesSoftwareColl.insert_many(softwareData)
except errors.PyMongoError as err:
    # catch pymongo errors
    print ("pymongo ERROR: ", err)
except Exception as err:
    print('Exception: ', err)