#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

nbPCAServo=12 #Constants

#Parameters
MIN_IMP = 000
MAX_IMP = 2000
MIN_ANG = 0
MAX_ANG = 269

#Objects
pca = ServoKit(channels=16)

# function init 
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP , MAX_IMP)
      
# function main 
def main():
    pcaScenario();

# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG,MAX_ANG,1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG,MIN_ANG,-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)

if __name__ == '__main__':
    init()
    main()
