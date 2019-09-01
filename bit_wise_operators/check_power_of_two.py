def checkPowerofTwo(num):
    #check value of num&(num-1)
    if (num &(num-1) == 0):
        print("number is power of two")
    else:
        print("number is not power of two")

checkPowerofTwo(15)
