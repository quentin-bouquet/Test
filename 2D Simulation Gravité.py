import numpy as np
import matplotlib.pyplot as plt

dt = 0.005                       #en sec
tf = 30
time = np.arange(0, tf, dt)

point1 = (3, 3)
point2 = (0, -3)
point3 = (-2, 0)

m1 = 10                          #en kg*10**11
m2 = 10                          #en kg*10**11
m3 = 30                          #en kg*10**11

a1 = (0,0)
a2 = (0,0)
a3 = (0,0)
v1 = (-5,0)
v2 = (3,4)
v3 = (2,-2)

G = 6.674

def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

frame = None
n=0
for t in time:

    D12 = dist(point1, point2)
    D13 = dist(point1, point3)
    D23 = dist(point2, point3)
    vect_r21 = ((point1[0] - point2[0]), (point1[1] - point2[1]))/D12**2
    vect_r31 = ((point1[0] - point3[0]), (point1[1] - point3[1]))/D13**2
    vect_r32 = ((point2[0] - point3[0]), (point2[1] - point3[1]))/D23**2
    a1 = -G*m2/D12**2*vect_r21 - G*m3/D13**2*vect_r31
    a2 = G*m1/D12**2*vect_r21 - G*m3/D23**2*vect_r32
    a3 = G*m1/D13**2*vect_r31 + G*m2/D23**2*vect_r32

    v1 += a1*dt
    v2 += a2*dt
    v3 += a3*dt

    point1 += v1*dt
    point2 += v2*dt
    point3 += v3*dt

    n += 1
    if n%5 == 0:

        if frame:
            frame.remove()

        frame = ax.scatter(np.array([point1[0], point2[0], point3[0]]), np.array([point1[1], point2[1], point3[1]]), c=['b', 'r', 'g'], s=[5*m1, 5*m2, 3*m3], alpha = [1, 1, 0.6])
        plt.pause(0.001)

plt.show()