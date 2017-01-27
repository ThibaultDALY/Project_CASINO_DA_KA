# import random
# import itertools
#
# customer_returning = random.sample(range(100, 300), 3)
# customer_bachelors = random.sample(range(200, 500), 5)
# customer_one_time = []
# for i in range(10-(3 + 5)):
#     customer_one_time.append(random.randint(200, 300))
#
#
# customers_list = [customer_returning, customer_one_time, customer_bachelors]
# #print(customers_list)
# merged = list(itertools.chain.from_iterable(customers_list))
# #print(merged)
# list_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_dict = zip(list_id, merged)
#         new_dict2 = dict(new_dict)
#         #print(new_dict2)
#         minimum_roulette = [50, 100, 200]
#         minimum_craps = [0, 25, 50]
#         list1 = dict()
#         print(new_dict2)
#         for i in range(5):
#             dict.add(new_dict2.pop(random.choice(list(new_dict2.keys()))))
#
#         print(new_dict2)
#         print(list1)  # list1 = dict()
# print(new_dict2)
# for i in range(5):
#     dict.add(new_dict2.pop(random.choice(list(new_dict2.keys()))))
#
# print(new_dict2)
# print(list1)


# To create the first table
# table1 = dict(random.sample(new_dict2.items(), 5))
#
# # To create the second table
# table_int = dict(set(new_dict2.items()) - set(table1.items()))
# table2 = dict(random.sample(table_int.items(), 5))
#
# # a = [table1,table2]
# print(new_dict2)
# print(table1)
# print(table2)
#
# a = [dict(table1), dict(table2)]
# print(a[0])


print(range(0,3))
for i in range(3):
    if i==0:

        # Evening.croupiers_gain3 = []
        # Evening_croupiers_loop = []
        # for i in range(1):
        #     if i == 0:
        #         Evening(Evening(customers_dict))
        #         Evening_croupiers_loop.append(Evening.croupiers_gain)
        #         player_game2 = Evening(Evening(customers_dict))
        #     else :
        #         Evening(player_game2)
        #         Evening_croupiers_loop.append(Evening.croupiers_gain)
        #     Evening.croupiers_gain3.append(Evening_croupiers_loop)
        # print(Evening.croupiers_gain3)



# class Craps_90gain(object):
#     def __init__(self, minimum):
#         self.minimum = minimum
#     def SimulateGame(self, bets,amounts):
#         result = []
#         def AboveMinimum(amounts):
#             for i in amounts:
#                 if i < self.minimum:
#                     result.append(False)
#                 else:
#                     result.append(True)
#             return result
#         AboveMinimum(amounts)
#         result_amount = np.array(result) * np.array(amounts)
#         result_S = []
#         def RollTheDices(bets):
#             randoms = random.randint(1, 6) + random.randint(1, 6)
#             print(" dices " +str(randoms))
#             for i in bets:
#                 if i != randoms:
#                     result_S.append(0)
#                 else:
#                     result_S.append(1)
#             sum(x > 0 for x in result_S)
#         RollTheDices(bets)
#         def Cote(bets):
#             cote = []
#             for i in bets:
#                 if i == 2 or i == 12:
#                     cote.append(35)
#                 elif i == 3 or i == 11:
#                     cote.append(17)
#                 elif i == 4 or i == 10:
#                     cote.append(11)
#                 elif i == 5 or i == 9:
#                     cote.append(8)
#                 elif i == 6 or i == 8:
#                     cote.append(7.2)
#                 else:
#                     cote.append(5)
#             #print(cote)
#             return cote
#         # print("dummy won" +str(result_S))
#         for k in result_S:
#             result_amount2 = np.array(result_S) * np.array(result_amount)
#         lost_bets =np.array(result_amount2) * np.array(Cote(bets))
#         result4 = []
#         # print("lost bets" +str(lost_bets))
#         for w in lost_bets:
#             if w == 0:
#                 result4.append(1)
#             else:
#                 result4.append(0)
#         result_full = np.array(result4) * np.array(amounts)  # list of the amounts in dollars won by the casino
#         result_final = [sum(result_full), lost_bets.tolist()]
#         #print(result_final)  # list of the full lost and gains from the customers and casino :
#         return result_final

# table3 = Craps_90gain(0)
#
# casino_gain = []
# customer_gain = []
#
# for i in range(100):
#     bets3 = random.sample(range(2,13),10)
#     amounts3 = random.sample(range(9, 20), 10)
#     A = table3.SimulateGame(bets3, amounts3)
#
#     casino_gain.append(A[0] / (A[0] + sum(A[1])))
#     customer_gain.append(sum(A[1]) / (A[0] + sum(A[1])))
#
# print("Casino gain " + str(np.mean(casino_gain)))
# print("Players gain " + str(np.mean(customer_gain)))
#