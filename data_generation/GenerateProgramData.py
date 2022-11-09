from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#set up browser to not open and use firefox
options = Options()
options.headless = True
browser1 = webdriver.Firefox(options=options)
browser2 = webdriver.Firefox(options=options)
errorLog = open("GenerateProgramData_ErrorLog.txt", "w")

counter = 0 ####DELETE

program_name = ""
description = ""
url = ""
is_grad_program = ""
area_of_study = ""
program = ""
credit_requirement = ""
is_stem = ""
url = ""

browser1.get("https://catalog.drexel.edu/majors/")

elemTextContainer = browser1.find_element(By.ID, "textcontainer")
elemMajors = elemTextContainer.find_elements(By.XPATH, ".//p/a")

for p in elemMajors:
    if (p.text == "" or p.get_attribute("href") == None):
        continue
    try:
        browser2.get(p.get_attribute("href"))

        elemTextContainer = browser2.find_element(By.ID, "textcontainer")
        elemInfo = elemTextContainer.find_element(By.XPATH, ".//p[1]")
        infoBlock = elemInfo.get_attribute("outerHTML") #get block of information in string var

        infoBlock.replace("<p>", "")
        infoBlock.replace("<em>", "")
        infoBlock.replace("<br>", "")
        print(infoBlock + "\n")
    except:
        errorLog.write(p.text+"\n")
    
    counter += 1
    if (counter == 3):
        break