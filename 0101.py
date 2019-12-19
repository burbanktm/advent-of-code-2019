# advent of code
# day 1, puzzle 1

# 0101.py

##Fuel required to launch a given module is based on its mass.
##Specifically, to find the fuel required for a module,
##take its mass, divide by three, round down, and subtract 2.

import csv

def readInputs():
    values = []
    with open ('0101.csv', 'r', newline='') as f:
        reader =csv.reader(f)
        for row in reader:
##            print(int(row[0]))
            values.append(int(row[0]))
    return values
            

def fuelCounterUpper(mass):
    return int(mass / 3) - 2

def prob1(massVals):
    fuelCount = 0
    for item in massVals:
        fuelCount += fuelCounterUpper(item)
    return fuelCount

def prob2(massVals):
    fuelCount = 0
    for item in massVals:
        while item >= 9:
            mass = fuelCounterUpper(item)
            fuelCount += mass
            item = mass
    return fuelCount

if __name__ == '__main__':

    massVals = readInputs()
    print(prob1(massVals))
    print(prob2(massVals))

