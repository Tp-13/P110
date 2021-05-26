import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
dataSet = []

popMean = statistics.mean(data)

print("Population Mean: ", popMean)
""" fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show() """

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    sampMean = statistics.mean(dataSet)
    return(sampMean)

def showFig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def mean():
    mean_list = []
    for i in range (0, 100):
        setOfMeans = randomSetOfMeans(30)
        mean_list.append(setOfMeans)
    sampMean = statistics.mean(mean_list)
    print(sampMean)


def setUp():
    mean_list = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMeans(30)
        mean_list.append(setOfMeans)
    showFig(mean_list)

setUp()
mean()