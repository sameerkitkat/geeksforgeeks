my_list=[5,3,20,15,8,3]
print (my_list[-1])
current_max=my_list[-1]
for i in range(len(my_list)-1,0,-1):
    if (my_list[i]>current_max):
        print(my_list[i])
        current_max=my_list[i]
