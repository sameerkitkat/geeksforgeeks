def generatePowersetofSet(word):
    #number of subsets = 2^len(wornd)
    n = len(word)
    print("Length of word is {0}".format(n))
    count = (1<<n)
    print("Length of power set is {0}".format(count))

    #run two loops one for number of elements and one for characters in string
    for i in range(0,count):
        for j in range(0,n):
            if i&(1<<j)>0:
                print(word[j],end="")
        print("")

#et = ['a','b','c']
generatePowersetofSet("ABC")
