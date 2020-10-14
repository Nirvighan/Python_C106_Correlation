import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    temprature = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            temprature.append(float(row["Temperature"]))

        return {"x":ice_cream_sales,"y":temprature}

    print(ice_cream_sales)

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("CORRELATION BETWEEN ICE_CREAM AND TEMPRATURE SALES",correlation[0,1])

def setup():
    data_path = "data1.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()
