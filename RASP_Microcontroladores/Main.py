from Meter import *
from Button import *
import time
from threading import Thread
"""
import RPi.GPIO as GPIO                #UNCOMMENT
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_PWM=20
GPIO_SENSOR1 = 23


# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_PWM,GPIO.OUT)
GPIO.setup(GPIO_SENSOR1, GPIO.IN)



def calcularpulso():
    StartTime = time.time()
    StopTime = StartTime+1

    aux2=0
    i=0

    while (time.time()<=StopTime):
        aux1= GPIO.input(24)
        if(aux1!=aux2):
            i=i+1

        aux2=aux1

    v=i*60
    print(v)

    return v


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

pwm = GPIO.PWM(GPIO_PWM,100)
pwm.start(0)
"""
#Create the duty cycle variable
dutyC = 0

sensorMax = 50
sensorMin = 10

def sentido(self):
    if self.sentido == 0:
        self.button6.configure(bg="#4ed885")
        self.button5.configure(bg=self.orig_color)
    else:
        self.button5.configure(bg="#4ed885")
        self.button6.configure(bg=self.orig_color)
"""
def pseudo():
    print("START")
    StartTime = time.time()
    StopTime = StartTime+10
    aux2=0
    i=0
    v=0
    while (time.time()<=StopTime):
        i=i+1

    v=i
    print(v)
    print("END")

    return v
    
"""

def do_main():
    global v
    v=0
    root = Tk()
    frame_1 = Frame()
    frame_2 = Frame()
    frame_3 = Frame()
    frame_4 = Frame()

    frame_1.grid(row=0, column=0,rowspan=2)
    frame_2.grid(row=0, column=1,rowspan=2)
    frame_3.grid(row=0, column=3)
    frame_4.grid(row=1, column=3)

    Element_1 = Analog_Meter(master=frame_1, side=300, start=0, end=100, grad_max=10, grad_min=5, lim1=0, lim2=100,value=0, text="PWM - Duty Cycle", units="%")
    Element_2 = Analog_Meter(master=frame_2, side=300, start=0, end=100, grad_max=10, grad_min=2, lim1=0, lim2=100,value=0, text="Velocidade", units="rpm")
    Element_3 = Analog_Meter(master=frame_3, side=200, start=0, end=200, grad_max=50, grad_min=5, lim1=sensorMin, lim2=sensorMax,value=0, text="Sensor", units="cm")
    Element_4 = Button_Class(master=frame_4, height=100, width=200)

    root.resizable(width=FALSE, height=FALSE)           # window size is not resizable
    aux = 0
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    Analog_Meter.delete_entry(Element_2)
    Analog_Meter.delete_entry(Element_3)
    Analog_Meter.delete_entry(Element_1)
    velTXT = Element_2.can_meter.create_text(Element_2.side/2,Element_2.origy+Element_2.R*1.3,text=" ")

    while True:                                         # creates a loop for the main window
        #if Element_4.sentido == 1:
        #    print("HORARIO")
            #pwm = GPIO.PWM(GPIO_PWM, 100)           #UNCOMMENT
        #else:
        #    print("ANTI-HORARIO")
            #pwm = GPIO.PWM(GPIO_PWMH, 100)          #UNCOMMENT
        text=Button_Class.GetText(Element_4)


        if text == "PWM":
            sentido(Element_4)
            Analog_Meter.delete_entry(Element_3)
            Analog_Meter.delete_entry(Element_2)
            Analog_Meter.enable_entry(Element_1)
            Element_2.can_meter.itemconfigure(velTXT, text=" ")

            Analog_Meter.Read(Element_3, 0)
            Analog_Meter.ChangeText(Element_3, "Desativado")

            #dutyC=Element_1.value                              #UNCOMMENT
            #pwm.ChangeDutyCycle(dutyC)                         #UNCOMMENT

        elif text == "Velocidade":
            sentido(Element_4)
            Analog_Meter.delete_entry(Element_1)
            Analog_Meter.delete_entry(Element_3)
            Analog_Meter.enable_entry(Element_2)
            Analog_Meter.Read(Element_3,0)
            Analog_Meter.ChangeText(Element_3,"Desativado")
            Element_2.can_meter.itemconfigure(velTXT, text="Velocidade medida: {} rpm".format(Element_2.value),font=("Purisa", 12))      #MUDAR PARA A FUNCAO LER VEL

        elif text == "Sensor":
            sentido(Element_4)
            #time.sleep(0.5)                                        #UNCOMMENT
            Analog_Meter.ChangeText(Element_3, "Sensor")
            Element_2.can_meter.itemconfigure(velTXT, text=" ")

            Analog_Meter.delete_entry(Element_1)
            Analog_Meter.delete_entry(Element_2)
            Analog_Meter.enable_entry(Element_3)
            #Element_3.can_meter.bind("<Button-1>", '')          #UNCOMMENT

            #dist = round(distance(),2)                         #Uncomment
            #Analog_Meter.Read(Element_3,dist)                  #Uncomment
            dist = Element_3.value                              #Comment

            if dist < sensorMin:
                dist = sensorMin
            if dist > sensorMax:
                dist = sensorMax
            dutyC = round((((100-0)*(dist-sensorMin))/(sensorMax-sensorMin)+0),1)
            Analog_Meter.Read(Element_1, dutyC)
            #pwm.ChangeDutyCycle(dutyC)                         #UNCOMMENT

        elif text == "Desligado":
            Element_2.can_meter.itemconfigure(velTXT, text=" ")
            Analog_Meter.delete_entry(Element_1)
            Analog_Meter.delete_entry(Element_2)
            Analog_Meter.delete_entry(Element_3)
            Analog_Meter.Read(Element_1, 0)
            Analog_Meter.Read(Element_2, 0)
            Analog_Meter.Read(Element_3, 0)
            #pwm.ChangeDutyCycle(0)                            #UNCOMMENT

        root.update_idletasks()
        root.update()
        time.sleep(0.01)


if __name__ == "__main__":
    t1=Thread(target= do_main , args= [])
    t1.start()

    while True:
        t2 = Thread(target=calcularpulso, args=[])
        t2.start()
        t2.join()