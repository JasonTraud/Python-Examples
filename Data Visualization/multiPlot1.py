import csv                          
import matplotlib.pyplot as plt 
import numpy as np

# Initialize arrays
x_axis = []
y_axis_sin = []
y_axis_cos = []
y_axis_sinc = []

# Retrieve our data from external CSV file
with open('multiPlotData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # populate arrays
    for row in readCSV:
        x_axis.append(float(row[0])) 
        y_axis_sin.append(float(row[1]))
        y_axis_cos.append(float(row[2]))
        y_axis_sinc.append(float(row[3]))

# format our plot
plt.xlabel('Sample')
plt.ylabel('Voltage')
plt.title('Example Plot')

# apply data to plot
plt.plot(x_axis,y_axis_sin, label='SIN')
plt.plot(x_axis,y_axis_cos, label='COS')
plt.plot(x_axis,y_axis_sinc, label='SINC')

plt.legend()

# show plot
plt.show()