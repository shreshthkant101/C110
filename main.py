import plotly.figure_factory as ff
import plotly.graph_objects as gob
import csv
import statistics as st
import random as r
import pandas as pd

"""with open("data1.csv") as file:
    data = csv.reader(file)

    datalist = data['temp'].tolist()

    datalist = pd.
"""

dataframe = pd.read_csv("data.csv")

datalist = dataframe['average'].tolist()

    #print(datalist)


dataPoints = []

for i in range(0,100):
    ind = r.randint(0,len(datalist)) // 1
    valueToBeAdded = datalist[ind]

    dataPoints.append(valueToBeAdded)

mean = st.mean(dataPoints)

std = st.stdev(dataPoints)

print(mean)
print(std)

fig = ff.create_distplot([dataPoints],["Average"],show_hist=False)

fig.add_trace(gob.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))

fig.show()



"""
mean = st.mean(datalist)

fig = ff.create_distplot([datalist],["Temprature"],show_hist=False)

fig.add_trace(gob.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))



#std = st.stdev(datalist)

#print(std)


fig.show()
"""