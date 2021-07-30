#######################################################################################
# Links to Resources
#https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
# https://www.instructables.com/How-to-Make-a-Numerical-Integration-Program-in-Pyt/
#######################################################################################
# Imports
from math import *
#######################################################################################
# Start the program
numOfSums = int(input("Enter how many times you want to sum(more times = more accurate): "))
lowerBound = float(input("Enter the lower integration bound: "))
upperBound = float(input("Enter the upper integraion bound: "))
#######################################################################################
# Functions
def Integrate(N,a,b):
    def f(x):
        # change your function
        return x**2
    value = 0
    value2 = 0
    for n in range(1,N+1):
        value += f(a+((n-(1/2)*(b-a)/N)))
        return str(value2) # return as a string so it can print
#######################################################################################
# Show your answer
print("...................................")
print("Here is your answer: "+Integrate(numOfSums,lowerBound,upperBound))
