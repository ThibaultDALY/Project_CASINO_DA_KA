
import random
# This is used to fixed the random generator so we can test the output
random.seed(3456)

my_randoms = random.sample(range(1,11),5)
print(my_randoms)

j = [4, 5, 6, 7, 1, 3, 7, 5]
print(len(j))
# j2 = [i for i in j if i >= 5]
# print(j2)

def AboveMinium(bets,minimun):
    result = []
    for i in bets:
        if i < minimun:
            result.append(0)
        else : result.append(1)
    return print(result)

bets1=[10,22,32]
AboveMinium(bets1,20)

