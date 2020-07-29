def isPrime(x):
<<<<<<< HEAD
	if x == 1 or x < 0:		#Good 
=======
	if x == 1 or x < 0:                          # this is where you check if x is sma;ller than 1 
>>>>>>> 3c4e3be18155db0b3cd9d30a4b800dfb4c740e55
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

<<<<<<< HEAD
def testisPrime(): 
	print("Testing isPrime()....")
	assert (isPrime(-1) == False)
	assert (isPrime(0) == False)
	assert (isPrime(677) == True)			#See where the errors occur 
	assert (isPrime(1013) == True)
	assert (isPrime(1014)== False)
	print ("Passed!")

testisPrime()
=======



def testIsPrime():
    print("Testing isPrime()...")
    assert(isPrime(-1) == False)  # negative
    assert(isPrime(0) == False)   # zero
    assert(isPrime(1) == False)   # 1 is quite the special case
    assert(isPrime(2) == True)    # 2, only even prime
    assert(isPrime(3) == True)    # 3, smallest odd prime
    assert(isPrime(4) == False)   # 4, smallest even non-prime
    assert(isPrime(9) == False)   # 9, perfect square of odd prime
    assert(isPrime(987) == False) # somewhat larger non-prime
    assert(isPrime(997) == True)  # somewhat larger prime
    print("Passed!")

testIsPrime()
>>>>>>> 3c4e3be18155db0b3cd9d30a4b800dfb4c740e55
