
import Roulette
import Craps
import random
import numpy as np
import operator
from collections import Counter
from matplotlib import pyplot as plt
random.seed(3456)

bets1=[10, 24, 36, 0, 11, 24]
bets2=[10, 4, 6, 7, 11, 2]
amounts1=[10, 85, 120, 65, 150, 122]

# Roulette Simulations
# table1 = Roulette.Roulette(100)
# table1.SimulateGame(bets1, amounts1)
# table1.SimulateGame(bets1, amounts1)

# Craps Simulations
# table2 = Craps.Craps(50)
# print(table2.SimulateGame(bets2, amounts1))
# print(table2.SimulateGame(bets2, amounts1))

#
# def dice(n):
#     rolls = []
#     for i in range(n):
#         two_dice = random.randint(1, 6) + random.randint(1, 6)
#         rolls.append(two_dice)
#     return rolls
#
# thousandsthrows = dice(1000)
#
# labels, values = zip(*Counter(thousandsthrows).items())
# indexes = np.arange(len(labels))
# width = 1
# plt.bar(indexes, values,width)
# plt.xticks(indexes + width * 0.5, labels)
# plt.show()

# Simulation to find the correct amount that should be won by the players

# 10% of the amount ?
# 10% of the game won ?

class Craps_90gain(object):
    def __init__(self, minimum):
        self.minimum = minimum
    def SimulateGame(self, bets,amounts):
        result = []
        def AboveMinimum(amounts):
            for i in amounts:
                if i < self.minimum:
                    result.append(False)
                else:
                    result.append(True)
            return result
        AboveMinimum(amounts)
        result_amount = np.array(result) * np.array(amounts)
        result_S = []
        def RollTheDices(bets):
            randoms = random.randrange(1, 13)
            for i in bets:
                if i != randoms:
                    result_S.append(0)
                else:
                    result_S.append(1)
            number = sum(x > 0 for x in result_S)
        RollTheDices(bets)
        for k in result_S:
            result_amount2 = np.array(result_S) * np.array(result_amount)
            lost_bets = [item * 40 for item in result_amount2]
        result4 = []
        for w in lost_bets:
            if w == 0:
                result4.append(1)
            else:
                result4.append(0)
        result_full = np.array(result4) * np.array(amounts)  # list of the amounts in dollars won by the casino
        result_final = [sum(result_full), lost_bets]
        #print(result_final)  # list of the full lost and gains from the customers and casino :
        return result_final

table3 = Craps_90gain(50)

casino_gain = []
customer_gain = []

for i in range(10):
    A = table3.SimulateGame(bets2,amounts1)
    casino_gain.append(A[0] / (A[0] + sum(A[1])))
    customer_gain.append(sum(A[1]) / (A[0] + sum(A[1])))
print(casino_gain)
print(customer_gain)
print(np.mean(casino_gain))
print(np.mean(customer_gain))