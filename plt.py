#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

dx, dy = [], [] #nr_dirty
with open("./nr_dirty", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        dx.append(value[0])
        dy.append(value[1])



btx, bty = [], [] #nr_dirty_background_threshold
with open("./nr_dirty_background_threshold", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        btx.append(value[0])
        bty.append(value[1])
        
        
plt.plot(dx, dy, color = "blue", linestyle = "-", label = "nr_dirty")
plt.plot(btx, bty, color = "red", linestyle = "--", label = "bg_thresh")
plt.show()
