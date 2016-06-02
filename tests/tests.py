from schematax import *
"""
Testing functionaliity of the schemata package

"""
import time

import random

timesf = []
timess = []
for t in xrange(50):
    xs = []

    for _ in range(t):

        string = ""
        for i in range(10):
            string += str(random.randint(0,1))
        xs.append(string)

    start = time.clock()       
    ssn = complete_fast(xs)
    end = time.clock()
    nt= end - start
    timesf.append(nt)
    
    start = time.clock()
    ssf = complete(xs)
    end = time.clock()
    ft =  end - start
    timess.append(ft)
    print ft,nt
    if len(ssf) - len(ssn) !=0:
       print 'fucked'
       break

import matplotlib.pyplot as plt

plt.plot(timesf,color='red')
plt.plot(timess)
plt.show()

