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
    print "left triggered"
    return "left"

@app.route("/go/right")
# Right turn signal
def goRight():
    ser.write("right\n")
    print "right triggered"
    return "right"

def listen():
	while True:
		recv = ser.readline()
		print recv
		stat = 0
		if "1" in recv:
			#send sms to emerg contact
			client = TwilioRestClient(apikeys.TWILIO_ATSID, apikeys.TWILIO_TOKEN)
			message = client.messages.create(to="+14122568726", from_="+15859783364", body="This is an automatic alert from HEADSMART. Your friend ZACK THOMPSON has potentially been in a collission, please attempt to contact them and/or alert emergency services.")
			print message
                        print "Collision detected. Sent twilio message"
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

main()

ser.close()
