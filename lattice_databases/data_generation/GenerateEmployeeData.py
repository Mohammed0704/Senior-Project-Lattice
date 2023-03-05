import csv
import json
import random
import os
import names
import random_address

currentDirectory = os.getcwd()

employer = "Drexel University"

#MariaDB.drexel_people.basic_employee_info
basicEmployeeInfoHeaders = ["Drexel ID", "Last Name", "First Name", "Middle Name", "Date of Birth", "Chosen Name",
                            "Personal Pronouns", "Email", "Department", "Gender", "Marital Status", "Ethnicity", 
                            "Race", "Living Address", "Mailing Address", "Phone Number", "Role"] 

personalPronounsOptions = ["She/Her/Hers", "He/Him/His", "They/Them/Theirs"]

maritalStatusOptions = ["Single", "Married", "Divorced", "Widow", "Seperated"]
ethnicityOptions = ["Non Hispanic", "Hispanic or Latino"]
raceOptions = ["African American/Black", "White", "Asian", "Native", "Other"]

departmentOptions = ["Biodiversity, Earth & Environmental Science","Biology","Chemistry","Communication",
                       "Criminology & Justice Studies","English & Philosophy","Global Studies and Modern Languages",
                       "History","Mathematics","Physics","Politics","Psychological and Brain Sciences","Sociology",
                       "Chemical and Biological Engineering","Civil, Architectural and Environmental Engineering",
                       "Electrical and Computer Engineering","Engineering Leadership and Society",
                       "Materials Science and Engineering","Mechanical Engineering and Mechanics"]

#we can add more as we go
HighestLevelRoleOptions = ["Program Director", "Deputy Director", "Executive Director", "Research Director"]
HighLevelRoleOptions = ["Senior Advisor", "Research Manager", "Professor", "Clinician", "Program Coordinator", "Payroll Administrator", 
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

currentEmployeeIDs = []
#Manually Appending Department Heads to Employee Data Object
#David Velinsky
basicEmployeeInfoRows.append(["djv23", "Velinsky", "David", "", "1/24/1973", "David", "He/Him/His", "djv23@drexel.edu", "Biodiversity, Earth & Environmental Science", 
"M", "Single", "Non Hispanic", "White", "123 Main St", "123 Main St", "215-571-4651", "Department Head"])

employeeSalariesRows.append(["djv23", 100500, "1/24/1973", "David Velinsky", "Department Head", 1998, employer, "semi-monthly",
"TRUE", "TRUE", "Included"])
currentEmployeeIDs.append("djv23")

#Mary Katherine Gonder
basicEmployeeInfoRows.append(["mkg62", "Gonder", "Mary", "Katherine", "2/10/1980", "Mary", "She/Her/Hers", "mkg62@drexel.edu", "Biology", 
"F", "Married", "Non Hispanic", "White", "868 Lookout Street", "868 Lookout Street", "215-895-2788", "Department Head"])

employeeSalariesRows.append(["mkg62", 95687, "2/10/1980", "Mary Katherine Gonder", "Department Head", 2005, employer, "semi-monthly",
"TRUE", "FALSE", "Included"])
currentEmployeeIDs.append("mkg62")

#Joe Foley
basicEmployeeInfoRows.append(["jpf26", "Foley", "Joe", "", "4/13/1985", "Joe", "He/Him/His", "jpf262@drexel.edu", "Chemistry", 
"M", "Divorced", "Non Hispanic", "White", "64 San Juan Street", "360 Mayfield Lane", "215-895-2639", "Department Head"])

employeeSalariesRows.append(["jpf26", 97870, "4/13/1985", "Joe Foley", "Department Head", 2010, employer, "biweekly",
"FALSE", "FALSE", "Opt Out"])
currentEmployeeIDs.append("jpf26")

#Robert Kane
basicEmployeeInfoRows.append(["rjk72", "Kane", "Robert", "", "7/19/1964", "Robert", "He/Him/His", "rjk72@drexel.edu", "Criminology & Justice Studies", 
"M", "Married", "Non Hispanic", "Other", "992 Church Lane", "992 Church Lane", "215-571-4628", "Department Head"])

employeeSalariesRows.append(["rjk72", 102350, "7/19/1964", "Robert Kane", "Department Head", 1999, employer, "semi-monthly",
"FALSE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("rjk72")

#Roger Kurtz
basicEmployeeInfoRows.append(["jrk353", "Kurtz", "Roger", "", "9/2/1976", "Roger", "He/Him/His", "jrk353@drexel.edu", "English & Philosophy", 
"M", "Single", "Non Hispanic", "Native", "36 Pearl Road", "36 Pearl Road", "215-895-6911", "Department Head"])

employeeSalariesRows.append(["jrk353", 106790, "9/2/1976", "Roger Kurtz", "Department Head", 2002, employer, "semi-monthly",
"TRUE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("jrk353")

#Rebecca Clothey
basicEmployeeInfoRows.append(["rac52", "Clothey", "Rebecca", "", "3/14/1989", "Rebecca", "She/Her/Hers", "rac52@drexel.edu", "Global Studies and Modern Languages", 
"F", "Married", "Hispanic or Latino", "White", "81 Windfall Street", "81 Windfall Street", "215-895-1208", "Department Head"])

employeeSalariesRows.append(["rac52", 86500, "3/14/1989", "Rebecca Clothey", "Department Head", 2009, employer, "semi-monthly",
"FALSE", "TRUE", "Included"])
currentEmployeeIDs.append("rac52")

#Tiago Saraiva
basicEmployeeInfoRows.append(["tfs37", "Saraiva", "Tiago", "", "5/11/1982", "Tiago", "He/Him/His", "tfs37@drexel.edu", "History", 
"M", "Seperated", "Hispanic or Latino", "White", "850 South Peninsula Street", "8344 Lawrence Drive", "	215-895-2463", "Department Head"])

employeeSalariesRows.append(["tfs37", 97800, "5/11/1982", "Tiago Saraiva", "Department Head", 2012, employer, "semi-monthly",
"TRUE", "FALSE", "Included"])
currentEmployeeIDs.append("tfs37")

#Brian Daly
basicEmployeeInfoRows.append(["bpd36", "Daly", "Brian", "", "4/2/1972", "Brian", "He/Him/His", "bpd36@drexel.edu", "Psychological and Brain Sciences", 
"M", "Single", "Hispanic or Latino", "White", "222 Harvey Lane", "222 Harvey Lane", "215-895-1895", "Department Head"])

employeeSalariesRows.append(["bpd36", 110500, "4/2/1972", "Brian Daly", "Department Head", 2005, employer, "semi-monthly",
"TRUE", "TRUE", "Included"])
currentEmployeeIDs.append("bpd36")

#Steven Weber
basicEmployeeInfoRows.append(["spw26", "Weber", "Steven", "", "11/25/1963", "Steven", "He/Him/His", "spw26@drexel.edu", "Electrical and Computer Engineering", 
"M", "Married", "Non Hispanic", "Other", "7118 Rockwell Street", "7118 Rockwell Street", "215-895-2241", "Department Head"])

employeeSalariesRows.append(["spw26", 98765, "11/25/1963", "Steven Weber", "Department Head", 1994, employer, "biweekly",
"FALSE", "FALSE", "Opt Out"])
currentEmployeeIDs.append("spw26")

#Jonathan E. Spanier
basicEmployeeInfoRows.append(["jes53", "Spanier", "Jonathan", "E.", "8/29/1975", "Jonathan", "He/Him/His", "jes53@drexel.edu", "Mechanical Engineering and Mechanics", 
"M", "Married", "Non Hispanic", "White", "7013 Arrowhead Street", "12 Hilltop Drive", "215-895-2352", "Department Head"])

employeeSalariesRows.append(["jes53", 104876, "8/29/1975", "Jonathan E. Spanier", "Department Head", 1998, employer, "semi-monthly",
"FALSE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("jes53")

#Manually Appending Deans to Employee Data Object
#David S. Brown
basicEmployeeInfoRows.append(["dsb93", "Brown", "David", "S.", "6/15/1951", "David", "He/Him/His", "dsb93@drexel.edu", "Not Applicable", 
"M", "Married", "Non Hispanic", "White", "367 Trace Street", "367 Trace Street", "215-895-1891", "Dean"])

employeeSalariesRows.append(["dsb93", 130600, "6/15/1951", "David S. Brown", "Dean", 2022, employer, "semi-monthly",
"FALSE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("dsb93")

#Yi Deng
basicEmployeeInfoRows.append(["yd362", "Deng", "Yi", "", "2/20/1950", "Yi", "He/Him/His", "yd362@drexel.edu", "Not Applicable", 
"M", "Married", "Non Hispanic", "Asian", "4560 Pratt Street", "4560 Pratt Street", "215-895-2474", "Dean"])

employeeSalariesRows.append(["yd362", 150800, "2/20/1950", "Yi Deng", "Dean", 2016, employer, "semi-monthly",
"TRUE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("yd362")

#Laura N. Gitlin
basicEmployeeInfoRows.append(["lng45", "Gitlin", "Laura", "N.", "5/25/1952", "Laura", "She/Her/Hers", "lng45@drexel.edu", "Not Applicable", 
"F", "Married", "Non Hispanic", "White", "235 Wyoming Avenue", "235 Wyoming Avenue", "215-895-3654", "Dean"])

employeeSalariesRows.append(["yd362", 141000, "2/20/1950", "Laura N. Gitlin", "Dean", 2018, employer, "semi-monthly",
"TRUE", "FALSE", "Included"])
currentEmployeeIDs.append("lng45")

#Sharon Walker
basicEmployeeInfoRows.append(["slw384", "Walker", "Sharon", "L.", "4/21/1960", "Sharon", "She/Her/Hers", "slw384@drexel.edu", "Not Applicable", 
"F", "Single", "Non Hispanic", "White", "4013 Castor Avenue", "230 Blane Street", "215-895-2210", "Dean"])

employeeSalariesRows.append(["slw384", 139560, "4/21/1960", "Sharon L. Walker", "Dean", 2014, employer, "semi-monthly",
"FALSE", "FALSE", "Included"])
currentEmployeeIDs.append("slw384")

#Vibhas Madan
basicEmployeeInfoRows.append(["vm238", "Madan", "Vibhas", "", "12/4/1954", "Vibhas", "He/Him/His", "vm238@drexel.edu", "Not Applicable", 
"M", "Single", "Non Hispanic", "Other", "512 Racket Street", "512  Racket Street", "215-895-2124", "Dean"])

employeeSalariesRows.append(["vm238", 145790, "12/4/1954", "Vibhas Madan", "Dean", 2013, employer, "semi-monthly",
"TRUE", "TRUE", "Opt Out"])
currentEmployeeIDs.append("vm238")

#Charles B. Cairns
basicEmployeeInfoRows.append(["cbc39", "Cairns", "Charles", "B.", "10/18/1972", "Charles", "He/Him/His", "cbc39@drexel.edu", "Not Applicable", 
"M", "Divorced", "Non Hispanic", "White", "680 Pine Street", "680 Pine Street", "215-762-3500", "Dean"])

employeeSalariesRows.append(["cbc39", 138460, "10/18/1972", "Charles B. Cairns", "Dean", 2019, employer, "semi-monthly",
"FALSE", "TRUE", "Included"])
currentEmployeeIDs.append("cbc39")

#Jason Schupbach
basicEmployeeInfoRows.append(["jss422", "Schupbach", "Jason ", "", "6/24/1978", "Charles", "He/Him/His", "jss422@drexel.edu", "Not Applicable", 
"M", "Single", "Non Hispanic", "White", "882 Fletcher Road", "882 Fletcher Road", "215-762-3500", "Dean"])

employeeSalariesRows.append(["jss422", 129220, "6/24/1978", "Jason Schupbach", "Dean", 2020, employer, "semi-monthly",
"FALSE", "FALSE", "Included"])
currentEmployeeIDs.append("jss422")

#Paula Marantz Cohen
basicEmployeeInfoRows.append(["pmc49", "Cohen", "Paula", "Marantz", "7/30/1953", "Paula", "She/Her/Hers", "pmc49@drexel.edu", "Not Applicable", 
"F", "Married", "Non Hispanic", "White", "211 Trat Street", "5016 MacAlister Hall", "215-895-1266", "Dean"])

employeeSalariesRows.append(["pmc49", 145000, "7/30/1953", "Paula Marantz Cohen", "Dean", 2012, employer, "semi-monthly",
"TRUE", "FALSE", "Opt Out"])
currentEmployeeIDs.append("pmc49")

#Donna Marie De Carolis
basicEmployeeInfoRows.append(["dmd33", "de Carolis", "Donna", "", "8/29/1955", "Donna", "She/Her/Hers", "dmd33@drexel.edu", "Not Applicable", 
"F", "Married", "Non Hispanic", "White", "2018 Capper Avenue", "2018 Capper Avenue", "215-895-1795", "Dean"])

employeeSalariesRows.append(["dmd33", 155000, "8/29/1955", "Donna de Carolis", "Dean", 2015, employer, "semi-monthly",
"TRUE", "FALSE", "Opt Out"])
currentEmployeeIDs.append("dmd33")

#Ana V. Diez Roux
basicEmployeeInfoRows.append(["avd37", "Diez Roux", "Ana", "V.", "6/1/1964", "Ana", "She/Her/Hers", "avd37@drexel.edu", "Not Applicable", 
"F", "Single", "Non Hispanic", "White", "540 Frank Street", "4017 Ontario Avenue", "267-359-6070", "Dean"])

employeeSalariesRows.append(["avd37", 145000, "6/1/1964", "Ana V. Diez Roux", "Dean", 2009, employer, "semi-monthly",
"TRUE", "FALSE", "Opt Out"])
currentEmployeeIDs.append("avd37")

#Daniel M. Filler
basicEmployeeInfoRows.append(["dmf24", "Filler", "Daniel", "M.", "5/10/1958", "Daniel", "He/Him/His", "dmf24@drexel.edu", "Not Applicable", 
"M", "Married", "Non Hispanic", "White", "410 Stoke Street", "410 Stoke Street", "215-571-4705", "Dean"])

employeeSalariesRows.append(["dmf24", 133290, "5/10/1958", "Daniel M. Filler", "Dean", 2017, employer, "semi-monthly",
"TRUE", "TRUE", "Included"])
currentEmployeeIDs.append("dmf24")

#Janitor not assigned to department head
#Dean to only be picked to one department

#Assign instructors as employees based on classes
classInfoJSONFile = open(currentDirectory + "/../mongodb/data_files/MongoDB-class-info.json")
classInfoData = json.load(classInfoJSONFile)

def GenerateEmployeeInfo(isInstructor, currentEmployeeIDs, instructorFullName=None, instructorCourse=None):
    #NOTE: For some reason, the variables below that used to be global no longer are able to be referenced... yet somehow the global lists are. Due to that, the variables were moved here
    #MariaDB.drexel_people.basic_employee_info
    drexelID = ""
    lastName = ""
    firstName = ""
    middleName = ""
    dateOfBirth = ""
    chosenName = ""
    personalPronouns = ""
    email = ""
    department = ""
    gender = ""
    maritalStatus = ""
    ethnicity = ""
    race = ""
    livingAddress = ""
    mailingAddress  = ""
    phoneNumber = ""
    role = ""

    #Cassandra.finances.employee_salaries
    #drexelID = ""
    annualSalary = ""
    #dateOfBirth = ""
    fullName = ""
    #jobTitle = ""
    yearBeganWork = ""
    employer = "Drexel University"
    timeReportingPeriod = ""
    isDirectDepositEnabled = ""
    w2ElectronicConsent = ""
    turboTaxOptOut = ""
    
    if not isInstructor:
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
    else:
        fullName = instructorFullName
        fullNameSplit = fullName.split(" ")
        firstName = fullNameSplit[0]
        if len(fullNameSplit) == 3:
            middleName = fullNameSplit[1]
            lastName = fullNameSplit[2]
        else:
            lastName = fullNameSplit[1]

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
        if not middleName == "":
            drexelID = (firstName[0] + middleName[0] + lastName[0]).lower() + str(random.randint(10, 99))
            if tripleDigitChance <= 20:
                drexelID = drexelID + str(random.randint(1,9))
        else:
            drexelID = (firstName[0] + lastName[0]).lower() + str(random.randint(10, 99))
            drexelID = drexelID + str(random.randint(1,9))

        #prevent duplicate IDs
        if drexelID in currentEmployeeIDs:
            unique = False

    currentEmployeeIDs.append(drexelID)
    
    #Generate Email
    email = drexelID + "@drexel.edu"

    #Generate Chosen Name
    if not isInstructor:
        chosenNameChance = random.randint(1,100)
        if chosenNameChance <= 3:
            theyThemPronounsChance = random.randint(1,2)
            if gender == 'M':
                gender = 'F'
                chosenName = names.get_first_name(gender="female")
                if theyThemPronounsChance == 1:
                    personalPronouns = personalPronounsOptions[0]
                else:
                    personalPronouns = personalPronounsOptions[2]
            else:
                gender = 'M'
                chosenName = names.get_first_name(gender="male")
                if theyThemPronounsChance == 1:
                    personalPronouns = personalPronounsOptions[1]
                else:
                    personalPronouns = personalPronounsOptions[2]
        else:
            chosenName = firstName
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
    if not isInstructor:
        randomRoleChance = random.randint(1, 100)
        if randomRoleChance <= 20:
            role = random.choice(LowLevelRoleOptions)
            annualSalary = random.randint(26790, 49200)
        elif 21 <= randomRoleChance <= 50:
            role = random.choice(MediumLevelRoleOptions)
            annualSalary = random.randint(53680, 75100)
        elif 51 <= randomRoleChance <= 95:
            role = random.choice(HighLevelRoleOptions)
            annualSalary = random.randint(81940, 112790)
        else:
            role = random.choice(HighestLevelRoleOptions)
            annualSalary = random.randint(124320, 194770)
    else:
        role = "Professor"
        annualSalary = random.randint(81940, 112790)

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

    #Generating departments and making sure roles that aren't tied to one department don't receive one
    if isInstructor:
        for departmentOption in departmentOptions:
            if instructorCourse in departmentOption:
                department = departmentOption

    if department == "":
        if role == "Janitor" or role == "Dean" or role == "Drexel Central Coordinator" or role == "Financial Aid Officer" or role == "Public Safety Officer":
            department = "" 
        else:
            department = random.choice(departmentOptions)
    
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

instructorsAddedAsEmployee = []
for row in classInfoData:
    instructors = row["instructor"].split(", ")
    instructors = list(set(instructors))
    course = row["associated_course_code"].split(" ")[0]
    for instructor in instructors:
        if instructor in instructorsAddedAsEmployee:
            continue
        else:
            if not instructor.lower() == "staff":
                instructorsAddedAsEmployee.append(instructor)
                GenerateEmployeeInfo(True, currentEmployeeIDs, instructor, course)

for i in range(1200):
    GenerateEmployeeInfo(False, currentEmployeeIDs)

#MariaDB.drexel_people.basic_employee_info
with open(currentDirectory + "/../mariadb/data_files/MariaDB-basic_employee_info.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(basicEmployeeInfoHeaders)         
    csvwriter.writerows(basicEmployeeInfoRows)

#Cassandra.finances.employee_salaries
with open(currentDirectory + "/../cassandra/data_files/Cassandra-employee_salaries.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(employeeSalariesHeaders)       
    csvwriter.writerows(employeeSalariesRows)