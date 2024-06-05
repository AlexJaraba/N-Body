import numpy as np

G=0.000296014912


def writeInitialConditions():
    m1,m2 = 1.0, 0.5
    M = m1+ m2
    mu = m1*m2/M
    phi = 0.5 * np.pi
    a, e = 1.0, 0.8
    r = a * (1-e**2) / (1 + e*np.cos(phi))
    x,y,z = r * np.cos(phi) ,r * np.sin(phi),0
    vx,vy,vz = np.sqrt(G * M/a**3) * a / np.sqrt(1-e**2)* np.sin(phi),\
        np.sqrt(G * M/a**3) * a / np.sqrt(1-e**2)* (e + np.cos(phi)),\
        0
    
    
    x1,y1,z1 = -m2/M * x ,-m2/M * y ,-m2/M * z
    x2,y2,z2 = m1/M * x ,m1/M * y , m1/M * z
    vx1,vy1,vz1 = -m2/M * vx ,-m2/M * vy ,-m2/M * vz
    vx2,vy2,vz2 = m1/M * vx ,m1/M * vy , m1/M * vz

    print(m1,x1,y1,z1,vx1,vy1,vz1)
    print(m2,x2,y2,z2,vx2,vy2,vz2)
    
if __name__ == '__main__':
    writeInitialConditions()
