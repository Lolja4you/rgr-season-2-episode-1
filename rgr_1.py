import math, time
from prettytable import PrettyTable


lim_1 = 1
lim_2 = 2.6
koeff=1
result_dic = {}
precision = 0.0001
def for_8():
    first=lim_1
    second=0
    z = PrettyTable()

    sum_list = []
    allss = int((8))
    step = (lim_2-lim_1)/allss
    print("-------------------for 8-------------------")
    z.field_names = ["№", "Xi", "-XI-", "formula"]
    for i in range(0, allss+1):
        if second == 0:
            part_1 = None
            part_2 = None
        else:
            part_1 = (first+second)/2
            part_2 = 1/((math.pow(math.log(part_1, 10), 2)+1))
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
    h = 2
    z = PrettyTable()

    sum_list = []
    allss = int((h*koeff))
    if allss == 8:
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
            part_2 = 1/((math.pow(math.log(part_1, 10), 2)+1))
            data=f"{part_1}, {part_2}"
            sum_list.append(part_2)
        second = first
        first +=step
        z.add_row([i, first, part_1, part_2])
    result_dic[f'{allss}'] = sum(sum_list)*step
    print(z)
    koeff*=2
    sum_list = []
    check = abs((result_dic["8"]-result_dic[f'{allss}'])/3)
    if check < precision:
        print(check, allss, check < precision)
        time.sleep(1)
    else:
        print("continue", allss)