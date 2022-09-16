# Python Based TVC simulator
#Imports 
import turtle
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
class constants:
    gravity = 9.81
    burnTime = 

#RocketSpecs & Inputs
totalMass = float(input("Rocket Mass, g"))
COMdistfromnoseconetop = float(input("Center of Mass distance from tip of nose cone, cm"))
COMdistfrommotor = float(input("Center of Mass distance from motor/bottom, cm"))
distCM = COMdistfrommotor + COMdistfromnoseconetop
# If possible implement live wind update, see if that can reinforce gyro readings
windSpeed = float(input("Wind Speed, mph"))
windDir = str(input("Cardinal Direction relative to rocket (n, s, e, w, nw, ne, sw, se, nne, nnw, sse, ssw, see, sww, nee, nww"))
def windDirAssign(windDir):
    if 
