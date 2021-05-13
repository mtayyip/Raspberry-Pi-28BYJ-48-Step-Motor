
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

control_pins = [4,17,23,24]

for pin in control_pins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

halfstep_seq = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]

def setStepMotor(round,forward):
	if forward == 0:
		control_pins = [4,17,23,24]
	else :
		control_pins = [24,23,17,4]

	for i in range(round):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(control_pins[pin],halfstep_seq[halfstep][pin])
			time.sleep(0.001)

try:
	while True:
		round=raw_input("Kac Tur Donecek : ")
		forward=raw_input("Saat Yonu Icin(1),Saat Yonu Tersi Icin(0) : ")
		setStepMotor(int(round)*512,int(forward))
except KeyboardInterrupt:
	pass

GPIO.cleanup()