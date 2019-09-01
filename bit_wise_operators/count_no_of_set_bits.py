def countSetBits(num):
    res=0
    while(num>0):
        #calculate value of number using (num&(num-1))
        num = (num & (num-1))
        res=res+1
    return res

print (countSetBits(15))
