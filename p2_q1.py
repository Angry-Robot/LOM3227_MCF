import numpy as np
from numpy import pi as pi
import scipy.integrate as spi
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Defining the ODE #################################################################################
#   ((d^2)/(dt^2))*theta(t) + b*(d/dt)*theta(t) + c*sin(theta(t)) = 0
#   (d/dt)*theta(t) = omega(t)
#   (d/dt)*omega(t) = -b*omega(t) - c*sin(theta(t))

#   omega(t)        = (d/dt)*theta(t)         = Dtheta
#   (d/dt)*omega(t) = ((d^2)/(dt^2))*theta(t) = DDtheta

#   DDtheta = -b*Dtheta - c*sin(theta(t))
def pendulum(y, t, b, c):
    theta, Dtheta = y
    dydt = [Dtheta, -b*Dtheta - c*np.sin(theta)]
    return dydt

#####################
#                   #  
#   Questão 1-a)    #
#                   #  
#####################
# Parameters for solving the ODE ###################################################################
g = 9.81                                                        # Gravity
l = 3                                                           # Lenght
c = g/l
b = 0
omega = (np.sqrt(g/l))
tau = (2*pi)/omega
theta0 = (pi/6)                                                 # Initially at this angle
Dtheta0 = 0                                                     # Initially at rest
tmax = tau
tmin = 0
y0 = [theta0, Dtheta0]
# t = np.linspace(tmin, tmax, 100)
h=0.01                                                          # Curve resolution
t = np.arange(tmin, tmax+h, h)                                  # "t" vector with steps for iteration
# Solving the ODE ##################################################################################
solution = odeint(pendulum, y0, t, args=(b, c), tfirst=False)   # 100x2 array [theta, Dtheta]
# ODE Aproximation #################################################################################
thetaAprox = theta0*np.cos(omega*t)
# Graph plot #######################################################################################
plt.figure(1)
plt.title('Questão 1-a)')
# plt.subplot(211)
plt.plot(t, solution[:, 0], 'rx', markersize=3, label='Theta(t)')
plt.plot(t, solution[:, 1], 'bo', markersize=2, label='(d/dt)*Theta(t)')
plt.plot(t, thetaAprox, 'g^', markersize=3, label='Theta(t) aproximation')
plt.legend(loc='best')
plt.xlabel('Time (seconds)')
plt.ylabel('Radians')
plt.grid(True)
plt.legend()
# plt.show()

#####################
#                   #  
#   Questão 1-b)    #
#                   #  
#####################
# Parameters for solving the ODE ###################################################################
theta0 = (pi/3)                                                 # Initially at this angle
y0 = [theta0, Dtheta0]
# Solving the ODE ##################################################################################
solution = odeint(pendulum, y0, t, args=(b, c), tfirst=False)   # 'tmax':2 array [theta, Dtheta]
# ODE Aproximation #################################################################################
thetaAprox = theta0*np.cos(omega*t)
# Graph plot #######################################################################################
plt.figure(2)
plt.title('Questão 1-b)')
# plt.subplot(212)
plt.plot(t, solution[:, 0], 'rx', markersize=3, label='Theta(t)')
plt.plot(t, solution[:, 1], 'bo', markersize=2, label='(d/dt)*Theta(t)')
plt.plot(t, thetaAprox, 'g^', markersize=3, label='Theta(t) aproximation')
plt.legend(loc='best')
plt.xlabel('Time (seconds)')
plt.ylabel('Radians')
plt.grid(True)
plt.legend()
# plt.show()

#####################
#                   #  
#   Questão 1-c)    #
#                   #  
#####################
# Parameters for solving the ODE ###################################################################
tmax = 4
tmin = 0
# t = np.linspace(tmin, tmax, 1000)
h=0.001                                                         # Curve resolution
t = np.arange(tmin, tmax+h, h)                                  # "t" vector with steps for iteration
# Solving the ODE ##################################################################################
solution = odeint(pendulum, y0, t, args=(b, c), tfirst=False)   # 100x2 array [theta, Dtheta]
biggestTheta = np.max(solution[1:,0])
biggestThetaIter = np.argmax(solution[1:,0])
tauiteration = t[np.argmax(solution[1:,0])]
print('\n')
print('\n')
print('Initial theta: ',theta0)
print('Biggest theta through iteration: ',biggestTheta)
print('size of vector "t": ',len(t))
print('Iteration of the biggest theta: ',biggestThetaIter)
print('Tau through iteration: ',tauiteration)
print('Tau through equation: ',tau)
print('The difference of both (Taprox - Tite) is: ',(tau-tauiteration))
print('')

#####################
#                   #  
#   Questão 1-d)    #
#                   #  
#####################
# Parameters for solving the ODE ###################################################################
tmax = 5
tmin = 0
theta0V = [(pi/12), (pi/6), (pi/4), (pi/3), (5*pi/12), (pi/2)]      # Initially at this angle
tauiterationV = np.zeros(6)
for n in range(len(theta0V)) :
    y0 = [theta0V[n], Dtheta0]
    # t = np.linspace(tmin, tmax, 1000)
    h=0.001                                                         # Curve resolution
    t = np.arange(tmin, tmax+h, h)                                  # "t" vector with steps for iteration
    # Solving the ODE ##################################################################################
    solution = odeint(pendulum, y0, t, args=(b, c), tfirst=False)   # 100x2 array [theta, Dtheta]
    tauiterationV[n] = t[np.argmax(solution[1:,0])]

print('The theta values are: ')
print(theta0V[:])
print('The tau values are: ')
print(tauiterationV[:])

plt.figure(3)
plt.title('Questão 1-c)')
# plt.subplot(212)
plt.plot(theta0V, tauiterationV, 'kv', markersize=8, label='Theta(t)')
plt.legend(loc='best')
plt.xlabel('Initial theta (radians)')
plt.ylabel('Tau (1/s)')
plt.grid(True)
plt.legend()
# plt.show()

# Plot all the graphs #############################################################################
plt.show()