
def SimulateGame(bets,amount,minimun):
    result=[]
    def AboveMinimum(amount, minimun):
        for i in amount:
            if i < minimun:
                result.append(False)
            else:
                result.append(True)
        return result
    for j in AboveMinimum(amount,minimun):
        if j == True :
            result.append(1)
        else:
            result.append(0)
        result_amount = [result[i] * amount[i] for i in range(len(result))]
        return result_amount
    def SpinTheWheel(bets):
        randoms = random.randrange(37)
        print("Spinning the Wheel...")
        print("Ball lands on " + str(randoms))
        result_S = []
        for i in bets:
            if i != randoms:
                result_S.append(0)
            else:
                result_S.append(i)
        number = sum(x > 0 for x in result_S)
        if number > 0:
            print("There are %d correct bet(s)" % (number,))
        else:
            print("No winners this round")
        return result
    result_amount2 = [SpinTheWheel(bets)[i] * result_amount[i] for i in range(len(SpinTheWheel(bets)))]
    return result_amount2
minimun=100
bets1=[10, 24, 36, 0, 11, 24]
amount1=[10, 85, 120, 65, 150, 122]
SimulateGame(bets1,amount1,minimun)
