import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd
import random
import csv

df = pd.read_csv("data.csv")
data = df["writing score"].tolist()

mean = sum(data)/len(data)
std_devition = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start,first_std_deviation_end = mean - std_devition, mean + std_devition
second_std_deviation_start,second_std_deviation_end = mean - (2*std_devition), mean + (2*std_devition)
third_std_deviation_start,third_std_deviation_end = mean - (3*std_devition), mean + (3*std_devition)

fig = ff.create_distplot([data], ["writing score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))

fig.show()


list_of_data_within_1_std_deviation=[r for r in data if r > first_std_deviation_start and r <first_std_deviation_end]
list_of_data_within_2_std_deviation=[r for r in data if r > second_std_deviation_start and r <second_std_deviation_end]
list_of_data_within_3_std_deviation=[r for r in data if r > third_std_deviation_start and r <third_std_deviation_end]


print("The standard deviation is", std_devition)
print("The mean is {}".format(mean))
print("The median is{}".format(median))
print("The mode is{}".format(mode))
print("Standard deviation of this data is {}".format(std_devition))
print("{}% of data lines within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lines within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lines within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

