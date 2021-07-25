import numpy as np
import csv

def setUp():
    dataPath = './data.csv'
    dataSource = getDataSource(dataPath)
    findCorelation(dataSource)


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation Between Marks in Percentage and Days Present', correlation[0,1])


def getDataSource():
    marks = []
    daysPresent = []
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            daysPresent.append(float(row['Days Present']))
    return{"x":marks, "y":daysPresent}

setUp()
