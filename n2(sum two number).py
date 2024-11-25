import random

#def random_list(): # создание рандомного списка, значения которого не превышают 9, с длиной до 100 
#    ls = []
#    t = random.randint(1, 9)
#    i = 0
#    while i <= t:
#        c = random.randint(0, 9)
#        ls.append(c)
#        i += 1
#    return ls


l1 = [2,4,3]#list(input())#random_list()
l2 = [5,6,4]#list(input())#random_list()
l3 = []
print(f'l1 = {l1}, l2 = {l2}')
l1 = list(reversed(l1))
l2 = list(reversed(l2))

min_list = min(len(l1), len(l2))

next_num = 0
for i in range(min_list):
    number = int(l1[i]) + int(l2[i]) + next_num
    next_num = 0
    if number >= 10:
        next_num = number // 10        
        l3.append(number % 10)
    else:
        l3.append(number)                    
        
number = 0
if next_num != 0:
    if len(l1) < len(l2):
        number = int(l2[min_list]) + next_num
        l3.append(number)
        for i in range(min_list + 1, len(l2)):
            l3.append(int(l2[i]))
    else:       
        for i in range(min_list, len(l1)):
            l3.append(int(l1[i]))


print(l3)