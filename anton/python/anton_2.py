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

while True:

    first=lim_1
    second=0
    h = 4
    z = PrettyTable()
    sum_list = []


    allss = int((h*koeff))

    step = (lim_2-lim_1)/allss

    weight_Ai_list = weight_Ai(allss)

    print(f"-------------------for {allss}-------------------")
    z.field_names = ["№", "Xi", "formula", "weight Ai", "Ai*f(Xi)"]

    for i in range(0, allss+1):
        part_2 = (1+first+first**2)/math.sqrt(first+1)            

        
        element = weight_Ai_list[i]

        Ai_fXi = element*part_2 
    
        sum_list.append(Ai_fXi)

        z.add_row([i, round(first, 5), round(part_2, 6), element, round(Ai_fXi, 9)])
        
        first +=step

    result_dic[f'{allss}'] = sum(sum_list)*(step/2)

    print(z)
    print("sum: ", sum(sum_list), "sum*step: ", round(sum(sum_list)*step/2, 9))
    print("Allss:", allss)
    try: 
        check = abs((result_dic[f'{first_first}']-result_dic[f'{allss}']))/3
        
        if check <= precision:
            print(allss, "(Qn-Q2n)/3: ", check, check <= precision)
            break
        else:
            print("continue", allss, "(Qn-Q2n)/3: ", check, check <= precision)

    except: ...
    
    koeff*=2
    sum_list = []
    first_first = allss