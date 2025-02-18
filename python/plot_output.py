import matplotlib.pyplot as plt
import numpy as np

import numpy as np

def read_initial_conditions(filename):
    masses = []
    positions = []
    velocities = []

    with open(filename, 'r') as f:
        for line in f:
            data = line.split()
            data = data[1:]  # Skip the first column (time)

            num_bodies = len(data) // 7  # Each body has 7 values (mass + position + velocity)
            for i in range(num_bodies):
                masses.append(float(data[i * 7]))
                positions.append([float(data[i * 7 + 1]), float(data[i * 7 + 2]), float(data[i * 7 + 3])])
                velocities.append([float(data[i * 7 + 4]), float(data[i * 7 + 5]), float(data[i * 7 + 6])])

    return np.array(masses), np.array(positions), np.array(velocities)

def plot_initial_conditions(positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for pos in positions:
        ax.scatter(pos[0], pos[1], pos[2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')
    plt.title('Initial Positions of Bodies')
    plt.show()

def read_output(filename):
    nbodies = 0
    f = open(filename)
    firstline = f.readline()
    data = firstline.split()
    while (len(data) > (nbodies*7 + 1)): nbodies += 1
    f.close()

    masses = []
    x,y,z = [],[],[]
    vx,vy,vz = [],[],[]
    nlines = 0
    
    with open(filename, 'r') as f:
        for line in f:
            data = line.split()
            xx,yy,zz = [],[],[]
            vvxx,vvyy,vvzz = [],[],[]
            for n in range(nbodies):
                masses.append(float(data[n*7 + 1]))
                xx.append(float(data[n*7 + 2]))
                yy.append(float(data[n*7 + 3]))
                zz.append(float(data[n*7 + 4]))
                vvxx.append(float(data[n*7 + 5]))
                vvyy.append(float(data[n*7 + 6]))
                vvzz.append(float(data[n*7 + 7]))
            x.append(xx)
            y.append(yy)
            z.append(zz)
            vx.append(vvxx)
            vy.append(vvyy)
            vz.append(vvzz)
            nlines += 1
    return np.array(masses), np.array(x), np.array(y), np.array(z), np.array(vx), np.array(vy), np.array(vz) 

def plot_output(x,y,z):
    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(111,projection='3d')

    for xx,yy,zz in zip(x.T,y.T,z.T):
        print(xx)
        ax.plot(xx,yy,zz,'.')
        # ax.plot(xx-x[:,0],yy-y[:,0],zz-z[:,0],'.',ms=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(masses, loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid('True')
    plt.title('Simulated Bodies Positions')

    plt.show()

def plot_energy_output():
    H = open('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/param.txt')
    runtime = H.readlines()[1]
    H = open('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/param.txt')
    G_constant = H.readlines()[4]
    tf = float(runtime.split()[1])
    G = float(G_constant.split()[1])

    masses,x,y,z,vx,vy,vz,nlines, nbodies = read_output('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/output.txt')
    time = np.linspace(0,tf,nlines)
    Kinetic = np.zeros(nlines)
    Potential = np.zeros(nlines)

    for i in range(nlines):
        for j in range(nbodies):
            v = (vx[i,j])**2 + (vy[i,j])**2 + (vz[i,j])**2
            K = 0.5 * masses[j] * v
            Kinetic[i] += K
            for k in range(j+1,nbodies):
                r = ((x[i,j] - x[i,k]))**2 + ((y[i,j] - y[i,k]))**2 + ((z[i,j] - z[i,k]))**2
                U = (-1 * G * masses[k] * masses[j])/np.sqrt(r)
                Potential[i] += U

    M = Potential + Kinetic
    M_rel = np.abs((M - M[0])/M[0])

    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(111)
    plt.plot(time,M_rel)
    ax.set_box_aspect(None)
    plt.show()
    
def plot_energy(filename):
    f = open(filename)
    firstline = f.readline()
    data = firstline.split()
    f.close()

    masses,x,y,z,vx,vy,vz,nlines, nbodies = read_output('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/output.txt')
    H = open('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/param.txt')
    runtime = H.readlines()[1]
    tf = float(runtime.split()[1])
    time = np.linspace(0,tf,nlines)
    
    plt.plot(time[0:64],data)
    plt.show()
    

    

if __name__ == "__main__":
    # initial_masses, initial_positions, initial_velocities = read_initial_conditions('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/output.txt')
    masses, x, y, z, vx, vy, vz = read_output('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/output.txt')
    d = 1
    if d == 1:
        plot_output(x,y,z)
    if d == 2: 
        plot_energy_output()
    if d == 3:
        plot_energy('C:/Users/alexj/OneDrive/Apps/Code/FewBodyNC/data/output.txt')
