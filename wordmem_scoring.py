# -*- coding: utf-8 -*-
"""
mar 7 2023

@author: mauspad
"""
print("This script loops over every csv in the data directory. IF YOU GET AN ERROR, CHECK TO SEE IF THE CSV IS BUGGED")

#import packages
import pandas as pd
import glob

#set directory
path = "data/*.csv"
for fname in glob.glob(path):

	# turn csv into dataframe
	df = pd.read_csv(fname)

	# drop practice rows
	df.dropna(subset=["choose"], inplace=True)

	# make lists and variables
	corrans = df["corrans"].tolist()
	trialans = df["test_resp.keys"].tolist()
	hits = 0
	misses = 0
	correct_rejections = 0
	false_alarms = 0
	
	# loop!
	print(fname)
	for trial in range(40):
		if corrans[trial] == "1.0":
			if trialans[trial] == 1.0 or trialans[trial] == 2.0:
				hits += 1
			else:
				misses +=1
		else: 
			if trialans[trial] == 3.0 or trialans[trial] == 4.0:
				correct_rejections += 1
			else:
				false_alarms +=1
	score = hits + correct_rejections - misses - false_alarms
	print(score)