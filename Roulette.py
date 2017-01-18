
import random
import numpy as np
# This is used to fixed the random generator so we can test the output
random.seed(3456)
# my_randoms = random.sample(range(1,11),5)
# print(my_randoms)

def SimulateGame(bets,amount,minimun):
    result=[]
    result_full=[]
    def AboveMinimum(amount, minimun):
        for i in amount:
            if i < minimun:
                result.append(False)
            else:
                result.append(True)
        return result
    AboveMinimum(amount, minimun)
    result1=[]
    for j in result:
        if j == True :
            result1.append(1)
        else:
            result1.append(0)
        result_amount = np.array(result) * np.array(amount)
    result_amount
    #print(result_amount)
    result_S = []
    def SpinTheWheel(bets):
        randoms = random.randrange(37)
        print("Spinning the Wheel...")
        print("Ball lands on " + str(randoms))
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
    SpinTheWheel(bets)
    for k in result_S:
        result_amount2 = np.array(result_S)* np.array(result_amount)
        result_amount3= [item*30 for item in result_amount2]
    #print(result_amount3)
    result4=[]
    result_full=[]
    for w in result_amount3:
        if w == 0 :
            result4.append(1)
        else :
            result4.append(0)
    result_full=np.array(result4)* np.array(amount)
    casino_gain=sum(result_full)
    #print(casino_gain)
    result_final=[casino_gain,result_amount3]
    print(result_final)
    return
minimun=100
bets1=[10, 24, 36, 0, 11, 24]
amounts1=[10, 85, 120, 65, 150, 122]
SimulateGame(bets1,amounts1,minimun)
SimulateGame(bets1,amounts1,minimun)
