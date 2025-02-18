import numpy as np
import sys

G=0.000296014912

def ElementsToCordinates(a,e,M):
    phi = 0.5 * np.pi
    theta = 0.5 * np.pi
    r = a * (1-e**2) / (1 + e*np.cos(phi))
    x,y,z = r * np.cos(phi),r * np.sin(phi), 0 #np.sqrt((r*np.cos(phi))**2+(r*np.sin(phi))**2)
    vx,vy,vz = np.sqrt(G * M/a**3) * a / np.sqrt(1-e**2)* np.sin(phi),\
        np.sqrt(G * M/a**3) * a / np.sqrt(1-e**2)* (e + np.cos(phi)),\
        0 #np.sqrt(((G * M/a**3) * a**2/(1-e**2) * (np.sin(phi))**2)+((G * M/a**3) * a**2/(1-e**2) * (e + np.sin(phi))**2))
    return x,y,z,vx,vy,vz

def writeInitialConditions(a,e,m1,m2):
    M = m1+ m2
    mu = m1*m2/M

    x,y,z,vx,vy,vz = ElementsToCordinates(a,e,M)

    x1,y1,z1 = -m2/M * x ,-m2/M * y ,-m2/M * z
    x2,y2,z2 = m1/M * x ,m1/M * y , m1/M * z
    vx1,vy1,vz1 = -m2/M * vx ,-m2/M * vy ,-m2/M * vz
    vx2,vy2,vz2 = m1/M * vx ,m1/M * vy , m1/M * vz

    return x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2

def ask_question(question):
    return input(f"{question}\nYour answer: ")

def main():
    numberofbodies = ask_question("How many Bodies?")
    if int(numberofbodies) == 2:
        masses_str = ask_question("What are the masses of the two bodies? (separate with commas)")
        try:
            m1_str, m2_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please enter the masses in the format 'mass1, mass2'")
            sys.exit(1)

        a_e_str = ask_question("What is a and e for the system? (seperate with commas)")
        try:
            a1_str, e1_str = a_e_str.split(',')
            a = float(a1_str.strip())
            e = float(e1_str.strip())
        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please enter the values in the format 'a, e'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a,e,m1,m2)
        print(m1,x1,y1,z1,vx1,vy1,vz1)
        print(m2,x2,y2,z2,vx2,vy2,vz2)
    if int(numberofbodies) == 3:
        masses_str = ask_question("What are the masses? (m1,m2,m3)")
        try:
            m1_str, m2_str, m3_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2)")
        try:
            a1_str, e1_str, a2_str, e2_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2,...'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        print(m1,x1+x12,y1+y12,z1+z12,vx1+vx12,vy1+vy12,vz1+vz12)
        print(m2,x2+x12,y2+y12,z2+z12,vx2+vx12,vy2+vy12,vz2+vz12)
        print(m3,x3,y3,z3,vx3,vy3,vz3)
    if int(numberofbodies) == 4:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str, e1_str, a2_str, e2_str, a3_str, e3_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123,y123,z123,vx123,vy123,vz123,x4,y4,z4,vx4,vy4,vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        print(m1,x1+x123,y1+y123,z1+z123,vx1+vx123,vy1+vy123,vz1+vz123)
        print(m2,x2+x123,y2+y123,z2+z123,vx2+vx123,vy2+vy123,vz2+vz123)
        print(m3,x3+x123,y3+y123,z3+z123,vx3+vx123,vy3+vy123,vz3+vz123)
        print(m4,x4,y4,z4,vx4,vy4,vz4)
    if int(numberofbodies) == 5:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str, m5_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
            m5 = float(m5_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
            
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str, e1_str, a2_str, e2_str, a3_str, e3_str, a4_str, e4_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
            a4 = float(a4_str.strip())
            e4 = float(e4_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123,y123,z123,vx123,vy123,vz123,x4,y4,z4,vx4,vy4,vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        print(m1,x1+x1234,y1+y1234,z1+z1234,vx1+vx1234,vy1+vy1234,vz1+vz1234)
        print(m2,x2+x1234,y2+y1234,z2+z1234,vx2+vx1234,vy2+vy1234,vz2+vz1234)
        print(m3,x3+x1234,y3+y1234,z3+z1234,vx3+vx1234,vy3+vy1234,vz3+vz1234)
        print(m4,x4+x1234,y4+y1234,z4+z1234,vx4+vx1234,vy4+vy1234,vz4+vz1234)
        print(m5,x5,y5,z5,vx5,vy5,vz5)
    if int(numberofbodies) == 6:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str, m5_str, m6_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
            m5 = float(m5_str.strip())
            m6 = float(m6_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str, e1_str, a2_str, e2_str, a3_str, e3_str, a4_str, e4_str, a5_str, e5_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
            a4 = float(a4_str.strip())
            e4 = float(e4_str.strip())
            a5 = float(a5_str.strip())
            e5 = float(e5_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123, y123, z123, vx123, vy123, vz123, x4, y4, z4, vx4, vy4, vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        x12345, y12345, z12345, vx12345, vy12345, vz12345, x6, y6, z6, vx6, vy6, vz6 = writeInitialConditions(a5,e5,m1+m2+m3+m4+m5,m6)

        print(m1,x1+x12345,y1+y12345,z1+z12345,vx1+vx12345,vy1+vy12345,vz1+vz12345)
        print(m2,x2+x12345,y2+y12345,z2+z12345,vx2+vx12345,vy2+vy12345,vz2+vz12345)
        print(m3,x3+x12345,y3+y12345,z3+z12345,vx3+vx12345,vy3+vy12345,vz3+vz12345)
        print(m4,x1+x12345,y4+y12345,z4+z12345,vx4+vx12345,vy4+vy12345,vz4+vz12345)
        print(m5,x5+x12345,y5+y12345,z5+z12345,vx5+vx12345,vy5+vy12345,vz5+vz12345)
        print(m6,x6,y6,z6,vx6,vy6,vz6)
    if int(numberofbodies) == 7:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str, m5_str, m6_str, m7_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
            m5 = float(m5_str.strip())
            m6 = float(m6_str.strip())
            m7 = float(m7_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str,e1_str,a2_str,e2_str,a3_str,e3_str,a4_str,e4_str,a5_str,e5_str,a6_str,e6_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
            a4 = float(a4_str.strip())
            e4 = float(e4_str.strip())
            a5 = float(a5_str.strip())
            e5 = float(e5_str.strip())
            a6 = float(a6_str.strip())
            e6 = float(e6_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123, y123, z123, vx123, vy123, vz123, x4, y4, z4, vx4, vy4, vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        x12345, y12345, z12345, vx12345, vy12345, vz12345, x6, y6, z6, vx6, vy6, vz6 = writeInitialConditions(a5,e5,m1+m2+m3+m4+m5,m6)
        x123456, y123456, z123456, vx123456, vy123456, vz123456, x7, y7, z7, vx7, vy7, vz7 = writeInitialConditions(a6,e6,m1+m2+m3+m4+m5+m6,m7)

        print(m1,x1+x123456,y1+y123456,z1+z123456,vx1+vx123456,vy1+vy123456,vz1+vz123456)
        print(m2,x2+x123456,y2+y123456,z2+z123456,vx2+vx123456,vy2+vy123456,vz2+vz123456)
        print(m3,x3+x123456,y3+y123456,z3+z123456,vx3+vx123456,vy3+vy123456,vz3+vz123456)
        print(m4,x4+x123456,y4+y123456,z4+z123456,vx4+vx123456,vy4+vy123456,vz4+vz123456)
        print(m5,x5+x123456,y5+y123456,z5+z123456,vx5+vx123456,vy5+vy123456,vz5+vz123456)
        print(m6,x6+x123456,y6+y123456,z6+z123456,vx6+vx123456,vy6+vy123456,vz6+vz123456)
        print(m7,x7,y7,z7,vx7,vy7,vz7)
    if int(numberofbodies) == 8:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str, m5_str, m6_str, m7_str, m8_str= masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
            m5 = float(m5_str.strip())
            m6 = float(m6_str.strip())
            m7 = float(m7_str.strip())
            m8 = float(m8_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str,e1_str,a2_str,e2_str,a3_str,e3_str,a4_str,e4_str,a5_str,e5_str,a6_str,e6_str,a7_str,e7_str= a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
            a4 = float(a4_str.strip())
            e4 = float(e4_str.strip())
            a5 = float(a5_str.strip())
            e5 = float(e5_str.strip())
            a6 = float(a6_str.strip())
            e6 = float(e6_str.strip())
            a7 = float(a7_str.strip())
            e7 = float(e7_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123, y123, z123, vx123, vy123, vz123, x4, y4, z4, vx4, vy4, vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        x12345, y12345, z12345, vx12345, vy12345, vz12345, x6, y6, z6, vx6, vy6, vz6 = writeInitialConditions(a5,e5,m1+m2+m3+m4+m5,m6)
        x123456, y123456, z123456, vx123456, vy123456, vz123456, x7, y7, z7, vx7, vy7, vz7 = writeInitialConditions(a6,e6,m1+m2+m3+m4+m5+m6,m7)
        x1234567, y1234567, z1234567, vx1234567, vy1234567, vz1234567, x8, y8, z8, vx8, vy8, vz8 = writeInitialConditions(a7,e7,m1+m2+m3+m4+m5+m6+m7,m8)

        print(m1,x1+x1234567,y1+y1234567,z1+z1234567,vx1+vx1234567,vy1+vy1234567,vz1+vz1234567)
        print(m2,x2+x1234567,y2+y1234567,z2+z1234567,vx2+vx1234567,vy2+vy1234567,vz2+vz1234567)
        print(m3,x3+x1234567,y3+y1234567,z3+z1234567,vx3+vx1234567,vy3+vy1234567,vz3+vz1234567)
        print(m4,x4+x1234567,y4+y1234567,z4+z1234567,vx4+vx1234567,vy4+vy1234567,vz4+vz1234567)
        print(m5,x5+x1234567,y5+y1234567,z5+z1234567,vx5+vx1234567,vy5+vy1234567,vz5+vz1234567)
        print(m6,x6+x1234567,y6+y1234567,z6+z1234567,vx6+vx1234567,vy6+vy1234567,vz6+vz1234567)
        print(m7,x7+x1234567,y7+y1234567,z7+z1234567,vx7+vx1234567,vy7+vy1234567,vz7+vz1234567)
        print(m8,x8,y8,z8,vx8,vy8,vz8)
    if int(numberofbodies) == 9:
        masses_str = ask_question("What are the masses? (m1,m2,m3,...)")
        try:
            m1_str, m2_str, m3_str, m4_str, m5_str, m6_str, m7_str, m8_str, m9_str = masses_str.split(',')
            m1 = float(m1_str.strip())
            m2 = float(m2_str.strip())
            m3 = float(m3_str.strip())
            m4 = float(m4_str.strip())
            m5 = float(m5_str.strip())
            m6 = float(m6_str.strip())
            m7 = float(m7_str.strip())
            m8 = float(m8_str.strip())
            m9 = float(m9_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the masses in the format 'mass1, mass2, mass3, etc.'")
            sys.exit(1)
        a_e_str = ask_question("What is a and e? (a1,e1,a2,e2,...)")
        try:
            a1_str,e1_str,a2_str,e2_str,a3_str,e3_str,a4_str,e4_str,a5_str,e5_str,a6_str,e6_str,a7_str,e7_str,a8_str,e8_str = a_e_str.split(',')
            a1 = float(a1_str.strip())
            e1 = float(e1_str.strip())
            a2 = float(a2_str.strip())
            e2 = float(e2_str.strip())
            a3 = float(a3_str.strip())
            e3 = float(e3_str.strip())
            a4 = float(a4_str.strip())
            e4 = float(e4_str.strip())
            a5 = float(a5_str.strip())
            e5 = float(e5_str.strip())
            a6 = float(a6_str.strip())
            e6 = float(e6_str.strip())
            a7 = float(a7_str.strip())
            e7 = float(e7_str.strip())
            a8 = float(a8_str.strip())
            e8 = float(e8_str.strip())
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the values in the format 'a1, e1, a2, e2, etc.'")
            sys.exit(1)

        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123, y123, z123, vx123, vy123, vz123, x4, y4, z4, vx4, vy4, vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        x12345, y12345, z12345, vx12345, vy12345, vz12345, x6, y6, z6, vx6, vy6, vz6 = writeInitialConditions(a5,e5,m1+m2+m3+m4+m5,m6)
        x123456, y123456, z123456, vx123456, vy123456, vz123456, x7, y7, z7, vx7, vy7, vz7 = writeInitialConditions(a6,e6,m1+m2+m3+m4+m5+m6,m7)
        x1234567, y1234567, z1234567, vx1234567, vy1234567, vz1234567, x8, y8, z8, vx8, vy8, vz8 = writeInitialConditions(a7,e7,m1+m2+m3+m4+m5+m6+m7,m8)
        x12345678, y12345678, z12345678, vx12345678, vy12345678, vz12345678, x9, y9, z9, vx9, vy9, vz9 = writeInitialConditions(a8,e8,m1+m2+m3+m4+m5+m6+m7+m8,m9)

        print(m1,x1+x12345678,y1+y12345678,z1+z12345678,vx1+vx12345678,vy1+vy12345678,vz1+vz12345678)
        print(m2,x2+x12345678,y2+y12345678,z2+z12345678,vx2+vx12345678,vy2+vy12345678,vz2+vz12345678)
        print(m3,x3+x12345678,y3+y12345678,z3+z12345678,vx3+vx12345678,vy3+vy12345678,vz3+vz12345678)
        print(m4,x4+x12345678,y4+y12345678,z4+z12345678,vx4+vx12345678,vy4+vy12345678,vz4+vz12345678)
        print(m5,x5+x12345678,y5+y12345678,z5+z12345678,vx5+vx12345678,vy5+vy12345678,vz5+vz12345678)
        print(m6,x6+x12345678,y6+y12345678,z6+z12345678,vx6+vx12345678,vy6+vy12345678,vz6+vz12345678)
        print(m7,x7+x12345678,y7+y12345678,z7+z12345678,vx7+vx12345678,vy7+vy12345678,vz7+vz12345678)
        print(m8,x8+x12345678,y8+y12345678,z8+z12345678,vx8+vx12345678,vy8+vy12345678,vz8+vz12345678)
        print(m9,x9,y9,z9,vx9,vy9,vz9)    
    if int(numberofbodies) == 98:
        a1, e1 = 0.387, 0.206
        a2, e2 = 0.7233, 0.007
        a3, e3 = 1, 0.017
        a4, e4 = 1.5273, 0.093
        a5, e5 = 5.2028, 0.048
        a6, e6 = 9.5388, 0.056
        a7, e7 = 19.1914, 0.046
        a8, e8 = 30.0611, 0.010

        m1 = 1
        m2 = 1.65829146e-7
        m3 = 2.44723618e-6
        m4 = 3e-6
        m5 = 3.22613065e-7
        m6 = 9.53768844e-4
        m7 = 2.85427136e-4
        m8 = 4.36180905e-5
        m9 = 5.12562814e-5


        x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = writeInitialConditions(a1,e1,m1,m2)
        x12, y12, z12, vx12, vy12, vz12, x3, y3, z3, vx3, vy3, vz3 = writeInitialConditions(a2,e2,m1+m2,m3)
        x123, y123, z123, vx123, vy123, vz123, x4, y4, z4, vx4, vy4, vz4 = writeInitialConditions(a3,e3,m1+m2+m3,m4)
        x1234, y1234, z1234, vx1234, vy1234, vz1234, x5, y5, z5, vx5, vy5, vz5 = writeInitialConditions(a4,e4,m1+m2+m3+m4,m5)
        x12345, y12345, z12345, vx12345, vy12345, vz12345, x6, y6, z6, vx6, vy6, vz6 = writeInitialConditions(a5,e5,m1+m2+m3+m4+m5,m6)
        x123456, y123456, z123456, vx123456, vy123456, vz123456, x7, y7, z7, vx7, vy7, vz7 = writeInitialConditions(a6,e6,m1+m2+m3+m4+m5+m6,m7)
        x1234567, y1234567, z1234567, vx1234567, vy1234567, vz1234567, x8, y8, z8, vx8, vy8, vz8 = writeInitialConditions(a7,e7,m1+m2+m3+m4+m5+m6+m7,m8)
        x12345678, y12345678, z12345678, vx12345678, vy12345678, vz12345678, x9, y9, z9, vx9, vy9, vz9 = writeInitialConditions(a8,e8,m1+m2+m3+m4+m5+m6+m7+m8,m9)

        print(m1,x1+x12345678,y1+y12345678,z1+z12345678,vx1+vx12345678,vy1+vy12345678,vz1+vz12345678)
        print(m2,x2+x12345678,y2+y12345678,z2+z12345678,vx2+vx12345678,vy2+vy12345678,vz2+vz12345678)
        print(m3,x3+x12345678,y3+y12345678,z3+z12345678,vx3+vx12345678,vy3+vy12345678,vz3+vz12345678)
        print(m4,x4+x12345678,y4+y12345678,z4+z12345678,vx4+vx12345678,vy4+vy12345678,vz4+vz12345678)
        print(m5,x5+x12345678,y5+y12345678,z5+z12345678,vx5+vx12345678,vy5+vy12345678,vz5+vz12345678)
        print(m6,x6+x12345678,y6+y12345678,z6+z12345678,vx6+vx12345678,vy6+vy12345678,vz6+vz12345678)
        print(m7,x7+x12345678,y7+y12345678,z7+z12345678,vx7+vx12345678,vy7+vy12345678,vz7+vz12345678)
        print(m8,x8+x12345678,y8+y12345678,z8+z12345678,vx8+vx12345678,vy8+vy12345678,vz8+vz12345678)
        print(m9,x9,y9,z9,vx9,vy9,vz9)

if __name__ == '__main__':
    main()


# Saved Cool Intial Conditions
    # 3_body
        # 1.0 -1.434428809234844e-16 -2.342600021873326 -0.0 -0.010598185760159489 -0.007418728861931936 -0.0
        # 1e-07 -8.223503390209968e-17 -1.3430000218733258 0.0 0.006610341049520499 -0.0070745583257383355 0.0
        # 2.0 7.17214445734939e-17 1.171300078086664 0.0 0.005299092549562692 0.003709364784693885 0.0
    # Solar System
# 1 -9.421610931366106e-20 -0.0015386658321282184 -0.0 -1.6542993744312415e-07 -2.572916011539909e-09 -0.0
# 1.66e-07	-2.53e-01	2.20e-01	4.12e-02	-2.42e-02	-2.01e-02	5.78e-04
# 2.45e-06	-1.91e-01	6.93e-01	2.06e-02	-1.96e-02	-5.50e-03	1.05e-03
# 3.23e-07	4.70e-02	-1.02e+00	5.93e-05	1.69e-02	7.27e-04	-3.32e-07
# 3.00e-06	1.39e+00	1.34e-01	-3.13e-02	-8.09e-04	1.51e-02	3.37e-04
# 9.54e-04	2.42e+00	4.40e+00	-7.24e-02	-6.71e-03	3.99e-03	1.33e-04
# 2.86e-04	9.27e+00	-2.80e+00	-3.20e-01	1.30e-03	5.33e-03	-1.44e-04
# 4.36e-05	1.17e+01	1.57e+01	-9.37e-02	-3.19e-03	2.18e-03	4.92e-05
# 5.13e-05	2.99e+01	-1.24e+00	-6.63e-01	1.04e-04	3.16e-03	-6.73e-05