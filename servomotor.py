import time
from adafruit_servokit import ServoKit


pca = ServoKit(channels=16)
pca.servo[0].set_pulse_width_range(500 , 2500)
pca.servo[1].set_pulse_width_range(500 , 2500)
pca.servo[0].actuation_range = 270
pca.servo[1].actuation_range = 270

for i in range(10):
  pca.servo[0,1].angle = 0
  time.sleep(2)
  pca.servo[0,1].angle = 90
  time.sleep(2)
  pca.servo[0].angle = 180
  time.sleep(2)
  pca.servo[1].angle = 0
  time.sleep(2)
  pca.servo[0,1].angle = 0
  time.sleep(2)
  
