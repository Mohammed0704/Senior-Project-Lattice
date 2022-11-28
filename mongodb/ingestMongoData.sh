#!/usr/bin/env bash

#copy mariadb data into the mariadb container
docker cp ./mongodb/data_files mongo:/

docker cp ./mongodb/require.js mongo:/
docker exec -it mongo mongosh -u root -p root --eval "use classes
db.dropDatabase()
use classes"

docker exec -it mongo mongosh -u root -p root --eval "load('require.js');
db.software.insertMany(courseSoftwareJson);"

docker exec -it mongo mongosh -u root -p root --eval "use courses
db.dropDatabase()
use courses"

docker exec -it mongo mongosh -u root -p root --eval "load('require.js');
db.courses_info.insertMany(courseInfoJson);
db.courses_requirements.insertMany(courseReqsJson);"