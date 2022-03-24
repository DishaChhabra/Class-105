import pandas as pd
import math
import statistics

alldata = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/Standard_deviation/master/graphs/class1.csv')
data = alldata['Marks']

sum = 0
for i in data:
    sum = sum+i

mean = sum/len(data)
print(mean)

squares = []
for i in data:
    a = i-mean
    sq = a**2
    squares.append(sq)

add = 0
for i in squares:
    add = add+i

stddeviation = math.sqrt(add/(len(data)-1))
print(stddeviation)

std = statistics.stdev(data)
print(std)

