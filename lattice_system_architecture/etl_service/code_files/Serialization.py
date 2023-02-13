#import csv
import json
#import yaml #pip install pyyaml

class Serialization():
    #serializeTextDictList
    @staticmethod
    def Serialize(data, filePath):
        with open(filePath, "w+") as file:
            json.dump(data, file, indent=4)

    #deserializeTextDictList
    @staticmethod
    def Deserialize(filePath):
        with open(filePath, 'r') as file:
            try:
                data = json.load(file)
            except:
                data = []
        return data

    #def serializeYamlDictList(data, filePath):
    #    with open(filePath, "w+") as yamlFile:
    #        yaml.dump(data, yamlFile, default_flow_style=False)

    # def serializeCsvDictList(data, filePath):
    #     keys = data[0].keys()
    #     with open(filePath, "w+", newline='') as csvFile:
    #         dict_writer = csv.DictWriter(csvFile, keys)
    #         dict_writer.writeheader()
    #         dict_writer.writerows(data)

    #def deserializeYamlDictList(filePath):
    #    with open(filePath, 'r') as yamlFile:
    #        data = yaml.safe_load(yamlFile)
    #        return data


if __name__=="__main__":
    '''taggedColumnsList = [
    {
    "tag_name": "Housing",
    "all_columns": 
    [
        "cassandra.finances.housing_costs.residence_name", 
        "cassandra.finances.housing_costs.room_style", 
        "cassandra.finances.housing_costs.maximum_monthly_cost", 
        "cassandra.finances.housing_costs.minimum_monthly_cost",
        "postgres.campus_life.housing_options.residence_name",
        "postgres.campus_life.housing_options.address",
        "postgres.campus_life.housing_options.is_affiliated_housing"
    ],
    "all_concat_columns":
    [
        {
            "concat_name": "test", "concat_columns": 
        [
            {
                "concat_column": "cassandra.finances.housing_costs.room_style",
                "concat_column_order": 1
            },
            {
                "concat_column": "cassandra.finances.housing_costs.maximum_monthly_cost",
                "concat_column_order": 2
            }
        ]
        },
        {
            "concat_name": "another_test", "concat_columns": 
        [
            {
                "concat_column": "postgres.campus_life.housing_options.address",
                "concat_column_order": 1
            },
            {
                "concat_column": "postgres.campus_life.housing_options.residence_name",
                "concat_column_order": 2
            }
        ]
        }
    ],
    "join_columns":
    [
        "cassandra.finances.housing_costs.residence_name",
        "postgres.campus_life.housing_options.residence_name"
    ],
    "all_tables":
    [
        "cassandra.finances.housing_costs",
        "postgres.campus_life.housing_options"
    ]
    }
    ]'''

    dataSourceConnectionsExample = [
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
    },
    {
    "connection_name": "Post",
    "connection_type": "Postgres",
    "connection_URL": "196.22.77.108:5432",
    "connection_username": "user",
    "connection_password": ""
    },
    {
    "connection_name": "ES",
    "connection_type": "Elasticsearch",
    "connection_URL": "196.22.77.108:9200",
    "connection_username": "admin",
    "connection_password": "admin"
    }
    ]

    tagsExample = [
    {
        "tag_name": "Student"
    }, 
    {
        "tag_name": "Student.join"
    },
    {
        "tag_name": "Employee"
    },
    {  
        "tag_name": "Employee.join"
    },
    {
        "tag_name": "Housing"
    },
    {
        "tag_name": "System"
    },
    {
        "tag_name": "Departments"
    },
    {
        "tag_name": "Colleges"
    },
    {
        "tag_name": "Program"
    }
    ]
    
    Serialization.Serialize(tagsExample, "./SerializedTags.txt")
    deserializedTestObject = Serialization.Deserialize("./SerializedTags.txt")
    print(deserializedTestObject)
