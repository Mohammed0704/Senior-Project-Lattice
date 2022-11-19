import csv
import os.path

currentDirectory = os.getcwd()

with open(currentDirectory + "/AreaOfStudyProgramNames.txt", "r") as f:
    programNames = f.read().splitlines()

#Postgres.education.areas_of_study
name = ""
department = ''
act = ""
plan = ""

#Elasticsearch.additional_education_info.areas_of_study
#name = ""
description = ""
hasMajor =""
hasMinor = "" 
hasCertificate = ""

#Postgres.education.areas_of_study
areaOfStudyHeaders = ["Name", "Department", "Act", "Plan"]
areaOfStudyRows = []

areaOfStudyRows.append([programNames[0], "Department of Accounting", "NULL", "NULL"]) #Accounting

areaOfStudyRows.append([programNames[1], "Department of Marketing", "NULL", "NULL"]) #Brand & Reputation Management

areaOfStudyRows.append([programNames[2], "Department of General Business", "NULL", "NULL"]) #Business Administration

areaOfStudyRows.append([programNames[3], "Department of Decision Sciences and MIS", "NULL", "NULL"]) #Business Analytics

areaOfStudyRows.append([programNames[4], "Department of Management", "NULL", "NULL"]) #Business Consulting

areaOfStudyRows.append([programNames[5], "Department of Decision Sciences and MIS", "NULL", "NULL"]) #Business & Engineering

areaOfStudyRows.append([programNames[6], "School of Economics", "NULL", "NULL"]) #Economics

areaOfStudyRows.append([programNames[7], "Department of Sport Business", "NULL", "NULL"]) #Esport Business

areaOfStudyRows.append([programNames[8], "Department of Finance", "NULL", "NULL"]) #Finance

areaOfStudyRows.append([programNames[9], "Department of Finance", "NULL", "NULL"]) #Financial Technology

areaOfStudyRows.append([programNames[10], "Department of General Business", "NULL", "NULL"]) #General Business

areaOfStudyRows.append([programNames[11], "Department of General Business", "NULL", "NULL"]) #International Business

areaOfStudyRows.append([programNames[12], "Department of Decision Sciences and MIS", "NULL", "NULL"]) #Management Information Systems

areaOfStudyRows.append([programNames[13], "Department of Marketing", "NULL", "NULL"]) #Marketing

areaOfStudyRows.append([programNames[14], "Department of Decision Sciences and MIS", "NULL", "NULL"]) #Operations & Supply Chain Management 

areaOfStudyRows.append([programNames[15], "Department of Management", "NULL", "NULL"]) #Organizational Management	 

areaOfStudyRows.append([programNames[16], "Department of Finance", "NULL", "NULL"]) #Real Estate Management & Development

areaOfStudyRows.append([programNames[17], "Department of Marketing", "NULL", "NULL"]) #Social Responsibility in Business

areaOfStudyRows.append([programNames[18], "Department of Sport Business", "NULL", "NULL"]) #Sport Business

areaOfStudyRows.append([programNames[19], "Department of Sport Business", "NULL", "NULL"]) #Sport Management

areaOfStudyRows.append([programNames[20], "Department of Management", "NULL", "NULL"]) #Technology Innovation Management

areaOfStudyRows.append([programNames[21], "Department of Computer Science", "NULL", "NULL"]) #Computer Science

areaOfStudyRows.append([programNames[22], "Department of Computer Science", "NULL", "NULL"]) #Software Engineering

areaOfStudyRows.append([programNames[23], "Department of Information Science", "NULL", "NULL"]) #Data Science

areaOfStudyRows.append([programNames[24], "Department of Computer Science", "NULL", "NULL"]) #Artificial Intelligence and Machine Learning

areaOfStudyRows.append([programNames[25], "Department of Computer Science", "NULL", "NULL"]) #Cybersecurity

areaOfStudyRows.append([programNames[26], "Department of Computer Science", "NULL", "NULL"]) #Software Architecture

areaOfStudyRows.append([programNames[27], "Department of Computer Science", "NULL", "NULL"]) #Software Management

areaOfStudyRows.append([programNames[28], "Department of Information Science", "NULL", "NULL"]) #Information Systems

areaOfStudyRows.append([programNames[29], "Department of Information Science", "NULL", "NULL"]) #Human-Computer Interaction & User Experience

areaOfStudyRows.append([programNames[30], "Department of Information Science", "NULL", "NULL"]) #Computing and Security Technology

areaOfStudyRows.append([programNames[31], "Department of Information Science", "NULL", "NULL"]) #Health Informatics

areaOfStudyRows.append([programNames[32], "Department of Information Science", "NULL", "NULL"]) #Information Science

areaOfStudyRows.append([programNames[33], "Department of Information Science", "NULL", "NULL"]) #Big Data Analytics

areaOfStudyRows.append([programNames[34], "Department of Civil, Architectural and Environmental Engineering", "NULL", "NULL"]) #Architectural Engineering

areaOfStudyRows.append([programNames[35], "Department of Chemical and Biological Engineering", "NULL", "NULL"]) #Chemical Engineering

areaOfStudyRows.append([programNames[36], "Department of Civil, Architectural and Environmental Engineering", "NULL", "NULL"]) #Civil Engineering

areaOfStudyRows.append([programNames[37], "Department of Electrical and Computer Engineering", "NULL", "NULL"]) #Computer Engineering

areaOfStudyRows.append([programNames[38], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Construction Management

areaOfStudyRows.append([programNames[39], "Department of Electrical and Computer Engineering", "NULL", "NULL"]) #Electrical Engineering

areaOfStudyRows.append([programNames[40], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Engineering Technology

areaOfStudyRows.append([programNames[41], "Department of Civil, Architectural and Environmental Engineering", "NULL", "NULL"]) #Environmental Engineering

areaOfStudyRows.append([programNames[42], "Department of Materials Science and Engineering", "NULL", "NULL"]) #Materials Science and Engineering

areaOfStudyRows.append([programNames[43], "Department of Mechanical Engineering and Mechanics", "NULL", "NULL"]) #Mechanical Engineering

areaOfStudyRows.append([programNames[44], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Engineering Management

areaOfStudyRows.append([programNames[45], "Department of Electrical and Computer Engineering", "NULL", "NULL"]) #Internet of Things

areaOfStudyRows.append([programNames[46], "Department of Electrical and Computer Engineering", "NULL", "NULL"]) #Machine Learning Engineering

areaOfStudyRows.append([programNames[47], "Department of Materials Science and Engineering", "NULL", "NULL"]) #Nanomaterials

areaOfStudyRows.append([programNames[48], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Peace Engineering

areaOfStudyRows.append([programNames[49], "Department of Electrical and Computer Engineering, Department of Mechanical Engineering and Mechanics", "NULL", "NULL"]) #Robotics And Autonomy

areaOfStudyRows.append([programNames[50], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Systems Engineering

areaOfStudyRows.append([programNames[51], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Engineering Leadership

areaOfStudyRows.append([programNames[52], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Hardware Systems Engineering

areaOfStudyRows.append([programNames[53], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Naval Engineering

areaOfStudyRows.append([programNames[54], "Department of Chemical and Biological Engineering", "NULL", "NULL"]) #Pharmaceutical and Medical Device Manufacturing

areaOfStudyRows.append([programNames[55], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Systems Design and Development

areaOfStudyRows.append([programNames[56], "Department of Engineering Leadership and Society", "NULL", "NULL"]) #Systems Reliability Engineering

areaOfStudyRows.append([programNames[57], "Department of Animation & Visual Effects", "NULL", "NULL"]) #Animation & Visual Effects

areaOfStudyRows.append([programNames[58], "Department of Architecture", "NULL", "NULL"]) #Architecture

areaOfStudyRows.append([programNames[59], "Department of Design & Merchandising", "NULL", "NULL"]) #Design & Merchandising

areaOfStudyRows.append([programNames[60], "Department of Digital Media", "NULL", "NULL"]) #Digital Media & Virtual Production

areaOfStudyRows.append([programNames[61], "Department of Fashion Design", "NULL", "NULL"]) #Fashion Design

areaOfStudyRows.append([programNames[62], "Department of Game Design & Production", "NULL", "NULL"]) #Game Design & Production

areaOfStudyRows.append([programNames[63], "Department of Digital Media", "NULL", "NULL"]) #Graphic Design

areaOfStudyRows.append([programNames[64], "Department of Interior Design", "NULL", "NULL"]) #Interior Design

areaOfStudyRows.append([programNames[65], "Department of Music Industry", "NULL", "NULL"]) #Music Industry

areaOfStudyRows.append([programNames[66], "Department of Photography", "NULL", "NULL"]) #Photography

areaOfStudyRows.append([programNames[67], "Department of Product Design", "NULL", "NULL"]) #Product Design

areaOfStudyRows.append([programNames[68], "Department of User Experience & Interaction Design", "NULL", "NULL"]) #User Experience & Interaction Design

areaOfStudyRows.append([programNames[69], "Department of Digital Media", "NULL", "NULL"]) #Digital Research

areaOfStudyRows.append([programNames[70], "Department of Retail & Merchandising", "NULL", "NULL"]) #Retail & Merchandising

areaOfStudyRows.append([programNames[71], "Department of TV Production & Media Management", "NULL", "NULL"]) #Television & Media Management

areaOfStudyRows.append([programNames[72], "Department of Entertainment & Arts Management", "NULL", "NULL"]) #Entertainment & Arts Management

areaOfStudyRows.append([programNames[73], "Department of Music", "NULL", "NULL"]) #Music Performance

areaOfStudyRows.append([programNames[74], "Department of Film & Video", "NULL", "NULL"]) #Video Production

areaOfStudyRows.append([programNames[75], "Department of Dance", "NULL", "NULL"]) #Dance

areaOfStudyRows.append([programNames[76], "", "NULL", "NULL"]) #Behavaviroral Health Counseling

areaOfStudyRows.append([programNames[77], "", "NULL", "NULL"]) #Food and Hospitality Management

areaOfStudyRows.append([programNames[78], "Health Administration Department", "NULL", "NULL"]) #Health Administration

areaOfStudyRows.append([programNames[79], "Health Sciences Department", "NULL", "NULL"]) #Health Sciences

areaOfStudyRows.append([programNames[80], "Nutrition Sciences Department", "NULL", "NULL"]) #Nutrition Sciences

areaOfStudyRows.append([programNames[81], "Undergraduate Nursing Department", "NULL", "NULL"]) #Undergraduate Nursing

areaOfStudyRows.append([programNames[82], "Food and Hospitality Management Department", "NULL", "NULL"]) #Food and Hospitality Management

areaOfStudyRows.append([programNames[83], "Graduate Nursing Department", "NULL", "NULL"]) #Graduate Nursing

areaOfStudyRows.append([programNames[84], "Physical Therapy and Rehabilitation Sciences Department", "NULL", "NULL"]) #Physical Therapy and Rehbilitation Science

areaOfStudyRows.append([programNames[85], "Physician Assistant Department", "NULL", "NULL"]) #Physician Assistant



#Elasticsearch.additional_education_info.areas_of_study
additionalAreaOfStudyHeaders = ["Name", "Desciption", "Has Major", "Has Minor", "Has Certificate"]
additionalAreaOfStudyRows = []

additionalAreaOfStudyRows.append([programNames[0], programNames[0], "TRUE", "TRUE", "FALSE"]) #Accounting

additionalAreaOfStudyRows.append([programNames[1], programNames[1], "FALSE", "FALSE", "TRUE"]) #Brand & Reputation Management

additionalAreaOfStudyRows.append([programNames[2], programNames[2], "FALSE", "TRUE", "FALSE"]) #Business Administration

additionalAreaOfStudyRows.append([programNames[3], programNames[3], "TRUE", "TRUE", "FALSE"]) #Business Analytics

additionalAreaOfStudyRows.append([programNames[4], programNames[4], "FALSE", "TRUE", "FALSE"]) #Business Consulting

additionalAreaOfStudyRows.append([programNames[5], programNames[5], "TRUE", "FALSE", "FALSE"]) #Business & Engineering

additionalAreaOfStudyRows.append([programNames[6], programNames[6], "TRUE", "TRUE", "FALSE"]) #Economics

additionalAreaOfStudyRows.append([programNames[7], programNames[7], "TRUE", "TRUE", "FALSE"]) #Esport Business

additionalAreaOfStudyRows.append([programNames[8], programNames[8], "TRUE", "TRUE", "FALSE"]) #Finance

additionalAreaOfStudyRows.append([programNames[9], programNames[9], "FALSE", "TRUE", "FALSE"]) #Financial Technology

additionalAreaOfStudyRows.append([programNames[10], programNames[10], "TRUE", "TRUE", "FALSE"]) #General Business

additionalAreaOfStudyRows.append([programNames[11], programNames[11], "TRUE", "FALSE", "FALSE"]) #International Business

additionalAreaOfStudyRows.append([programNames[12], programNames[12], "TRUE", "TRUE", "FALSE"]) #Management Information Systems

additionalAreaOfStudyRows.append([programNames[13], programNames[13], "TRUE", "TRUE", "FALSE"]) #Marketing

additionalAreaOfStudyRows.append([programNames[14], programNames[14], "TRUE", "TRUE", "FALSE"]) #Operations & Supply Chain Management 

additionalAreaOfStudyRows.append([programNames[15], programNames[15], "TRUE", "TRUE", "FALSE"]) #Organizational Management

additionalAreaOfStudyRows.append([programNames[16], programNames[16], "TRUE", "TRUE", "FALSE"]) #Real Estate Management & Development

additionalAreaOfStudyRows.append([programNames[17], programNames[17], "FALSE", "FALSE", "TRUE"]) #Social Responsibility in Business

additionalAreaOfStudyRows.append([programNames[18], programNames[18], "TRUE", "TRUE", "FALSE"]) #Sport Business

additionalAreaOfStudyRows.append([programNames[19], programNames[19], "FALSE", "TRUE", "FALSE"]) #Sport Management

additionalAreaOfStudyRows.append([programNames[20], programNames[20], "TRUE", "TRUE", "FALSE"]) #Technology Innovation Management

additionalAreaOfStudyRows.append([programNames[21], programNames[21], "TRUE", "TRUE", "TRUE"]) #Computer Science

additionalAreaOfStudyRows.append([programNames[22], programNames[22], "TRUE", "FALSE", "FALSE"]) #Software Engineering

additionalAreaOfStudyRows.append([programNames[23], programNames[23], "TRUE", "TRUE", "TRUE"]) #Data Science

additionalAreaOfStudyRows.append([programNames[24], programNames[24], "TRUE", "FALSE", "TRUE"]) #Artificial Intelligence and Machine Learning

additionalAreaOfStudyRows.append([programNames[25], programNames[25], "TRUE", "FALSE", "TRUE"]) #Cybersecurity

additionalAreaOfStudyRows.append([programNames[26], programNames[26], "FALSE", "FALSE", "TRUE"]) #Software Architecture

additionalAreaOfStudyRows.append([programNames[27], programNames[27], "FALSE", "FALSE", "TRUE"]) #Software Management

additionalAreaOfStudyRows.append([programNames[28], programNames[28], "TRUE", "TRUE", "FALSE"]) #Information Systems

additionalAreaOfStudyRows.append([programNames[29], programNames[29], "FALSE", "TRUE", "TRUE"]) #Human-Computer Interaction & User Experience

additionalAreaOfStudyRows.append([programNames[30], programNames[30], "TRUE", "FALSE", "FALSE"]) #Computing and Security Technology

additionalAreaOfStudyRows.append([programNames[31], programNames[31], "TRUE", "FALSE", "TRUE"]) #Health Informatics

additionalAreaOfStudyRows.append([programNames[32], programNames[32], "FALSE", "TRUE", "FALSE"]) #Information Science
      
additionalAreaOfStudyRows.append([programNames[33], programNames[33], "FALSE", "FALSE", "TRUE"]) #Big Data Analytics

additionalAreaOfStudyRows.append([programNames[34], programNames[34], "TRUE", "TRUE", "TRUE"]) #Architectural Engineering

additionalAreaOfStudyRows.append([programNames[35], programNames[35], "TRUE", "TRUE", "FALSE"]) #Chemical Engineering

additionalAreaOfStudyRows.append([programNames[36], programNames[36], "TRUE", "FALSE", "FALSE"]) #Civil Engineering

additionalAreaOfStudyRows.append([programNames[37], programNames[37], "TRUE", "TRUE", "FALSE"]) #Computer Engineering

additionalAreaOfStudyRows.append([programNames[38], programNames[38], "TRUE", "TRUE", "TRUE"]) #Construction Management

additionalAreaOfStudyRows.append([programNames[39], programNames[39], "TRUE", "TRUE", "FALSE"]) #Electrical Engineering

additionalAreaOfStudyRows.append([programNames[40], programNames[40], "TRUE", "FALSE", "FALSE"]) #Engineering Technology

additionalAreaOfStudyRows.append([programNames[41], programNames[41], "TRUE", "TRUE", "FALSE"]) #Environmental Engineering

additionalAreaOfStudyRows.append([programNames[42], programNames[42], "TRUE", "TRUE", "FALSE"]) #Materials Science and Engineering

additionalAreaOfStudyRows.append([programNames[43], programNames[43], "TRUE", "TRUE", "FALSE"]) #Mechanical Engineering

additionalAreaOfStudyRows.append([programNames[44], programNames[44], "TRUE", "TRUE", "TRUE"]) #Engineering Management

additionalAreaOfStudyRows.append([programNames[45], programNames[45], "TRUE", "FALSE", "FALSE"]) #Internet of Things

additionalAreaOfStudyRows.append([programNames[46], programNames[46], "TRUE", "FALSE", "FALSE"]) #Machine Learning Engineering

additionalAreaOfStudyRows.append([programNames[47], programNames[47], "TRUE", "FALSE", "FALSE"]) #Nanomaterials

additionalAreaOfStudyRows.append([programNames[48], programNames[48], "TRUE", "FALSE", "TRUE"]) #Peace Engineering

additionalAreaOfStudyRows.append([programNames[49], programNames[49], "TRUE", "TRUE", "FALSE"]) #Robotics And Autonomy

additionalAreaOfStudyRows.append([programNames[50], programNames[50], "TRUE", "TRUE", "TRUE"]) #Systems Engineering

additionalAreaOfStudyRows.append([programNames[51], programNames[51], "FALSE", "TRUE", "FALSE"]) #Engineering Leadership

additionalAreaOfStudyRows.append([programNames[52], programNames[52], "FALSE", "FALSE", "TRUE"]) #Hardware Systems Engineering

additionalAreaOfStudyRows.append([programNames[53], programNames[53], "FALSE", "FALSE", "TRUE"]) #Naval Engineering

additionalAreaOfStudyRows.append([programNames[54], programNames[54], "FALSE", "FALSE", "TRUE"]) #Pharmaceutical and Medical Device Manufacturing

additionalAreaOfStudyRows.append([programNames[55], programNames[55], "FALSE", "FALSE", "TRUE"]) #Systems Design and Development

additionalAreaOfStudyRows.append([programNames[56], programNames[56], "FALSE", "FALSE", "TRUE"]) #Systems Reliability Engineering

additionalAreaOfStudyRows.append([programNames[57], programNames[57], "TRUE", "TRUE", "FALSE"]) #Animation & Visual Effects

additionalAreaOfStudyRows.append([programNames[58], programNames[58], "TRUE", "TRUE", "FALSE"]) #Architecture

additionalAreaOfStudyRows.append([programNames[59], programNames[59], "TRUE", "TRUE", "FALSE"]) #Design & Merchandising

additionalAreaOfStudyRows.append([programNames[60], programNames[60], "TRUE", "FALSE", "FALSE"]) #Design & Merchandising

additionalAreaOfStudyRows.append([programNames[61], programNames[61], "TRUE", "FALSE", "FALSE"]) #Fashion Design

additionalAreaOfStudyRows.append([programNames[62], programNames[62], "TRUE", "FALSE", "FALSE"]) #Game Design & Production

additionalAreaOfStudyRows.append([programNames[63], programNames[63], "TRUE", "FALSE", "FALSE"]) #Graphic Design

additionalAreaOfStudyRows.append([programNames[64], programNames[64], "TRUE", "FALSE", "FALSE"]) #Interior Design

additionalAreaOfStudyRows.append([programNames[65], programNames[65], "TRUE", "TRUE", "FALSE"]) #Music Industry

additionalAreaOfStudyRows.append([programNames[66], programNames[66], "TRUE", "FALSE", "FALSE"]) #Photography

additionalAreaOfStudyRows.append([programNames[67], programNames[67], "TRUE", "TRUE", "FALSE"]) #Product Design

additionalAreaOfStudyRows.append([programNames[68], programNames[68], "TRUE", "TRUE", "FALSE"]) #User Experience & Interaction Design

additionalAreaOfStudyRows.append([programNames[69], programNames[69], "TRUE", "FALSE", "FALSE"]) #Digital Research

additionalAreaOfStudyRows.append([programNames[70], programNames[70], "TRUE", "FALSE", "TRUE"]) #Retail & Merchandising

additionalAreaOfStudyRows.append([programNames[71], programNames[71], "TRUE", "TRUE", "FALSE"]) #Television & Media Management

additionalAreaOfStudyRows.append([programNames[72], programNames[72], "FALSE", "TRUE", "FALSE"]) #Entertainment & Arts Management

additionalAreaOfStudyRows.append([programNames[73], programNames[73], "FALSE", "TRUE", "FALSE"]) #Music Performance

additionalAreaOfStudyRows.append([programNames[74], programNames[74], "FALSE", "TRUE", "FALSE"]) #Video Production

additionalAreaOfStudyRows.append([programNames[75], programNames[75], "FALSE", "TRUE", "TRUE"]) #Dance

additionalAreaOfStudyRows.append([programNames[76], programNames[76], "TRUE", "TRUE", "FALSE"]) #Behavaviroral Health Counseling

additionalAreaOfStudyRows.append([programNames[77], programNames[77], "TRUE", "TRUE", "TRUE"]) #Food and Hospitality Management

additionalAreaOfStudyRows.append([programNames[78], programNames[78], "TRUE", "TRUE", "FALSE"]) #Health Administration

additionalAreaOfStudyRows.append([programNames[79], programNames[79], "TRUE", "TRUE", "FALSE"]) #Health Sciences

additionalAreaOfStudyRows.append([programNames[80], programNames[80], "TRUE", "TRUE", "FALSE"]) #Nutrition Sciences

additionalAreaOfStudyRows.append([programNames[81], programNames[81], "TRUE", "FALSE", "TRUE"]) #Undergraduate Nursing

additionalAreaOfStudyRows.append([programNames[82], programNames[82], "TRUE", "TRUE", "TRUE"]) #Food and Hospitality Management

additionalAreaOfStudyRows.append([programNames[83], programNames[83], "TRUE", "FALSE", "TRUE"]) #Graduate Nursing

additionalAreaOfStudyRows.append([programNames[84], programNames[84], "TRUE", "TRUE", "TRUE"]) #Physical Therapy and Rehbilitation Science

additionalAreaOfStudyRows.append([programNames[85], programNames[85], "TRUE", "FALSE", "FALSE"]) #Physician Assistant



#Postgres.education.areas_of_study
with open(currentDirectory + "/Postgres_Data/Postgres-area_of_study.csv", "w", newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(areaOfStudyHeaders)         
    csvwriter.writerows(areaOfStudyRows)


#Elasticsearch.additional_education_info.areas_of_study
with open(currentDirectory + "/Elasticsearch_Data/Elasticsearch-additional_area_of_study.csv", "w", newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(additionalAreaOfStudyHeaders)         
    csvwriter.writerows(additionalAreaOfStudyRows)