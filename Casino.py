import random
import Roulette
import Craps
import decimal
import itertools
from random import shuffle
import Simulation
random.seed(4)
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
        for i in range(self.number_customers-(self.per_returning + self.per_bachelors)):
            customer_one_time.append(random.randint(200, 300))

        customers_list = [customer_returning, customer_one_time, customer_bachelors]
        customers_merged = list(itertools.chain.from_iterable(customers_list))

        list_id = []
        for i in range(1, self.number_customers+1):
            list_id.append(i)
        customers_dict = zip(list_id, customers_merged)
        customers_dict = dict(customers_dict)
        #print(customers_dict)

        customers_dict_int = []
        i = 0
        # list that contains all the dictionary of 5 players
        while i < 4:
            customers_dict_int.append(dict(random.sample(customers_dict.items(), 5)))
            customers_dict = dict(set(customers_dict.items()) - set(customers_dict_int[i].items()))
            i += 1
        print(customers_dict_int)

        """ Make the set of players more easy to manipulate """
        # A function sort a dictionary
        def sortByKey(dict):
            sortedByKeyDict = sorted(dict.items(), key=lambda t: t[0])
            return sortedByKeyDict

        customers_dict2 = []
        for group in customers_dict_int:
            customers_dict2.append(sortByKey(group))
        print(customers_dict2)

        """ Create the random minimum for the each game """

        minimum_roulette = [50, 100, 200]
        minimum_craps = [0, 25, 50]

        min_list = [random.choice(minimum_roulette),random.choice(minimum_roulette),random.choice(minimum_craps),
               random.choice(minimum_craps)]
        print(min_list)

        """ Create the random amount bet by each player """

        amounts = []
        for group in range(len(customers_dict2)):
            loop_amount = []
            for player in range(0, 5):
                if customers_dict2[group][player][0] <= self.per_returning :
                    if customers_dict2[group][player][1]>= min_list[group]:
                        loop_amount.append(min_list[group])
                    else:
                        loop_amount.append(0)
                elif customers_dict2[group][player][0] > self.per_returning and customers_dict2[group][player][0] <= \
                        (self.number_customers-self.per_bachelors):
                    loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1])/3))))
                else:
                    loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 1))))
            amounts.append(loop_amount)
        print(amounts)

        """ Create the random bet chosen by each player """
        bets = []
        for group in range(len(customers_dict2)):
            loop_bets = []
            for player in range(0, 5):
                if group <= 1:
                    loop_bets.append(random.randint(1, 36))
                else:
                    loop_bets.append(random.randint(2, 12))
            bets.append(loop_bets)
        print(bets)

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

        print(amounts_game1)

        """ Store the result of the Stage 1 """

        player_gain1 = [] # Here where are the payoff of each player after game 1
        casino_gain1 = [] # Here where are the payoff of the casino after game 1
        for game in range(len(customers_dict2)):
            player_gain1.append(amounts_game1[game][0][1])
            casino_gain1.append(amounts_game1[game][0][0])

        casino_gain1 = sum(casino_gain1)
        print(player_gain1)
        print(casino_gain1)

        """ Let's now compute the revenue of each players after game 1 : delete the amount betted and add potential
        payoff from Game 1"""

        customers_dict3 = customers_dict2

        income_game1 = [] # Here are the income of each player after game 1
        for group in range(len(customers_dict2)):
            for player in range(0, 5):
                income_game1.append(customers_dict3[group][player][1] - amounts[group][player] + player_gain1[group][player])

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

        # Create a function to replace an element in a list
        def replace_at_index1(tup, ix, val):
            lst = list(tup)
            lst[ix] = val
            return tuple(lst)

        customers_dict4 = []
        for group in range(len(customers_dict2)):
            loop_dico = []
            for player in range(0, 5):
                loop_dico.append(replace_at_index1(customers_dict3[group][player],1,income_game1[group][player]))
            customers_dict4.append(loop_dico)

        print(amounts)
        print(customers_dict2)
        print(customers_dict4) # Here is the income of each player after the game 1 !!

CASINO(500, 2, 3, 3, 200, 20, 10, 2).SimulateEvening(1)