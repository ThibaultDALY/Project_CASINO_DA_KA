import random
import numpy as np
#random.seed(3456)

class Craps(object):
    def __init__(self, minimum):
        self.minimum = minimum
    def SimulateGame(self, bets,amounts):
        result = []
        def AboveMinimum(amounts):
            for i in amounts:
                if i < self.minimum:
                    result.append(False)
                else:
                    result.append(True)
            return result
        AboveMinimum(amounts)
        result_amount = np.array(result) * np.array(amounts)
        result_S = []
        #print(result)
        def RollTheDices(bets):
            randoms = random.randint(1, 6) + random.randint(1, 6)
            #print("Throwing the dices...")
            #print("the sum of the dices is equal to " + str(randoms))
            for i in bets:
                if i != randoms:
                    result_S.append(0)
                else:
                    result_S.append(1)
            number = sum(x > 0 for x in result_S)
            # if number > 0:
            #     print("There are %d correct bet(s)" % (number,))
            # else:
            #     print("No winners this round")
            return result_S
        RollTheDices(bets)
        def Cote(bets):
            cote = []
            for i in bets:
                if i == 2 or i == 12:
                    cote.append(30)
                elif i == 3 or i == 11:
                    cote.append(15)
                elif i == 4 or i == 10:
                    cote.append(10)
                elif i == 5 or i == 9:
                    cote.append(8)
                elif i == 6 or i == 8:
                    cote.append(6)
                else:
                    cote.append(5)
            #print(cote)
            return cote
        #print(result_S)
        for k in result_S:
            result_amount2 = np.array(result_S) * np.array(result_amount)
        lost_bets =np.array(result_amount2) * np.array(Cote(bets))
        result4 = []
        # print("lost bets" +str(lost_bets))
        for w in lost_bets:
            if w == 0:
                result4.append(1)
            else:
                result4.append(0)
        result_full = np.array(result4) * np.array(amounts)  # list of the amounts in dollars won by the casino
        result_final = [sum(result_full), lost_bets.tolist()]
        # print(result_final)  # list of the full lost and gains from the customers and casino :
        return result_final



