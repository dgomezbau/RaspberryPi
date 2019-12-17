from tkinter import *
import time

class CustomCanvas(Canvas):
    def __init__(self):
        super().__init__
        self.cretaeFigure()

    def cretaeFigure(self):
        self.create_oval(10, 40, 590, 790, outline="#f11",
            fill="#1f1", width=2)



def main():

    root = Tk()
    #ex = UserInterface()
    cc = CustomCanvas()
    root.geometry('600x400')
    #time.sleep(5)
    #ex.configure(background="black")

    #root.geometry("330x220+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()