#umesh8joshi

#Function to check if the given integer is power of two or not

'''
	inpute type : int
	return type : bool
'''

def is_power_of_two(n):
	return n > 0 and not n & (n-1)

#test cases

power_of_two = [2,4,8,16]

if __name__ == "__main__":
	for i in power_of_two:
		ans = is_power_of_two(i)
		if ans == True:
			print('test passed')
		else:
			print('test failed')