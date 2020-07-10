# import math

# def fabricYards(inches):
# 	yard = inches /36.0
# 	yard = math.ceil(yard)
# 	return yard
# print fabricYards (35)


# def fabricExcess(purchase,desired):
# 	purchase = purchase * 36
# 	excess = purchase - desired
# 	return excess

# print fabricExcess (fabricYards(23),23)



# def eggCartons(x):
# 	if type(x) == int and x > 0:
# 		x = x/12.0
# 	x = math.ceil(x)

# 	return int(x)
# print eggCartons(40)

# def isEquailateralTriangle(x,y,z):
# 	if x == y == z:
# 		print 'true'
# 	else:
# 		print 'false'
# 	return x,y,z
# isEquailateralTriangle(3,3,3)

# def isLegalTriangle(a,b,c):
# 	if a < 0 or b < 0 or c < 0: print(false)
# 	if a + b < c or a + c < b or c + b < a: print(true)
# isLegalTriangle (3,5,7)

def isRightTriangle(x1,y1,x2,y2,x3,y3):
	x = (((x1-x2)**2)+((y1-y2)**2))**0.5
	y = (((x1-x3)**2)+((y1-y3)**2))**0.5
	z = (((x2-x3)**2)+((y2-y3)**2))**0.5

	a,b,c = sorted([x,y,z])

	return a**2 == b**2 + c**2


print isRightTriangle(0.123,0,4,0,4,3)




