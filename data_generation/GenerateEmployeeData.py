import csv
import random
import os
import names
import random_address

currentDirectory = os.getcwd()

#MariaDB.drexel_people.basic_employee_info
drexelID = ""#
lastName = ""#
firstName = ""#
middleName = ""#
dateOfBirth = ""#
chosenName = ""#
personalPronouns = ""#
email = ""#
department = "" #Will need to include same Drexel departments (leave blank for now)
gender = ""#
maritalStatus = ""#
ethnicity = ""#
race = ""#
livingAddress = ""#
mailingAddress  = ""#
phoneNumber = ""#
role = ""#

#Cassandra.finances.employee_salaries
#drexelID = ""
annualSalary = ""#
#dateOfBirth = ""
fullName = ""#
#jobTitle = ""
yearBeganWork = ""
employer = "Drexel University"
timeReportingPeriod = ""#
isDirectDepositEnabled = ""#
w2ElectronicConsent = ""#
turboTaxOptOut = ""#


#MariaDB.drexel_people.basic_employee_info
basicEmployeeInfoHeaders = ["Drexel ID", "Last Name", "First Name", "Middle Name", "Date of Birth", "Chosen Name",
                            "Personal Pronouns", "Email", "Department", "Gender", "Marital Status", "Ethnicity", 
                            "Race", "Living Address", "Mailing Address", "Phone Number", "Role"] 

personalPronounsOptions = ["She/Her/Hers", "He/Him/His", "They/Them/Theirs"]

maritalStatusOptions = ["Single", "Married", "Divorced", "Widow", "Seperated"]
ethnicityOptions = ["Non Hispanic", "Hispanic or Latino"]
raceOptions = ["African American/Black", "White", "Asian", "Native", "Other"]

#we can add more as we go
HighestLevelRoleOptions = ["Program Director", "Deputy Director", "Executive Director", "Research Director"]
HighLevelRoleOptions = ["Department Head", "Dean", "Senior Advisor", "Research Manager",  "Professor", "Clinician", "Program Coordinator", "Payroll Administrator", 
                        "Research Professor", "Adjunct Instructor", "Finance Coordinator"]
MediumLevelRoleOptions = ["Administrative Coordinator", "Academic Advisor", "Financial Aid Officer", "Research Coordinator", "Accountant", "Software Engineer",
                            "Systems Analyst", "Human Resources", "Talent Acquistion Consultant", "Psychologist", "Designer", "Assistant Professor", "Drexel Central Coordinator"]
LowLevelRoleOptions = ["Janitor", "Public Safety Officer", "Event Services Specialist", "Science Librarian", "Learning Specialist", "Technician", "Reference Librarian", "Receptionist/Scheduler"]


basicEmployeeInfoRows = []

#Cassandra.finances.employee_salaries
employeeSalariesHeaders = ["Drexel ID", "Annual Salary", "Date of Birth", "Full Name", "Job Title", "Year Started",
                            "Employer", "Time Reporting Period", "Direct Deposit", "Electronic W2 Form", "Turbo Tax Option"]

timeReportingPeriodOptions = ["biweekly", "semi-monthly"]
turboTaxOptOutOptions = ["Included", "Opt Out"]

employeeSalariesRows = [] 

for i in range(100):
    #MariaDB.drexel_people.basic_employee_info
    genderChance = random.randint(1,2)

    #Generate Name and Personal Pronouns based on gender
    if genderChance == 1:
        gender = 'M'
        firstName = names.get_first_name(gender="male")
        middleName = names.get_first_name(gender="male")
        personalPronouns = personalPronounsOptions[1]
    else:
        gender = 'F'
        firstName = names.get_first_name(gender="female")
        middleName = names.get_first_name(gender="female")
        personalPronouns = personalPronounsOptions[0]
    lastName = names.get_last_name()

    #Generate Full Name
    fullName = firstName + " " + middleName + " " + lastName

    #Generate Marital Status
    maritalStatus = random.choice(maritalStatusOptions)

    #Generate Race
    race = random.choice(raceOptions)

    #Generate Ethnicity (Trying to make it make sense relative to their race)
    if race == raceOptions[1] or race == raceOptions[4]:
        ethnicity = random.choice(ethnicityOptions)
    else:
        ethnicityChance = random.randint(1, 100)
        if ethnicityChance <= 20:
            ethnicity = ethnicityOptions[1]
        else:
             ethnicity = ethnicityOptions[0]

    #Generate Drexel ID
    unique = False
    while not unique:
        unique = True
        tripleDigitChance = random.randint(1, 100)
        drexelID = (firstName[0] + middleName[0] + lastName[0]).lower() + str(random.randint(10, 99))
        if tripleDigitChance <= 20:
            drexelID = drexelID + str(random.randint(1,9))

        #prevent duplicate IDs
        for row in basicEmployeeInfoRows:
            if row[0] == drexelID:
                unique = False
    
    #Generate Email
    email = drexelID + "@drexel.edu"

    #Generate Chosen Name
    chosenNameChance = random.randint(1,100)
    if chosenNameChance <= 3:
        if gender == 'M':
            gender = 'F'
            chosenName = names.get_first_name(gender="female")
        else:
            gender = 'M'
            chosenName = names.get_first_name(gender="male")
    else:
        chosenName = firstName

    #Generate Date of Birth and Year Began Work (making sure that the year began work makes sense relative to when they were born)
    month = random.randint(1,12)
    day = random.randint(1,28)
    olderEmployeeChance = random.randint(1,3)
    year = None
    if olderEmployeeChance <= 2:
        year = random.randint(1950, 1980)
        yearBeganWork = year + random.randint(20, 40)
    else:
        year = random.randint(1981, 1995)
        yearBeganWork = year + random.randint(20, 27)
    
    dateOfBirth = str(month) + "/" + str(day) + "/" + str(year)

    #Generate Phone Number
    phoneNumber = str(random.randint(200, 989)) + "-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))

    #Generating Role/Job Title amd Annual Salary (salary to make sense based off role)
    randomRoleChance = random.randint(1, 100)
    if randomRoleChance <= 20:
        role = random.choice(LowLevelRoleOptions)
        annualSalary = random.randint(26790, 49200)
    elif 21 <= randomRoleChance <= 50:
        role = random.choice(MediumLevelRoleOptions)
        annualSalary = random.randint(53680, 75100)
    elif 51 <= randomRoleChance <= 95:
        role = random.choice(MediumLevelRoleOptions)
        annualSalary = random.randint(81940, 112790)
    else:
        role = random.choice(HighestLevelRoleOptions)
        annualSalary = random.randint(124320, 194770)

    #Generate Living and Mailing Addresses
    livingAddress = random_address.real_random_address_by_state('CA')['address1']

    #Chances for mailing address to be same as living address or different
    mailingAddressChance = random.randint(1, 100)
    if mailingAddressChance >= 30:
        mailingAddress = livingAddress
    else:
        mailingAddress = random_address.real_random_address_by_state('CA')['address1']

    #Generating Other Employee Salaries Stuff
    timeReportingPeriod = random.choice(timeReportingPeriodOptions)

    turboTaxOptOut = random.choice(turboTaxOptOutOptions)

    #Using two different ramdomChance to get different data for each
    randomChanceDeposit = random.randint(1, 2)
    if randomChanceDeposit == 1:
        isDirectDepositEnabled = True
    else: 
        isDirectDepositEnabled = False

    randomChanceConsent = random.randint(1, 2)
    if randomChanceConsent == 1:
        w2ElectronicConsent = True
    else:
        w2ElectronicConsent = False

    #append current row to be written to CSV later
    basicEmployeeInfoRows.append([drexelID, lastName, firstName, middleName, dateOfBirth, chosenName, personalPronouns, email, department, 
    gender, maritalStatus, ethnicity, race, livingAddress, mailingAddress, phoneNumber, role])

    employeeSalariesRows.append([drexelID, annualSalary, dateOfBirth, fullName, role, yearBeganWork, employer, timeReportingPeriod,
    isDirectDepositEnabled, w2ElectronicConsent, turboTaxOptOut])

#MariaDB.drexel_people.basic_employee_info
with open(currentDirectory + "/MariaDB_Data/MariaDB-basic_employee_info.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(basicEmployeeInfoHeaders)         
    csvwriter.writerows(basicEmployeeInfoRows)

#Cassandra.finances.employee_salaries
with open(currentDirectory + "/Cassandra_Data/Cassandra-employee_salaries.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(employeeSalariesHeaders)       
    csvwriter.writerows(employeeSalariesRows)