import csv
import os
import itertools
import random
from datetime import datetime, timedelta

currentDirectory = os.getcwd()

year = 2021
month = random.randint(1, 3)
day = random.randint(1, 28)
hour = random.randint(1,23)
minute = random.randint(1, 59)
second = random.randint(1, 59)
lineDateTime = datetime(year, month, day, hour, minute, second)

#Reading csv file with student data into a list of lists
file = open(currentDirectory + "/../mariadb/data_files/MariaDB-basic_student_info.csv", 'r')
data = list(csv.DictReader(file, delimiter=","))
file.close()

#Initializing each list into a variable, using column headers as index
drexelIDList = [row["Drexel ID"] for row in data]
firstNameList = [row["First Name"] for row in data]
lastNameList = [row["Last Name"] for row in data]

systems = ["Blackboard Learn", "Degree Works", "McGraw-Hill Connect", "Zoom", "PuTTY", "Tux"]

isFirstIteration = True
#Writing to text file, iterating over multiple lists simultaneously
with open(currentDirectory + "/../elasticsearch/data_files/logs/SystemsLogs.txt", "w") as f:
    for line in range(7500):
        randomStudentChoice = random.randint(0, len(drexelIDList) - 1)
        if not isFirstIteration:
            timeAddition = timedelta(hours=random.randint(0,3), minutes=random.randint(1,59), seconds=random.randint(1,59))
            lineDateTime = lineDateTime + timeAddition
        else:
            isFirstIteration = False

        '''
        I wanted to make the string written to the text file variable, so I made it an f string and added
        different usage keywords for Zoom.  Cudos to Mohammed for finding and figuring out itertools.zip_longest,
        very handy and convenient way to utilize all the drexel id's.
        '''
        system = random.choice(systems)
        writeString = ""
        if system == "Zoom":
            accessedThreshold = random.random()
            if accessedThreshold < 0.8:
                writeString = f"[{lineDateTime}] | {firstNameList[randomStudentChoice]} {lastNameList[randomStudentChoice]} | Drexel ID: {drexelIDList[randomStudentChoice]} | accessed | {system}"
            else:
                writeString = f"[{lineDateTime}] | {firstNameList[randomStudentChoice]} {lastNameList[randomStudentChoice]} | Drexel ID: {drexelIDList[randomStudentChoice]} | created-room | {system}"
        else:
            writeString = f"[{lineDateTime}] | {firstNameList[randomStudentChoice]} {lastNameList[randomStudentChoice]} | Drexel ID: {drexelIDList[randomStudentChoice]} | logged-in | {system}"
            
        
        f.write(writeString)
        f.write('\n')
        f.write("---------------------")
        f.write('\n')
f.close()