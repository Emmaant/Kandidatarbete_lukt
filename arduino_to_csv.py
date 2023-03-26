

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
data = np.zeros(samples)
start_time = time.time()

row = []

# Collect sensor data from the Arduino
for i in range(samples):
    line = series.readline()
    dataString = line.decode('utf-8')
    values = dataString.strip().split(',')
    data[i] = int(values[0])

# Calculate mean value and print to console
row.append(np.mean(data))

with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row)

series.close()
print("--- %s seconds ---" % (time.time() - start_time))
print("Collection of data done!")








