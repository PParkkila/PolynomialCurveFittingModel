import math, random
import time
from polynomial_curve_fitting import create_dataset, E
import numpy as np


## main loop will essentially start with random coefficient terms between 1 and 100000 and will do 50 runs per generation

## those results will be saved as a list of lists with the following format:
    ## [Error, W] - W is a respective array of coefficients

## loop will stop once a generations error value becomes less than .0001 
    ## prints out the lowest error value for generation

random.seed(time.time())

"""Definition for adding randomized variation to the coefficients in the coefficient matrix W"""
def randomness(W):
    negate = [-1,1]
    for i in range(len(W)):

        if (W[i] < 0.00001):
            W[i] = random.choice(negate) * random.random() * 5
        else:
            W[i] = W[i] + (random.choice(negate) * ((random.random() * (3/5) ) * W[i]) )


    return W

"""Definition for initially generating the coefficient matrix to be used"""
# X is the x inputs for the observed results
def generate_coeff(X):
    W = np.zeros(len(X) - 5)

    for i in range(len(W)):
        W[i] = ((2 * random.random()) - 1) * 50

    return W

X,T = create_dataset(0,1,10)


"""Function for running the machine that optimizes the coefficients for the polynomial distribution and also returns the error values.

 main loop will essentially start with random coefficient terms between 1 and 50 and will do 50 runs per generation

 those results will be saved as a list of lists with the following format:
    ## [Error, W] - W is a respective array of coefficients

 loop will stop once a generations error value becomes less than .0001 
    ## prints out the lowest error value for generation


"""
def run_machine():

    error = 10000
    generation = 0


    
    W = generate_coeff(X)
    # 50x2 array of results

    R = [[0 for i in range(2)] for n in range(50)]

    while error > .05:


        for i in range(50):
            randomW = randomness(W)
            R[i][0] = E(randomW,X,T)
            R[i][1] = randomW
        
        temp_error = R[0][0]
        temp_W = R[0][1]

        for n in range(len(R)):
            if R[n][0] < temp_error:

                temp_error = R[n][0]
                temp_W = R[n][1]
        

        if temp_error < error:
            W = temp_W
            error = temp_error


        
    
        # W = temp_W
        # error = temp_error

        print("----Generation " + str(generation) + " ----")
        print("Error Margin: " + str(error))
        print("Coefficients: " + str(W), end="\n\n\n")
        # time.sleep(1)

        # if (generation % 20 == 0):
        #     print("----Generation " + str(generation) + " ----")
        #     print("Error Margin: " + str(error))
        #     print("Coefficients: " + str(W), end="\n\n\n")
        #     time.sleep(1)

        generation = generation + 1

        if (generation > 300):
            break


    return error,W
        
    
"""Variable responsible for storing all the best attempts for the machine"""
best_attempts = []

for i in range(50):
    err, W_1 = run_machine()
    best_attempts.append([[err], W_1])
    # if err < LOWEST_ERROR:
    #     LOWEST_ERROR = err
    #     W_FINAL = W_1

best_attempts.sort()



# print("\n\n\nLowest Error: " + str(LOWEST_ERROR))
# print("Coefficients: " + str(W_FINAL))

print(best_attempts)
# print(str(best_attempts))