import numpy as np
import matplotlib.pyplot as plt

#change this var to path of desired csv or txt.
#delimiter must be a comma, may change to var later
data = 'data.csv'

#massL v time
x, y = np.loadtxt(data, skiprows=100, usecols=(11,2), delimiter=',', unpack=True,)

#massR v Time
x, z = np.loadtxt(data, skiprows=100, usecols=(11,3), delimiter=',', unpack=True)

#tempL v time
x, a = np.loadtxt(data, skiprows=100, usecols=(11,4), delimiter=',', unpack=True)

#tempR v time
x, b = np.loadtxt(data, skiprows=100, usecols=(11,5), delimiter=',', unpack=True)

#condL v time
x, c = np.loadtxt(data, skiprows=100, usecols=(11,6), delimiter=',', unpack=True)

#condR v time
x, d = np.loadtxt(data, skiprows=100, usecols=(11,7), delimiter=',', unpack=True)

#pHL v time
x, e = np.loadtxt(data, skiprows=100, usecols=(11,8), delimiter=',', unpack=True)

#pHR v Time
x, f = np.loadtxt(data, skiprows=100, usecols=(11,9), delimiter=',', unpack=True)

#fluxL v time
x, g = np.loadtxt(data, skiprows=100, usecols=(11,14), delimiter=',', unpack=True)

#fluxR v time
x, h = np.loadtxt(data, skiprows=100, usecols=(11,15), delimiter=',', unpack=True)


plt.figure(1)
plt.title('Draw Balance')
plt.xlabel('Time (min)')
plt.ylabel('Mass (g)')
plt.scatter(x,y, label='loaded from file')

plt.figure(2)
plt.title('Feed Balance')
plt.xlabel('Time (min)')
plt.ylabel('Mass (g)')
plt.scatter(x,z, label='loaded from file')

plt.figure(3)
plt.title('Draw Temperature')
plt.xlabel('Time (min)')
plt.ylabel('Temperature ($^\circ$C)')
plt.scatter(x,a, label='loaded from file')

plt.figure(4)
plt.title('Feed Temperature')
plt.xlabel('Time (min)')
plt.ylabel('Temperature ($^\circ$C)')
plt.scatter(x,b, label='loaded from file')

plt.figure(5)
plt.title('Draw Conductivity')
plt.xlabel('Time (min)')
plt.ylabel('Cond ($\mu$S/cm)')
plt.scatter(x,c, label='loaded from file')

plt.figure(6)
plt.title('Feed Conductivity')
plt.xlabel('time (min)')
plt.ylabel('Cond ($\mu$S/cm)')
plt.scatter(x,d, label='loaded from file')

plt.figure(7)
plt.title('Draw pH')
plt.xlabel('time (min)')
plt.ylabel('pH')
plt.scatter(x,e, label='loaded from file')

plt.figure(8)
plt.title('Feed pH')
plt.xlabel('time (min)')
plt.ylabel('pH')
plt.scatter(x,f, label='loaded from file')

plt.figure(9)
plt.title('Draw Flux')
plt.xlabel('time (min)')
plt.ylabel('Flux (LMH)')
plt.scatter(x,g, label='loaded from file')

plt.figure(10)
plt.title('Feed Flux')
plt.xlabel('time (min)')
plt.ylabel('Flux (LMH)')
plt.scatter(x,h, label='loaded from file')


#below with display all 10 graphs at once. 
plt.show()
