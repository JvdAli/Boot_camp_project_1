import pandas as pd
import pymongo
import json
#from pymongo.mongo_client import MongoClient
client = "mongodb+srv://jvdaliMG:<jvdaliMG123>@cluster0.uqobmge.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"D:\DS-AB\Project\B-Camp\Data\train.csv")   # data file path in local machine
DATABASE = "Machine_learning_data"  # defining database name for mongodb
COLLECTION_NAME = "DATASET"    # records are known as collections in mongodb

if __name__ == "__main__":     # this is used in python to filter the output as per needs
    df = pd.read_csv(DATA_FILE_PATH)      # reading data using pandas library
    print(f"Rows & Columns of our dataset: {df.shape}")
    df.reset_index(drop = True, inplace = True)  #droping the index column
    json_records = list(json.loads(df.T.to_json()).values())  # T=transpose/convert the data into json format
    print(json_records[0])            # printing the first record to check the data
    client[DATABASE][COLLECTION_NAME].insert_many(json_records) # inserting all data to mongodb