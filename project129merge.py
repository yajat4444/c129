import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

d1 = []
d2 = []

with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
p1 = d1[1:]

h2 = d2[0]
p2 = d2[1:]

headers = h1 + h2

planet_data = []
for i in p1:
    planet_data.append(i)
for j in p2:
    planet_data.append(j)   

with open("final_stars.csv", 'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)