import serial
import threading
from flask import Flask
import time
from twilio.rest import TwilioRestClient
import apikeys

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

#while True:
#	print ser.readline()

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

def listen():
	while True:
		recv = ser.readline()
		print recv
		stat = 0
		if "1" in recv:
			print "Collision received."
			stat = 1
			break
	return stat

def main():
	threads = []
	flas = threading.Thread(target=app.run)
	flas.start()
	threads.append(flas)
	lsfne = threading.Thread(target=listen)
	lsfne.start()
	threads.append(listen)

	#threads
	for thread in threads:
		thread.join()
    # Wait til a collision i guess

main()

ser.close()
