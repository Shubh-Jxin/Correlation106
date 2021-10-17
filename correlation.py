import csv
import numpy as np

import pandas as pd
import plotly.express as pl

coffee = []
sleep = []
marks = []
days = []

poppedData1 = []
poppedData2 = []

result1 = ''
result2 = ''

def getDataSource():

    with open("cups of coffee vs hours of sleep.csv") as f1:
        data1 = csv.reader(f1)

        for i in data1:
            poppedData1.append(i)

        poppedData1.pop(0)

        for item in poppedData1:
            coffee.append(float(item[1]))
            sleep.append(float(item[2]))

    with open("Student Marks vs Days Present.csv") as f2:
        data2 = csv.reader(f2)

        for i in data2:
            poppedData2.append(i)

        poppedData2.pop(0)

        for item in poppedData2:
            marks.append(float(item[1]))
            days.append(float(item[2]))

def findCorrelation():
    result1 = np.corrcoef(coffee,sleep)

    print("The correlation between coffee and sleep is :",str(result1[0,1]))

    result2 = np.corrcoef(marks,days)

    print("The correlation between attendance and marks is :" , str(result2[0,1]))

def plotFigure():
    data_csv1 = pd.read_csv("cups of coffee vs hours of sleep.csv")
    data_csv2 = pd.read_csv("Student Marks vs Days Present.csv")

    graph1 = pl.scatter(data_csv1,x='Coffee in ml',y='sleep in hours')
    graph2 = pl.scatter(data_csv2,x = 'Marks In Percentage',y = 'Days Present')

    graph1.show()
    graph2.show()

def setup():
    getDataSource()
    findCorrelation()
    plotFigure()

setup()