my_list = [1,8,30,-5,20,7]
n = len(my_list)
k = 3
max_sum = 0
current_sum = 0
for i in range (0,k):
	current_sum += my_list[i]
max_sum = current_sum
for i in range (k,n):
	current_sum += (my_list[i]-my_list[i-k])
	if current_sum > max_sum:
		max_sum = current_sum

print("Maxmimum sum of k elements is :{0}".format(max_sum))