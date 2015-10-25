import serial
from xbee import XBee

PORT = '/dev/ttyUSB0'
BAUD_Rate = 9600
ser = serial.Serial(PORT, BAUD_RATE)
xbee = XBee(ser)

# Left turn signal
def goLeft():
    ser.write("left/n")

# Right turn signal
def goRight():
    ser.write("right/n")

def main():
    # Wait til a collision i guess
    while True:
        try:
            xbee.wait_read_frame()
            
        except KeyboardInterrupt:
            break
    ser.close()
