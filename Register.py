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

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

#cap = cv2.VideoCapture(0) #Captura webcam # 0 for webcam
cap = cv2.VideoCapture('http://192.168.100.7:8080/video')
#how to connect > connect directly > mobile internet connection
j=1

while j < 26:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)        #Reconhece a posição do rosto
        
        for (x,y,w,h) in faces:
                #print(x,y,w,h)

                color = (255, 0, 0) #BGR 0-255
                stroke = 2
                end_cord_x = x + int(1.5*w)
                end_cord_y= y + int(1.5*h)
                x=int(x*0.5)
                y=int(y*0.5)
                cv2.rectangle(frame,(int(x),int(y)),(int(end_cord_x),int(end_cord_y)),color,stroke)

                roi_gray = gray[y:end_cord_y,x:end_cord_x] #Region of intrest - Rosto preto e branco
                img_item = path + '/' + str(j) +"img.png"
                cv2.imwrite(img_item, roi_gray)
                j += 1
                print(j)

        cv2.imshow('frame1', frame)  # Exibir imagem

        if cv2.waitKey(20) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()