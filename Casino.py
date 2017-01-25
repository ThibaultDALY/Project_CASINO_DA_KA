import random
import Roulette
import Craps
import decimal
import itertools
from random import shuffle
import Simulation

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
        print(customers_dict)

        def sortByKey(dict):
            sortedByKeyDict = sorted(dict.items(), key=lambda t: t[0])
            return sortedByKeyDict

        print(sortByKey(customers_dict))

        # customers_dict2 = []
        # i = 0
        # # list that contains all the dictionary of 5 players
        # while i < 4:
        #     customers_dict2.append(dict(random.sample(customers_dict.items(), 5)))
        #     customers_dict = dict(set(customers_dict.items()) - set(customers_dict2[i].items()))
        #     i += 1
        # print(customers_dict2)

        minimum_roulette = [50, 100, 200]
        minimum_craps = [0, 25, 50]

        min_list = [random.choice(minimum_roulette),random.choice(minimum_roulette),random.choice(minimum_craps),
               random.choice(minimum_craps)]
        print(min_list)

        j = 0
        loop_amount = []
        amounts = []
        # loop to create their amount betted of the players
        for group in customers_dict2:
            for i in customers_dict2[j].keys():
                if i <= self.per_returning:
                    loop_amount.append(min_list[j])
                elif i > self.per_returning and i < self.per_bachelors:
                    loop_amount.append(random.randint(0, customers_dict2[j].get(i)+1))
                else :
                    loop_amount.append(random.randint(0, int(customers_dict2[j].get(i)/3)+1))
            amounts.append(loop_amount[j*5:5+5*j])
            j += 1
        print(amounts)

        k = 0
        loop_bets = []
        bets = []
        # loop to create the bests to put in the simulate Game
        for group in range(len(customers_dict2)):
            # first 2 groups go to the roulette table
            if group <= 1:
                loop_bets.append(random.sample(range(1, 37), 5))
            else:
                loop_bets.append(random.sample(range(2, 13), 5))
        bets.append(loop_bets[k*5:5+5*k])
        bets = bets[0]
        k += 1
        print(bets)

        g = 0
        amounts_game1 = []
        loop_amounts =[]
        for g in range(len(customers_dict2) ):
            if g <= int(len(customers_dict2) / 2 - 1):
                table = Roulette.Roulette(min_list[g])
                loop_amounts.append(table.SimulateGame(bets[g], amounts[g]))
            else:
                table = Simulation.Craps_90gain(min_list[g])
                loop_amounts.append(table.SimulateGame(bets[g], amounts[g]))
        amounts_game1.append(loop_amounts)
        amounts_game1 = amounts_game1[0]
        print(amounts_game1)

        #first_game

CASINO(500, 2, 3, 3, 200, 20, 10, 2).SimulateEvening(1)