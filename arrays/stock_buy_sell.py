my_list = [100, 180, 260, 310, 40, 535, 695]
profit_dict = {}
n = len(my_list)
count = 0
i = 0
while i < n - 1:
    while i < n - 1 and my_list[i + 1] <= my_list[i]:
        i += 1
    if i == n - 1:
        break
    profit_dict = {'Buy': i}
    i = i + 1
    print(profit_dict)

    while i < n and my_list[i] >= my_list[i - 1]:
        i += 1
    i = i - 1
    profit_dict = {'Sell': i}
    print(profit_dict)

    count += 1

