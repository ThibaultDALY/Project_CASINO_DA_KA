
import random
# This is used to fixed the random generator so we can test the output
random.seed(3456)

# print(random.randrange(0,10,5))
# print(random.randrange(10))
my_randoms = random.sample(range(1,11),5)
print(my_randoms)
