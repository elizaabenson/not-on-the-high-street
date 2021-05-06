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

# count the occurences of each value in the OFNS_DESC column in desc order
ctr = Counter(OFNS_DESC)
sorted(ctr, key=ctr.get, reverse=True)

#print first 10 values from count above

listofTuples = sorted(ctr.items() , reverse=True, key=lambda x: x[1])
listofTuples[:10]

#see screenshot 1 for the results of the above query

#allow the user to enter part of an offense description and bring back the number of occurrences for that description
#this code allows for printing the result on the screen, however the next step will also save the results to a csv as requested, so line 40 could be omitted if not required

# initializing search key string
search_key = input("Enter offence descripton: ")
  
# Using dict() + filter() + lambda
# Substring Key match in dictionary
res = dict(filter(lambda item: search_key in item[0], ctr.items()))
  
# printing result 
print("The volume of occurrences for that offense description is: " + str(res))

#see screenshot 2 for the results of the above query

#write the results to a csv file
with open('C:/Users/frizz/OneDrive/Desktop/test.csv', 'w') as f:  
    writer = csv.writer(f)
    for k, v in res.items():
       writer.writerow([k, v])
    
#see screenshot 3 for the results of the above query

#unit test 1 - search for all instances of word in the entire CSV and check it is identical to the result from just searching OFNS_DESC column 
total = 0

with open('C:/Users/frizz/OneDrive/Desktop/nypd-arrest-data-2018-1.csv') as f:
    for line in f:
        found = line.find('DANGEROUS DRUGS')
        if found != -1 and found != 0:
            total += 1           

print (total)

#see screenshot 4 for the results of the above query

# unit test 2 - check that the final CSV correctly contains the right value for the instances of DANGEROUS

#check whole csv for instances
total = 0

with open('C:/Users/frizz/OneDrive/Desktop/nypd-arrest-data-2018-1.csv') as f:
    for line in f:
        found = line.find('DANGEROUS')
        if found != -1 and found != 0:
            total += 1

print (total)

#check against values produced from code below 
search_key = input("Enter offence descripton: ")
res = dict(filter(lambda item: search_key in item[0], ctr.items()))
print("The volume of occurrences for that offense description is: " + str(res))
with open('C:/Users/frizz/OneDrive/Desktop/test.csv', 'w') as f:  
    writer = csv.writer(f)
    for k, v in res.items():
       writer.writerow([k, v])

#see screenshots 5a and 5b for the results of the above query

# unit test 3 - check that all instances of ASSAULT are found by inputing ASSAULT, ASSAUL, ASSAU
search_key = input("Enter offence descripton: ")
res = dict(filter(lambda item: search_key in item[0], ctr.items()))
print("The volume of occurrences for that offense description is: " + str(res))
with open('C:/Users/frizz/OneDrive/Desktop/test.csv', 'w') as f:  
    writer = csv.writer(f)
    for k, v in res.items():
       writer.writerow([k, v])

