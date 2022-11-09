import csv
import random
import os
import names
import random_address

currentDirectory = os.getcwd()

#MariaDB.drexel_people.basic_student_info
drexelID = ""
lastName = ""
middleName = ""
firstName = ""
dateOfBirth = ""
email = ""
chosenName = ""
gender = None
expectedGraduationYear = ""
studentProgramType = ""
phone = ""
homeAddress = ""

campusAddressOptions = ["115 N. 32nd Street", "203 N. 34th Street", "223 N. 34th Street", "3301 Race Street", "3200 Race Street", "101 N 34th Street", "3320 Powelton Avenue", 
                            "3301 Arch Street", "3400 Lancaster Avenue", "3200 Chestnut Street"]
studentProgramTypeOptions = ["Undergraduate", "Graduate"]
basicStudentInfoHeaders = ["Drexel ID", "First Name", "Middle Name", "Last Name", "Date of Birth", "Email", "Chosen Name", "Gender", "Expected Graduation Year",
                            "Student Program Type", "Phone", "Home Address"]
basicStudentInfoRows = []

#MariaDB.locations.student_locations
isInternational = False
livingAddress = ""
#drexelID
isCommuter = False
hasParkingPass = False

studentLocationsHeaders = ["Drexel ID", "International", "Living Address", "Commuter", "Has Parking Pass"]
studentLocationsRows = []

#Cassandra.finances.health_insurance
#drexelID
isWaived = False
provider = ""
deductible = 0

providerOptions = ["Cigna", "Aetna", "Humana", "Blue Cross", "Molina Healthcare", "UnitedHealthOne", "MagnaCare"]
deductibleOptions = [200, 500, 1000, 2500, 3000, 5000, 10000]
healthInsuranceHeaders = ["Drexel ID", "Waived", "Provider", "Deductible"]
healthInsuranceRows = []

#Postgres.education.student_education_choices
#drexelID
#firstName
#middleName
#lastName
major = ""
minor = ""

areaOfStudyOptions = [""]
minorOptions = [""]
majorOptions = [""]
studentEducationChoicesHeaders = ["Drexel ID", "First Name", "Middle Name", "Last Name", "Major", "Minor"]
studentEducationChoicesRows = []

#Cassandra.finances.tuition
#drexelID
year = ""
tuitionAndFees = 0.00
annualFinancialAidAward = 0.00
subsidizedLoanOffered = 0.00
unsubsidizedLoanOffered = 0.00
acceptedSubsidized = False
acceptedUnsubsidized = False
outstandingBalances = 0.00

tuitionAndFeesChoices = [58965.00, 52300.00, 48980.00, 60000.00]
annualFinancialAidAwardChoices = [18600.00, 20000.00, 16200.00]
subsidizedLoanOfferedChoices = [5500.00, 3200.00, 4500.00]
unsubsidizedLoanOfferedChoices = [2000.00, 1000.00, 0.00]
tuitionHeaders = ["Drexel ID", "Year", "Tuition And Fees", "Annual Financial Aid Award", "Subsidized Loan Offered", "Unsubsidized Loan Offered",
                    "Accepted Subsidized", "Accepted Unsubsidized", "Outstanding Balances"]
tuitionRows = []

rows = []

for i in range(100):
    #MariaDB.drexel_people.basic_student_info
    genderChance = random.randint(1,2)

    if genderChance == 1:
        gender = 'M'
        firstName = names.get_first_name(gender="male")
        middleName = names.get_first_name(gender="male")
    else:
        gender = 'F'
        firstName = names.get_first_name(gender="female")
        middleName = names.get_first_name(gender="female")
    lastName = names.get_last_name()
    
    unique = False
    while not unique:
        unique = True
        tripleDigitChance = random.randint(1, 100)
        drexelID = (firstName[0] + middleName[0] + lastName[0]).lower() + str(random.randint(10, 99))
        if tripleDigitChance <= 20:
            drexelID = drexelID + str(random.randint(1,9))

        #prevent duplicate IDs
        for row in basicStudentInfoRows:
            if row[0] == drexelID:
                unique = False
    
    email = drexelID + "@drexel.edu"

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

    month = random.randint(1,12)
    day = random.randint(1,28)
    olderStudentChance = random.randint(1,100)
    year = None
    if olderStudentChance <= 2:
        year = random.randint(1982, 1997)
    else:
        year = random.randint(1999, 2004)
    dateOfBirth = str(month) + "/" + str(day) + "/" + str(year)

    studentProgramType = random.choice(studentProgramTypeOptions)

    randomGraduationYearChance = random.randint(1,100)
    if randomGraduationYearChance <= 10 or olderStudentChance <= 3:
        expectedGraduationYear = random.randint(2023, 2027)
    else:
        if year == 1999:
            expectedGraduationYear = 2023
        elif year == 2000:
            expectedGraduationYear = 2024
        elif year == 2001:
            expectedGraduationYear = 2025
        elif year == 2002:
            expectedGraduationYear = 2026
        elif year == 2003:
            expectedGraduationYear = 2027
    
    phone = str(random.randint(200, 989)) + "-" + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))

    campusAddressChance = random.randint(1,100)
    if campusAddressChance <= 50:
        homeAddress = random.choice(campusAddressOptions)
    else:
        homeAddress = random_address.real_random_address_by_state('CA')['address1']

    #MariaDB.locations.student_locations
    internationalChance = random.randint(1,100)
    if internationalChance <= 35:
        isInternational = True
    else:
        isInternational = False

    livingAddress = homeAddress

    if homeAddress in campusAddressOptions:
        isCommuter = False
    else:
        isCommuter = bool(random.getrandbits(1))

    hasParkingPass = bool(random.getrandbits(1))

    #Cassandra.finances.health_insurance
    isWaived = bool(random.getrandbits(1))

    if isWaived:
        provider = random.choice(providerOptions)
    else:
        provider = "Aetna"
    
    deductible = random.choice(deductibleOptions)

    #Postgres.education.student_education_choices
    areaOfStudy = random.choice(areaOfStudyOptions)
    major = random.choice(majorOptions)
    minor = random.choice(minorOptions)

    #Cassandra.finances.tuition
    year = expectedGraduationYear
    tuitionAndFees = random.choice(tuitionAndFeesChoices)
    annualFinancialAidAward = random.choice(annualFinancialAidAwardChoices)
    subsidizedLoanOffered = random.choice(subsidizedLoanOfferedChoices)
    unsubsidizedLoanOffered = random.choice(unsubsidizedLoanOfferedChoices)
    acceptedSubsidized = bool(random.getrandbits(1))
    acceptedUnsubsidized = bool(random.getrandbits(1))
    outstandingBalancesChance = random.randint(1,100)
    if outstandingBalancesChance <= 60:
        outstandingBalances = 0
    elif outstandingBalances >= 61 and outstandingBalances <= 85:
        outstandingBalances = random.uniform(0.01, 25.00)
    else:
        outstandingBalances = random.uniform(25.01, 100.00)
    outstandingBalances = round(outstandingBalances, 2)

    #append current row to be written to CSV later
    basicStudentInfoRows.append([drexelID, firstName, middleName, lastName, dateOfBirth, email, chosenName, gender, expectedGraduationYear, studentProgramType, phone, homeAddress])

    studentLocationsRows.append([drexelID, isInternational, livingAddress, isCommuter, hasParkingPass])

    healthInsuranceRows.append([drexelID, isWaived, provider, deductible])

    studentEducationChoicesRows.append([drexelID, firstName, middleName, lastName, major, minor])

    tuitionRows.append([drexelID, year, tuitionAndFees, annualFinancialAidAward, subsidizedLoanOffered, unsubsidizedLoanOffered, acceptedSubsidized, acceptedUnsubsidized, outstandingBalances])

#MariaDB.drexel_people.basic_student_info
with open(currentDirectory + "/MariaDB_Data/MariaDB-basic_student_info.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(basicStudentInfoHeaders)         
    csvwriter.writerows(basicStudentInfoRows)

#MariaDB.locations.student_locations
with open(currentDirectory + "/MariaDB_Data/MariaDB-student_locations.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(studentLocationsHeaders)         
    csvwriter.writerows(studentLocationsRows)

#Cassandra.finances.health_insurance
with open(currentDirectory + "/Cassandra_Data/Cassandra-health_insurance.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(healthInsuranceHeaders)         
    csvwriter.writerows(healthInsuranceRows)

#Postgres.education.student_education_choices
with open(currentDirectory + "/Postgres_Data/Postgres-student_education_choices.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(studentEducationChoicesHeaders)         
    csvwriter.writerows(studentEducationChoicesRows)

#Cassandra.finances.tuition
with open(currentDirectory + "/Cassandra_Data/Cassandra-tuition.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(tuitionHeaders)         
    csvwriter.writerows(tuitionRows)