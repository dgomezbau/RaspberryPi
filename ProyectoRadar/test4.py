import tkinter as tk
import threading
import time

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_line(0, 0, 100,50, fill="white")
        self.canvas1.create_rectangle(150,10, 250,110, fill="white")
        self.canvas1.create_oval(300,10,400,150, fill="red")
        self.canvas1.create_arc(420,10,550,110, fill="yellow", start=180, extent=90)
        self.canvas1.create_rectangle(150,210, 250,310, outline="white")
        self.canvas1.create_oval(300,210,400,350, outline="red")
        self.canvas1.create_arc(420,210,550,310, outline="yellow", start=180, extent=90)        
        self.ventana1.mainloop()

    def remove(self):
        self.canvas1.delete(all)
        self.ventana1.update_idletasks()
       



def main():
    app=Aplicacion()
    t = threading.Thread(app)
    t2 = threading.Thread(app.remove())

    t.start()

    #t2 = threading.Thread
    print("PASA")
    time.sleep(5)
    app.remove()

if __name__ == '__main__':
    main()