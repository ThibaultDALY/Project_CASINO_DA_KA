
import random
# This is used to fixed the random generator so we can test the output
random.seed(3456)
#
# my_randoms = random.sample(range(1,11),5)
# print(my_randoms)

# A function AboveMinimum that takes a list of betted amounts and returns a list of booleans
# def AboveMinium(amount,minimun):
#     result = []
#     for i in amount:
#         if i < minimun:
#             result.append(False)
#         else : result.append(True)
#     return print(result)
#
# ammount1=[10, 220, 120]
# AboveMinium(ammount1,100)

# A function SpinTheWheel that has a variables ‘bets’ which is a list of integers ranging from 0 to 36 (both included).
# It should determine a random number between that range and return a list of the same length as bets indicating which
# bets where correct and which not. It should print out the location of the ball in the roulette wheel. If there are
# winners is should print out how many, if not it should be mentioned that no player won. 

def SpinTheWheel(bets):
    randoms= random.randrange(37)
    print("Ball lands on " +str(randoms))
    result_Spin = []
    for i in bets:
        if i != randoms:
            result_Spin.append(False)
        else:
            result_Spin.append(True)
    return result_Spin, randoms # multiple output return
bets1=[14, 24, 24]
result_Spin,randoms=SpinTheWheel(bets1) #split the tuple

print(result_Spin)

