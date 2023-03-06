import csv
import json
import os
import random
import re

#to be run from the Senior-Project-Lattice/lattice_databases/data_generation/ directory

currentDirectory = os.getcwd()

###MUST RUN AFTER THESE TWO FILES ARE GENERATED (Student and Class and Course):
filePathClass = currentDirectory + "/../mongodb/data_files/MongoDB-class-info.json"
filePathStudent = currentDirectory + "/../mariadb/data_files/MariaDB-basic_student_info.csv"
filePathCourse = currentDirectory + "/../mongodb/data_files/MongoDB-course-info.json"
filePathOutput = currentDirectory + "/../cassandra/data_files/Cassandra-registration.csv"

#put class info into different lists for each term
with open(filePathClass, 'r') as jsonClass:
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
        print("missed: " + aClass) #classes marked with terms that arent the above
        
  dataTerms = [dataFall22, dataWinter22, dataSpring22, dataSummer22, dataFall21] #not adding Winter21 b/c of problem, idk 

dataHeaderRegistration = ["crn, student_id"]
dataRowsRegistration = []

with open(filePathCourse, 'r') as jsonCourse:
  dataCourse = json.load(jsonCourse)
  keys = [item["Course Code"] for item in dataCourse] #get every course code
  dataCourse = dict(zip(keys, dataCourse)) #remake into a single dictionary with course code as the keys

with open(filePathStudent, 'r') as csvStudent:
  
  maxCredits = 0 #set to a random number for each student
  termCredits = 0 #updates for each student to track credits
  partTimeChance = 0.07
  regexValidCredits = "^([0-9]+\.?[0-9]?){1}(-{1}[0-9]+\.?[0-9]?)?$"
  regexValidSingleCredits = "^([0-9]+\.?[0-9]?){1}$"
  
  reader = csv.reader(csvStudent)
  next(reader) #skip header row
  for student in reader: #each row corresponds to a student
    for term in dataTerms:
      termCredits = 0 #reset num of credits student is taking
      termRegistration = [] #reset, to be filled w/ new classes
      if (random.random() <= partTimeChance): #7% chance of being part-time student in a term
        fullTime = False
      else:
        fullTime = True
      
      if (fullTime):
        maxCredits = random.randint(12,20) #12 to 20 credits is full-time
      else:
        maxCredits = random.randint(4, 11) #4 to 11 credits is part-time

      while(True): #run till we break out of while loop (WHILE LOOP CHECK is further down)

        #get a class
        regenerate = False
        newClass = random.choice(term)
        
        #error checking first new class
        for termClass in termRegistration:
          if termClass[0] == newClass["crn"]:
            regenerate = True
            break
        if (not regenerate):
          if newClass["associated_course_code"] not in dataCourse.keys():
            regenerate = True #class not in course data
            #print (newClass["associated_course_code"]) #debugging
        if (not regenerate):
          if (not re.search(regexValidCredits, dataCourse[newClass["associated_course_code"]]["Credits"])):
            regenerate = True #credits in course data that we can't deal with rn
            #print(dataCourse[newClass["associated_course_code"]]["Credits"]) #debugging
          else:
            dataCorrCourseCredits = dataCourse[newClass["associated_course_code"]]["Credits"]

        #if first class didn't work, keep going till one does
        while(regenerate):
          #get a class
          regenerate = False
          newClass = random.choice(term)

          #error checking new class again and again
          for termClass in termRegistration:
            if termClass[0] == newClass["crn"]:
              regenerate = True
              break
          if (not regenerate):
            if newClass["associated_course_code"] not in dataCourse.keys():
              regenerate = True #class not in course data
              #print (newClass["associated_course_code"]) #debugging
          if (not regenerate):
            if (not re.search(regexValidCredits, dataCourse[newClass["associated_course_code"]]["Credits"])):
              regenerate = True #credits in course data that we can't deal with rn
              #print(dataCourse[newClass["associated_course_code"]]["Credits"]) #debugging
            else:
              dataCorrCourseCredits = dataCourse[newClass["associated_course_code"]]["Credits"]
        
        ###WHILE LOOP CHECK###
        #first check if is credit num (if) or credit range (else), then check if we should even add it.  if not go to next term, if so then add it
        if (re.search(regexValidSingleCredits, dataCorrCourseCredits)):
          if (termCredits + float(dataCorrCourseCredits) <= maxCredits):
            termCredits += float(dataCorrCourseCredits)
          else: 
            break #move on from registering for this term, break out of while loop
        else:
          creditsLowerBound = dataCorrCourseCredits.split("-")[0]
          creditsUpperBound = dataCorrCourseCredits.split("-")[1]
          tempCredits = random.randint(int(float(creditsLowerBound)), int(float(creditsUpperBound)))
          if(termCredits + tempCredits <= maxCredits):
            termCredits += tempCredits
          else: 
            break #move on from registering for this term, break out of while loop

        termRegistration.append([newClass["crn"], student[0]]) #crn and the student id
      for registration in termRegistration:
        dataRowsRegistration.append([registration[0], registration[1]])

with open(filePathOutput, 'w', newline='') as csvOutput:
  writer = csv.writer(csvOutput)

  writer.writerow(dataHeaderRegistration)
  writer.writerows(dataRowsRegistration)
