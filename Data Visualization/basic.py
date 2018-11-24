import csv                          
import matplotlib.pyplot as plt 
import numpy as np

# Initialize arrays
x_axis = []
y_axis = []

# Retrieve our data from external CSV file
with open('sineData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # populate arrays
    for row in readCSV:
        x_axis.append(float(row[0])) 
        y_axis.append(float(row[1]))

# format our plot
plt.xlabel('Sample')
plt.ylabel('Voltage')
plt.title('Example Plot')

# apply data to plot
plt.plot(x_axis,y_axis)

# show plot
plt.show()