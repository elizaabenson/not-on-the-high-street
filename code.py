#import libraries
import csv
from collections import defaultdict
from collections import Counter

#read in csv file
columns = defaultdict(list) # each value in each column is appended to a list

with open('C:/Users/frizz/OneDrive/Desktop/nypd-arrest-data-2018-1.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v)

            #bring back results just for OFNS_DESC column
OFNS_DESC=(columns['OFNS_DESC'])
