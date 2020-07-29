def isPrime(x):
	if x == 1 or x < 0:		#Good 
		return False
	for i in range (2, x):	#Try to modify x in range 
		print i 
		if x % i == 0:
			return False
		else:					#Perhaps a problem in order 
			return True

print isPrime(39)


def nthPrime(n):			#If set numbers are 0, then you need to change the numbers or add by more than 1
	counter = 0
	integer = 0
	while counter < n:			#what happens when n==1? 
		integer += 1
		if isPrime(integer) == True:
			counter += 1
		print counter, integer
	return integer

print nthPrime(4)

def testisPrime(): 
	print("Testing isPrime()....")
	assert (isPrime(-1) == False)
	assert (isPrime(0) == False)
	assert (isPrime(677) == True)			#See where the errors occur 
	assert (isPrime(1013) == True)
	assert (isPrime(1014)== False)
	print ("Passed!")

testisPrime()
