

import random
import Craps
import numpy as np
import operator
from collections import Counter
from matplotlib import pyplot as plt
#random.seed(3456)

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
    table = Craps.Craps(100) # Attribute a minimum to the table
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
