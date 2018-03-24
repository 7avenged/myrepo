import serial
import matplotlib.pyplot as plt
import numpy as np
import csv

#csvfile = open('data_log1.csv', 'wb') #open file for operation
#writer = csv.writer(csvfile) 

ser = serial.Serial("/dev/ttyACM4", 9600)
#ser = serial.Serial("/dev/rfcomm0", 9600)
a=0 
while a!=120:
    print ser.readline()    
    #k = ser.readline()
    #sound,smoke = k.split(",")
    #angle = float(angle)
          
    #writer.writerow([sound, smoke])
              
    a = a+1
#THIS IS FOR THE FILEweewre
