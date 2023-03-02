

import serial 
import csv
samples = 15
arduino = '/dev/cu.usbmodem14201'
baud = 9600
series = serial.Serial(arduino,baud)


filename = 'sensordata.csv'

# Open serial port
series = serial.Serial(arduino, baud)

# Open CSV file in append mode
filename = 'sensordata.csv'
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    
    # Read sensor data from the Arduino and append to the CSV file
    for i in range(samples):
        line = series.readline()
        dataString = line.decode('utf-8')
        
        values = dataString.strip().split(',')
        
        writer.writerow(values)


series.close()
print("Collection of data done!")








