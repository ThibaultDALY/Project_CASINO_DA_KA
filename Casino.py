import random
import Roulette
import Craps
import decimal
import itertools
from random import shuffle


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

        customers_dict2 = []
        i = 0
        # list that contains all the dictionary of 5 players
        while i < 4:
            customers_dict2.append(dict(random.sample(customers_dict.items(), 5)))
            customers_dict = dict(set(customers_dict.items()) - set(customers_dict2[i].items()))
            i += 1
        print(customers_dict2)

        minimum_roulette = [50, 100, 200]
        minimum_craps = [0, 25, 50]

        print(customers_dict2[0].keys())

        # Roulette
        table1_min = random.choice(minimum_roulette)
        table1 = Roulette.Roulette(random.choice(minimum_roulette))
        print(table1_min)

        # print(self.per_returning)
        # print(customers_dict2[0].values())
        # print(customers_dict2[0].get(12))
        print(customers_dict2[0])
        j = 0
        amounts = []
        for group in customers_dict2:

            for i in customers_dict2[j].keys():
                if i <= self.per_returning:
                    amounts.append(table1_min)
                elif i > self.per_returning and i < self.per_bachelors:
                    amounts.append(random.randint(0, customers_dict2[j].get(i)+1))
                else :
                    amounts.append(random.randint(0, int(customers_dict2[j].get(i)/3)+1))
        print([[amounts]])

        # bets1 = random.sample(range(1,37),5)
        # print(bets1)
        # table1.SimulateGame(bets1, amounts1)


        # # Craps
        # table2 = Craps.Craps(random.choice(minimum_craps))
        # print(table2.SimulateGame(bets2, amounts1))
        # print(table2.SimulateGame(bets2, amounts1))
        # print(table2.SimulateGame(bets2, amounts1))

CASINO(500, 2, 3, 3, 200, 20, 5, 2).SimulateEvening(1)