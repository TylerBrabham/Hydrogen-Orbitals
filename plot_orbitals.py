# Tyler Brabham
# Phys 137A Fall 2013
# HW 11

'''
Opens the four plots in order. User can save plot once it opens
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_s1():
	fig = plt.figure()

	X = np.arange(-10, 10, 0.1)
	Z = np.arange(-10, 10, 0.1)
	X, Z = np.meshgrid(X, Z)

	R = np.sqrt(X**2 + Z**2)
	f = R**2 * (1/np.pi)*np.exp(-2*R)
	plt.contourf(X, Z, f, 18, alpha=1, cmap='hot')

	plt.show()
	plt.close()

def plot_s2():
	fig = plt.figure()

	X = np.arange(-20, 20, 0.1)
	Z = np.arange(-20, 20, 0.1)
	X, Z = np.meshgrid(X, Z)

	R = np.sqrt(X**2 + Z**2)
	f = R**2 * (1/(8*np.pi))*(1 - R/2)**2 * np.exp(-1*R)
	plt.contourf(X, Z, f, 18, alpha=1, cmap='hot')

	plt.show()
	plt.close()

def plot_2p0():
	fig = plt.figure()

	X = np.arange(-20, 20, 0.1)
	Z = np.arange(-20, 20, 0.1)
	X, Z = np.meshgrid(X, Z)

	R = np.sqrt(X**2 + Z**2)
	f = R**2 * (1/(32*np.pi))* (Z**2) * np.exp(-1*R)
	plt.contourf(X, Z, f, 18, alpha=1, cmap='hot')

	plt.show()
	plt.close()

def plot_3d0():
	fig = plt.figure()

	X = np.arange(-22, 22, 0.05)
	Z = np.arange(-22, 22, 0.05)
	X, Z = np.meshgrid(X, Z)

	R = np.sqrt(X**2 + Z**2)
	f = R**2 * (1/(81*81*6*np.pi))* (R**4) * np.exp(-.66666667*R) * ((3*(Z**2)/(R**2)) - 1)**2
	plt.contourf(X, Z, f, 18, alpha=1, cmap='hot')

	plt.show()
	plt.close()


plot_s1()

plot_s2()

plot_2p0()

plot_3d0()