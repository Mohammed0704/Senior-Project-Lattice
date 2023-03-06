import csv
import json
import os
import random

currentDirectory = os.getcwd()

###MUST RUN AFTER THESE TWO FILES ARE GENERATED (Student and Class):
filePathStudent = currentDirectory + "/../mariadb/data_files/MariaDB-basic_student_info.csv"
filePathClass = currentDirectory + "/../mongodb/data_files/MongoDB-class-info.json"

#put class info into different lists for each term
with open(filePathClass) as jsonClass:
  dataClass = json.load(jsonClass)

  #All 6 terms in data (as of early march 2023)
  dataFall22 = []
  dataWinter22 = []
  dataSpring22 = []
  dataSummer22 = []
  dataFall21 = []
  dataWinter21 = []

  #Python 3.10 and later can use switch statements (pattern match)
  for aClass in dataClass:
    match aClass["associated_term"]:
      case "Fall Quarter 22-23":
        dataFall22.append(aClass)
      case "Winter Quarter 22-23":
        dataWinter22.append(aClass)
      case "Spring Quarter 22-23":
        dataSpring22.append(aClass)
      case "Summer Quarter 22-23":
        dataSummer22.append(aClass)
      case "Fall Quarter 21-22":
        dataFall21.append(aClass)
      case "Winter Quarter 21-22":
        dataWinter21.append(aClass)
      case _:
        print("missed: " + aClass) #should never run
  print(dataWinter22)
