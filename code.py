import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"] , show_hist=False)
fig.show()

population_mean = statistics.mean(data)
print("Mean of population = ",population_mean)
population_SD =  statistics.stdev(data)
print("SD of population = ",population_SD)


dataset =[]
for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
sD = statistics.stdev(dataset)
print("Mean of 1000 value is : ",mean)
print ("SD of 1000 values is : ",sD)


# mean of population is same as mean of sample
# SD of sample = SD Population / sqrt (number of data in each sample)  
# mean of population = 6.134910878918254
# mean of sampling = 6.226

# SD of population  = 3.2319184864194765
# SD of sampleing  =  3.153231178785797