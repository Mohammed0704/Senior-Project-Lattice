import os
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def driverSetup():
    # This can be used to add additional options like a download path if you wanted your web scrapper to hit a button and download a file on a website 
    options = Options()
    options.headless = True # If false, the browser window will pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrapeMajor(driver, data, url, program_name, table_rows_xpath):
    '''
        Go to url, get course requirement table, scrape course code data from table
    '''
    driver.get(url)
    time.sleep(2)

    table = driver.find_elements(By.XPATH, table_rows_xpath)
    program = program_name
    for row in table:

        try:
            tmp = row.find_element(By.XPATH, ".//*[@class='courselistcomment areaheader']")
            requirement_type = tmp.text
            continue
        except Exception as e:
            pass 

        colData = [program]
        try:
            ''' I print out course codes as it goes so you can see the web scraper working, and will know when it isn't '''
            codeCol = row.find_element(By.XPATH, ".//*[@class='codecol']")
            codeColText = codeCol.text.replace(" [WI]", "")
            codeColText = codeColText.replace("\n&", ",")
            print(codeColText)
            colData.append(codeColText)
        except Exception as e:
            try:
                orCodeCol = row.find_element(By.XPATH, ".//*[@class='codecol orclass']")
                data[-1][1] = data[-1][1] + ", " +  orCodeCol.text.replace("or ", "")
            except:
                pass
            continue
        colData.append(requirement_type)
        data.append(colData)
    print(f"Finished scraping major: {program_name}")
    return data

def main():
    
    driver = driverSetup()

    data = []
    data = scrapeMajor(driver, data, "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computerscience/#requirementsbstext", "Bachelor of Science in Computer Science", "//*[@id='requirementsbstextcontainer']/table[1]/tbody/tr")
    data = scrapeMajor(driver, data, "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/softwareengineering/#degreerequirementstext", "Bachelor of Science in Software Engineering", "//*[@id='degreerequirementstextcontainer']/table/tbody/tr")
    data = scrapeMajor(driver, data, "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/biologicalsciences/#degreerequirementsbstext", "Bachelor of Science in Biological Sciences", "//*[@id='degreerequirementsbstextcontainer']/table[1]/tbody/tr")
    df = pd.DataFrame(data, columns=["program_name", "course_code", "requirement_category"])
    print(df)

    df.to_csv("ProgramRequirements.csv", index=False)



if __name__ == "__main__":
    main()