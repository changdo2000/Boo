import B1
import json 

file_inp = open("path.txt", "r")
file_out = open("path.json", "w")

dis = {}
disj = []

s = file_inp.readlines()

for i in s:
	d = {
		"path" : i,
		"file_name" : B.boo(i)
	}
	disj.append(d)

x = json.dumps(disj, indent = 4)

file_out.write(x)

file_inp.close()
file_out.close()

