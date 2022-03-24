import math
from tracemalloc import Statistic
import pandas as pd
import math
import statistics

data=[60,61,65,63,98,99,90,95,91,96]

mean = statistics.mean(data)

squares = []
for i in data:
    a = (i-mean)**2
    squares.append(a)

sum=0
for i in squares:
    sum=sum+i

stdev=math.sqrt(sum/(len(data)-1))
print(stdev)

print(statistics.stdev(data))

