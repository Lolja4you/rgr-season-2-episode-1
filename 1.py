import math
from prettytable import PrettyTable

lim_1 = 1
lim_2 = 2.2
koeff=1
result_dic = {}
precision = 0.001
def for_8():
    first=lim_1
    second=0
    z = PrettyTable()

    sum_list = []
    allss = int((12))
    step = (lim_2-lim_1)/allss
    print("-------------------for 12-------------------")
    z.field_names = ["№", "Xi", "-XI-", "formula"]
    for i in range(0, allss+1):
        if second == 0:
            part_1 = None
            part_2 = None
        else:
            part_1 = (first+second)/2
            part_2 = math.exp(part_1/2)/math.sqrt(part_1+1)
            sum_list.append(part_2)
        
        z.add_row([i, first, part_1, part_2])
        
        second = first
        first +=step
    print(z)
    result_dic[f'{allss}'] = sum(sum_list)*step
    sum_list = []


for_8()

while True:

    first=lim_1
    second=0
    h = 6
    z = PrettyTable()

    sum_list = []
    allss = int((h*koeff))
    if allss == 12:
        allss*=2

    step = (lim_2-lim_1)/allss
    print(f"-------------------for {allss}-------------------")
    z.field_names = ["№", "Xi", "-XI-", "formula"]

    for i in range(0, allss+1):
        if second == 0:
            part_1 = None
            part_2 = None
        else:
            part_1 = (first+second)/2
            part_2 = math.exp(part_1/2)/math.sqrt(part_1+1)
            data=f"{part_1}, {part_2}"
            sum_list.append(part_2)
        second = first
        z.add_row([i, first, part_1, part_2]) #!!!!!!
        first +=step
    result_dic[f'{allss}'] = sum(sum_list)*step
    print(z)
    koeff*=2
    sum_list = []
    check = abs((result_dic["12"]-result_dic[f'{allss}']))/3
    if check < precision:
        print(check, allss)
        break
    else:

        print("continue", allss, check)