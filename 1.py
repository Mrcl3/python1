import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy.optimize import curve_fit
import copy
import sys

def convertStr(s):
    """Convert string to either int or float."""
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret

def func(x, a, b, c):
	""" Definition of exponent""" 
	return a * np.exp(-b * x) +c

""" Definition of variables """
E=[]
CE=[]
Transmisson=[]
NewEnergy=[]
line_n=0
""" trying to open choosen file"""
try:
	data_file = open(input (str("Please enter the name of the file you wish to open:" )),"r")## Open the file and "r" read it
except IOError:
	print (" Could not open")
""" Reading lines from file and inserting them into lists"""
for line in data_file:
	line = line.split()
	line_n += 1
	if line_n < 100:
		continue
	if line_n > 1000:
		continue
	Ei = float(line[0])
	Ai = float(line[1])
	Zi = float(line[2])
	E.append(Ei)
	CE.append(Ai)
	Transmisson.append(Zi)
	n=Ai/Zi
	NewEnergy.append(n)

fig1=plt.figure()
plt.plot(E,NewEnergy)
plt.hold(True)
plt.show(block=False)
Enp = np.array(E)
NEnp = np.array(NewEnergy)
Earr=copy.copy(Enp)
NewEnergyarr=copy.copy(NEnp)
E1 = input("Podaj E1 (eV) : ")
E2 = input("Podaj E2 (eV) : ")
e1=convertStr(E1)//10-100
e2=convertStr(E2)//10-100
del E[e1:e2]
del NewEnergy[e1:e2]
plt.plot(E,NewEnergy)
plt.xlim(1000,10000)
plt.ylim(0,500000)
popt, pcov = curve_fit(func, Earr, NEnp,p0 = (100000, 1e-6,1), maxfev=20000)
print (popt[0],popt[1],popt[2])
yy=func(Enp,popt[0],popt[1],popt[2])
plt.plot(Enp,yy, lw='2')
plt.show(block=False)

""" Asking if fit is correct"""
answer = str(input("Is the fitting correct? Enter Y for yes or N for no "))
proceed="y" or "Y" 
if answer.lower() in ['y','yes','Y','Yes','Tak','tak']:
	print("Calculation correct")
	plt.close()
else:
	exit()

fig2=plt.figure()
plt.plot(Enp,np.subtract(NewEnergyarr,yy))
plt.xlim(1000,6000)
plt.savefig(str(input("Podaj nazwe wykresu: ")))
plt.show(block=False)
quit()
