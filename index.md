 # Shaunak D
 # Facial Recognition Doorlock
This will serve as a brief description of your project. Limit this to three sentences because it can become overly long at that point. This copy should draw the user in and make she/him want to read more.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Shaunak | Evergreen Valley High School | Aerospace Engineering | Rising Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLUyPm9lDkql57HACJpmlW91aN88FNzyqxOioTUiMTENQXb8N1k2SJOokscovDwvwWpHQtxzqjl9eZkr3oGKPCluUKkqFlOtY0NmaqmNtPLWZtcC9R8DLAHgj4aWDrxZ7iRT_iMwPqLYGsAs-knikgB_=w1830-h1828-no?authuser=0)
  
# Final Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint. 

[![Final Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612573869/video_to_markdown/images/youtube--F7M7imOVGug-c05b58ac6eb4c4700831b2b3070cd403.jpg )](https://www.youtube.com/watch?v=F7M7imOVGug&feature=emb_logo "Final Milestone"){:target="_blank" rel="noopener"}

# Second Milestone 

For my second milestone, I’ll talk about the workflow and steps that I progressed through to configure and set up all the aspects of AWS that have to work together in my project. To communicate and manage AWS services, I installed the AWS command line interface onto my raspberry pi. Alongside the CLI, I installed the AWS Python SDK, which allows me to write Python scripts and connect to the secure AWS Internet Of Things.

With the preliminary steps and setup completed, I could now work on setting up the primary services that work at the forefront of my program: an Amazon S3 bucket, a Rekognition collection and database table using the DynamoDB. Amazon S3 is the commonly abbreviated form of Amazon Simple Storage System, which stores large amounts of information in buckets; essentially a hard disk in the cloud that securely holds the user's data with the added functionality of being able to communicate with other AWS services. When the doorbell is pressed, the raspberry pi takes a picture of the guest and uploads the image to the S3 bucket. To scan the image, a face search request is sent to Amazon Rekognition, a powerful visual search engine with various utlities. In Rekognition, reference images are stored in databanks called collections, similar to how Apple store's the user's face as the owner's for faceID. Rekognition then scans the image from the S3 Bucket, returning a match if found along with a confidence percentage. The information is then indexed to Amazon DynamoDB, a database which stores the face to name information. For small items, such as the information matching imageIDs to names, DynamoDB preforms tasks much faster than Amazon S3, where larger ifiles such as images are stored. If the guest is identified, the door lock opens and a notification is sent to the owner with the the guest's name and the time the door was opened. If a proper match is not recognized, an email containing an image of the guest is sent to the user. 

Throughout this process, I struggled in a few places. When storing the image IDs in DynamoDB my image file types were not supported despite appearing as JPEG files. As it turned out, when converting my images, the file type hadn’t actually changed. A handfull of other less significant errors popped up throughout the configuration and testing process. At this point, I have most of my individual components ready. My next steps just include meshing all my code together to function at the press of one button. 


[![Third Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612574014/video_to_markdown/images/youtube--y3VAmNlER5Y-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=y3VAmNlER5Y&feature=emb_logo "Second Milestone"){:target="_blank" rel="noopener"}

# Documenting progress in between milestones
include button event, camera, and email

# First Milestone

My first milestone is a hardware showcase demonstrating the fuctionality of the lock mechanism and the rasberry pie camera module. The lock is a simple 3D printed assembly put together with screws. A sliding bolt is controlled by a servo motor, forming a rack and pinion mechanism which converts the rotational motion of the servo motor to linear motion, allowing the bolt to slide in and out. To demonstrate, I programmed the arduino to open or close the lock when a push button is pressed, creating a toggle switch. The code for this was esepcially interesting to develop despite it not having a direct connection to my main project. 

![toggleDeomstratorCode](https://i.postimg.cc/cJb3sQ2j/Screen-Shot-2022-07-01-at-10-18-09-AM.png)

In addition to the lock hardware, I assembled the rasbery pi camera continue...

[![First Milestone](https://i3.ytimg.com/vi/aTZep-6-vyo/maxresdefault.jpg)](https://www.youtube.com/watch?v=aTZep-6-vyo){:target="_blank" rel="noopener"}

# Starter Project: Customizable Arduino project 
  
  For my starter project, I opted to work on the cuztomizable arduino. I chose this particular project as a precursor to my main project, which also uses an arduino board and curcuit building. For input and output, I picked a potentiometer and a servo motor, the other primary parts of my curcuit an arduino uno microcontroller, a protoboard, as well as jumper and solid core wires. A potentiometer is a variable resister which can take a constant input voltage and output a restance that varies as the user turns a knob. This varying output volatge is read by a built in function analogRead() which assigns an integer value from 0 and 1023 to the changing voltage. Another function in the code takes this 10 bit integer and scales it between 0 and 180 degrees, which are the rotation limits of the servo motor. Servos are special types of motors that take a pulse through a PWM connection on the arduino board and make precise movements to specific locations. As the potentiometer knob is rotated, the servo motor turns. 

  I didn't face all to many challenges when working on the core project, only a little difficulty when soldering connections onto the protoboard. Motivated by my success, I decided to modify my project by adding a 7 segment display to further scale the potentiometer readings between 1 and 5 to display a crude percentage of how much the servo had rotated. A 7 segemnt display is an eletrical component with 7 LEDs arranged in a rectangular pattern. As these LEDs are lit up in sequence, different numerals and characters are displayed. Although I was able to complete a working ciruit and program a cycle of numbers to be displayed, I was unable to interface the display with the project itself as the programming is something I have to work out over the next few weeks. 

[![Starter Project](https://i3.ytimg.com/vi/Zb-74cf-3_k/maxresdefault.jpg)](https://youtu.be/Zb-74cf-3_k "Starter Project"){:target="_blank" rel="noopener"}
