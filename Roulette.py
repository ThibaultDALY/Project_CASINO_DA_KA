
import random
import numpy as np
# This is used to fixed the random generator so we can test the output
random.seed(3456)
#
# my_randoms = random.sample(range(1,11),5)
# print(my_randoms)

#A function AboveMinimum that takes a list of betted amounts and returns a list of booleans


# def AboveMinimum(amount,minimun):
#     result = []
#     for i in amount:
#         if i < minimun:
#             result.append(False)
#         else : result.append(True)
#     return print(result)
#
# amounts1=[10, 85, 120, 65, 150, 122]
# AboveMinimum(amounts1,100)


# A function SpinTheWheel that has a variables ‘bets’ which is a list of integers ranging from 0 to 36 (both included).
# It should determine a random number between that range and return a list of the same length as bets indicating which
# bets where correct and which not. It should print out the location of the ball in the roulette wheel. If there are
# winners is should print out how many, if not it should be mentioned that no player won. 
#
# def SpinTheWheel(bets):
#     randoms= random.randrange(37)
#     print("Spinning the Wheel...")
#     print("Ball lands on " +str(randoms))
#     result = []
#     for i in bets:
#         if i != randoms:
#             result.append(0)
#         else:
#             result.append(i)
#     number = sum(x > 0 for x in result)
#     if number>0:
#         print("There are %d correct bet(s)" % (number,))
#     else :
#         print("No winners this round")
#     return print(result)
# bets1=[10, 24, 36, 0, 11, 24]
# SpinTheWheel(bets1)

def SimulateGame(bets,amount,minimun):
    result=[]
    def AboveMinimum(amount, minimun):
        for i in amount:
            if i < minimun:
                result.append(False)
            else:
                result.append(True)
        return result
    AboveMinimum(amount, minimun)
    result1=[]
    for j in result:
        if j == True :
            result1.append(1)
        else:
            result1.append(0)
        result_amount = [result[j] * amount[j] for j in range(len(amount))]
    result_amount
    result_S = []
    def SpinTheWheel(bets):
        randoms = random.randrange(37)
        print("Spinning the Wheel...")
        print("Ball lands on " + str(randoms))

        for i in bets:
            if i != randoms:
                result_S.append(0)
            else:
                result_S.append(1)
        number = sum(x > 0 for x in result_S)
        if number > 0:
            print("There are %d correct bet(s)" % (number,))
        else:
            print("No winners this round")
        return result_S
    SpinTheWheel(bets)
    for k in result_S:
        result_amount2 = [result_S[j]* result_amount[j] for j in range(len(amount))]
        result_amount3= [item*30 for item in result_amount2]
    print(result_amount3)
    return result_amount3
minimun=100
bets1=[10, 24, 36, 0, 11, 24]
amounts1=[10, 85, 120, 65, 150, 122]
SimulateGame(bets1,amounts1,minimun)
