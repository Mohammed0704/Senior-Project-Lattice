import csv
import os
import itertools
import random
from datetime import datetime
from datetime import timedelta

currentDirectory = os.getcwd()

#Reading csv file with student data into a list of lists
file = open(currentDirectory + "/MariaDB_Data/MariaDB-basic_student_info.csv", 'r')
data = list(csv.DictReader(file, delimiter=","))
file.close()

#Initializing each list into a variable, using column headers as index
drexelID = [row["Drexel ID"] for row in data]
firstName = [row["First Name"] for row in data]
lastName = [row["Last Name"] for row in data]

#Writing to text file, iterating over multiple lists simultaneously
#zip_longest stops when all lists are exhausted. When the shorter iterator(s) are exhausted, zip_longest yields a tuple with None value.
with open('LibraryLogFile.txt', 'w') as f:
    for (ID, first, last) in itertools.zip_longest(drexelID, firstName, lastName):
        #Getting the current date and time, incrementing it by random num of seconds and converting it to a string
        dt = datetime.now()
        incrementDT = timedelta(seconds=random.randint(1, 10000000)) 
        randomTime = dt + incrementDT
        strDateTime = randomTime.strftime("%d-%m-%Y %H:%M:%S")

        f.write("[" + strDateTime + "]" + " " + "|" + " " + first + " " + last + " " + "|" + " " 
        + "Drexel ID:" + " " + ID + " " + "|" + " " + "accessed" + " " + "|" + " " + "W. W. Hagerty Library")
        f.write('\n')
        f.write("---------------------")
        f.write('\n')
f.close()





