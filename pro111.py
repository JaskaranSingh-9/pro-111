import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv,statistics,random
import pandas as pd

df = pd.read_csv("C:/Users/jaska/OneDrive/Desktop/data/python/class/projects/pro 110/medium_data.csv")
data = df["id"].tolist()
population_mean = statistics.mean(data)
print("Population mean = ", population_mean)
population_stdev = statistics.stdev(data)
print("Population stdev = ", population_stdev)
def random_set(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,1000):
    SetOfMean = random_set(100)
    meanlist.append(SetOfMean)
stdDev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)
firststdDevStart, firststdDevEnd = mean - stdDev, mean + stdDev
secondstdDevStart, secondstdDevEnd = mean - (2*stdDev), mean + (2*stdDev)
thirdstdDevStart, thirdstdDevEnd = mean - (3*stdDev), mean + (3*stdDev)
df = pd.read_csv("C:/Users/jaska/OneDrive/Desktop/data/python/class/projects/pro 110/medium_data.csv")
data = df["id"].to_list()
meanOfSample = statistics.mean(data)
print("Mean of Sampling Distribution", meanOfSample)
fig = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
fig.show()
zScore = (meanOfSample - mean)/stdDev
print("Z Score is = ", zScore)