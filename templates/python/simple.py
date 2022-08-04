""" 
 Simple Simulation without any additional software as referenced by 
 with types and a few minor enhancements 
 Introduction to the Modeling and Analysis of Complex Systems 
 Sayama pg 41

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from typing import List

x: float #x output state variable
t: float #time state variable
r: float = 1.1 #growth rate 
timesteps: List[float]


def initialize():
  global x, result, t, timesteps
  x = .1 
  t = 0
  timesteps = [t]
  result = [x]

def observe():
    global x, result, t, timesteps
    timesteps.append(t)
    result.append(x)

def update():
    global x, result, t, r
    x = r * x
    t = t + 1 

initialize()
while t < 30:
  update()
  observe()

plt.plot(timesteps, result)