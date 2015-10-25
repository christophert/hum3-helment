import serial
from xbee import XBee
from flask import Flask
import time

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)
#xbee = XBee(ser)
app = Flask(__name__)

#while True:
#    try:
#		print ser.readline()
#        print xbee.wait_read_frame()
#        if input is "1":
#            print "you idiot you hit wall"
#    except KeyboardInterrupt:
#        break

line = []
while True:
	print ser.readline()
ser.close()

@app.route("/go/left")
# Left turn signal
def goLeft():
    ser.write("left\n")
    return "left"

@app.route("/go/right")
# Right turn signal
def goRight():
    ser.write("right\n")
    return "right"


def main():
    app.run()
    # Wait til a collision i guess

main()
