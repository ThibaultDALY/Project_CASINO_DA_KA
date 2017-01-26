import random
import Roulette
import Craps
import decimal
import itertools
from random import shuffle
import Simulation
#random.seed(6)

def Evening(customers_dict):
    customers_dict_int = []
    i = 0
    # list that contains all the dictionary of 5 players
    while i < len(customers_dict):
        if len(customers_dict) % 5 == 0:
            customers_dict_int.append(dict(random.sample(customers_dict.items(), 5)))
            customers_dict = dict(set(customers_dict.items()) - set(customers_dict_int[i].items()))
        else:
            rounding = round(len(customers_dict) / 5)
            j = 0
            while j <= rounding:
                if j != rounding:
                    customers_dict_int.append(dict(random.sample(customers_dict.items(), 5)))
                    customers_dict = dict(set(customers_dict.items()) - set(customers_dict_int[j].items()))
                else:
                    customers_dict_int.append(
                        dict(random.sample(customers_dict.items(), len(customers_dict) % 5)))
                    customers_dict = dict(set(customers_dict.items()) - set(customers_dict_int[j].items()))
                j += 1
        i += 1
    # print(customers_dict_int)
    #
    """ Make the set of players more easy to manipulate """

    # A function sort a dictionary
    def sortByKey(dict):
        sortedByKeyDict = sorted(dict.items(), key=lambda t: t[0])
        return sortedByKeyDict

    customers_dict2 = []
    for group in customers_dict_int:
        customers_dict2.append(sortByKey(group))
    # print(customers_dict2)

    """ Create the random minimum for the each game """

    minimum_roulette = [50, 100, 200]
    minimum_craps = [0, 25, 50]

    number_craps = random.randint(round(len(customers_dict2) / 2), round(len(customers_dict2) / 2) + 1)
    number_roulette = int(len(customers_dict2) - number_craps)

    # print(number_craps)
    # print(number_roulette)

    min_list = []
    for group in range(len(customers_dict2)):
        if group <= number_roulette:
            min_list.append(random.choice(minimum_roulette))
        else:
            min_list.append(random.choice(minimum_craps))

    """ Create the random amount bet by each player """

    amounts = []
    for group in range(len(customers_dict2)):
        loop_amount = []
        for player in range(len(customers_dict2[group])):
            if customers_dict2[group][player][0] <= self.per_returning:
                if customers_dict2[group][player][1] >= min_list[group]:
                    loop_amount.append(min_list[group])
                else:
                    loop_amount.append(0)
            elif customers_dict2[group][player][0] > self.per_returning and customers_dict2[group][player][
                0] <= \
                    (self.number_customers - self.per_bachelors):
                loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 3))))
            else:
                loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 1))))
        amounts.append(loop_amount)
    # print(amounts)

    """ Create the random bet chosen by each player """
    bets = []
    for group in range(len(customers_dict2)):
        loop_bets = []
        for player in range(len(customers_dict2[group])):
            if group <= 1:
                loop_bets.append(random.randint(1, 36))
            else:
                loop_bets.append(random.randint(2, 12))
        bets.append(loop_bets)
    # print(bets)

    """ Run the first round of game for each table """

    amounts_game1 = []
    for group in range(len(customers_dict2)):
        loop_game1 = []
        if group <= 1:
            table = Roulette.Roulette(min_list[group])
            loop_game1.append(table.SimulateGame(bets[group], amounts[group]))
        else:
            table = Craps.Craps(min_list[group])
            loop_game1.append(table.SimulateGame(bets[group], amounts[group]))
        amounts_game1.append(loop_game1)

    # print(amounts_game1)

    """ Store the result of the Stage 1 """

    player_gain1 = []  # Here where are the payoff of each player after game 1
    casino_gain1 = []  # Here where are the payoff of the casino after game 1
    for game in range(len(customers_dict2)):
        player_gain1.append(amounts_game1[game][0][1])
        casino_gain1.append(amounts_game1[game][0][0])

    casino_gain1 = casino_gain1
    print(player_gain1)
    print(casino_gain1)

    """ Let's now compute the revenue of each players after game 1 : delete the amount betted and add potential
    payoff from Game 1"""

    customers_dict3 = customers_dict2

    income_game1 = []  # Here are the income of each player after game 1
    for group in range(len(customers_dict2)):
        for player in range(len(customers_dict2[group])):
            income_game1.append(customers_dict3[group][player][1] - amounts[group][player] + \
                                player_gain1[group][player])

    # Create a function to split list
    def split(arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

    income_game1 = split(income_game1, 5)

    # print(income_game1)

    # Create a function to replace an element in a list
    def replace_at_index1(tup, ix, val):
        lst = list(tup)
        lst[ix] = val
        return tuple(lst)

    customers_dict4 = []
    for group in range(len(customers_dict2)):
        loop_dico = []
        for player in range(len(customers_dict2[group])):
            loop_dico.append(
                replace_at_index1(customers_dict3[group][player], 1, income_game1[group][player]))
        customers_dict4.append(loop_dico)

    # print(amounts)
    # print(customers_dict2)
    # print(customers_dict4) # Here is the income of each player after the game 1 !!

    """ Let's now keep only players with income > 0 after the game 1 """

    # Here is the final list of income for each player
    customers_dict5 = []
    for group in customers_dict4:
        customers_dict5.append([i for i in group if i[1] > 0])
    print(customers_dict5)
    #
    Bal = []
    for group in customers_dict5:
        Bal.append(dict(group))
    # print(Bal)

    # Re-transform the output into dico form
    player_game1_int = []
    for group in customers_dict5:
        player_game1_int.append(dict(group))
    # print(player_game1_int)

    # Transform the different dico in a unique dictionary
    from functools import reduce
    def update(d, other):
        d.update(other)
        return d

    player_game1 = reduce(update, player_game1_int, {})
    print(player_game1)
    return player_game1 and casino_gain1

