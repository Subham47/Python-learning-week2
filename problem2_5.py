import random
def problem2_5():
    list=[]
    random.seed(171)
    for i in range(0,10,1):
        list.append(random.randint(1,6))
    for i in list:    
        print(i) 