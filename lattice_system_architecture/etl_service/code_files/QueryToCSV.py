import datetime
import pandas as pd

class QueryToCSV:
    def writeQueryToCSV(self, tag, queryResultDataframe: pd.DataFrame, currentTime):
        time = None
        if currentTime is None:
            time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        else:
            time = currentTime

        #TODO: Time is currently not included in the CSV names; eventually, we would like to move previous data at a specific time to some sort of cache for saving previous entries
        #queryResultDataframe.to_csv("data_object_data/" + tag + "_" + time + ".csv".format()) #writes the query to a CSV file
        queryResultDataframe.to_csv("data_object_import_data/" + tag + ".csv".format(), index=False) #TODO: Abstract the directory path
        return time #time is returned so every query in the same timeframe has the same exact datetime