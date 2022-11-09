import csv
import os

currentDirectory = os.getcwd()

'''
(Structure)
    Database System:
        Database:
            Table:
                Fields


https://catalog.drexel.edu/colleges/       
Postgres:
    education:
          colleges
                name
                description
                campus
                address
                contact_email
                url
                year_founded
                current_dean
                number_of_departments
                college_ranking
'''

#Postgres.education.colleges
name=""
description=""
campus=""
address=""
contact_email=""
url=""
year_founded=""
current_dean=""
college_ranking=""
number_of_departments=""

collegeHeaders = ["Name", "Description", "Campus", "Address", "Contact Email", "URL", "Year Founded", "Current Dean", "Number Of Departments", "College Ranking"]
collegeRows = []

collegeRows.append(["College of Arts and Sciences", "Here in Drexel's CoAS, we are committed to implementing in-the-moment change, not for personal glory, but because it's what the world needs.",
                            "University City", "3250 Chestnut Street MacAlister Hall, Suite 4020 Philadelphia, PA 19104", "coas@drexel.edu", "https://drexel.edu/coas/",
                            1990, "David S. Brown", 13, "30%"])

collegeRows.append(["LeBow College of Business", "At Drexel LeBow, our rigorous and experience-based business education is custom built for the driven and determined.",
                            "University City", "3220 Market St, Philadelphia, PA 19104", "lcbdeansoffice@drexel.edu", "https://www.lebow.drexel.edu/",
                            1981, "Vibhas Madan", 9, "25%"])

collegeRows.append(["College of Computer & Informatics", "The College of Computing & Informatics is a national leader in information and technology education.",
                            "University City", "3675 Market Street, Philadelphia, PA 19104", "cciinfo@drexel.edu", "https://drexel.edu/cci/",
                            2014, "Yi Deng", 8, "5%"])

collegeRows.append(["College of Engineering", "Since its beginning, engineering has been the cornerstone of Drexel, and our students, faculty and alumni produce robust research, integrate emerging engineering practices and innovate for positive change in our world.",
                            "University City", "3100 Market St, Philadelphia, PA 19104", "coe.outreach@drexel.edu", "https://drexel.edu/engineering/",
                            1892, "Sharon L. Walker", 6, "25%"])

collegeRows.append(["College of Medicine", "The Graduate School's academic programs emphasize real-world experience.",
                            "East Falls", "2900 W Queen Ln, Philadelphia, PA 19129", "medadmis@drexel.edu", "https://drexel.edu/medicine/",
                            1848, "Charles B. Cairns", 20, ""])

collegeRows.append(["College of Nursing and Health Professions", "Going beyond the standard, our curricula emphasize the emerging field of interprofessional care.",
                            "Center City", "1601 Cherry St, Philadelphia, PA 19102", "CNHPIT@drexel.edu", "https://drexel.edu/cnhp/",
                            2002, "Laura N. Gitlin", 10, "35%"])

collegeRows.append(["Goodwin College of Professional Studies", "Drexel's Goodwin College of Professional Studies can find the program that's right for you, around your goals and schedule.",
                            "University City", "3220 Market St #369, Philadelphia, PA 19104", "goodwin@drexel.edu", "https://drexel.edu/goodwin/",
                            1892, "Laura N. Gitlin", 5, ""])

collegeRows.append(["Antoinette Westphal College of Media Arts & Design", "At Drexel's Westphal College of Media Arts & Design we go about teaching design, media, and the performing arts in a different way.",
                            "University City", "URBN Center, 3501 Market St, Philadelphia, PA 19104", "coe.outreach@drexel.edu", "https://drexel.edu/westphal/",
                            1892, "Jason Schupbach", 0, ""])

collegeRows.append(["Pennoni Honors College", "The Pennoni Honors College is a community for all Drexel Dragons, where they are invited to become explorers of the unknown and plot one's own path through conversation, debate, discovery, intellectual curiosity, self-reflection, and more.",
                            "University City", "3250 Chestnut Street, 5016 MacAlister Hall, Philadelphia, PA 19104", "HonorsProgram@drexel.edu", "https://drexel.edu/pennoni/",
                            1991, "Paula Marantz Cohen", 5, ""])
                            
# collegeRows.append(["Biomedical Engineering, Science and Health Systems", "We believe in our mission to educate our students in a culture of scientific discovery and technological innovations.",
#                             "University City", "3141 Chestnut Street Philadelphia, PA 19104", "biomed@drexel.edu", "https://drexel.edu/biomed/",
#                             1961, "David S. Brown", ])


#Postgres.campus_life.locations
print('running')
with open(currentDirectory + "/Postgres_Data/Postgres-colleges.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(collegeHeaders)         
    csvwriter.writerows(collegeRows)