
import random
import numpy as np
# This is used to fixed the random generator so we can test the output
random.seed(3456)
# my_randoms = random.sample(range(1,11),5)
# print(my_randoms)

def SimulateGame(bets,amounts):
    result=[]
    minimum = 100
    #minimum bet function
    def AboveMinimum(amounts, minimum):
        for i in amounts:
            if i < self.minimum:
                result.append(False)
            else:
                result.append(True)
        return result
    AboveMinimum(amounts, minimum)
    result_amount = np.array(result) * np.array(amounts)
    #print(result_amount) # the list of bets that can play the game ( with the amount they play) !
    result_S = []
    # Spinning the Wheel function that determines the number of loosers and winners
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
    #print(result_S) # list of bets that are winners as dummies !
    # computation on the amount lost and won by palyers and the casino
    for k in result_S:
        result_amount2 = np.array(result_S)* np.array(result_amount)
        lost_bets= [item*30 for item in result_amount2]
    result4=[]
    for w in lost_bets:
        if w == 0 :
            result4.append(1)
        else :
            result4.append(0)
    #print(result4) # list of the amounts won by the casino as dummies !
    result_full=np.array(result4)* np.array(amounts) # list of the amounts in dollars won by the casino
    result_final=[sum(result_full),lost_bets]
    print(result_final) # list of the full lost and gains from the customers and casino :
    return

bets1=[10, 24, 36, 0, 11, 24]
amounts1=[10, 85, 120, 65, 150, 122]
# Roulette(bets1,amounts1,minimun)
# Roulette(bets1,amounts1,minimun)

class Roulette(object):
    def __init__(self, minimum):
        self.minimum=  minimum
    def SimulateGame(self, bets, amounts):
        self.bets = bets
        self.amounts = amounts
        return SimulateGame(bets,amounts)

table1=Roulette(100)
print(table1.SimulateGame(bets1,amounts1))
print(table1.SimulateGame(bets1,amounts1))
