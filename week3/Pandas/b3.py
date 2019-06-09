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
	laptops.columns = [clear_name(x) for x in laptops.columns]
	laptops['resolution'] = laptops.screen.str.extract("([0-9]+[x]+[0-9]*)")
	print(len(laptops.resolution[(laptops['resolution'] == '1920x1080')]))
	Mac = laptops[(laptops['model_name'].str.slice(0, 7)  == 'MacBook')].resolution
	print (Mac.value_counts())
if __name__ == '__main__':
	main()