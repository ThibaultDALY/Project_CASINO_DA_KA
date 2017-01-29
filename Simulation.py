
import Roulette
import Craps
import random
import numpy as np
import operator
from collections import Counter
from matplotlib import pyplot as plt
#random.seed(3456)

bets1 = [10, 24, 36, 0, 11, 24]
bets2 = [10, 4, 6, 7, 11, 2]
amounts1 = [10, 85, 120, 65, 150, 122]

# # Roulette Simulations
# table1 = Roulette.Roulette(100)
# print(table1.SimulateGame(bets1, amounts1))
# print(table1.SimulateGame(bets1, amounts1))
# #
# # Craps Simulations
# table2 = Craps.Craps(50)
# print(table2.SimulateGame(bets2, amounts1))
# print(table2.SimulateGame(bets2, amounts1))
# #
# #
# def dice(n):
#     rolls = []
#     for i in range(n):
#         two_dice = random.randint(1, 6) + random.randint(1, 6)
#         rolls.append(two_dice)
#     return rolls
# thousandsthrows = dice(1000)
# labels, values = zip(*Counter(thousandsthrows).items())
# indexes = np.arange(len(labels))
# width = 1
# plt.bar(indexes, values, width)
# plt.title('Simualtion of 1000 throws of 2 dices')
# plt.xticks(indexes + 0.5, labels)
# plt.grid(True)
# plt.show()

# Simulation to find the correct amount that should be won by the players

