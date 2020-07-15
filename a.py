
def carrylessAdd(x,y):
	if x < 0 and y < 0 and type(x) != int and type(y) != int:
		return False
	else:
		z = max(len(str(x)),len(str(y)))
		
		result = 0
		for i in range (1,z+1):
			a = (( (x / (10 **(i -1)) ) % 10) + (y / (10 **(i - 1)) ) % 10) % 10 * (10 ** (i -1 ))
			result += a 
		return result

print carrylessAdd (785,376)



