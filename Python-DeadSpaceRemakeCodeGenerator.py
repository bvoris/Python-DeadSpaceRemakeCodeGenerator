# Dead Space Remake Code Generator
# Created By: Brad Voris
# Version: 1.0
# Requirements: none
# Description: This tool generates stomp and melee codes for the Dead Space Remake game. This codes can be used in the ritual room. There are approximately 4092 code combinations.
# A CSV file will be written to c:\temp\deadspacecombinations.csv. If you are able to test these, please let me know which ones work.
#

import random
import csv

options = ["melee", "stomp"]

with open('c:/temp/deadspacecombinations.csv', mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Combination"])
    for i in range(4096):
        combination = []
        for j in range(12):
            combination.append(random.choice(options))
        csv_writer.writerow([",".join(combination)])
