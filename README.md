## How to use

#### 1. Execute [Register.py](https://github.com/feippolito/FaceRecognition/blob/master/Register.py) to take pictures to register faces.
 

to use computer native webcam make sure the code is:

```python
cap = cv2.VideoCapture(0)
```

its also possible to use an phone camera to register:
insert the adress as parameter

```python
cap = cv2.VideoCapture('http://192.168.100.7:8080/video')
```


#### 2. Run [Trainer.py](https://github.com/feippolito/FaceRecognition/blob/master/Trainer.py) to execute the Cascade Classifier Training.
 
 
#### 3. [Recognition.py](https://github.com/feippolito/FaceRecognition/blob/master/Recognition.py) should correctly display and recognize faces.
