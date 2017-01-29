import random
import numpy as np
from matplotlib import pyplot as plt
# random.seed(3456)

class Craps(object):
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
        #print(result)
        def RollTheDices(bets):
            randoms = random.randint(1, 6) + random.randint(1, 6)
            #print("Throwing the dices...")
            #print("the sum of the dices is equal to " + str(randoms))
            for i in bets:
                if i != randoms:
                    result_S.append(0)
                else:
                    result_S.append(1)
            number = sum(x > 0 for x in result_S)
            # if number > 0:
            #     print("There are %d correct bet(s)" % (number,))
            # else:
            #     print("No winners this round")
            return result_S
        RollTheDices(bets)
        def Cote(bets):
            cote = []
            for i in bets:
                if i == 2 or i == 12:
                    cote.append(0.9*36)
                elif i == 3 or i == 11:
                    cote.append(0.9*18)
                elif i == 4 or i == 10:
                    cote.append(0.9*12)
                elif i == 5 or i == 9:
                    cote.append(0.9*9)
                elif i == 6 or i == 8:
                    cote.append(0.9*(36/5))
                else:
                    cote.append(0.9*6)
            #print(cote)
            return cote
        #print(result_S)
        for k in result_S:
            result_amount2 = np.array(result_S) * np.array(result_amount)
        lost_bets =np.array(result_amount2) * np.array(Cote(bets))
        result4 = []
        # print("lost bets" +str(lost_bets))
        for w in lost_bets:
            if w == 0:
                result4.append(1)
            else:
                result4.append(0)
        result_full = np.array(result4) * np.array(amounts)  # list of the amounts in dollars won by the casino
        result_final = [sum(result_full), lost_bets.tolist()]
        # print(result_final)  # list of the full lost and gains from the customers and casino :
        return result_final


import random
import numpy as np
import operator
from collections import Counter
from matplotlib import pyplot as plt
#random.seed(3456)


# # Craps Simulations
# table2 = Craps(0)
# print(table2.SimulateGame(bets2, amounts1))
# print(table2.SimulateGame(bets2, amounts1))
# #

# Amount = []
# Bet = []
# for time in range(1000):
#     Amount.append(random.randint(50, 100))
#     # Bet.append(random.randint(2, 12))
""" We are going now to proof the theoretical reasoning such as in average the player get 90% of outcomes
To do so we will consider a unique representative player who chooses N times a random number between 2 to 12"""

N = 50000

""" We create first two lists to store the share of outcomes received by the casino and the representative player
 for each simulation"""
part_player = []
part_casino = []
for i in range(N):
    Amount = []
    Bet = []
    "For each round of simulation a random number and a random amount of money are attributed to the player"
    for player in range(1):
        Bet.append(random.randint(2, 12))
        Amount.append(random.randint(50, 100))
    "We make the assumption that there is no minimum "
    table = Craps(100) # Attribute a minimum to the table
    #For each simulation we are going to run the Craps game
    player_gain = table.SimulateGame(Bet, Amount)[1]
    casino_gain = table.SimulateGame(Bet, Amount)[0]
    "An important assumption that we did here is to only store result when the representative player win the round"
    if sum(player_gain)!= 0:
        print("Money casino ", casino_gain)
        print("Money player", sum(player_gain))

        "We do now simple computation to get the share of outcomes obtained  by the player and the casino"
        part_player.append(sum(player_gain) / (sum(player_gain)+casino_gain))
        part_casino.append(casino_gain / (sum(player_gain) + casino_gain))

""" When computing the mean of the share of outcomes obtained by the player and the casino, we can state that in
average the player gets 90% of the outcomes of the game"""
print(np.mean(part_player)) # 0.90

plt.plot(part_player)
plt.ylabel('Share of outcomes gained')
plt.xlabel('Times')
plt.title('Share of the player obtained for N = 50000')
plt.grid(True)
plt.show()
