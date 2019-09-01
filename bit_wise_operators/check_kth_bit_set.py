def checkKthBitSet(num,k):
    #generate number with only kth bit is set by using formaula 1<<(k-1)
    special_num = 1<<(k-1)
    if (num & special_num) != 0:
        print("bit is set")
    else:
        print("bit is not set")

checkKthBitSet(5,2)
