import csv
import os
import itertools
import random
from datetime import datetime
from datetime import timedelta

currentDirectory = os.getcwd()

year = 2021
month = random.randint(1, 3)
day = random.randint(1, 28)
hour = random.randint(1,23)
minute = random.randint(1, 59)
second = random.randint(1, 59)
lineDateTime = datetime(year, month, day, hour, minute, second)

#Reading csv file with student data into a list of lists
file = open(currentDirectory + "/MariaDB_Data/MariaDB-basic_student_info.csv", 'r')
data = list(csv.DictReader(file, delimiter=","))
file.close()

#Initializing each list into a variable, using column headers as index
drexelIDList = [row["Drexel ID"] for row in data]
firstNameList = [row["First Name"] for row in data]
lastNameList = [row["Last Name"] for row in data]

isFirstIteration = True
#Writing to text file, iterating over multiple lists simultaneously
#zip_longest stops when all lists are exhausted. When the shorter iterator(s) are exhausted, zip_longest yields a tuple with None value.
with open(currentDirectory + "/Elasticsearch_Data/LibraryLogFile.txt", "w") as f:
    #for (ID, first, last) in itertools.zip_longest(drexelID, firstName, lastName):
    for line in range(8500):
        randomStudentChoice = random.randint(0, len(drexelIDList) - 1)
        if not isFirstIteration:
            timeAddition = timedelta(hours=random.randint(0,3), minutes=random.randint(1,59), seconds=random.randint(1,59))
            lineDateTime = lineDateTime + timeAddition
        else:
            isFirstIteration = False

        f.write("[" + str(lineDateTime) + "]" + " " + "|" + " " + firstNameList[randomStudentChoice] + " " + lastNameList[randomStudentChoice] + " " + "|" + " " 
        + "Drexel ID:" + " " + drexelIDList[randomStudentChoice] + " " + "|" + " " + "scanned in" + " " + "|" + " " + "W. W. Hagerty Library")
        f.write('\n')
        f.write("---------------------")
        f.write('\n')
f.close()





