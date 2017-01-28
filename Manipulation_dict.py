""" Let's now compute the revenue of each players after game 1 : delete the amount betted and add potential
                payoff from Game 1"""

def Change(customers_dict2, player_gain1, amounts, repartition2):
    customers_dict3 = customers_dict2
    income_game1 = []  # Here are the income of each player after game 1
    for group in range(len(customers_dict2)):
        for player in range(len(customers_dict2[group])):
            income_game1.append(customers_dict3[group][player][1] - amounts[group][player] + \
                                player_gain1[group][player])

    # Create a function to split list
    # def split(arr, size):
    #     arrs = []
    #     while len(arr) > size:
    #         pice = arr[:size]
    #         arrs.append(pice)
    #         arr = arr[size:]
    #     arrs.append(arr)
    #     return arrs

    # income_game1 = split(income_game1, 5)
    income_game2 = []
    h = 0
    for z in repartition2:
        income_game2.append(income_game1[h:z + h])
        h = z

    # Create a function to replace an element in a list
    def replace_at_index1(tup, ix, val):
        lst = list(tup)
        lst[ix] = val
        return tuple(lst)

    customers_dict4 = []
    for group in range(len(customers_dict2)):
        loop_dico = []
        for player in range(len(customers_dict2[group])):
            loop_dico.append(replace_at_index1(customers_dict3[group][player], 1, income_game2[group][player]))
        customers_dict4.append(loop_dico)



    """ Let's now keep only players with income > 0 after the game 1 """

    # Here is the final list of income for each player
    customers_dict5 = []
    for group in customers_dict4:
        customers_dict5.append([i for i in group if i[1] > 0])




    Bal = []
    for group in customers_dict5:
        Bal.append(dict(group))



    # Re-transform the output into dico form
    player_game1_int = []
    for group in customers_dict5:
        player_game1_int.append(dict(group))
    # Transform the different dico in a unique dictionary
    D = []
    for group in player_game1_int:
        D.append(len(group))
    #print("Start", sum(D))


    # from functools import reduce
    # def update(d, other):
    #     d.update(other)
    #     return d
    #
    # player_game1 = reduce(update, player_game1_int, {})

    from collections import ChainMap
    player_game1 = dict(ChainMap(*player_game1_int))


    # D = []
    # for group in player_game1:
    #     D.append(len(group))
    #print("END", player_game1)

    return player_game1