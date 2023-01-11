#import csv
import json
import yaml #pip install pyyaml

taggedColumnsList = [
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
                        ]


#def serializeYamlDictList(data, filePath):
#    with open(filePath, "w+") as yamlFile:
#        yaml.dump(data, yamlFile, default_flow_style=False)

#serializeTextDictList
def Serialize(data, filePath):
    with open(filePath, "w+") as file:
        json.dump(data, file, indent=4)

# def serializeCsvDictList(data, filePath):
#     keys = data[0].keys()
#     with open(filePath, "w+", newline='') as csvFile:
#         dict_writer = csv.DictWriter(csvFile, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(data)

#deserializeYamlDictList
def Deserialize(filePath):
    with open(filePath, 'r') as yamlFile:
        data = yaml.safe_load(yamlFile)
    return data


#def deserializeTextDictList(filePath):
#    with open(filePath, 'r') as file:
#        data = json.load(file)
#    return data

if __name__=="__main__":
    Serialize(taggedColumnsList, "./serialize_test.txt")
    deserializedTestObject = Deserialize("./serialize_test.txt")
    print(deserializedTestObject[0]["tag_name"])
