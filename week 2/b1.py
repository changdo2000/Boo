def main():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("fizzbuzz", end = ' ')
		elif i % 3 == 0:
			print("fizz", end = ' ')
		elif i % 5 == 0:
			print("buzz", end = ' ')
		else: print (i, end = ' ')
if __name__ == '__main__':
	main()