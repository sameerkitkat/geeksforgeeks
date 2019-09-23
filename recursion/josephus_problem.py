def josephusProblem(n,k):
	if n==1:
		return n
	return (josephusProblem(n-1,k)+k-1)%n+1
print(josephusProblem(7,3))