#!/usr/bin/env bash

#copy mariadb data into the mariadb container
docker cp ./mariadb/data_files mariadb:/

docker exec -it mariadb mariadb --user root -puser mariadb -e "DROP SCHEMA IF EXISTS drexel_people;"
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE SCHEMA drexel_people"

docker exec -it mariadb mariadb --user root -puser mariadb -e "DROP SCHEMA IF EXISTS locations;"
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE SCHEMA locations"

#basic_employee_info
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE TABLE drexel_people.basic_employee_info(
                                  drexel_id varchar(16) PRIMARY KEY,
                                  last_name varchar(64),
                                  first_name varchar(64),
                                  middle_name varchar(32),
                                  date_of_birth varchar(32),
                                  chosen_name varchar(32),
                                  personal_pronouns varchar(16),
                                  email varchar(64),
                                  primary_department varchar(128),
                                  gender varchar(16),
                                  marital_status varchar(16),
                                  ethnicity varchar(16),
                                  race varchar(16),
                                  living_address varchar(128),
                                  mail_address varchar(128),
                                  phone_number varchar(32),
                                  role varchar(64)
                                  );"


docker exec -it mariadb mariadb --user root -puser mariadb -e "LOAD DATA LOCAL INFILE '/data_files/MariaDB-basic_employee_info.csv' 
                                                               INTO table drexel_people.basic_employee_info 
                                                               FIELDS TERMINATED BY ','  
                                                               LINES TERMINATED BY '\r\n'
                                                               IGNORE 1 lines
                                                               (drexel_id, last_name, first_name, middle_name, date_of_birth, chosen_name, personal_pronouns, email, primary_department, gender, marital_status, ethnicity, race, living_address, mail_address, phone_number, role)
                                                               ;"

<<asdf
#basic_student_info
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE TABLE drexel_people.basic_student_info(
                                  drexel_id varchar(16) PRIMARY KEY, 
                                  first_name varchar(64), 
                                  middle_name varchar(64),
                                  last_name varchar(128),
                                  date_of_birth text(64),
                                  email varchar(128),
                                  chosen_name varchar(64),
                                  gender char,
                                  personal_pronoun varchar(32),
                                  ethnicity varchar(32),
                                  race varchar(32),
                                  expected_graduation_year int,
                                  student_program_type varchar(32),
                                  phone varchar(16),
                                  home_address varchar(64)
                                  );"

docker exec -it mariadb mariadb --user root -puser mariadb -e "COPY drexel_people.basic_student_info (drexel_id, first_name, middle_name, last_name, date_of_birth, email, chosen_name, gender, personal_pronoun, ethnicity, race, expected_graduation_year, student_program_type, phone, home_address) 
                FROM '/data_files/MariaDB-basic_student_info.csv' 
                WITH HEADER = TRUE;"

#resource_locations
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE TABLE location.resource_locations(
                                  name_of_resource varchar(64) PRIMARY KEY,
                                  address varchar(128),
                                  description varchar(256)
                                  );"

docker exec -it mariadb mariadb --user root -puser mariadb -e "COPY location.resource_locations (name_of_resource, address, description)
                FROM '/data_files/MariaDB-resource_locations.csv'
                WITH HEADER = TRUE;"

#student_locations
docker exec -it mariadb mariadb --user root -puser mariadb -e "CREATE TABLE location.student_locations(
                                  drexel_id varchar(16) PRIMARY KEY,
                                  is_international boolean,
                                  living_address varchar(64),
                                  is_communter boolean,
                                  has_parking_pass boolean
                                  );"

docker exec -it mariadb mariadb --user root -puser mariadb -e "COPY location.student_locations (name_of_resource, address, description)
                FROM '/data_files/MariaDB-student_locations.csv' 
                WITH HEADER = TRUE;" 
               