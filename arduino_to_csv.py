

import serial

import csv

samples = 15
arduino = '/dev/cu.usbmodem14201'
baud = 9600
series = serial.Serial(arduino,baud)


#print_label = False'

filename = 'sensordata.csv'

file = open(filename,'a')
print('File created')

row = 0
sensordata = []
while row <= samples:

    line=series.readline()
    dataString = line.decode('utf-8')

    data=dataString[0:][:-1]
    print(data)

    read = data.split(",")
    print(read)

    sensordata.append(read)
    print(sensordata)

    row = row+1


with open(filename, 'w', encoding='UTF8', newline='') as f:
    write = csv.writer(f)
    write.writerows(sensordata)

print("Collection of data done!")
file.close()








