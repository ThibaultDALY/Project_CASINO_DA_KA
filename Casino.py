import random
import Roulette
import Craps
import decimal
import itertools
import Manipulation_dict
import Table_repartition
import numpy as np
from random import shuffle
import Simulation
import operator
from collections import Counter
from matplotlib import pyplot as plt
random.seed(3456)

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

        cash_nights = []
        barmen_tips_all = []
        barmen_tips_loop = []
        casino_drink_night_loop = []
        casino_drink_night_all = []
        money_croupiers = []
        money_croupiers_all = []
        for number_of_evenings in range(evenings):
            "Step 1 : Set up the configuration for the  determination of each type of players"
            customer_returning = random.sample(range(100, 300), self.per_returning)
            customer_bachelors = random.sample(range(200, 500), self.per_bachelors)
            customer_one_time = []
            for i in range(self.number_customers - (self.per_returning + self.per_bachelors)):
                customer_one_time.append(random.randint(200, 300))

            """Limit 1 : We attribute the 200 bonus for bachelors but we are limited to keep the bachelor players to bet
            an amount between 0 to their amount at the beginning of the game while that is was stipulated that bachelor
             cannot bet the bonus for the first round"""

            customer_bachelors = [x+200 for x in customer_bachelors]

            customers_list = [customer_returning, customer_one_time, customer_bachelors]
            customers_merged = list(itertools.chain.from_iterable(customers_list))

            list_id = []
            for i in range(1, self.number_customers + 1):
                list_id.append(i)

            """We store identification and initial income into a dictionary to easily follow each player
            during the entire evening """

            customers_dict = zip(list_id, customers_merged)
            customers_dict = dict(customers_dict)
            print(customers_dict)

            """ Drink or not before playing !"""
            casino_money_drink = []
            tips_all = []

            for keys in customers_dict:
                get_a_drink = random.randint(1, 2)
                get_a_bartender = random.randint(1, 2)
                if customers_dict[keys] > 60:
                    if get_a_drink == 1:
                        if get_a_bartender == 1:
                            tips = random.randint(0, 20)
                            tips_all.append(tips)
                            casino_money_drink.append(20)
                            customers_dict[keys] = customers_dict[keys] - (20 + tips)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            # creating a function that will run a game on each table and have a dictionary as an output
            def Evening(customers_dict):
                # We just  transform the dictionary into a list of tuples to make easier manipulation
                def Dict_to_tuple(dict):
                    transformation = sorted(dict.items(), key=lambda t: t[0])
                    return transformation

                customers_dict0 = Dict_to_tuple(customers_dict)

                """ Step 2 : The 100 players are randomly distributed among the 20 tables of the casino. See the
                Table_repartition.py script to get more details for the procedure"""
                customers_dict_int = Table_repartition.table_repartition(customers_dict0, \
                                                        self.craps_tables+self.roulette_tables, len(customers_dict0))
                repartition2 = customers_dict_int[2]

                customers_dict00 = customers_dict_int[0]
                customers_dict_int2 = []

                for group in customers_dict00:
                    customers_dict_int2.append(dict(group))

                customers_dict2 = []
                for group in customers_dict_int2:
                    customers_dict2.append(Dict_to_tuple(group))
                # print(customers_dict2)

                """ Create the random minimum for the each game """

                number_roulette = random.randint(round(len(customers_dict_int[2])/2)-1,\
                                                 round(len(customers_dict_int[2])/2)+2)
                min_list = []
                for group in range(len(customers_dict2)):
                    if group <= number_roulette:
                        min_list.append(random.choice([50, 100, 200]))
                    else:
                        min_list.append(random.choice([0, 25, 50]))

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
                        elif customers_dict2[group][player][0] > self.per_returning and \
                            customers_dict2[group][player][0]<= (self.number_customers - self.per_bachelors):
                            loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 3))))
                        else:
                            loop_amount.append(random.randint(0, int(((customers_dict2[group][player][1]) / 1))))
                    amounts.append(loop_amount)
                #print(amounts)

                """ Create the random bet chosen by each player """
                bets = []
                for group in range(len(customers_dict2)):
                    loop_bets = []
                    for player in range(len(customers_dict2[group])):
                        if group <= number_roulette:
                            loop_bets.append(random.randint(1, 36))
                        else:
                            loop_bets.append(random.randint(2, 12))
                    bets.append(loop_bets)
                #print(bets)
                """ Run the first round of game for each table """

                amounts_game1 = []
                for group in range(len(customers_dict2)):
                    loop_game1 = []
                    if group <= number_roulette:
                        table = Roulette.Roulette(min_list[group])
                        loop_game1.append(table.SimulateGame(bets[group], amounts[group]))
                    else:
                        table = Craps.Craps(min_list[group])
                        loop_game1.append(table.SimulateGame(bets[group], amounts[group]))
                    amounts_game1.append(loop_game1)
                #print(amounts_game1)

                """ Store the result of the Stage 1 """

                player_gain1 = []  # Here where are the payoff of each player after game 1
                casino_gain1 = []  # Here where are the payoff of the casino after game 1
                for game in range(len(customers_dict2)):
                    player_gain1.append(amounts_game1[game][0][1])
                    casino_gain1.append(amounts_game1[game][0][0])

                casino_gain1 = casino_gain1
                # print(player_gain1)
                # print(casino_gain1)

                """ Money the croupiers wins 0.5% """

                croupiers_gain = []
                # for croupier in range(self.roulette_tables + self.craps_tables):
                for croupier in range(len(customers_dict2)):
                    croupiers_gain.append(round(casino_gain1[croupier] * 0.05))

                """ Step 3 : Update the income of each player after the first round of the evening"""

                # doing some manipulation on the list for winning and loosing money of the players
                " See the Manipulation_dict.py to get more details"
                player_game1 = Manipulation_dict.Change(customers_dict2, player_gain1, amounts, repartition2)
                #print(player_game1)

                """ Drink time after the game """

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
                result_final = [player_game1, casino_gain1, player_gain1, croupiers_gain, sum(casino_money_drink),\
                                tips_all]
                return result_final

            Evening(customers_dict)

            A = Evening(customers_dict)
            B = Evening(A[0])
            C = Evening(B[0]) # third game

            """ Casino fees and cash for the night """

            casino_wage_fix = 200 * (self.roulette_tables + self.craps_tables + self.barmen)
            casino_wage_total = casino_wage_fix + sum(A[3] + B[3] + C[3])
            casino_lost = sum(list(map(sum, A[2]))) + sum(list(map(sum, B[2]))) + sum(list(map(sum, C[2])))
            casino_croupiers = sum(A[3] + B[3] + C[3])
            casino_drink_night = A[4] + B[4] + C[4]
            barmen_tips = A[5] + B[5] + C[5]

            barmen_tips_loop.append(np.mean(barmen_tips))
            casino_drink_night_loop.append(casino_drink_night)
            money_croupiers.append(np.mean(A[3] + B[3] + C[3]))

            if number_of_evenings != 0:
                self.cash = casino_money

                casino_money = self.cash + casino_drink_night + sum(
                    A[1] + B[1] + C[1]) - casino_wage_total - casino_lost - casino_croupiers
                cash_nights.append(casino_money)
            else:
                cash_nights.append(self.cash)
                casino_money = self.cash + casino_drink_night + sum(
                    A[1] + B[1] + C[1]) - casino_wage_total - casino_lost - casino_croupiers
                cash_nights.append(casino_money)
            print("the casino has " + str(casino_money), "$ after the night", "with a cash start of " + str(self.cash), "$")

        barmen_tips_all.append(barmen_tips_loop)
        barmen_tips_all = barmen_tips_all[0]
        casino_drink_night_all.append(casino_drink_night_loop)
        casino_drink_night_all = casino_drink_night_all[0]
        money_croupiers_all.append(money_croupiers)
        money_croupiers_all = money_croupiers_all[0]
        return cash_nights, barmen_tips_all, casino_drink_night_all, money_croupiers_all


W = CASINO(50000, 10, 10, 4, 200, 100, 50, 20).SimulateEvening(1000)

""" Evolution of the cash of the Casino """
print(W[0])
plt.plot(W[0])
plt.ylabel('Cash of the casino')
plt.xlabel('Evenings')
plt.title('Profit of the casino ')
plt.grid(True)
plt.show()

""" Average tips barmen by night """

plt.plot(W[1])
plt.ylabel('Average tips in dollars')
plt.xlabel('Evenings')
plt.title('Tips per barmen by evening')
plt.grid(True)
plt.show()

""" Average tips croupiers by night """
plt.plot(W[3])
plt.ylabel('Average tips in dollars')
plt.xlabel('Evenings')
plt.title('Tips per croupiers by evening')
plt.grid(True)
plt.show()

# """ Number of drinks by night """
# number_of_drinks = CASINO(50000, 2, 2, 4, 200, 20, 10, 2).SimulateEvening(1000)[2]
# number_of_drinks = [x / 20 for x in number_of_drinks]
# plt.plot(number_of_drinks)
# plt.ylabel('Numbers of drinks per evening')
# plt.xlabel('Evenings')
# plt.title('Number of drinks ')
# plt.grid(True)
# plt.show()
