def maximumConsecutiveOnes(number):
    count = 0
    while(number!=0):
        number = number&(number<<1)
        count = count + 1
    return count

print ("Maximum number of consecutive ones is {0}".format(maximumConsecutiveOnes(222)))
