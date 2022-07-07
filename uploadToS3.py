import time
import boto3 
s3 = boto3.resource('s3')
from picamera import PiCamera
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
previousEdge = 1

def captureImage():
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)
        camera.capture('guestImage.jpg')
        print("Guest image captured")
        camera.stop_preview()
        camera.close()
        
def buttonPressed(Pin4):
        global previousEdge
        input = GPIO.input(Pin4)
        if (previousEdge != 1 and input):
                print("Button pressed")
                captureImage()
                uploadToS3()
                #conditional statement looking for a rising edge in the button voltage confirming a button press
        previousEdge = input 

def uploadToS3():
        fullName = "Guest"
        file = open('guestImage.jpg', 'rb')
        object = s3.Object('shaunak2','guestImage.jpg')
        ret = object.put(Body=file, Metadata={'FullName':fullName})
        print("Image uploaded")
        return
        #uploads the captured image to the S3 bucket 

try:
        while(True):
                buttonPressed(4)
except KeyboardInterrupt:
        GPIO.cleanup()



