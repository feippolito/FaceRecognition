import cv2
import pickle

#Mudar  resolução
def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)
def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)
def change_res(width,height):
    cap.set(3, width)
    cap.set(4, height)
def rescale_frame(frame, percent=75):
    scale_percent = 75
    width = int(frame.shape[1]*scale_percent / 100 )
    height = int(frame.shape[0]*scale_percent / 100 )
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

labels = {}
with open ("labels.pickle", 'rb') as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

cap = cv2.VideoCapture(0) #Captura webcam # 0 for webcam
#how to connect > connect directly > mobile internet connection

make_480p()

while True:
    ret, frame = cap.read()         #Captura webcam  #Frame -> Imagem colorida
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rescale_frame(frame, 50)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)        #Reconhece rosto
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+h] #Region of intrest - Rosto preto e branco
        roi_color = frame[y:y+h,x:x+h] #Region of intrest - Rosto colorido

        id_, conf = recognizer.predict(roi_gray)  #Label , confidence
        print("conf: {}".format(conf))
        if conf <= 30:
            print(labels[id_], conf)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke ,cv2.LINE_AA)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y= y + h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)

    cv2.imshow('frame1', frame)  # Exibir imagem

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break