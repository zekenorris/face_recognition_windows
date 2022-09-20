import face_recognition
import imutils
import pickle
import cv2
import re
# import os
# from imutils import paths
# dumbPath = list(paths.list_images('models'))

import os
from os.path import join, getsize

from PIL import Image, ImageDraw

import random

# import pyautogui
spam = 20
spammed = False
modelsDirectory = []
dirCount = 0
defaultName = "intruder"
saveDir = 'models\\'
folderBase = 'dumb_dumb_'
nextDir = saveDir
started = False
pictures = []
makeup = []
lastUser = ''
currentUser = ''
zekeActivated = False
loser = False
changedEarly = False
# pics = []

timer = 0
lastTime=0
firstLoop = True
pictureList = []
totalPics = 0
dirChanged = False
# seconds between pictures
picInterval = 0.1
# number of pictures to take
numberPics = 6
picsTaken = 0
# have to get the wrong image 5 times in a row to start filming
caughtDebounceMax = 2
caughtDebounceNumber = 0
# have to be caught over number of seconds per times
caughtDebounceInterval = 1
caughtDebounceTimer = 1

# def setupDirectory(folderBase, dirCount, nextDir)
def setupDirectory(fB=folderBase, nD = nextDir) :
    dC = 0
    with os.scandir(path=nD) as it:
        for entry in it:
            print(entry.name)
            modelsDirectory.append(entry.name)
            if(re.search("^dumb.*[0-9]$", entry.name)) :
                print(entry.name + ' matched')
                dC += 1   
    fB += str(dC)
    nD += fB
    # print('modelsDirectory', modelsDirectory, dirCount, nD)
    return nD
    

# def resetCapture(dirChanged, firstLoop, started, loser, zekeActivated, picsTaken, lastUser, currentUser, pictures, changedEarly) :

def toggle(x) :
    if(x == True) :
        return False
    if(x == False) :
        return True
    if(re.search('\W', x)) :
        return 0
    

# def resetEarly() :
#     resetCapture(dirChanged, firstLoop, started, loser, zekeActivated, picsTaken, lastUser, currentUser, pictures, changedEarly)
#     setupDirectory(folderBase, dirCount, nextDir)

nextDir = setupDirectory()

cascPathface = os.path.dirname(
 cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
# load the harcaascade in the cascade classifier
faceCascade = cv2.CascadeClassifier(cascPathface)
# load the known faces and embeddings saved in last file
data = pickle.loads(open('face_enc', "rb").read())
print("Streaming started")
video_capture = cv2.VideoCapture(0)
# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    # convert the input frame from BGR to RGB 
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # the facial embeddings for face in input
    encodings = face_recognition.face_encodings(rgb)
    names = []
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple fcaes
    for encoding in encodings:
       #Compare encodings with encodings in data["encodings"]
       #Matches contain array with boolean values and True for the embeddings it matches closely
       #and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
         encoding)
        #set name =inknown if no encoding matches
        name = defaultName
        if ((firstLoop)):
            os.mkdir(nextDir)
            firstLoop = False
            started = True 
        # check to see if we have found a match
        # if False in matches:

        #         # lastTime = time.time()
        #         firstLoop = False
        #         started = True 
        if True in matches:
            if(loser == True) :
                nextDir = setupDirectory()
                firstLoop = toggle(firstLoop)
                started = toggle(started)
                loser = toggle(loser)
                caughtDebounceNumber = 0
                picsTaken = 0
            if(zekeActivated != True) :
                zekeActivated = True
                loser = False
            #Find positions at which we get True and store them
            caughtDebounceNumber = 0
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                #Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                #increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
            #set name which has highest count
            name = max(counts, key=counts.get)
        # update the list of names
        names.append(name)
        # loop over the recognized faces
        for ((x, y, w, h), name) in zip(faces, names):
            # rescale the face coordinates
            # draw the predicted face name on the image
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
             0.75, (0, 0, 255), 2)
        if(name == defaultName) :
            if(loser != True) :
                loser = True
            if(caughtDebounceNumber <= caughtDebounceMax) :
                caughtDebounceNumber += 1
            else :
                if(picsTaken < numberPics) :
                # if(time.time()-lastTime > picInterval):
                    # pics.append(cv2.imshow("Frame", frame))
                    # cv2.imwrite(nextDir + '_' + str(picsTaken) + '.jpg', frame)
                    if(dirChanged != True) :
                        os.chdir(nextDir)
                        dirChanged = True
                    cv2.imwrite(folderBase + str(picsTaken) + '.jpg', frame)
                    picsTaken += 1
                    # lastTime = time.time()

        if(picsTaken+1 >= numberPics) :
            picIndex = 0
            clownCounter = 1
            with os.scandir(saveDir) as it:
                for entry in it:
                    # if entry.name.startswith('dumb') and entry.is_file() and entry.endswith('.jpg'):
                    if(re.search("^dumb.*png$", entry.name)) :
                        clownCounter += 1
            os.chdir(saveDir)
            with os.scandir(nextDir) as it:
                for entry in it:
                    # if entry.name.startswith('dumb') and entry.is_file() and entry.endswith('.jpg'):
                    if(re.search("^dumb.*jpg$", entry.name)) :
                        pictures.append(nextDir+'\\'+entry.name)
                        totalPics += 1
                        makeup.append(face_recognition.load_image_file(nextDir+'\\'+entry.name))
                        face_landmarks_list = face_recognition.face_landmarks(makeup[picIndex])
                        pil_image = Image.fromarray(makeup[picIndex])
                        for face_landmarks in face_landmarks_list:
                            d = ImageDraw.Draw(pil_image, 'RGBA')

                            # Make the eyebrows into a nightmare
                            d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
                            d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
                            d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
                            d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

                            # Gloss the lips
                            d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
                            d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
                            d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
                            d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

                            # Sparkle the eyes
                            d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
                            d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

                            # Apply some eyeliner
                            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
                            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

                            # pil_image.show()
                            pil_image.save(folderBase + str(clownCounter) + '.png')
                            pictures.append(saveDir + folderBase + str(clownCounter) + '.png')
                            totalPics += 1
                            # cv2.imwrite(folderBase + str(clownCounter) + '.jpg', pil_image)
                            clownCounter += 1
                        picIndex += 1
                        # print(entry.name)
            f=open(saveDir+'list.txt', 'w')
            for i in range(picIndex) :
                f.write(pictures[i]+'\n')
            # os.system('logoff')
            f.close()
            os.startfile(saveDir+'list.txt')
            if(spammed == False) :
                for i in range(spam) :
                    os.startfile(pictures[random.randint(0, totalPics-1)])
                spammed = True
                os.system('logoff')
            picsTaken = 0
            
    # cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()


