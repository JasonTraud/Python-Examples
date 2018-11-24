import csv

c = csv.writer(open("output.csv", "wb"))

with open('csvDataSample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        print("Sample " + row[0] + " value is " + row[1])

        c.writerow([row[0],row[1],str(int(row[1])+10)])