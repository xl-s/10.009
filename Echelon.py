# -*- coding: utf-8 -*-
'''
Created on Thu Jan 31 11:55:06 2019

@author: Xu Liang

This program solves systems of linear equations using Gauss-Jordan elimination.
'''

eqn = [[]] # Standardize that equation number starts from n = 1, so eqn[0] is empty
unknowns = 0 # For this program, number of equations will always equal number of unknowns
incomplete = False # Set to true if there are any free variables

def swap(first, second):
    # This function swaps the positions of two rows
    print("We are now swapping rows " + str(int(first)) + " and " + str(int(second)) + ".")
    temp = eqn[first]
    eqn[first] = eqn[second]
    eqn[second] = temp
    visualize()
    

def mult(row, multiple):
    # This function multiplies a row by a non-zero scalar
    print("We are now multiplying row " + str(int(row)) + " by " + str(multiple) + " times.")
    for n in range((unknowns+1)):
        eqn[row][n] = round((eqn[row][n] * multiple), 8)
    visualize()
    

def add(target, row, multiple):
    # This function adds the scalar multiple of one row to another
    print("We are now adding " + str(multiple) + " times of row " + str(int(row)) + " to row " + str(int(target)) + ".")
    for n in range((unknowns+1)):
        eqn[target][n] = round(eqn[target][n] + multiple * eqn[row][n], 8)
    visualize()
    

def visualize():
    # This function prints out a visualization of the matrix
    for n in range(len(eqn) - 1):
        print(eqn[n+1][1:], end=' ')
        print('['+str(eqn[n+1][0])+']')
    print("\n")
    
    
def intake():
    # Take input and convert it into a list
    inp = input("Please enter the first row of the linear system (Example: 2x + 4y = 1 ==> 2 4 1)\n")
    inp = list(map(float, inp.split()))
    global unknowns
    unknowns = len(inp) - 1
    
    # Rearrange the list into a format such that eqn[n][0] is the right hand side
    temp = inp[unknowns]
    for i in range(unknowns, 0, -1):
        inp[i] = inp[i-1]
    inp[0] = temp
    eqn.append(inp)
    
    # Take input and convert all of the other equations
    for i in range(unknowns - 1):
        if(i == unknowns - 2):
            inp = input("Please enter the last row in the same format:\n")
        else:
            inp = input("Please enter the next row in the same format:\n")
        inp = list(map(float, inp.split()))
        
        if (len(inp) != unknowns + 1):
            print("Please enter the row in a valid format.\n")
            break
        
        temp = inp[unknowns]
        for i in range(unknowns, 0, -1):
            inp[i] = inp[i-1]
        inp[0] = temp
        eqn.append(inp)


​        

def echelon():
    # This function converts the system into an echelon form
    for n in range(unknowns - 1):
        if(rearrange(n+1)):
            for i in range(unknowns - 1 - n):
                # make n + 1 + i [n+1] = 0 using n+1th equation, if not already zero
                if(eqn[n+1+(i+1)][n+1] and eqn[n+1][n+1]):
                    factor = -(eqn[n+1+(i+1)][n+1]/eqn[n+1][n+1])
                    add(n+1+(i+1), n+1, factor)
                    
    
    
def rearrange(n):
    # This function ensures that the nth row has a nonzero value in its nth column.
    # If all of the columns are zero, it returns a false and forces echelon to move to the next n.
    if(eqn[n][n]):
            return True
    else:
            for i in range(n, unknowns + 1):
                if(eqn[i][n]):
                    swap(i, n)
                    return True
            return False
    


def reduce():
    # This function converts the system into a reduced row echelon form
    global incomplete
    
    # Cancel out all other unknowns for each respective equation
    for n in range(unknowns, 0, -1):
        for i in range(1, n):
            if(eqn[i][n] and eqn[n][n]):
                factor = -(eqn[i][n]/eqn[n][n])
                add(i, n, factor)


​            
​        
    # Scale each unknown to a multiple of one
    for n in range(1, unknowns+1):
        if(eqn[n][n] and eqn[n][n] != 1):
            mult(n, 1/(eqn[n][n]))
            
        else:
            incomplete = True

def output():
    # This function prints out the solution to the linear system
    
    if(incomplete):
        print("\nThis system of linear equations has free variables. Please perform further analysis on necessary rows.\n")
    else:
        print("Solution to this system of linear equations:")
        for n in range(1, unknowns+1):
            print("x" + str(n) + " = " + str(eqn[n][0]))


while(True):
    eqn = [[]]
    unknowns = 0
    intake()
    print("\nYour input:")
    visualize()
    print("\nConverting to row echelon form...\n")
    echelon()
    print("Converting to reduced row echelon form...\n")
    reduce()
    output()
    response = input("Solve another linear system? [Y/N]")
    if(response == 'N'):
        break

