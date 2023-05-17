import math
from prettytable import PrettyTable

lim_1 = 1
lim_2 = 2.6
koeff=1
result_dic = {}
precision = 0.0001


while True:
    
    first=lim_1
    second=0
    h = 4
    z = PrettyTable()

    sum_list = []
    allss = int((h*koeff))
    #if allss == 8:
    #    allss*=2

    step = (lim_2-lim_1)/allss
    print(f"-------------------for {allss}-------------------")
    z.field_names = ["№", "Xi", "-XI-", "formula"]

    for i in range(0, allss+1):
        if second == 0:
            part_1 = None
            part_2 = None
        else:
            part_1 = (first+second)/2
            part_2 = (1+part_1+part_1**2)/math.sqrt(part_1+1)
            data=f"{part_1}, {part_2}"
            sum_list.append(round(part_2, 9))
        
        second = first
        try:    z.add_row([i, round(first, 3), round(part_1, 3), part_2])
        except: z.add_row([i, first, None, None])
        first +=step

    result_dic[f'{allss}'] = round(sum(sum_list)*step, 9)
    
    print(z)
    print("sum: ", sum(sum_list), "sum*step: ", round(sum(sum_list)*step, 9))


    try: 
        check = abs((result_dic[f'{first_first}']-result_dic[f'{allss}']))/3
        
        if round(check, 4) <= precision:
            print(allss, "(Qn-Q2n)/3: ", check, check <= precision)
            break
        else:
            print("continue", allss, "(Qn-Q2n)/3: ", check, check <= precision)
    except: ...
    koeff*=2
    sum_list = []
    
    first_first = allss