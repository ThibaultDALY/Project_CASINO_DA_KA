import random
import itertools

def table_repartition(dic,nb_table,nb_player_round_i):

    # 1) I create a function to generate a list of random number between 1 to 5
    def function(nb_table):
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        list = [random.choice(number) for _ in range(nb_table)]
        return list

    # 2) I draw 5000 times all the possible list that we can be randomly get
    list1 = []
    for i in range(10000):
        list1.append(function(nb_table))

    # 3) I select only the list with the full number of player ( the sum of player for each table must be 16)
    list2 = []
    for group in list1:
        if sum(group) == nb_player_round_i:
            list2.append(group)
        else:
            pass

    # 4) I remove all the duplicate element to get a list with unique possible elements = 35
    list2.sort()
    list3 = list(list2 for list2, _ in itertools.groupby(list2))

    # I choose randomly the repartition of player by table considering the fact that all players must to play
    list4_gross = random.choice(list3)
    list4_full = []
    for repart in list4_gross:
        if repart != 0:
            list4_full.append(repart)
        else:
            pass

    def filter_list(full_list, excludes):
        s = set(excludes)
        return (x for x in full_list if x not in s)

    list_final = []
    test = dic

    for compo in list4_full:
        A = random.sample(test, compo)
        list_final.append(A)
        test = list(filter_list(test, A))
        # player = list(filter_list(dic, A))
    result_table = [list_final, list4_gross, list4_full]
    return result_table

