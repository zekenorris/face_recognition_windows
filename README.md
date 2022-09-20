------------------------------------DESCRIPTION-------------------------------------------------

This program builds directly upon the repository by ageitgey located: https://github.com/ageitgey/face_recognition - It is made to be used on a Windows 10 machine running Python 3.8.

An additional layer of security is added to a Windows 10 machine by continually monitoring an attached USB webcam and subsequently performing scripted Windows activities based on who is detected, was last detected and if there is a person detected or not.

The program first scans and parses the chosen folder, then creates a naming scheme based on selected options in the chosen folder.  Defaults are to name detected intruders as 'dumb_dumb<number>.jpg inside the models folder, with a specific matching 'dumb_dumb' folder.

After the 'intruder's' picture is captured, the program also applies digital makeup to 'sillify' the image, then saves the modified image directly in the chosen root folder, default 'models'

A user could set the windows wallpaper to automatically create a slideshow from the intruder's images so as to easily identify intrusions at logon.

------------------------------INSTALLATION-------------------------------------------

2022/09/19

NOTE - had issue getting this running on Python3.10 in the form of an error with getting cmake to install.  After revertin to Python3.8, did not experience the error anymore even after upgrading back to 3.10.

Step 1 - open your favorite shell editor.  I'm using Windows Terminal and/or PowerShell 7.  

Step 2 - clone this projects using the command `git clone https://github.com/zekenorris/face_recognition_windows.git`

Step 3 - install latest python3 as per instruction here https://www.python.org/downloads/ which should also include pip

Step 4 - install Open CV using the python pip command `pip install opencv-contrib-python` 

Step 5 - install cmake using the pip command `pip install cmake`

Step 6 - try running face_scan.py using the command `python face_scan.py` and install any other package dependencies that appear as error messages using `pip install <whatever is missing>`  until it runs, then do the same with face_security.py

For any other errors check the detailed installations for the main packages used which are OpenCV : https://opencv.org/ and face_recognition: https://github.com/ageitgey/face_recognition and make sure there are no other missing dependencies.

------------------------------------USAGE-------------------------------------------------

In order to detect faces, the program needs to first scan some pictures to make a list of known people.  In the project root is a folder named `models`.  In order to train the algorithm to recognize a face, perform the following

ADDING A NEW FACE
Step 1 - Create a new folder in the models folder with the desired model name, ie, `face_recognition/models/<insert desired name here>`
Step 2 - Paste some pictures of the desired model into the newly created folder.  Anything from 1-desired amount appears fine, however, my computer seems to start taking significantly longer to create models with over 15 pictures.
Step 3 - change directory to the folder root if not already there, then execute the command `python3 face_scan.py`
Step 4 (OPTIONAL) - check the root directory for a file named `face_enc`, but don't bother trying to open it as it's not a human readable format. It is however what the machine will use to verify models against.
Step 5 - again in the project root execute the command `python3 scan_faces.py` to start the face scanning program.
