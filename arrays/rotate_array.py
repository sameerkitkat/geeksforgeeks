my_list = [1,2,3,4,5]
k=2
i=0
j=len(my_list)-1

def reverse_array(my_list,i,j):
    while i<j:
        temp=my_list[i]
        my_list[i]=my_list[j]
        my_list[j]=temp
        i=i+1
        j=j-1
    return my_list

def rotate_array(my_list):
    new_list = reverse_array(my_list,i,j)
    new_list = reverse_array(new_list,i,k)
    new_list = reverse_array(new_list,k+1,j)
    print (new_list)

rotate_array(my_list)
