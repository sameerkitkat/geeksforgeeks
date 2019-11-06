my_list = [1,2,3,4,5]
i=0 
j=len(my_list)-1
while i<j:
    temp=my_list[i]
    my_list[i]=my_list[j]
    my_list[j]=temp
    i=i+1
    j=j-1

print(my_list)
