
from tkinter import *
from math import *

#http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html  Key names

class Analog_Meter():
    def __init__ (self, master, side, start, end, grad_max, grad_min, lim1, lim2, value, text,units):
        self.master = master                                                                        #create window
        self.master.title=("Messgeraet")                                                            #name of the window
        self.create(side,end,start,grad_max,grad_min,lim1,lim2,text,units)                          #parameters (side,end,start,grad_max,grad_min,lim1,lim2)
        self.Read(value)                                                                            #parameter (value)
        self.can_meter.grid(row=0,column=0,columnspan=5,rowspan=20)                                 #create window
        self.delete_entry()

    def create(self,side,end,start,grad_max,grad_min,lim1,lim2,text,units):
        self.side=side                                                                              #size of the window
        self.end = end                                                                              #maximum value at scale
        self.start = start                                                                          #minimum value at scale
        self.grad_max = grad_max                                                                    #interval for big scale(red)
        self.grad_min = grad_min                                                                    #interval for small scale(black)
        self.lim1=lim1                                                                              #lower limit - green area
        self.lim2=lim2                                                                              #higher limit - yellow area                                                                          #Type of measurement
        self.text=text
        self.units= units

        self.origy = self.side / 2.0 + 90
        self.origx= self.side/2.0                                                                    #center of the circle and window
        self.R= 0.95*self.side/2                                                                    #radius of the big circle
        self.r= 0.9*self.side/2                                                                     #radius of the small circle
        self.num_r=0.8*self.side/2                                                                  #radius of the circle for the numbers

        self.can_meter = Canvas(master = self.master, height = self.side+180, width = self.side, bg='#4c4c4c')             #define veriable for construction of the forms
        self.can_meter.create_oval(self.origx - self.R , self.origy - self.R , self.origx + self.R , self.origy + self.R , fill='#ffffff' , width = 2) #create big circle
        self.Create_Color()                                                                         #function - create green and orange colors

        for n in range(self.start,self.end+1):                                                                                      #create scale Lines
            alpha_deg = 225-(n-self.start)*270/(self.end-self.start)                                                                #calculate the angle in degrees
            alpha = radians(alpha_deg)                                                                                              #transform angles in degrees to radians
            if n%self.grad_min == 0:                                                                                                #create thin lines
                y=self.R*sin(alpha)                                                                                                 #calculate vertical position
                x=self.R*cos(alpha)                                                                                                 #calculate horizontal position
                self.can_meter.create_line(self.origx,self.origy,self.origx+x,self.origy-y)                                             #create thin scale lines
            if n%self.grad_max == 0:                                                                                                #create thick scale lines
                y = self.R*sin(alpha)                                                                                               #calculate vertical position
                x = self.R*cos(alpha)                                                                                               #calculate horizontal position
                self.can_meter.create_line(self.origx,self.origy,self.origx + x, self.origy -y,width = 3, fill="black")                   #create thick scale lines

        self.can_meter.create_oval(self.origx - self.r,self.origy - self.r, self.origx + self.r,self.origy + self.r, fill = 'white' )  #inner circle

        self.lable1=self.can_meter.create_text(self.origx, self.origy+self.R*0.65,text = self.text,fill = "black")         #create text

        for n in range (self.start,self.end + 1):                                                   #create scale number
            alpha_deg = 225-(n-self.start)*270/(self.end-self.start)                                #calculate the angle in degrees
            alpha = radians(alpha_deg)                                                              #transform angles in degrees to radians
            if n%self.grad_max == 0:
                y = self.num_r * sin(alpha)                                                         #calculate vertical position
                x = self.num_r *cos(alpha)                                                          #calculate horizontal position
                self.can_meter.create_text(self.origx +x,self.origy - y , text=str(n),fill='black')     #create scale number

        self.entry=Entry(master=self.master, bd=3)                                                  #create textfield
        self.button=Button(master=self.master, text="Apply",command=self.Apply,bd=3) #create button
        self.button.grid(row =19, column =2,)                                                       #set button position
        self.entry.grid(row=19,column=1)                                                            #set textfield position
        self.entry.bind("<Return>",self.Enter)                                                      #bind enter key to event self.Enter
        self.entry.bind("<Up>",self.UpKey)                                                          #bind up key to event self.Up
        self.entry.bind("<Down>",self.DownKey)                                                      #bind down key to event self.Down
        self.can_meter.bind("<Button-1>",self.MouseClick)                                           #bind mouse click to event self.MouseClick

    def delete_entry(self):
        self.button.grid_forget()
        self.entry.grid_forget()
        self.can_meter.bind("<Button-1>", '')  # bind mouse click to event self.MouseClick
        self.can_meter.configure(background='#4c4c4c')

    def enable_entry(self):
        self.can_meter.bind("<Button-1>", self.MouseClick)                                          #bind mouse click to event self.MouseClick
        self.can_meter.configure(background='#4ed885')
        #self.can_meter.create_text(self.origx + x, self.origy - y, text=str(n), fill='red')

    def Read(self,value):                                                                           #value shown by the pointer
        self.value=value
        self.can_meter.delete("Needle")                                                             #delete previous pointer (needle)
        self.can_meter.delete("VALUE")                                                              #delete precious value shown (text)
        self.can_meter.create_text(self.origx,self.origy+self.R*0.8,text="{} {}".format(value,self.units),fill = "black",tag = "VALUE",font=("Purisa", 12))  #create text
        self.value = int(value)                                                                     #assignment of new value
        if (self.value > self.end):                                                                 #when the value is too high
            self.value = self.end                                                                   #value receives max value by the scale
            self.can_meter.delete("LABEL2")                                                         #delete previous text, if any
            self.can_meter.delete("LABEL1")                                                         #delete previous text, if any
            #self.can_meter.create_text(self.origx, self.origy*1.7,text = "ZU HOCH",fill = "red",tag="LABEL1")    #create new text "Too high"

        if (self.value < self.start):                                                               #when the value is too low
            self.value = self.start                                                                 #value receives minimum  value by the scale
            self.can_meter.delete("LABEL1")                                                         #delete previous text, if any
            self.can_meter.delete("LABEL2")                                                         #delete previous text, if any
            #self.can_meter.create_text(self.origx, self.origy*1.7,text = "ZU NIEDRIG",fill = "red",tag="LABEL2")     #create new text "Too low"
        if ((self.value > self.start)and(self.value < self.end) ):                                  #if value is not too high or too low
            self.can_meter.delete("LABEL1")                                                         #delete previous text, if any
            self.can_meter.delete("LABEL2")                                                         #delete previous text, if any


        alpha_deg = 225-(self.value-self.start) *270.0/(self.end-self.start)                        #calculate the angle in degrees
        alpha = radians(alpha_deg)                                                                  #transform angles in degrees to radians
        beta=radians(135)                                                                           #135 is the angle which the scale is turned counterclockwise
        ax = self.origx+0.025*self.side*cos(alpha-beta)                                              #calculation of the horizontal of a position for the needle construction
        ay = self.origy - 0.025*self.side*sin(alpha-beta)                                            #calculation of the vertical of a position for the needle construction
        bx = self.origx + 0.025*self.side*cos(alpha+beta)                                            #calculation of the horizontal of b position for the needle construction
        by = self.origy - 0.025*self.side*sin(alpha+beta)                                            #calculation of the vertical of b position for the needle construction
        cx =self.origx + self.r*cos(alpha)                                                           #calculation of the horizontal of c position for the needle construction
        cy = self.origy - self.r*sin(alpha)                                                          #calculation of the vertical of c position for the needle construction
        self.needle = self.can_meter.create_polygon(ax,ay,bx,by,cx,cy,tag="Needle")                 #create needle with the variables ax,ay,bx,by,cx,cy

        self.spindle = self.can_meter.create_oval(self.origx-0.01*self.side,self.origy-0.01*self.side,self.origx+0.01*self.side,self.origy+0.01*self.side,fill="#ffffff") #create intern small circle on top of the needle

    def Apply(self):                                                                                #function for the button "Apply" - Transfers the value in the text feld to the pointer
        self.Text=self.entry.get()                                                                  #reads the text and assign to the variable self.Text
        self.Text=int(self.Text)                                                                    #transforms the variable self.Text in an integer
        self.Read(self.Text)                                                                        #calls the function self.Read with the new value of the textfeld

    def Enter(self,Event):                                                                          #Event for the Key Enter "<Return>"
        self.Apply()                                                                                #function self.Apply is called

    def ChangeText(self,txt):
        return self.can_meter.itemconfigure(self.lable1,text=txt)

    def UpKey(self,Event):                                                                          #Event for the Up Key "<Up>"
        self.value=self.value + self.grad_min//2                                                    #the value increases equal to the smaller scale divided by 2
        self.Read(self.value)                                                                       #function self.Read is called
        
    def DownKey(self,Event):                                                                        #Event for the Down Key "<Down>"
        self.value=self.value - self.grad_min//2                                                    #the value decreases equal to the smaller scale divided by 2
        self.Read(self.value)                                                                       #function self.Read is called
        
    def MouseClick(self,Event):                                                                     #Event to change the value of the pointer with the click of the mouse
        x,y=(Event.x,Event.y)                                                                       #reads the position of the mouse in relation to the window
        ax=(x-self.origx)                                                                           #ax receives the value o the horizontal position of the mouse in relation to the center of the circle
        ay=-(y-self.origy)                                                                          #ay receives the value o the vertical position of the mouse in relation to the center of the circle
        if ((ax==0.0) and (ay>0.0)) :                                                               #if the mouse click center of the circle
            Alpha=radians(90)                                                                       #the angle alpha is 90 degrees
        if ((ax==0.0)and (ay<0.0)):                                                                 #if the mouse click is in the line unter the center of the circle
            Alpha=radians(270)                                                                      #the angle alpha is 270 degrees
        if((ax<0.0)and (ay>=0.0)):                                                                  #if the mouse click is in the second quadrant
            Alpha=atan(ay/ax)+radians(180)                                                          #the angle is calculated using the inverse tangent function + 180 degrees                                                              
        if((ax<0.0)and (ay<=0)):                                                                    #if the mouse click is the third quadrant
            Alpha=atan(ay/ax)+radians(180)                                                          #the angle is calculated using the inverse tangent function + 180 degrees
        if((ax>0.0)and(ay<=0.0)):                                                                   #if the mouse click is the fourth quadrant
            Alpha=atan(ay/ax)                                                                       #the angle is calculated using the inverse tangent function
        if((ax>0.0)and(ay>0.0)):                                                                    #if the mouse click is in the first quadrant
            Alpha=atan(ay/ax)                                                                       #the angle is calculated using the inverse tangent function
                    
        Alpha=degrees(Alpha)+270*self.grad_min/(self.start-self.end)/2                              #transform angles in radians to degrees
        
        self.value=int(self.start-((Alpha-225)*(self.end-self.start)/270))                          #the value of the pointer (self.value) is calculated for the angle of the mouse click (Alpha)
    
        if(self.value>self.end):                                                                    #when the value is too high
            self.value=self.end                                                                     #the receives shown is the max value of the scale
        if(self.value<self.start):                                                                  #when the value is too low
            self.value=self.start                                                                   #the receives shown is the minimum value of the scale
        #print(self.value)                                                                          #test
        self.value=(self.value//self.grad_min)*self.grad_min                                        #this ensures that the value shown is a value that can bee shown in the scale      
        self.Read(self.value)                                                                       #calls the function read with the new value
        
  
    def Create_Color(self):
        a1 = 225-(self.start-self.start)*270/(self.end-self.start) 
        b1 = -a1+(225-(self.lim1-self.start)*270/(self.end-self.start))
        #print(b1)
        a2 = 225-(self.end-self.start)*270/(self.end-self.start) 
        b2 = -a2+(225-(self.lim2-self.start)*270/(self.end-self.start))
        
        self.can_meter.create_arc(self.origx-self.R,self.origy+self.R,self.origx+self.R,self.origy-self.R,start=a1,extent=b1,fill="gray")
        self.can_meter.create_arc(self.origx-self.R,self.origy+self.R,self.origx+self.R,self.origy-self.R,start=a2,extent=b2,fill="gray")