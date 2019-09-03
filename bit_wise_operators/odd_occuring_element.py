def oddOccuringElement(my_list):
    res=0
    for i in my_list:
        res=res^i
    return res

my_list = [2,2,2,5,4,4,5]
print ("Odd occuring element is {}".format(oddOccuringElement(my_list)))
