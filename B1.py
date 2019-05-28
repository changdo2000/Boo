def boo(s):
	n = int(len(s))
	ans = ""
	for i in range(0, n):
		if s[i] == '/' :
			ans = ""
		else:
			ans = ans + str(s[i])

	while (ans[len(ans) - 1] == ' '): 
		ans = ans.replace(ans[len(ans) - 1], '')
	return ans	

s = str(input())
print(boo(s))

#print(len(input().split('/')[-1]))