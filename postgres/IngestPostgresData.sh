#!/usr/bin/env bash

#copy postgres data into the postgres container
docker cp ./postgres/data_files postgres:/

#docker exec -it postgres psql -U postgres

#Drop schemas if exists
docker exec -it postgres psql -U postgres -c "DROP SCHEMA IF EXISTS education CASCADE;"
docker exec -it postgres psql -U postgres -c "DROP SCHEMA IF EXISTS campus_life CASCADE;"

#Create Schemas 
docker exec -it postgres psql -U postgres -c "CREATE SCHEMA education;" 
docker exec -it postgres psql -U postgres -c "CREATE SCHEMA campus_life;"

#Create table and ingest into education.colleges
docker exec -it postgres psql -U postgres -c "CREATE TABLE education.colleges (
                                                name text,
                                                description text,
                                                campus text,
                                                address text,
                                                contact_email text,
                                                URL text,
                                                year_founded integer,
                                                current_dean text,
                                                num_of_departments integer,
                                                college_ranking text
                                            );"

docker exec -it postgres psql -U postgres -c "\copy education.colleges from '/data_files/Postgres-colleges.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into education.departments
docker exec -it postgres psql -U postgres -c "CREATE TABLE education.departments (
                                                department_name text,
                                                college_name text,
                                                description text,
                                                URL text,
                                                main_office_location text,
                                                main_office_phone text,
                                                department_head text,
                                                department_administrator text
                                            );"

docker exec -it postgres psql -U postgres -c "\copy education.departments from '/data_files/Postgres-education-departments.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into education.programs
docker exec -it postgres psql -U postgres -c "CREATE TABLE education.programs (
                                                program_name text,
                                                description text,
                                                is_graduate_program boolean,
                                                area_of_study text,
                                                credit_requirement decimal,
                                                is_stem boolean
                                            );"

docker exec -it postgres psql -U postgres -c "\copy education.programs (program_name, description, is_graduate_program, area_of_study, credit_requirement, is_stem) from '/data_files/Postgres-programs.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into education.areas_of_study
docker exec -it postgres psql -U postgres -c "CREATE TABLE education.areas_of_study (
                                                name text,
                                                department text,
                                                act text,
                                                plan text
                                            );"

docker exec -it postgres psql -U postgres -c "\copy education.areas_of_study from '/data_files/Postgres-area_of_study.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into education.student_education_choices
docker exec -it postgres psql -U postgres -c "CREATE TABLE education.student_education_choices (
                                                    drexel_id text,
                                                    first_name text,
                                                    middle_name text,
                                                    last_name text,
                                                    majors text,
                                                    minors text
                                                );"

docker exec -it postgres psql -U postgres -c "\copy education.student_education_choices from '/data_files/Postgres-student_education_choices.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into campus_life.housing_options
docker exec -it postgres psql -U postgres -c "CREATE TABLE campus_life.housing_options (
                                                residence_name text,
                                                address text,
                                                front_desk_phone text,
                                                owner text,
                                                is_affiliated_housing boolean,
                                                on_campus boolean,
                                                URL text
                                            );"

docker exec -it postgres psql -U postgres -c "\copy campus_life.housing_options from '/data_files/Postgres-housing-options.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into campus_life.student_organizations
docker exec -it postgres psql -U postgres -c "CREATE TABLE campus_life.student_organizations (
                                                website_url text,
                                                email text,
                                                address text,
                                                phone_number text,
                                                organization_name text
                                            );"

docker exec -it postgres psql -U postgres -c "\copy campus_life.student_organizations from '/data_files/Postgres-organizations.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"

#Create table and ingest into campus_life.locations
docker exec -it postgres psql -U postgres -c "CREATE TABLE campus_life.locations (
                                                building_name text,
                                                description text,
                                                address text,
                                                phone text,
                                                email text,
                                                website text,
                                                zip_code text,
                                                campus text,
                                                sign_in_required boolean,
                                                student_accessible boolean
                                            );"

docker exec -it postgres psql -U postgres -c "\copy campus_life.locations from '/data_files/Postgres-locations.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';"