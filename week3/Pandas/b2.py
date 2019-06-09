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
	laptops['size_scr'] = laptops.screen_size.str.slice(0, -1).astype('float')
	print(laptops.size_scr.value_counts())
	ultrabook = laptops[(laptops['category'] == 'Ultrabook')].size_scr
	print(ultrabook.min())
	game = laptops[(laptops['category'] == 'Gaming')].size_scr
	print(game.sum() / len(game))
if __name__ == '__main__':
	main()