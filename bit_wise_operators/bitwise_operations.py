def bitwise_and(num1,num2):
    result = num1 & num2
    return result

def bitwise_or(num1,num2):
    result = num1 | num2
    return result

def bitwise_not(num):
    result = ~ num
    return result

def bitwise_xor(num1,num2):
    result = num1 ^ num2
    return result

def bitwise_shift(num,k):
    result=(num>>k)
    return result

print (bitwise_and(4,5))
print (bitwise_or(4,5))
print (bitwise_not(2))
print (bitwise_xor(1,2))
print (bitwise_shift(5,2))
