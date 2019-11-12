my_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = 0 
for i in range (1,len(my_list)-1):
    left = my_list[i]
    for j in range(0,i):
        left=max(left,my_list[j])
    right = my_list[i]
    for j in range(i+1,len(my_list)-1):
        right=max(right,my_list[j])
    res=res+(min(left,right)-my_list[i])

print ("Trapped water is :{0}".format(res))
