from tkinter import *

class Button_Class():
    def __init__ (self, master, height,width):
        self.master = master                                                                    #create window
        self.master.title=("Button")                                                            #name of the window
        self.create(height,width)
        self.sentido = 1

    def create(self,height,width):
        self.height = height    # height of the window
        self.width = width      # height of the window
        self.can_meter = Canvas(master=self.master, height=self.height, width=self.width,
                                bg='#4c4c4c')  # define veriable for construction of the forms
        self.can_meter.grid(row=0, column=0, columnspan=5, rowspan=20)


        self.button1 = Button(master=self.master, text="Velocidade", command=self.Velocidadef, bd=3, height = 1, width = 6)
        self.button1.grid(row=19, column=2, )

        self.button2 = Button(master=self.master, text="Sensor", command=self.Sensorf, bd=3, height = 1, width = 3)
        self.button2.grid(row=19, column=3, )

        self.button3 = Button(master=self.master, text="PMW", command=self.PWMf, bd=3, height = 1, width = 2)
        self.button3.grid(row=19, column=1, )

        self.button4 = Button(master=self.master, text="Off", command=self.Offf, bd=3 ,height = 1, width = 4,bg="#770e0e")
        self.button4.grid(row=4, column=2, )

        self.button5 = Button(master=self.master, text="Horario", command=self.horariof, bd=3 ,height = 1, width = 4)
        self.button5.grid(row=4, column=1, )

        self.button6 = Button(master=self.master, text="Anti-Horario", command=self.ahorariof, bd=3 ,height = 1, width = 4)
        self.button6.grid(row=4, column=3, )

        self.text = self.can_meter.create_text(self.width/2,55, text="Desligado", fill="black",
                                   tag="VALUE", font=("Purisa", 12))
        self.orig_color = self.button1.cget("background")

    def horariof(self):
        self.sentido = 1


    def ahorariof(self):
        self.sentido = 0


    def PWMf(self):
        self.can_meter.itemconfigure(self.text, text='PWM')
        self.button3.configure(bg="#4ed885")
        self.button2.configure(bg=self.orig_color)
        self.button1.configure(bg=self.orig_color)
        self.button4.configure(bg=self.orig_color)


    def Velocidadef(self):
        self.can_meter.itemconfigure(self.text,text='Velocidade')
        self.button1.configure(bg="#4ed885")
        self.button2.configure(bg=self.orig_color)
        self.button3.configure(bg=self.orig_color)
        self.button4.configure(bg=self.orig_color)

    def Sensorf(self):
        self.can_meter.itemconfigure(self.text, text='Sensor')
        self.button2.configure(bg="#4ed885")
        self.button1.configure(bg=self.orig_color)
        self.button3.configure(bg=self.orig_color)
        self.button4.configure(bg=self.orig_color)

    def Offf(self):
        self.can_meter.itemconfigure(self.text, text='Desligado')
        self.button2.configure(bg=self.orig_color)
        self.button1.configure(bg=self.orig_color)
        self.button3.configure(bg=self.orig_color)
        self.button4.configure(bg="#770e0e")
        self.button5.configure(bg=self.orig_color)
        self.button6.configure(bg=self.orig_color)

    def GetText(self):
        return self.can_meter.itemcget(self.text,'text')


"""
def do_main():  # main program
    root = Tk()  # defines root as the main window (parameter for master)
    frame_1 = Frame()

    RElement_1 = Button_Class(master=frame_1,height=400,width=400)  # parameters ()
    frame_1.grid(row=1, column=0)

    root.resizable(width=TRUE, height=TRUE)  # window size is not resizable
    root.mainloop()  # creates a loop for the main window


if (__name__ == "__main__"):
    do_main()

"""