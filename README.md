------------------------------------------DESCRIPTION-------------------------------------------------------

This program builds directly upon the repository by ageitgey located: https://github.com/ageitgey/face_recognition - It is made to be used on a Windows 10 machine running Python 3.8.

An additional layer of security is added to a Windows 10 machine by continually monitoring an attached USB webcam and subsequently performing scripted Windows activities based on who is detected, was last detected and if there is a person detected or not.

------------------------------------------INSTALLATION-------------------------------------------------------

2022/09/19

NOTE - had issue getting this running on Python3.10 in the form of an error with getting cmake to install.  After revertin to Python3.8, did not experience the error anymore even after upgrading back to 3.10.

Step 1 - open your favorite shell editor.  I'm using Windows Terminal and/or PowerShell 7.  

Step 2 - clone this projects using the command `git clone https://github.com/zekenorris/face_recognition_windows.git`

Step 1 - install latest python3 as per instruction here https://www.python.org/downloads/ which should also include pip

Step 2 - install Open CV using the python pip command "pip install opencv-contrib-python" 

Step 3 - install cmake using the pip command "pip install cmake"

Step 4 - try running install other package dependencies using pip, I normally just try and run the program then keep doing "pip install <whatever is missing>"  until it runs.

For any complex errors check the detailed installations for the main packages used which are OpenCV : https://opencv.org/ and face_recognition:://opencv.org/ 

------------------------------------------USAGE-------------------------------------------------------


