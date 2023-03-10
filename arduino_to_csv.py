

import serial 
import numpy as np
import csv
import time



samples = 1000
arduino = '/dev/cu.usbmodem14201'
baud = 9600
series = serial.Serial(arduino,baud)



# Open CSV file in append mode
filename = 'sensordata.csv'

# Initialize numpy array to store sensor data
data1 = np.zeros(samples)
data2 = np.zeros(samples)
data3 = np.zeros(samples)
data4 = np.zeros(samples)

start_time = time.time()

# Collect sensor data from the Arduino
for i in range(samples):
    line = series.readline()
    dataString = line.decode('utf-8')
    values = dataString.strip().split(',')
    data1[i] = int(values[0])
    data2[i] = int(values[1])
    data3[i] = int(values[2])
    data4[i] = int(values[3])

# Calculate mean value and print to console
meanValue1 = np.mean(data1)
meanValue2 = np.mean(data2)
meanValue3 = np.mean(data3)
meanValue4 = np.mean(data4)

with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data1, data2, data3, data4)

series.close()
print("--- %s seconds ---" % (time.time() - start_time))
print("Collection of data done!")








