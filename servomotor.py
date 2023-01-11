import time
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)
pca.servo[0].set_pulse_width_range(500 , 2500)
pca.servo[0].actuation_range = 270
for i in range(10):
  pca.servo[0].angle = 0
  time.sleep(4)
  pca.servo[0].angle = 90
  time.sleep(1)
  pca.servo[0].angle = 0
  time.sleep(2)
  pca.servo[0].angle = 180
  time.sleep(1)
  pca.servo[0].angle = 0
  time.sleep(2)
  pca.servo[0].angle = 270
  time.sleep(1)
