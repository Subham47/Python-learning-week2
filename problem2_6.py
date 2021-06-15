import random

def problem2_6():
    list=[]
    random.seed(431)
    for i in range(0,100,1):
        n1=random.randint(1,6)
        n2=random.randint(1,6)
        result=n1+n2
        list.append(result)
    for i in list:
        print(i)