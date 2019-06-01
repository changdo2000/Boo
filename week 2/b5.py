def check(s):
	if s == s[::-1]:
		return "True"
	else: return	"False"

def main():
	s = str(input())
	print(check(s))

if __name__ == '__main__':
	main()
