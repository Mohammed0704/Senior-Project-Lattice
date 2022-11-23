#!/usr/bin/env bash

#copy postgres data into the postgres container
docker cp ./postgres/data_files postgres:/

#docker exec -it postgres psql -U postgres
docker exec -it postgres psql -U postgres -c "DROP SCHEMA IF EXISTS education CASCADE;"
docker exec -it postgres psql -U postgres -c "DROP TABLE IF EXISTS education.colleges;"

: '
DROP TABLE IF EXISTS education.departments;
DROP TABLE IF EXISTS education.programs;
DROP TABLE IF EXISTS education.areas_of_study;
DROP TABLE IF EXISTS education.student_education_choices;
DROP TABLE IF EXISTS campus_life.housing_options;
DROP TABLE IF EXISTS campus_life.student_organizations;
DROP TABLE IF EXISTS campus_life.locations;
DROP SCHEMA IF EXISTS education;
DROP SCHEMA IF EXISTS campus_life;

docker exec -it postgres psql -U postgres -c "CREATE SCHEMA education;" 

'
docker exec -it postgres psql -U postgres -c "CREATE SCHEMA education;" 

docker exec -it postgres psql -U postgres -c "CREATE TABLE education.colleges (
                                                name text primary key,
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


: '
CREATE TABLE education.departments (
    department_name text primary key,
    college_name text,
    description text,
    URL text,
    main_office_location text,
    main_office_phone text,
    department_head text,
    department_administrator text
);

\copy education.departments from '/data_files/Postgres-education-departments.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE education.programs (
    program_name text primary key,
    description text,
    is_graduate_program boolean,
    area_of_study text,
    credit_requirement decimal,
    is_stem boolean
);

\copy education.programs from '/data_files/Postgres-programs.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE education.areas_of_study (
    name text primary key,
    department text,
    act text,
    plan text
);

\copy education.areas_of_study from '/data_files/Postgres-area_of_study.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE education.student_education_choices (
    drexel_id text,
    first_name text,
    middle_name text,
    last_name text,
    majors text,
    minors text
);

\copy education.student_education_choices from '/data_files/Postgres-student_education_choices.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE campus_life.housing_options (
    residence_name text,
    address text,
    front_desk_phone text,
    owner text,
    is_affiliated_housing boolean,
    on_campus boolean,
    URL text
);

\copy campus_life.housing_options from '/data_files/Postgres-housing-options.csv' DELIMITER ',' CSV HEADER;

CREATE SCEHMA campus_life;

CREATE TABLE campus_life.student_organizations (
    website_url text,
    email text,
    address text,
    phone_number text,
    organization_name text
);

\copy campus_life.student_organizations from '/data_files/Postgres-organizations.csv ' DELIMITER ',' CSV HEADER;

CREATE TABLE campus_life.locations (
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
);

\copy campus_life.student_organizations from '/data_files/Postgres-locations.csv' DELIMITER ',' CSV HEADER;

'