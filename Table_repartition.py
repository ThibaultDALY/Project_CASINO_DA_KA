import random
import itertools


def table_repartition(dic,nb_table, customers_dict0):
    # 1) I create a function to generate a list of random number between 1 to 5
    def function(nb_table):
        number = [0, 1, 2, 3, 4, 5]
        list = [random.choice(number) for _ in range(nb_table)]
        return list

    # 2) I draw 5000 times all the possible list that we can be randomly get
    list1 = []
    for i in range(5000):
        list1.append(function(nb_table))

    # 3) I select only the list with the full number of player ( the sum of player for each table must be 16)
    list2 = []
    for group in list1:
        if sum(group) == 19:
            list2.append(group)
        else:
            pass

    # 4) I remove all the duplicate element to get a list with unique possible elements = 35
    list2.sort()
    list3 = list(list2 for list2, _ in itertools.groupby(list2))

    # I choose randomly the repartition of player by table considering the fact that all players must to play
    list4 = random.choice(list3)

    def filter_list(full_list, excludes):
        s = set(excludes)
        return (x for x in full_list if x not in s)

    list_final = []
    for compo in list4:
        A = random.sample(dic, compo)
        list_final.append(A)
        player = list(filter_list(dic, A))
        result_table = [list_final, list4]
    return result_table

