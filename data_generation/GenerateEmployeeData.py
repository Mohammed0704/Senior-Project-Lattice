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

departmentOptions = ["Biodiversity, Earth & Environmental Science","Biology","Chemistry","Communication",
                       "Criminology & Justice Studies","English & Philosophy","Global Studies and Modern Languages",
                       "History","Mathematics","Physics","Politics","Psychological and Brain Sciences","Sociology",
                       "Chemical and Biological Engineering","Civil, Architectural and Environmental Engineering",
                       "Electrical and Computer Engineering","Engineering Leadership and Society",
                       "Materials Science and Engineering","Mechanical Engineering and Mechanics"]

#we can add more as we go
HighestLevelRoleOptions = ["Program Director", "Deputy Director", "Executive Director", "Research Director"]
HighLevelRoleOptions = ["Dean", "Senior Advisor", "Research Manager", "Professor", "Clinician", "Program Coordinator", "Payroll Administrator", 
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
        role = random.choice(HighLevelRoleOptions)
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

    #Generating departments and making sure roles that aren't tied to one department don't receive one
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

#Manually Appending Employees to Employee Data Object
#David Velinsky
basicEmployeeInfoRows.append(["djv23", "Velinsky", "David", "", "1/24/1973", "David", "He/Him/His", "djv23@drexel.edu", "Biodiversity, Earth & Environmental Science", 
"M", "Single", "Non Hispanic", "White", "123 Main St", "123 Main St", "215-571-4651", "Department Head"])

employeeSalariesRows.append(["djv23", 100500, "1/24/1973", "David Velinsky", "Department Head", 1998, employer, "semi-monthly",
"TRUE", "TRUE", "Included"])

#Mary Katherine Gonder
basicEmployeeInfoRows.append(["mkg62", "Gonder", "Mary", "Katherine", "2/10/1980", "Mary", "She/Her/Hers", "mkg62@drexel.edu", "Biology", 
"F", "Married", "Non Hispanic", "White", "868 Lookout Street", "868 Lookout Street", "215-895-2788", "Department Head"])

employeeSalariesRows.append(["mkg62", 95687, "2/10/1980", "Mary Katherine Gonder", "Department Head", 2005, employer, "semi-monthly",
"TRUE", "FALSE", "Included"])

#Joe Foley
basicEmployeeInfoRows.append(["jpf26", "Foley", "Joe", "", "4/13/1985", "Joe", "He/Him/His", "jpf262@drexel.edu", "Chemistry", 
"M", "Divorced", "Non Hispanic", "White", "64 San Juan Street", "360 Mayfield Lane", "215-895-2639", "Department Head"])

employeeSalariesRows.append(["jpf26", 97870, "4/13/1985", "Joe Foley", "Department Head", 2010, employer, "biweekly",
"FALSE", "FALSE", "Opt Out"])

#Robert Kane
basicEmployeeInfoRows.append(["rjk72", "Kane", "Robert", "", "7/19/1964", "Robert", "He/Him/His", "rjk72@drexel.edu", "Criminology & Justice Studies", 
"M", "Married", "Non Hispanic", "Other", "992 Church Lane", "992 Church Lane", "215-571-4628", "Department Head"])

employeeSalariesRows.append(["rjk72", 102350, "7/19/1964", "Robert Kane", "Department Head", 1999, employer, "semi-monthly",
"FALSE", "TRUE", "Opt Out"])

#Roger Kurtz
basicEmployeeInfoRows.append(["jrk353", "Kurtz", "Roger", "", "9/2/1976", "Roger", "He/Him/His", "jrk353@drexel.edu", "English & Philosophy", 
"M", "Single", "Non Hispanic", "Native", "36 Pearl Road", "36 Pearl Road", "215-895-6911", "Department Head"])

employeeSalariesRows.append(["jrk353", 106790, "9/2/1976", "Roger Kurtz", "Department Head", 2002, employer, "semi-monthly",
"TRUE", "TRUE", "Opt Out"])

#Rebecca Clothey
basicEmployeeInfoRows.append(["rac52", "Clothey", "Rebecca", "", "3/14/1989", "Rebecca", "She/Her/Hers", "rac52@drexel.edu", "Global Studies and Modern Languages", 
"F", "Married", "Hispanic or Latino", "White", "81 Windfall Street", "81 Windfall Street", "215-895-1208", "Department Head"])

employeeSalariesRows.append(["rac52", 86500, "3/14/1989", "Rebecca Clothey", "Department Head", 2009, employer, "semi-monthly",
"FALSE", "TRUE", "Included"])

#Tiago Saraiva
basicEmployeeInfoRows.append(["tfs37", "Saraiva", "Tiago", "", "5/11/1982", "Tiago", "He/Him/His", "tfs37@drexel.edu", "History", 
"M", "Seperated", "Hispanic or Latino", "White", "850 South Peninsula Street", "8344 Lawrence Drive", "	215-895-2463", "Department Head"])

employeeSalariesRows.append(["tfs37", 97800, "5/11/1982", "Tiago Saraiva", "Department Head", 2012, employer, "semi-monthly",
"TRUE", "FALSE", "Included"])

#Brian Daly
basicEmployeeInfoRows.append(["bpd36", "Daly", "Brian", "", "4/2/1972", "Brian", "He/Him/His", "bpd36@drexel.edu", "Psychological and Brain Sciences", 
"M", "Single", "Hispanic or Latino", "White", "222 Harvey Lane", "222 Harvey Lane", "215-895-1895", "Department Head"])

employeeSalariesRows.append(["bpd36", 110500, "4/2/1972", "Brian Daly", "Department Head", 2005, employer, "semi-monthly",
"TRUE", "TRUE", "Included"])

#Steven Weber
basicEmployeeInfoRows.append(["spw26", "Weber", "Steven", "", "11/25/1963", "Steven", "He/Him/His", "spw26@drexel.edu", "Electrical and Computer Engineering", 
"M", "Married", "Non Hispanic", "Other", "7118 Rockwell Street", "7118 Rockwell Street", "215-895-2241", "Department Head"])

employeeSalariesRows.append(["spw26", 98765, "11/25/1963", "Steven Weber", "Department Head", 1994, employer, "biweekly",
"FALSE", "FALSE", "Opt Out"])

#Jonathan E. Spanier
basicEmployeeInfoRows.append(["jes53", "Spanier", "Jonathan", "E.", "8/29/1975", "Jonathan", "He/Him/His", "jes53@drexel.edu", "Mechanical Engineering and Mechanics", 
"M", "Married", "Non Hispanic", "White", "7013 Arrowhead Street", "12 Hilltop Drive", "215-895-2352", "Department Head"])

employeeSalariesRows.append(["jes53", 104876, "8/29/1975", "Jonathan E. Spanier", "Department Head", 1998, employer, "semi-monthly",
"FALSE", "TRUE", "Opt Out"])

#Janitor not assigned to department head
#Dean to only be picked to one department

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