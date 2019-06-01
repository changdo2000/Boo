def main():	
	my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
	ans = my_dict.keys()
	ans = sorted(ans, key = lambda x: my_dict[x])
	print (ans)

if __name__ == '__main__':
	main()