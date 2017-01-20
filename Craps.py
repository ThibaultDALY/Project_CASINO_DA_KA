import random
import numpy as np
random.seed(3456)

def SimulateGame(bets,amounts):
    minimum = 100
    result = []
    def AboveMinimum(amounts, minimum):
        for i in amounts:
            if i < minimum:
                result.append(False)
            else:
                result.append(True)
        return result
    AboveMinimum(amounts, minimum)
    result_amount = np.array(result) * np.array(amounts)
    result_S = []
    print(result)
    def RollTheDices(bets):
        randoms = random.randrange(1,13)
        print("Throwing the dices...")
        print("the sum of the dices is equal to " + str(randoms))
        for i in bets:
            if i != randoms:
                result_S.append(0)
            else:
                result_S.append(1)
        number = sum(x > 0 for x in result_S)
        if number > 0:
            print("There are %d correct bet(s)" % (number,))
        else:
            print("No winners this round")
        return result_S
    RollTheDices(bets)
    print(result_S)
    for k in result_S:
        result_amount2 = np.array(result_S) * np.array(result_amount)
        lost_bets = [item * 30 for item in result_amount2]
    result4 = []
    for w in lost_bets:
        if w == 0:
            result4.append(1)
        else:
            result4.append(0)
    # print(result4) # list of the amounts won by the casino as dummies !
    result_full = np.array(result4) * np.array(amounts)  # list of the amounts in dollars won by the casino
    result_final = [sum(result_full), lost_bets]
    print(result_final)  # list of the full lost and gains from the customers and casino :
    return

bets2=[10, 6, 3, 7, 5, 4]
amounts1=[10, 85, 120, 165, 150, 122]
SimulateGame(bets2,amounts1)