def ntoOne(num):
    if num == 0:
        return
    else:
        print(num)
        ntoOne(num - 1)


ntoOne(5)
