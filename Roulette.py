
import random
# This is used to fixed the random generator so we can test the output
random.seed(3456)
#
# my_randoms = random.sample(range(1,11),5)
# print(my_randoms)

#A function AboveMinimum that takes a list of betted amounts and returns a list of booleans

def AboveMinium(amount,minimun):
    result = []
    for i in amount:
        if i < minimun:
            result.append(False)
        else : result.append(True)
    return print(result)

ammount1=[10, 85, 120, 65, 150, 122]
AboveMinium(ammount1,100)

# A function SpinTheWheel that has a variables ‘bets’ which is a list of integers ranging from 0 to 36 (both included).
# It should determine a random number between that range and return a list of the same length as bets indicating which
# bets where correct and which not. It should print out the location of the ball in the roulette wheel. If there are
# winners is should print out how many, if not it should be mentioned that no player won. 

def SpinTheWheel(bets):
    randoms= random.randrange(37)
    print("Spinning the Wheel...")
    print("Ball lands on " +str(randoms))
    result = []
    for i in bets:
        if i != randoms:
            result.append(0)
        else:
            result.append(i)
    number = sum(x > 0 for x in result)
    if number>0:
        print("There are %d correct bet(s)" % (number,))
    else :
        print("No winners this round")
    return print(result)
bets1=[10, 4, 36, 0, 11, 2]
SpinTheWheel(bets1)





