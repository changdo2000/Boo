import numpy as np 
import pandas as pd 


def clear_name(s):
	s = s.strip();
	s = s.replace("Operating System", "os")
	s = s.replace(" ", "_")
	s = s.replace("(", "")
	s = s.replace(")", "")
	s = s.lower()
	return s
		
def main():
	laptops = pd.read_csv("laptops.csv", encoding = 'latin - 1')
	new_name = [clear_name(x) for x in laptops.columns]
	laptops.columns = new_name
	laptops['Ram_GB'] = laptops.ram.str.slice(0, -2).astype('int')
	laptops["Speed_ghz"] =  laptops.cpu.str.replace("GHz", "").str.extract(" ([0-9\.]*)$").astype("float")
	mapping = {"Windows": "Windows", "No OS": "No OS", "Linux": "Linux", "Chrome OS": "Chrome OS", "macOS": "macOS", "Mac OS": "macOS", "Android": "Android"}
	laptops['os_new'] = laptops.os.map(mapping)
	laptops.loc[laptops.os_new == "No OS", "os_version"] = "No OS"
	laptops.loc[laptops.os_new == "macOS", "os_version"] = "X"
	print(laptops)

if __name__ == '__main__':
	main()