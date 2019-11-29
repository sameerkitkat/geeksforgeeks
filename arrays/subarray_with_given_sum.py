def max_sum():
    my_list = [1, 4, 20, 3, 10, 5]
    current_sum = my_list[0]
    start = 0
    given_sum = 33
    for end in range(1, len(my_list)):
        while current_sum > given_sum and start < end - 1:
            current_sum -= my_list[start]
            start = start + 1
        if current_sum == given_sum:
            return True
        if end < len(my_list):
            current_sum += my_list[end]
    if current_sum == given_sum:
        return True
    else:
        return False


data = max_sum()
print(data)
