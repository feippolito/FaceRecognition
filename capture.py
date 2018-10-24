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

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) #Captura webcam # 0 for webcam
#how to connect > connect directly > mobile internet connection
j=0
while j <= 100:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)        #Reconhece a posição do rosto
        
        for (x,y,w,h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h,x:x+h] #Region of intrest - Rosto preto e branco

                             
                img_item = path + '/' + str(j) +"img.png"
                cv2.imwrite(img_item, roi_gray)
                j += 1

                color = (255, 0, 0) #BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y= y + h
                cv2.rectangle(frame,(int(0.5*x),int(0.5*y)),(int(1.5*end_cord_x),int(1.5*end_cord_y)),color,stroke)


        cv2.imshow('frame1', frame)  # Exibir imagem

        if cv2.waitKey(20) & 0xFF == ord('q'):
                break
