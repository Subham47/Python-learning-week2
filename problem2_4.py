import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    list=[]
    random.seed(70)
    for i in range(0,10,1):
        list.append(5*random.random()+30)
    print(list)