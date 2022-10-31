import csv
import random
import names

#MariaDB.drexel_people.basic_student_info
drexelID = ""#
lastName = ""#
middleName = ""#
firstName = ""#
dateOfBirth = None#
email = ""#
chosenName = ""#
gender = None#
expectedGraduationYear = ""#
studentProgramType = ""
phone = ""
homeAddress = ""

studentProgramTypeOptions = ["Undergraduate", "Graduate"]
basicStudentInfoHeaders = ["Drexel ID", "First Name", "Middle Name", "Last Name", "Date of Birth", "Email", "Chosen Name", "Gender", "Expected Graduation Year",
                            "Student Program Type", "Phone", "Home Address"]

rows = []

for row in range(6):
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
    
    tripleDigitChance = random.randint(1, 100)
    drexelID = (firstName[0] + middleName[0] + lastName[0]).lower() + str(random.randint(10, 99))
    if tripleDigitChance <= 20:
        drexelID = drexelID + str(random.randint(1,9))
    
    email = drexelID + "@drexel.edu"

    chosenNameChance = random.randint(1,100)
    if chosenNameChance <= 3:
        if gender == 'M':
            gender = 'F'
            chosenName = names.get_first_name(gender="female")
        else:
            gender = 'M'
            chosenName = names.get_first_name(gender="male")

    month = random.randint(1,12)
    day = random.randint(1,28)
    olderStudentChance = random.randint(1,100)
    year = None
    if olderStudentChance <= 3:
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
    
    
    print(studentProgramType)