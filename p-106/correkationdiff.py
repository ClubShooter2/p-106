import csv 
import numpy as np

def getDataSource(data_path):
    Roll_No = []
    Days_Present = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Roll_No.append(float(row["Roll No"]))
            Days_Present.append(float(row["Days Present"]))

    return {"x": Roll_No, "y":Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between  Roll_No and Days Present:-  \n--->",correlation[0,1])

def setup():
    data_path = "data.csv"

    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()
