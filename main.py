import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

sw=18
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)

NULL_CHAR = chr(0)
def write_movement(movement):
  with open("/dev/hidg0", "rb+") as fd:
    fd.write(NULL_CHAR.encode())
    fd.write(movement.to_bytes(1,"little",signed=True))
    fd.write(NULL_CHAR.encode())

movement = 16
while True:
  sw_status = GPIO.input(sw)
  if sw_status == 0:
    write_movement(movement)
    movement = ~movement+1
  else:
    pass
  time.sleep(0.5)
