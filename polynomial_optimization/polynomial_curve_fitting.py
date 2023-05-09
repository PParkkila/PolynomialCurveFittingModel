import numpy as np
import random as r
import math
import matplotlib.pyplot as plt


"""Function for the generation of the polynomial expansion to be evaluated
    @param x - the independent variable for the expanded polynomial function
    @param W - the array of coefficients for the polynomial
    @param W_length - the length of the array of coefficients
"""
def polynomial_function(x, W, W_length):
    Q = np.zeros(W_length)
    for i in range(W_length):
        Q[i] = x ** i

    return W @ Q.T
    #return np.matrix(W,float) * (np.matrix(Q,float).T)

"""
THe sum of squares error function denoted as E(W)
@param W - is the coefficients vector
@param X - is the x values for the observation dataset
@param T - is the observed values for the specified x's in the observation dataset
"""
def E(W,X,T):
    sum = 0

    for i in range(len(X)):
        sum = sum + (polynomial_function(X[i], W, len(W)) - T[i]) ** 2
    #print("Error val: " + str(sum/2))
    return sum / 2

"""Function for setting the predefined X array to be used for setting the observed points
    @param start - the start value of the range
    @param ranges - the end value of the range
    @param amount - the amount of x values produced for the observed points

"""
def find_x(start, ranges, amount):
    iteration_size = (ranges - start) / amount
    X = np.zeros(amount)

    for i in range(amount):
        X[i] = start

        
        start = start + iteration_size

    #print(x)
    return X

"""Predefined sine function for setting observed values
@param x - the dependent variable for the function
"""
def sine(x):
    return math.sin(2*np.pi*x)
"""Predefined polynomial function for setting observed values
@param x - the dependent variable for the function
"""
def polynomial_test_func(x):
    returnval = 1 + 4 * x + 3 * (x ** 2) + 2 * (x**3)
    return returnval

"""Predefined cosh function for setting observed values
@param x - the dependent variable for the function
"""
def func(x):
    return math.cosh(x)

"""Function for creating the predefined dataset of X and T arrays
@param start - the start point of the range
@param ranges - the end point of the range
@param amount - the amount of x values produced for the observed points
"""
def create_dataset(start, ranges, amount):
    X = np.zeros(amount) # not transposed yet
    T = np.zeros(amount) # not transposed yet

    X = find_x(start, ranges, amount)
    negate = [-1,1]
    for i in range(amount):
        
        variation = (r.random() * r.choice(negate)) #/ 10
        

        #T[i] = sine(X[i]) + variation
        #T[i] = func(X[i]) + variation
        T[i] = polynomial_test_func(X[i]) + variation

    return X, T #returns tuple with x and t as the values
    #print("x = " + str(x), end = "\n\n")

    #print("t = " + str(t))
    

"""Function for plotting out the points for observation dataset, includes a couple of test cases as well."""
def plot_points():
    X,T = create_dataset(-1,1, 10)
    X1,T1 = create_dataset(-1,1, 50)

   # X2,T2 = create_dataset(-3,3, 100)


    plt.title("Plotted Prediction Points")
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.xlim(-3,3)
   # plt.ylim(-3,3)

    plt.plot(X,T, "o", color="black")

    plt.plot(X1,T1, "o", color="red")

   # plt.plot(X2,T2, "o", color="green")

    plt.show()




#testing polynomial function
# W = [1,4,3,2]

# print(polynomial_function(6,W,len(W)))

# #testing error function
# X, T = create_dataset(0,1,3)
# E(W,X,T)


#plot_points()




