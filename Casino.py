import random
import Roulette
import Craps
import decimal
import itertools
import Manipulation_dict
import numpy as np
from random import shuffle
import Simulation
random.seed(7)

class CASINO(object):
    def __init__(self, cash, roulette_tables, craps_tables, barmen, employee_wage, number_customers,
                 per_returning, per_bachelors):
        self.roulette_tables = roulette_tables
        self.craps_tables = craps_tables
        self.barmen = barmen
        self.employee_wage = employee_wage
        self.number_customers = number_customers
        self.per_returning = per_returning
        self.per_bachelors = per_bachelors
        self.cash = cash

    def SimulateEvening(self, evenings):

        customer_returning = random.sample(range(100, 300), self.per_returning)
        customer_bachelors = random.sample(range(200, 500), self.per_bachelors)
        customer_one_time = []
        for i in range(self.number_customers - (self.per_returning + self.per_bachelors)):
            customer_one_time.append(random.randint(200, 300))

        customers_list = [customer_returning, customer_one_time, customer_bachelors]
        customers_merged = list(itertools.chain.from_iterable(customers_list))

        list_id = []
        for i in range(1, self.number_customers + 1):
            list_id.append(i)
        customers_dict = zip(list_id, customers_merged)
        customers_dict = dict(customers_dict)
        print(customers_dict)

        # creating a function that will run a game on each table and have a dictionary as an output
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
                            customers_dict_int.append(dict(random.sample(customers_dict.items(), len(customers_dict)\
                                                                         % 5)))
                            customers_dict = dict(set(customers_dict.items()) - set(customers_dict_int[j].items()))
                        j += 1
                i += 1
            # print(customers_dict_int)

            # tables_empty = ([{}]*(self.roulette_tables+self.craps_tables))
            # for x in customers_dict:
            #     tables_empty.insert(random.randint(0, len(tables_empty)),x)
            # print(tables_empty)

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
                    elif customers_dict2[group][player][0] > self.per_returning and customers_dict2[group][player][0] \
                        <= (self.number_customers - self.per_bachelors):
                        loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 3))))
                    else:
                        loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 1))))
                amounts.append(loop_amount)
            #print("money betted by players" +str(amounts))

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
            #print( "money won by players" +str(player_gain1))
            #print("money casino " +str(casino_gain1))

            """ Money the croupiers wins 0.5% """

            croupiers_gain = []
            for croupier in range(number_roulette + number_craps):
                croupiers_gain.append(round(casino_gain1[croupier] * 0.05))

            # doing some manipulation on the list for winning and loosing money of the players
            Manipulation_dict.Change(customers_dict2,player_gain1,amounts)
            player_game1 = Manipulation_dict.Change(customers_dict2,player_gain1,amounts)

            """ Drink time """
            # need less then 2 drinks
            casino_money_drink = []
            tips = 0
            tips_all = []
            for keys in player_game1:
                get_a_drink = random.randint(1,2)
                get_a_bartender = random.randint(1,2)
                if player_game1[keys] > 60:
                    if get_a_drink == 1:
                        if get_a_bartender == 1:
                            tips = random.randint(0, 20)
                            tips_all.append(tips)
                            casino_money_drink.append(20)
                            player_game1[keys] = player_game1[keys]-(20+tips)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            # money made by the casino from drinks
            #print("tip bar " +str(tips))
            #print("money drinks " +str(sum(casino_money_drink)))
            #print(player_game1)
            result_final = [player_game1, casino_gain1, player_gain1, croupiers_gain, casino_money_drink, tips_all]
            return result_final

        """ Result of the night """

        for section in range(1,3):
            A = Evening(customers_dict)
            print(A[section])
            B = Evening(A[0])
            print(B[section])
            C = Evening(B[0])
            print(C[section])
            E = sum(np.array(A[section])+np.array(B[section])+np.array(C[section]))
        print(E)

        # 3 games per night
        #Evening(Evening(Evening(customers_dict)[0])[0])


CASINO(500, 2, 2, 3, 200, 16, 10, 2).SimulateEvening(1)