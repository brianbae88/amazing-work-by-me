def isPrime(x):
	if x == 1 or x < 0:                          # this is where you check if x is sma;ller than 1 
		return False
	for i in range (2, x):
		print i 
		if x % i == 0:
			return False
		else:
			return True

print isPrime(39)


def nthPrime(n):
	counter = 0
	integer = 0
	while counter < n:
		integer += 1
		if isPrime(integer) == True:
			counter += 1
		print counter, integer
	return integer

print nthPrime(4)




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
