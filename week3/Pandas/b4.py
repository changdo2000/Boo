import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

def clear_name(s):
	s = s.strip();
	s = s.replace("Operating System", "os")
	s = s.replace(" ", "_")
	s = s.replace("(", "")
	s = s.replace(")", "")
	s = s.lower()
	return s

def main():
	plt.style.use("ggplot")
	plt.rcParams["figure.figsize"] = [8, 6]
	laptops = pd.read_csv("laptops.csv", encoding = 'latin - 1')
	laptops.columns = [clear_name(x) for x in laptops.columns]
	SSD = 

if __name__ == '__main__':
	main()