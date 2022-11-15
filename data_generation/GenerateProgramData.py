from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import os
import csv
import re

currentDirectory = os.getcwd()

#set up browser to not open and use firefox
options = Options()
options.headless = True
browser1 = webdriver.Firefox(options=options)
browser2 = webdriver.Firefox(options=options)

postgres_programs_headers = []
postgres_programs_rows = []
elasticsearch_programs_headers = []
elasticsearch_programs_rows = []

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
elemPrograms = elemTextContainer.find_elements(By.XPATH, './/p/a')

for p in elemPrograms:
    if (p.text == '' or p.get_attribute('href') == None):
        continue
    try:
        browser2.get(p.get_attribute('href')) #follows link to page with a new browser, necessary to open a new one

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

        postgres_programs_rows.append([program_name, description, is_graduate_program, area_of_study, credit_requirement, is_stem, url, calendar_type])
        elasticsearch_programs_rows.append([program_name, url, calendar_type])
    except Exception:
        print("FAILED ON: " + p.text)
###END UNDERGRAD MAJOR SCRAPING

###BEGIN UNDERGRAD MINOR SCRAPING
browser1.get('https://catalog.drexel.edu/minors/undergraduate/')
print('\nUNDERGRAD MINORS NOT CAPTURED:')

elemTextContainer = browser1.find_element(By.ID, 'textcontainer')
elemPrograms = elemTextContainer.find_elements(By.XPATH, './/p/a')

for p in elemPrograms:
    if (p.text == '' or p.get_attribute('href') == None):
        continue
    try:
        browser2.get(p.get_attribute('href')) #follows link to page with a new browser, necessary to open a new one

        program_name = 'Minor in ' + p.text.replace('NEW: ', '')
        description = browser2.find_element(By.ID, 'textcontainer').find_element(By.XPATH, './/p[1]').get_attribute('outerHTML').replace('&nbsp;', '').replace('\n', '')
        description = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})', '' , description) #get description w/o html crap
        is_graduate_program = False
        area_of_study = ''
        credit_requirement = browser2.find_element(By.CLASS_NAME, 'listsum').text[-4:]
        is_stem = True if ('Engineering' in program_name or 'Science' in program_name or 'Mathematics' in program_name or 'STEM' in program_name) else False
        url = p.get_attribute('href')
        calendar_type = 'Quarter'

        postgres_programs_rows.append([program_name, description, is_graduate_program, area_of_study, credit_requirement, is_stem, url, calendar_type])
        elasticsearch_programs_rows.append([program_name, url, calendar_type])
    except:
        print("FAILED ON: " + p.text)
###END UNDERGRAD MINOR SCRAPING

###BEGIN GRADUATE PROGRAM SCRAPING
browser1.get('https://catalog.drexel.edu/graduateprograms/')
print("\nGRADUATE PROGRAMS NOT CAPTURED:") #prints to console any that fail

elemTextContainer = browser1.find_element(By.ID, 'textcontainer')
elemPrograms = elemTextContainer.find_elements(By.XPATH, './/p/a')

for p in elemPrograms:
    if (p.text == '' or p.get_attribute('href') == None):
        continue
    try:
        browser2.get(p.get_attribute('href')) #follows link to page with a new browser, necessary to open a new one

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

        program_name = infoList[1] + " in " + infoList[0]
        if (program_name[:2] == ': '):
            program_name = program_name.replace(': ', '', 1)
        description = elemTextContainer.find_element(By.XPATH, './/p[2]').text.replace("\n", "  ").strip('"')
        is_graduate_program = True #currently scraping grad programs
        area_of_study = ''
        credit_requirement = float(infoList[3])
        if ('Engineering' in infoList[1] or 'Science' in infoList[1]):
            is_stem = True
        else:
            is_stem = False
        url = p.get_attribute('href')
        calendar_type = infoList[2]

        postgres_programs_rows.append([program_name, description, is_graduate_program, area_of_study, credit_requirement, is_stem, url, calendar_type])
        elasticsearch_programs_rows.append([program_name, url, calendar_type])

    except Exception:
        print("FAILED ON: " + p.text)
###END GRADUATE PROGRAM SCRAPING

#Postgres.education.programs
with open(currentDirectory + "/Postgres_Data/Postgres-programs.csv", 'w', encoding='utf-8', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(postgres_programs_headers)
    csvwriter.writerows(postgres_programs_rows)

#Elasticsearch.drexel_additional_education_info.programs
with open(currentDirectory + "/Elasticsearch_Data/Elasticsearch-programs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(elasticsearch_programs_headers)
    csvwriter.writerows(elasticsearch_programs_rows)