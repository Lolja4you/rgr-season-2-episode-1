import math
from prettytable import PrettyTable


z = PrettyTable()
z.field_names = ["node", "g(node)", "weight Ai", "Ai*g(node)"]

node_list = [-0.774597, 0, 0.774597]
weight_list = [5/9, 8/9, 5/9]

lim_1 = 1
lim_2 = 2.2

summurise = 0

average = (lim_2 - lim_1)/2
for i in range(0, len(node_list)):
    
    dx = node_list[i] * average
    x =  dx + (lim_2 + lim_1)/2

    g_node_i =  math.exp(x/2)/math.sqrt(x+1)
    Ai_g_node_i = weight_list[i] * g_node_i
    summurise += Ai_g_node_i

    z.add_row([node_list[i], round(g_node_i, 6), weight_list[i], round(Ai_g_node_i, 6)])
z.add_row(['Sum Ai*g(node)', summurise, None, None])

jj = round(average*summurise, 10)
z.add_row(['conclusion', jj, None, round(jj, 3)])
print(z)
