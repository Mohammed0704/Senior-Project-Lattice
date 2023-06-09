import random
import csv
import os

def main():
    
    '''
    (Structure)
    Database System:
        Database:
            Table:
                Fields
    
    Postgres:
        education:
            departments:
                department_name
                college_name
                description
                url
                main_office_location
                main_office_phone
                department_head
                department_administrator

    Elasticserach:
        drexel_additional_education_info:
            departments:
                department_name
                url
                has_field_sites
				
	REF:
    What colleges and schools have departments within them:
        https://drexel.edu/coas/academics/departments-centers/
        https://drexel.edu/engineering/academics/departments/
        
    '''
    
    departmentNames = ["Biodiversity, Earth & Environmental Science","Biology","Chemistry","Communication",
                       "Criminology & Justice Studies","English & Philosophy","Global Studies and Modern Languages",
                       "History","Mathematics","Physics","Politics","Psychological and Brain Sciences","Sociology",
                       "Chemical and Biological Engineering","Civil, Architectural and Environmental Engineering",
                       "Electrical and Computer Engineering","Engineering Leadership and Society",
                       "Materials Science and Engineering","Mechanical Engineering and Mechanics"]			   
    
    educationDepartmentsHeader = ["Department Name", "College Name", "Description", "URL", "Main Office Location", 
                                  "Main Office Phone", "Department Head", "Department Administrator"]
    
    additionalInfoDepartmentHeader = ["Department Name", "Has Field Sites", "URL"]
    
    educationDepartments = []
    additionInfoDepartments = []
    
    educationDepartments.append([departmentNames[0], "College of Arts and Sciences", "Drexel University's Department of Biodiversity, Earth and Environmental Science (BEES) lives by the 'Field Experience, Early and Often' motto. Students gain hands-on experience in an environmental department right from the start through our Pre-Term Field Experience. Students also have unprecedented access to incredible facilities, including local and international field sites, Drexel's Gold-LEED-certified Papadakis Integrated Sciences Building, and the Academy of Natural Sciences of Drexel University, which is the oldest natural history museum in the Western Hemisphere.", "https://drexel.edu/coas/academics/departments-centers/bees/", "Papadakis Integrated Sciences Building (PISB), Room 123 3245 Chestnut Street Philadelphia, PA 19104", "215.571.4651", "David Velinsky", "Donna Fahres"])
    educationDepartments.append([departmentNames[1], "College of Arts and Sciences", "Drexel University's Department of Biology is home to a dynamic group of researchers who are leaders in the fields of cell and molecular biology, biochemistry, genomics and more. Students learn through hands-on experiences gained in and outside of the classroom. As a leader in STEM education, from research in faculty labs to co-op positions with the Children's Hospital of Pennsylvania to a study abroad on Bioko Island, our undergraduates have the opportunity to explore real-life career options before graduation.", "https://drexel.edu/coas/academics/departments-centers/biology/", "Constantine Papadakis Integrated Sciences Building (PISB) 3245 Chestnut Street Philadelphia, PA 19104", "215.895.2788", "Mary Katherine Gonder", "Brenda Jones"])
    educationDepartments.append([departmentNames[2], "College of Arts and Sciences", "Drexel University's Department of Chemistry is dedicated to excellence in education and advanced research in chemical sciences. Chemistry is often called 'the central science' because it drives all life processes and is the foundation of modern technology. Undergraduate and graduate students study the traditional disciplines of chemistry and explore the workings of chemistry in the natural and technological worlds.", "https://drexel.edu/coas/academics/departments-centers/chemistry/", "Disque Hall, room 305 32 South 32nd Street Philadelphia, PA 19104", "215.895.2639", "Joe Foley", "Trish Milnamow"])
    educationDepartments.append([departmentNames[3], "College of Arts and Sciences", "Students in Drexel University's Department of Communication gain broad theoretical knowledge and hands-on experience as they work toward successful careers in public relations, corporate communication, social media management, journalism, digital storytelling, media analytics, audience research and countless areas in which strategic communication and media skills are essential.", "https://drexel.edu/coas/academics/departments-centers/communication/", "3201 Arch Street, Suite 100 Philadelphia, PA 19104", "215.895.2456", "Hilde Van den Bulck", "Sharon Wallace"])
    educationDepartments.append([departmentNames[4], "College of Arts and Sciences", "How did the War on Drugs of the '80s and '90s impact urban communities, from street-corner dealing and violence, to overall community health? How do so-called Three Strikes laws typically influence the decisions of judges at sentencing? How far will the War on Terrorism push the legal boundaries of government surveillance? How is “big data” used by justice, intelligence or private organizations to identify social networks, assess risk, and make decisions about crime policy and resource deployment? Drexel University's Department of Criminology and Justice Studies empowers students to address these and other issues of crime and justice policy.", "https://drexel.edu/coas/academics/departments-centers/criminology-justice-studies/", "3401 Market Street, Suite 110 Philadelphia, PA 19104", "215.571.4628", "Robert Kane", "Rachel Koresky"])
    educationDepartments.append([departmentNames[5], "College of Arts and Sciences", "Drexel University's Department of English and Philosophy offers undergraduate degrees in English, with concentrations in Literary Studies and Writing; Philosophy; and Philosophy, Politics and Economics; as well as a variety of minors and certificate programs.", "https://drexel.edu/coas/academics/departments-centers/english-philosophy/", "MacAlister Hall, Room 5016 3250-60 Chestnut Street Philadelphia, PA 19104", "215.895.6911", "Roger Kurtz", "Liz Heenan"])
    educationDepartments.append([departmentNames[6], "College of Arts and Sciences", "The Global Studies and Modern Languages department emphasizes opportunities for experiential learning as central to the curriculum. Learning by doing allows students to expand their knowledge outside of the classroom through essential hands-on engagement – from around the world to just around the corner.", "https://drexel.edu/coas/academics/departments-centers/global-studies-modern-languages/", "Academic Building 101 N. 33rd Street, 3rd Floor Philadelphia, PA 19104", "215.895.1208", "Rebecca Clothey", "Jessica Kratzer"])
    educationDepartments.append([departmentNames[7], "College of Arts and Sciences", "In the Department of History at Drexel University, our students learn through experience — from full-time co-op positions in archives, museums and other sites, to conducting and presenting original research, to visiting sites of historical significance. The department has particular strengths in the History of Science, Technology and the Environment, and in Global History.", "https://drexel.edu/coas/academics/departments-centers/history/", "MacAlister Hall, Room 3025 3250-60 Chestnut Street Philadelphia, PA 19104", "215.895.2463", "Tiago Saraiva", "Khushi Patel"])
    educationDepartments.append([departmentNames[8], "College of Arts and Sciences", "The mathematics department at Drexel University is a close-knit, energetic and diverse group. The Bachelor of Science and Bachelor of Arts in Mathematics provide a healthy foundation of abstract reasoning, applications and computing. With the Doctorate and Master of Science in Mathematics, the department is focused on developing the next generation of mathematicians. Comprised of internationally recognized researchers, the Department of Mathematics faculty specializes in several areas of mathematics, including mathematical biology, combinatorics, matrix and operator theory, geometry, optics, probability, numerical analysis and partial differential equations.", "https://drexel.edu/coas/academics/departments-centers/mathematics/", "Korman Center, Room 291 15 S. 33rd Street Philadelphia PA, 19104", "215.895.2668", "J. Douglas Wright", "Paige Chmielewski"])
    educationDepartments.append([departmentNames[9], "College of Arts and Sciences", "The Department of Physics provides a solid understanding of physical principles, problem solving, mathematical and computational skills, as well as broad experimental training. Students studying physics have countless opportunities to conduct research as early as freshman year through Drexel's renowned cooperative education program and in faculty research and worldwide collaborations.", "https://drexel.edu/coas/academics/departments-centers/physics/", "Disque Hall, Room 816 32 S. 32nd Street Philadelphia, PA 19104", "215.895.2708", "Stephen L.W. McMillan", "Lisa Ferrara"])
    educationDepartments.append([departmentNames[10], "College of Arts and Sciences", "Political science at its core looks at the distribution of power: in world capitals, between states and in our everyday lives. The Department of Politics at Drexel University trains students in research methods and offers countless opportunities for students to learn beyond the classroom through the Drexel Co-op program, undergraduate research opportunities and interdisciplinary work. The department offers several graduate and undergraduate degrees, including the BA in Political Science and the BA in Philosophy, Politics and Economics.", "https://drexel.edu/coas/academics/departments-centers/politics/", "MacAlister Hall, Room 3025 3250-60 Chestnut Street Philadelphia, PA 19104", "215.895.2463", "Richardson Dilworth", "Khushi Patel"])
    educationDepartments.append([departmentNames[11], "College of Arts and Sciences", "Drexel University's Department of Psychological and Brain Sciences is an active community of internationally known faculty and student scholars. Our department features state-of-the-art research labs, a training clinic, and a wide array of research and clinical opportunities for our graduate and undergraduate students.", "https://drexel.edu/coas/academics/departments-centers/psychology/", "Stratton Hall 3201 Chestnut Street Philadelphia, PA 19104", "215.895.1895", "Brian Daly", "Roxane Staley-Hope"])
    educationDepartments.append([departmentNames[12], "College of Arts and Sciences", "Sociology investigates how communities are formed and maintained and how people resist social conventions and inequalities. Drawing from Philadelphia's rich cultural landscape, Drexel's Bachelor of Arts degree in Sociology educates students to examine the interplay between institutions and individuals to better understand how one's life is shaped by society. Students develop strong skills in critical thinking, research design, research methods, data analysis, writing and public speaking in order to address contemporary social challenges.", "https://drexel.edu/coas/academics/departments-centers/sociology/", "3201 Arch Street Philadelphia, PA 19104", "215.895.1314", "Emmanuel Koku", "Rachel Koresky"])
    educationDepartments.append([departmentNames[13], "College of Engineering", "In Chemical Engineering, the science gets applied to real products and real solutions that have the greatest impact on society. The department of chemical engineering at Drexel combines many different concepts and skill sets, and is broadly applicable. Find out more about how a Chemical Engineering degree from Drexel sets the foundation for your success across a spectrum of professions within the chemical and biological engineering field.", "https://drexel.edu/engineering/academics/departments/chemical-biological-engineering/", "3101 Ludlow Street CAT Suite 288 Philadelphia, PA 19104", "215.895.2227", "Cameron Abrams", "Samantha Pearsall"])
    educationDepartments.append([departmentNames[14], "College of Engineering", "The Civil, Architectural and Environmental Engineering Department provides students with a comprehensive and outstanding educational experience. Classes are taught by experienced faculty who specialize in cutting-edge research and practice. Students have proven success of taking what they learn in the classroom and using it in their co-op experience, which provides them with unparalleled achievement in their careers.", "https://drexel.edu/engineering/academics/departments/civil-architectural-environmental-engineering/", "3141 Chestnut Street Curtis 251 Philadelphia, PA 19104", "215.895.2341", "Michael Waring", "Noelle Palladino"])
    educationDepartments.append([departmentNames[15], "College of Engineering", "Electrical and Computer Engineering traditionally includes circuits and electronics, telecommunications, power, and controls. Today, ECE graduates also lead projects in audio, optics, machine learning, biomedical imaging, and nanotechnology; they explore new frontiers in robotics, self-driving cars, Internet of Things, nanotechnology, cybersecurity, wearable electronics, wireless, computer chips, and renewable energy technologies.", "https://drexel.edu/engineering/academics/departments/electrical-computer-engineering/", "3120 Market Street Bossone Research Building Room 313 Philadelphia, PA 19104", "215.895.2241", "Steven Weber", "Sherri Hackett"])
    educationDepartments.append([departmentNames[16], "College of Engineering", "The Department of Engineering Leadership and Society seeks to educate a new generation of engineers who are prepared to address the complex challenges of the 21st century with analytical minds and community-focused hearts. Launched in 2020 in response to the leadership and technological challenges of industry as well as areas of national need, the department comprises the disciplines of construction management, engineering management, engineering technology, peace engineering and systems engineering.", "https://drexel.edu/engineering/academics/departments/engineering-leadership-society/", "3175 JFK Boulevard University Crossing, Room 110 Philadelphia, PA 19104", "215.895.6253", "James Tangorra", "Gergana Willis"])
    educationDepartments.append([departmentNames[17], "College of Engineering", "Materials science and engineering is an interdisciplinary field that forms the foundation for many engineering applications by extending the current supply of materials, improving existing materials, and developing new, superior, and sustainable materials and processes. A key characteristic of the Drexel Materials undergraduate program is experiential learning integrated into the curriculum through co-op, a six-month internship program, as well as Vertically Integrated Projects (VIP) linking graduate, and undergraduate project-based learning and undergraduate research with our award-winning faculty.", "https://drexel.edu/engineering/academics/departments/materials-science-engineering/", "3100 Market Street LeBow Engineering Center 344 Philadelphia, PA 19104", "215.895.2323", "Steven May", "Sean Blake"])
    educationDepartments.append([departmentNames[18], "College of Engineering", "Mechanical engineers use the principles of energy, materials, and mechanics to design and manufacture machines and devices of all types. At Drexel, our mechanical engineering programs explore how matter behaves at extremes and poke at the boundary between human activity and what machines can do. Traditional career pathways have broadened into new opportunities in biomechanics, high-performance computing, infrastructure systems, materials, and frontiers of human-machine interfaces for the benefit of humankind.", "https://drexel.edu/engineering/academics/departments/mechanical-engineering/", "3141 Chestnut Street Randell Hall, Room 115 Philadelphia, PA 19104", "215.895.2352", "Jonathan E. Spanier", "Zovi Khrimian"])
    
    '''
    Didn't know where to find field sites for the departments so I randomized the data
    I'm assuming that more departments have field sites than not, so I weighted it 75% True to 25% False
    '''
    bools = [True, True, True, False]
    
    additionInfoDepartments.append([departmentNames[0], bools[random.randint(0,3)], educationDepartments[0][3]])
    additionInfoDepartments.append([departmentNames[1], bools[random.randint(0,3)], educationDepartments[1][3]])
    additionInfoDepartments.append([departmentNames[2], bools[random.randint(0,3)], educationDepartments[2][3]])
    additionInfoDepartments.append([departmentNames[3], bools[random.randint(0,3)], educationDepartments[3][3]])
    additionInfoDepartments.append([departmentNames[4], bools[random.randint(0,3)], educationDepartments[4][3]])
    additionInfoDepartments.append([departmentNames[5], bools[random.randint(0,3)], educationDepartments[5][3]])
    additionInfoDepartments.append([departmentNames[6], bools[random.randint(0,3)], educationDepartments[6][3]])
    additionInfoDepartments.append([departmentNames[7], bools[random.randint(0,3)], educationDepartments[7][3]])
    additionInfoDepartments.append([departmentNames[8], bools[random.randint(0,3)], educationDepartments[8][3]])
    additionInfoDepartments.append([departmentNames[9], bools[random.randint(0,3)], educationDepartments[9][3]])
    additionInfoDepartments.append([departmentNames[10], bools[random.randint(0,3)], educationDepartments[10][3]])
    additionInfoDepartments.append([departmentNames[11], bools[random.randint(0,3)], educationDepartments[11][3]])
    additionInfoDepartments.append([departmentNames[12], bools[random.randint(0,3)], educationDepartments[12][3]])
    additionInfoDepartments.append([departmentNames[13], bools[random.randint(0,3)], educationDepartments[13][3]])
    additionInfoDepartments.append([departmentNames[14], bools[random.randint(0,3)], educationDepartments[14][3]])
    additionInfoDepartments.append([departmentNames[15], bools[random.randint(0,3)], educationDepartments[15][3]])
    additionInfoDepartments.append([departmentNames[16], bools[random.randint(0,3)], educationDepartments[16][3]])
    additionInfoDepartments.append([departmentNames[17], bools[random.randint(0,3)], educationDepartments[17][3]])
    additionInfoDepartments.append([departmentNames[18], bools[random.randint(0,3)], educationDepartments[18][3]])
    
    cwd = os.getcwd()
    
    educationInfoPath = cwd + os.sep + ".." + os.sep + "postgres" + os.sep + "data_files" + os.sep + "Postgres-education-departments.csv"
    additionalInfoPath = cwd + os.sep + ".." + os.sep + "elasticsearch" + os.sep + "data_files" + os.sep + "Elasticsearch-drexel_additional_education_info-departments.csv"
    
    with open(educationInfoPath, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(educationDepartmentsHeader)         
        csvwriter.writerows(educationDepartments)
    
    with open(additionalInfoPath, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(additionalInfoDepartmentHeader)         
        csvwriter.writerows(additionInfoDepartments)
					   
if __name__ == "__main__":
    main()