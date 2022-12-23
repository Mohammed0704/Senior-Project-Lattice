#!/usr/bin/env bash

set isWindows = 0

#checks if the machine is Windows and provides alternate commands if so
winpty || set isWindows = 1
RESULT=$?
if [[ $isWindows == 0 ]]; then

    #copy mariadb data into the mariadb container
    docker cp ./mongodb/data_files mongo:/
    docker cp ./mongodb/require.js mongo:/

    winpty docker exec -it mongo mongosh -u root -p root --eval "use classes" --eval "db.dropDatabase()"

    winpty docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.software.insertMany(courseSoftwareJson)"
    winpty docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.classes_info.insertMany(classInfoJson)"
    winpty docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.classes_instruction_info.insertMany(classInstrInfoJson)"


    winpty docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "db.dropDatabase()"

    winpty docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "load('require.js')" --eval "db.courses_info.insertMany(courseInfoJson)"
    winpty docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "load('require.js')" --eval "db.courses_requirements.insertMany(courseReqsJson)"
else
        #copy mariadb data into the mariadb container
    docker cp ./mongodb/data_files mongo:/
    docker cp ./mongodb/require.js mongo:/

    docker exec -it mongo mongosh -u root -p root --eval "use classes" --eval "db.dropDatabase()"

    docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.software.insertMany(courseSoftwareJson)"
    docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.classes_info.insertMany(classInfoJson)"
    docker exec -it mongo mongosh -u root -p root --eval "use classes;" --eval "load('require.js')" --eval "db.classes_instruction_info.insertMany(classInstrInfoJson)"


    docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "db.dropDatabase()"

    docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "load('require.js')" --eval "db.courses_info.insertMany(courseInfoJson)"
    docker exec -it mongo mongosh -u root -p root --eval "use courses;" --eval "load('require.js')" --eval "db.courses_requirements.insertMany(courseReqsJson)"
fi