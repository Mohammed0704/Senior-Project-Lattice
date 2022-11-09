from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import os
import csv

currentDirectory = os.getcwd()

#set up browser to not open and use firefox
options = Options()
options.headless = True
browser1 = webdriver.Firefox(options=options)
browser2 = webdriver.Firefox(options=options)

#counter = 0 ####DELETE

postgres_programs_headers = []
postgres_programs_rows_undergradmajors = []
elasticsearch_programs_headers = []
elasticsearch_programs_rows_undergradmajors = []

#Postgres.education.programs
postgres_programs_headers = ['program_name', 'description', 'is_graduate_program', 'area_of_study', 'credit_requirement', 'is_stem']
program_name = ''
description = ''
is_graduate_program = ''
area_of_study = ''  
credit_requirement = ''
is_stem = ''

#Elasticsearch.drexel_additional_education_info.programs
elasticsearch_programs_headers = ['program_name', 'url', 'calendar_type']
#program_name #getting filled in from above
url = ''
calendar_type = ''

###BEGIN UNDERGRAD MAJOR SCRAPING
browser1.get('https://catalog.drexel.edu/majors/')
print("\nUNDERGRAD MAJORS NOT CAPTURED:") #prints to console any that fail

elemTextContainer = browser1.find_element(By.ID, 'textcontainer')
elemMajors = elemTextContainer.find_elements(By.XPATH, './/p/a')

for p in elemMajors:
    if (p.text == '' or p.get_attribute('href') == None):
        continue
    try:
        browser2.get(p.get_attribute('href')) #follows link to page with a new browser

        elemTextContainer = browser2.find_element(By.ID, 'textcontainer')
        elemInfo = elemTextContainer.find_element(By.XPATH, './/p[1]')
        infoTextBlock = elemInfo.get_attribute('outerHTML') #get block of information in a string var

        #gotta get rid of HTML crap
        infoTextBlock = infoTextBlock.replace("<p>", "")
        infoTextBlock = infoTextBlock.replace("</p>", "")
        infoTextBlock = infoTextBlock.replace("<em>", "")
        infoTextBlock = infoTextBlock.replace("</em>", "")
        infoTextBlock = infoTextBlock.replace("<br>", "")
        infoTextBlock = infoTextBlock.replace("</br>", "")
        infoTextBlock = infoTextBlock.replace("&nbsp;", "")
        infoTextBlock = infoTextBlock.replace('<span class=""course_number"">', "")
        infoTextBlock = infoTextBlock.replace('<span class="tccopy">', "")
        infoTextBlock = infoTextBlock.replace('</span>', '')
        infoList = infoTextBlock.split("\n")
        
        #Need to clean up the data I got
        infoList[0] = p.text.strip().replace('NEW: ', '')
        if (infoList[0].split()[-1][0] == '(' and infoList[0].split()[-1][-1] == ')'):
            infoList[0] = " ".join(infoList[0].split()[:-1]) #get rid of (BS) or w/e at the end of the degree type
        infoList[0] = infoList[0].strip('"')    
        infoList[1] = infoList[1][15:].strip()
        if (infoList[1].split()[-1][0] == '(' and infoList[1].split()[-1][-1] == ')'):
            infoList[1] = " ".join(infoList[1].split()[:-1]) #get rid of (BS) or w/e at the end of the degree type
        infoList[1] = infoList[1].strip('"')    
        infoList[2] = infoList[2][14:].strip()
        infoList[3] = infoList[3][25:].strip()

        program_name = (infoList[1] + " in " + infoList[0].replace('NEW: ', '')).strip('"')
        description = elemTextContainer.find_element(By.XPATH, './/p[2]').text.replace("\n", "  ").strip('"')
        is_graduate_program = False #currently scraping undergrad majors
        area_of_study = ''
        credit_requirement = float(infoList[3])
        if (infoList[1] == 'Bachelor of Science'):
            is_stem = True
        else:
            is_stem = False
        url = p.get_attribute('href')
        calendar_type = infoList[2]

        postgres_programs_rows_undergradmajors.append([program_name, description, is_graduate_program, area_of_study, credit_requirement, is_stem, url, calendar_type])
        elasticsearch_programs_rows_undergradmajors.append([program_name, url, calendar_type])
    except Exception as e:
        print("FAILED ON: " + p.text)

#Postgres.education.programs
with open(currentDirectory + "/Postgres_Data/Postgres-programs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(postgres_programs_headers)         
    csvwriter.writerows(postgres_programs_rows_undergradmajors)

#Elasticsearch.drexel_additional_education_info.programs
with open(currentDirectory + "/Elasticsearch_Data/Elasticsearch-programs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(elasticsearch_programs_headers)         
    csvwriter.writerows(elasticsearch_programs_rows_undergradmajors)      