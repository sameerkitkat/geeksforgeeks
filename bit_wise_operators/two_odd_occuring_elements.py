def twoOddOccuringElements(my_list):
    res=0
    for i in my_list:
        res=res^i
    print ("Result of XOR is {0}".format(res))
    #find right most set bit in XOR
    set_bit = res & (~(res-1))
    print ("Rightmost set bit in XOR is {0}".format(set_bit))

    x=0
    y=0
    for i in my_list:
        if (i & set_bit):
            x=x^i
        else:
            y=y^i
    print("Result is {0} {1}".format(x,y))


my_list=[3,3,3,4,5,4,5,6]
twoOddOccuringElements(my_list)
