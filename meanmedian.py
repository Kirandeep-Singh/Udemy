#import pandas as pd

import numpy as np
import statistics

x=[1,5,7,3,63,7,8,4]

y= np.array(x)
print (len(y))

print (y)

print ("mean is :",y.mean())

print (np.median(x))
print (statistics.mode(y))

import random

print (random.randint(0,100000))
