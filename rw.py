# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:48:18 2019

@author: Kevin
"""

import matplotlib.pyplot as plt
import random 
position = 0
walk = [position]
steps =1000
for i in range(steps):
    step =1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
    
    
plt.plot(walk[:200])
