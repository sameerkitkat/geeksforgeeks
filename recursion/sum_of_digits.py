def sumOfDigits(num):
	if (num<10):
		return num
	return sumOfDigits(num//10)+num%10

print("Sum of digits in number :{}".format(sumOfDigits(253)))