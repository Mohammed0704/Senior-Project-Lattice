import csv
import os

currentDirectory = os.getcwd()

#Postgres.campus_life.organizations
websiteURL = ''
email = ""
address = ""
phoneNumber = ''
organizationName = ''


campusOrganizationsHeaders = ["Website URL", "Email", "Address", "Phone Number", "Organzation Name"]
campusOrganizationsRows = []

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/8ttb", "8tothebar@gmail.com", "", "", "8 to the Bar"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/alpha-chi-rho", "itb26@drexel.edu", "206 N. 34th Street", "434-825-5008", "Alpha Chi Rho"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/alpha-omega-epsilon", "aoe.drexel.president@gmail.com", "3141 Chestnut Street", "", "Alpha Omega Epsilon"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/anime-and-gaming-organization", "ak3933@drexel.edu", "115 N 32nd St", "410-812-1013", "Anime and Gaming Organization"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/bgsa", "jmc662@drexel.edu", "3245 Chestnut St", "", "Biology Graduate Student Association"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/campus-actitivies-board", "cab@drexel.edu", "30 N. 33rd Street", "215-895-2575", "Campus Activities Board"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/drexel-architectural-engineering-institute", "drexel.aei@gmail.com", "3141 Chestnut Street", "215-895-1502", "Drexel Architectural Engineering Institute"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/drexel_badminton_club", "drexelbc@gmail.com", "3301 Market Street", "", "Drexel Badminton Club"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/formula-sae", "drexel.fsae@gmail.com", "3101 Market St", "", "Formula SAE"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/gsa", "dsogsa@drexel.edu", "3141 Chestnut Street", "954-610-9449", "Graduate Student Association"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/jewish-student-association", "hillel@drexel.edu", "118 N. 34th Street", "215-571-4841", "Jewish Student Association"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/lambda-chi-alpha", "ekz.alpha1@gmail.com", "3401 Powelton Ave", "", "Lambda Chi Alpha"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/nobedrexel", "drexelnobe@outlook.com", "105 N. 33rd Street", "", "National Organization for Business and Engineering - Drexel Chapter"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/phillymaza", "phillymaza@gmail.com", "", "626-722-7652", "Philly Maza"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/sigmapsizeta", "syzardire@gmail.com", "30 N 33rd St", "", "Sigma Psi Zeta Sorority, Inc."])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/sasedrexel", "at3349@drexel.edu", "", "408-483-8008", "Society of Asian Scientists and Engineers: Drexel University Chapter"])

campusOrganizationsRows.append(["https://dragonlink.drexel.edu/organization/zetaphibeta", "kappasigma1920@gmail.com", "3141 Chestnut Street", "", "Zeta Phi Beta Sorority Inc."])


#Postgres.campus_life.locations
with open(currentDirectory + "/data_generation/Postgres_Data/Postgres-organizations.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(campusOrganizationsHeaders)         
    csvwriter.writerows(campusOrganizationsRows)