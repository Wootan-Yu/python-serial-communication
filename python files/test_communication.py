#!usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0) #'baud' should be the same with arduino
time.sleep(3)
ser.reset_input_buffer() #clear input buffer
#print("Serial ok")



try:
    while True: #line from arduino will be sent every 1 second

        # arduino -> raspberry pi
        #time.sleep(0.01)
        #if ser.in_waiting > 0:
        #    line = ser.readline().decode('utf-8').rstrip()
        #    print(line)
        
        
        # raspberry pi -> arduino 
        time.sleep(1)
        #print("sending msg to arduino")
        user_input = input("input direction (left, right, forward): ")
        msg = user_input + "\n"
        ser.write(msg.encode('utf-8'))
except KeyboardInterrupt: #to stop press (crtl+c).  note: pressing stop above will not 
    print("close serial communication") # 				  stop the program
    ser.close() 
        