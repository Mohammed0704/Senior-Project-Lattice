import csv
import os

currentDirectory = os.getcwd()

#Postgres.education.programs
programName = ""
description = ""
isGraduateProgram =""
areaOfStudy = ""
creditRequirement = ""
isSTEM = ""

#Elasticsearch.additional_education_info.programs
programName = ""
URL = ""
programNames = ["test", "test2"]



#Postgres.education.programs
educationProgramHeaders = ["Program Name", "Description", "Is Graduate Program", "Area of Study", "Credit Requirement", "is STEM"]
educationProgramRows = []

educationProgramRows.append([programNames[0], "Students in Drexel’s Bachelor of Science/Bachelor of Arts in Computer Science (BS/BACS) program learn about the theory and practice of effective computing. CS majors tend to be skilled at math and writing code, and like to apply computer science to solve complex computing problems. This accredited degree program in computer science ranked in the top 35 computer science programs (top 15%) in the 2020 nationwide ranking of U.S. Colleges and Universities by College Factual.",
"No", "Computer Science", "TRUE", "186.5"])



#Elasticsearch.additional_education_info.programs
additionalEducationProgramHeaders = ["Program Name", "URL"]
additionalEducationProgramRows = []

additionalEducationProgramHeaders.append([programNames[1], "https://drexel.edu/cci/academics/undergraduate-programs/bsba-computer-science/"])


#Postgres.education.programs
with open(currentDirectory + "/Postgres_Data/Postgres-education_programs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(educationProgramHeaders)         
    csvwriter.writerows(educationProgramRows)

#Elasticsearch.additional_education_info.programs
with open(currentDirectory + "/Elasticsearch_Data/Elasticsearch-additional_education_info_programs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(additionalEducationProgramHeaders)         
    csvwriter.writerows(additionalEducationProgramRows)