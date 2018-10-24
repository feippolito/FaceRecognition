import os
import cv2

def createFolder(directory):

        if not os.path.exists(directory):
                os.makedirs(directory)
                return 1
        else:
                print ('Nome já existe.')
                return 0
        
        
i=0
while i==0:
        print('Name:')
        name = input()
        path  = './images/' + name
        i = createFolder(path)
        print(i)

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt_tree.xml')

cap = cv2.VideoCapture(0) #Captura webcam # 0 for webcam
#how to connect > connect directly > mobile internet connection

while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)        #Reconhece a posição do rosto
        
        for (x,y,w,h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h,x:x+h] #Region of intrest - Rosto preto e branco

        j=0
        
        for j in range (0,10):
                img_item = str(j) +"img.png"
                cv2.imwrite(img_item, roi_gray)
