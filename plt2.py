#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

Dx, Dy = [], [] #nr_dirtied
with open("./nr_dirtied", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        Dx.append(value[0])
        Dy.append(value[1])

Wx, Wy = [], [] #nr_written
with open("./nr_written", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        Wx.append(value[0])
        Wy.append(value[1])

btx, bty = [], [] #nr_dirty_background_threshold
with open("./nr_dirty_background_threshold", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        btx.append(value[0])
        bty.append(value[1])
        
tx, ty = [], [] #nr_dirty_threshold
with open("./nr_dirty_threshold", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        tx.append(value[0])
        ty.append(value[1])

D0 = Dy[0]
W0 = Wy[0]
i = 0 
while i < 500:
    Dy[i] -= D0
    Wy[i] -= W0
    i += 1

plt.plot(Dx, Dy, color = "blue", linestyle = "-", label = "nr_dirtied")
plt.plot(Wx, Wy, color = "green", linestyle = "-", label = "bg_written")
plt.plot(btx, bty, color = "black", linestyle = "--", label = "bg_threshold")
plt.plot(tx, ty, color = "red", linestyle = "--", label = "threshold")
plt.show()
