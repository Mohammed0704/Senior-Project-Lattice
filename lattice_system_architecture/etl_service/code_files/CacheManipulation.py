import os
from Serialization import Serialize
from Serialization import Deserialize 

def AppendToCache(filepath, dict):
    if not os.path.exists(filepath):
        open(filepath, "x")
    cacheData = Deserialize(filepath)
    cacheData.append(dict)
    Serialize(cacheData, filepath)

def DeleteFromCache(filepath, dict):
    if not os.path.exists(filepath):
        print("Cache file {} does not exist.".format(filepath))
        return
    try:
        cacheData = Deserialize(filepath)
        cacheData.remove(dict)
        Serialize(cacheData, filepath)
    except:
        print("Value could not be found in {}.".format(filepath))


if __name__ == "__main__":
    connectionTestDict = [
                            {
                            "connection_name": "MDB",
                            "connection_type": "MariaDB",
                            "connection_URL": "196.22.77.108:3306",
                            "connection_username": "user",
                            "connection_password": "pass"
                            },
                            {
                            "connection_name": "MonDB",
                            "connection_type": "MongoDB",
                            "connection_URL": "196.22.77.108:27017",
                            "connection_username": "root",
                            "connection_password": "password"
                            }
                        ]
    Serialize(connectionTestDict, "./ConnectionsTest.txt")
    
    AppendToCache("./ConnectionsTest.txt", {"connection_name": "Post", "connection_type": "Postgres", "connection_URL": "196.22.77.108:5432", "connection_username": "user", "connection_password": ""})
    DeleteFromCache("./ConnectionsTest.txt", {"connection_name": "Post", "connection_type": "Postgres", "connection_URL": "196.22.77.108:5432", "connection_username": "user", "connection_password": ""})

    print(Deserialize("./ConnectionsTest.txt"))