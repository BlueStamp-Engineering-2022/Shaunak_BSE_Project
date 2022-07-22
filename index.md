 # Shaunak D
 # Facial Recognition Doorlock
This will serve as a brief description of your project. Limit this to three sentences because it can become overly long at that point. This copy should draw the user in and make she/him want to read more.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Shaunak | Evergreen Valley High School | Aerospace Engineering | Rising Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLUyPm9lDkql57HACJpmlW91aN88FNzyqxOioTUiMTENQXb8N1k2SJOokscovDwvwWpHQtxzqjl9eZkr3oGKPCluUKkqFlOtY0NmaqmNtPLWZtcC9R8DLAHgj4aWDrxZ7iRT_iMwPqLYGsAs-knikgB_=w1830-h1828-no?authuser=0)
  
# Final Milestone 

My third and final milestone is a demonstration of my fully functional project. To test and assemble the parts of my program, I built each core function separately before combining them together. For example, I tested the uploadToS3 function by itself and then added it to the main program. I did the same for the sendEmail and buttonPressed functions. This unique approach allowed me to tweak and perfect each function by focusing only on its core functionality individually. 

One particularly interesting feauture of my program is the email and notification function. By impleneting the MIME or, Multipurpose Internet Mail Extensions library, in my program, I am able to send emails from my raspbery pi to any gmail user. In this case, I set the to and from address to a single email id that I can access. If the person at the door is identified as a verified guest, the lock will of course open and the raspbery pi will send an email to the owner notifying them that the door was unlocked, along with the name of the guest that entered the room. If the guest is not identified, the owner will receive an  email with an image attachment of the guest at the door.

Email functions: 
![emailFunciton](https://i.postimg.cc/SQVgg2XB/Screen-Shot-2022-07-22-at-9-47-55-AM.png)

The final steps before the system was functional included programming the guestSearch function, which actvily calls Amazon Rekognition and looks in the database, and establishing a serial connection between the arduino and the Raspbery Pi so that the two would be able to communicate. Although I could run the servo to control the lock without the Arduino and directly from the GPIO pins on the Pi, I decided to use the Arduino as I was interested in learning about the serial connection. Essentially, the Arduino program opens a serial connection that I've set to a baud rate of 9600. After establishing a wired connection between the two computers, the Pi is able to access the device and send commands to the Arduino console. 

Establishing the serial connection:
![serialConnection](https://i.postimg.cc/mgS3gKQ0/Screen-Shot-2022-07-22-at-9-49-06-AM.png)

[![Final Milestone](https://i3.ytimg.com/vi/C91z8Jmsm0g/maxresdefault.jpg)](https://www.youtube.com/watch?v=F7M7imOVGug&feature=emb_logo "Final Milestone"){:target="_blank" rel="noopener"}

Program Workflow:
![workFlow1](https://i.postimg.cc/XJW0kGZZ/Screen-Shot-2022-07-22-at-9-51-03-AM.png)
![workFlow2](https://i.postimg.cc/3JNQ1HwZ/Screen-Shot-2022-07-22-at-9-51-32-AM.png)

# Second Milestone 

For my second milestone, I’ll talk about the workflow and steps that I progressed through to configure and set up all the aspects of AWS that have to work together in my project. To communicate and manage AWS services, I installed the AWS command line interface onto my raspberry pi. Alongside the CLI, I installed the AWS Python SDK, which allows me to write Python scripts and connect to the secure AWS Internet Of Things.

With the preliminary steps and setup completed, I could now work on setting up the primary services that work at the forefront of my program: an Amazon S3 bucket, a Rekognition collection and database table using the DynamoDB. Amazon S3 is the commonly abbreviated form of Amazon Simple Storage System, which stores large amounts of information in buckets; essentially a hard disk in the cloud that securely holds the user's data with the added functionality of being able to communicate with other AWS services. When the doorbell is pressed, the raspberry pi takes a picture of the guest and uploads the image to the S3 bucket. To scan the image, a face search request is sent to Amazon Rekognition, a powerful visual search engine with various utlities. In Rekognition, reference images are stored in databanks called collections, similar to how Apple store's the user's face as the owner's for faceID. Rekognition then scans the image from the S3 Bucket, returning a match if found along with a confidence percentage. The information is then indexed to Amazon DynamoDB, a database which stores the face to name information. For small items, such as the information matching imageIDs to names, DynamoDB preforms tasks much faster than Amazon S3, where larger ifiles such as images are stored. If the guest is identified, the door lock opens and a notification is sent to the owner with the the guest's name and the time the door was opened. If a proper match is not recognized, an email containing an image of the guest is sent to the user. 

Throughout this process, I struggled in a few places. When storing the image IDs in DynamoDB my image file types were not supported despite appearing as JPEG files. As it turned out, when converting my images, the file type hadn’t actually changed. A handfull of other less significant errors popped up throughout the configuration and testing process. At this point, I have most of my individual components ready. My next steps just include meshing all my code together to function at the press of one button. 


[![Third Milestone](https://i3.ytimg.com/vi/bJItlKtGedE/maxresdefault.jpg)](https://www.youtube.com/watch?v=bJItlKtGedE "Second Milestone"){:target="_blank" rel="noopener"}

# Documenting progress in between milestones

In between milestones, I worked on some functions that would be important to the rest of my program. Firstly, I programmed the button event handler. Essentially, the button press varies the circuit voltage which, as read by the input pins on the Raspberry Pi, reads a value of either 0 or 1. By creating a conditional statement that looks for a rising edge in the voltage graph, the program can confirm a button press and call the next function. 

![buttonEventHandler](https://i.postimg.cc/MKQz7SHj/Screen-Shot-2022-07-22-at-9-42-00-AM.png)

Following the button event, I had to program the camera. The program for this was relativley simple and I was able to utilize Raspberry Pi documentation and other resources to complete the funcionality of the camera module. 

![cameraModule](https://i.postimg.cc/nr1gk0yg/Screen-Shot-2022-07-22-at-9-43-13-AM.png)


# First Milestone

My first milestone is a hardware showcase demonstrating the fuctionality of the lock mechanism and the rasberry pie camera module. The lock is a simple 3D printed assembly put together with screws. A sliding bolt is controlled by a servo motor, forming a rack and pinion mechanism which converts the rotational motion of the servo motor to linear motion, allowing the bolt to slide in and out. To demonstrate, I programmed the arduino to open or close the lock when a push button is pressed, creating a toggle switch. The code for this was esepcially interesting to develop despite it not having a direct connection to my main project. 

![toggleDeomstratorCode](https://i.postimg.cc/cJb3sQ2j/Screen-Shot-2022-07-01-at-10-18-09-AM.png)


[![First Milestone](https://i3.ytimg.com/vi/aTZep-6-vyo/maxresdefault.jpg)](https://www.youtube.com/watch?v=aTZep-6-vyo){:target="_blank" rel="noopener"}

# Starter Project: Customizable Arduino project 
  
  For my starter project, I opted to work on the cuztomizable arduino. I chose this particular project as a precursor to my main project, which also uses an arduino board and curcuit building. For input and output, I picked a potentiometer and a servo motor, the other primary parts of my curcuit an arduino uno microcontroller, a protoboard, as well as jumper and solid core wires. A potentiometer is a variable resister which can take a constant input voltage and output a restance that varies as the user turns a knob. This varying output volatge is read by a built in function analogRead() which assigns an integer value from 0 and 1023 to the changing voltage. Another function in the code takes this 10 bit integer and scales it between 0 and 180 degrees, which are the rotation limits of the servo motor. Servos are special types of motors that take a pulse through a PWM connection on the arduino board and make precise movements to specific locations. As the potentiometer knob is rotated, the servo motor turns. 

  I didn't face all to many challenges when working on the core project, only a little difficulty when soldering connections onto the protoboard. Motivated by my success, I decided to modify my project by adding a 7 segment display to further scale the potentiometer readings between 1 and 5 to display a crude percentage of how much the servo had rotated. A 7 segemnt display is an eletrical component with 7 LEDs arranged in a rectangular pattern. As these LEDs are lit up in sequence, different numerals and characters are displayed. Although I was able to complete a working ciruit and program a cycle of numbers to be displayed, I was unable to interface the display with the project itself as the programming is something I have to work out over the next few weeks. 

[![Starter Project](https://i3.ytimg.com/vi/Zb-74cf-3_k/maxresdefault.jpg)](https://youtu.be/Zb-74cf-3_k "Starter Project"){:target="_blank" rel="noopener"}
