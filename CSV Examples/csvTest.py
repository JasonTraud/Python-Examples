import csv

with open('csvDataSample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        print("Sample " + row[0] + " value is " + row[1])