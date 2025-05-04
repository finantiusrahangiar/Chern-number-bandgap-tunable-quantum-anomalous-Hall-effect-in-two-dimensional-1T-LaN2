import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

kpath = []
Band = []

with open('Band_SOC.BANDDAT1', 'r') as fin:
    for line in fin:
        # Split the line into elements
        elements = line.split()

        # Check if the line has the expected number of elements
        if len(elements) == 2:
            kpath.append(float(elements[0]))
            Band.append(float(elements[1]))

# Convert lists to numpy arrays
kpath = np.array(kpath)
Band = np.array(Band)

kpath2 = []
Band2 = []

with open('Band.BANDDAT1', 'r') as fin:
    for line in fin:
        # Split the line into elements
        elements = line.split()

        # Check if the line has the expected number of elements
        if len(elements) == 2:
            kpath2.append(float(elements[0]))
            Band2.append(float(elements[1]))

# Convert lists to numpy arrays
kpath2 = np.array(kpath2)
Band2 = np.array(Band2)

BC = []
kx = []
ky = []

with open('BerryC59.dat', 'r') as fin:
    for line in fin:
        # Split the line into elements
        elements = line.split()

        # Check if the line has the expected number of elements
        if len(elements) == 3:
            BC.append(float(elements[0]))
            kx.append(float(elements[1]))
            ky.append(float(elements[2]))

# Convert lists to numpy arrays
BC = np.array(BC)
kx = np.array(kx)
ky = np.array(ky)