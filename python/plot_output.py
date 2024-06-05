import matplotlib.pyplot as plt
import numpy as np

def read_initial_conditions(filename):
    masses = []
    positions = []
    velocities = []

    with open(filename, 'r') as f:
        for line in f:
            data = line.split()
            masses.append(float(data[0]))
            positions.append([float(data[1]), float(data[2]), float(data[3])])
            velocities.append([float(data[4]), float(data[5]), float(data[6])])

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
    print(nlines,nbodies)
    return np.array(masses), np.array(x), np.array(y), np.array(z), np.array(vx), np.array(vy), np.array(vz) 

def plot_output(x,y,z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for xx,yy,zz in zip(x.T,y.T,z.T):
        print(xx)
        ax.plot(xx,yy,zz)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')
    plt.title('Final Positions of Bodies')

    plt.show()

if __name__ == "__main__":
    initial_masses, initial_positions, initial_velocities = read_initial_conditions('../data/initial_conditions.txt')
    #plot_initial_conditions(initial_positions)
    
    masses, x,y,z,vx,vy,vz = read_output('../data/output.txt')

    plot_output(x,y,z)
