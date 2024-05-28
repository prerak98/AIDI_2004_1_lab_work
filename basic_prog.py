def fibo(n):
	if n<=1:
		return n
	else:    
		return (fibo(n-1)+fibo(n-2))


terms = int(input("Enter number of terms.  :  "))

if terms < 0:
	print("Please, enter positive value")
else:
	print("Series :")
	for i in range(terms):
		print(fibo(i))

