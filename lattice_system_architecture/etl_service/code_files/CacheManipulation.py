import os
from Serialization import Serialize
from Serialization import Deserialize


class CacheManipulation():
    # Check if the key value exists and if found, return the entire dictionary where the key value is found
    def CheckIfKeyValueAlreadyExists(self, keyName, keyValue, cacheData):
        for dict in cacheData:
            if dict[keyName] == keyValue:
                return dict
        return None

    # Append full dict to cache file. Create empty cache file if it doesn't already exist
    def AppendToCache(self, filepath, keyName, dict):
        if not os.path.exists(filepath):
            open(filepath, "x")
        cacheData = Deserialize(filepath)

        # if the key name is not expected to be in the current cache structure
        if len(cacheData) > 0: 
            if cacheData[0].get(keyName) == None:
                print("Failure to append: Key name \"{}\" could not be found in \"{}\"".format(keyName, filepath))
                return
            if dict.get(keyName) == None:
                print("Failure to append: Key name \"{}\" could not be found in dict".format(keyName))
                return

        keyValue = dict[keyName]
        if not self.CheckIfKeyValueAlreadyExists(keyName, keyValue, cacheData):
            cacheData.append(dict)
            Serialize(cacheData, filepath)
        else:
            print("Failure to append: The key value \"{}\" is already in use".format(keyValue))

    # Used to remove dict value from cache file based on itemValue of keyName
    def DeleteFromCache(self, filepath, keyName, keyValue):
        if not os.path.exists(filepath):
            print("Failure to remove: Cache file \"{}\" does not exist".format(filepath))
            return
        cacheData = Deserialize(filepath)

        # if the key name is not in the current cache data
        if len(cacheData) > 0: 
            if cacheData[0].get(keyName) == None:
                print("Failure to remove: Key name \"{}\" could not be found in \"{}\"".format(keyName, filepath))
                return

        dictToRemove = self.CheckIfKeyValueAlreadyExists(keyName, keyValue, cacheData)
        if dictToRemove:
            cacheData.remove(dictToRemove)
            Serialize(cacheData, filepath)
        else:
            print("Failure to remove: The key value \"{}\" does not exist".format(keyValue))

if __name__ == "__main__":
    #for testing purposes, uncomment the object and Serialize call below temporarily if the test file does not yet exist
    '''connectionTestDict = [
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
    Serialize(connectionTestDict, "./ConnectionsTest.txt")'''

    cacheManipulation = CacheManipulation()
    
    # cacheManipulation.AppendToCache("./ConnectionsTest.txt", "connection_name", {"connection_name": "Post", "connection_type": "Postgres", "connection_URL": "196.22.77.108:5432", "connection_username": "user", "connection_password": ""})
    cacheManipulation.DeleteFromCache("./ConnectionsTest.txt", "connection_name", "Post")

    #print(Deserialize("./ConnectionsTest.txt"))