def factorial(num):
	if num == 0:
		return 1
	else:
		return num*factorial(num-1)
number=input("Enter number to calculate factorial : ") 
print("Factorial of {0} is {1}".format(number,factorial(int(number))))