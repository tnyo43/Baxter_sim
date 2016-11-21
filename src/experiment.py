#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin

PI = np.pi
g = 9.81
FREQUENCY = 50.0


def ex01(sim_time = 10):
    name = "ex01/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.55 #T = 6s
        positions.append([x,y,z])

    return positions, name


def ex02(sim_time = 10):
    name = "ex02/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/2.0)+0.55 #T = 2s
        positions.append([x,y,z])

    return positions, name


