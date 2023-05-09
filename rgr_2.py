import math
from prettytable import PrettyTable

lim_1 = 1
lim_2 = 2.6
koeff=1
result_dic = {}
precision = 0.0001


def weight_Ai(step):
    weight_Ai_list = []
    for i in range(0, step+1):
        if i == 0 or i == step:
            weight_Ai_list.append(1)
        else:
            weight_Ai_list.append(2)
    return weight_Ai_list

def for_8():
    first=lim_1
    z = PrettyTable()

    sum_list = []
    allss = int((8))
    step = (lim_2-lim_1)/allss
    weight_Ai_list = weight_Ai(allss)
    print("-------------------for 8--------------------")
    z.field_names = ["№", "Xi", "formula", "weight Ai", "Ai*f(Xi)"]
    for i in range(0, allss+1):
        part_2 = 1/((math.pow(math.log(first, 10), 2)+1))
        
        element = weight_Ai_list[i]
        Ai_fXi = element*part_2 
        
        sum_list.append(Ai_fXi)


        z.add_row([i, round(first, 2), round(part_2, 6), element, round(Ai_fXi, 9)])
        
        first +=step
    print(z)
    result_dic[f'{allss}'] = sum(sum_list)*step/2
    print(result_dic)
    sum_list = []



for_8()

while True:
    first=lim_1
    second=0
    h = 2
    z = PrettyTable()
    sum_list = []


    allss = int((h*koeff))
    if allss == 8:
        allss*=2
    step = (lim_2-lim_1)/allss

    weight_Ai_list = weight_Ai(allss)

    print(f"-------------------for {allss}-------------------")
    z.field_names = ["№", "Xi", "formula", "weight Ai", "Ai*f(Xi)"]

    for i in range(0, allss+1):
        part_2 = 1/((math.pow(math.log(first, 10), 2)+1))
        
        element = weight_Ai_list[i]
        Ai_fXi = element*part_2 

        sum_list.append(Ai_fXi)

        z.add_row([i, round(first, 2), round(part_2, 6), element, round(Ai_fXi, 9)])
        
        first +=step

    result_dic[f'{allss}'] = sum(sum_list)*step/2
    
    print(z)

    koeff*=2
    sum_list = []
    check = abs((result_dic["8"]-result_dic[f'{allss}'])/3)
    if check < precision:
        print(check, allss)
        break
    else:
        print("continue", allss, check)
