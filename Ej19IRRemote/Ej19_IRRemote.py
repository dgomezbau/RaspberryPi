from lirc import RawConnection

def ProcessIRRemote():
       
    try:
        keypress = conn.readline(.0001) #lee la tecla pulsada
    except:
        keypress=""
              
    if (keypress != "" and keypress != None):
                
        data = keypress.split() #Separa los datos recibidos entre la cabecera y el numero del botón ( o identificación)
        sequence = data[1]
        command = data[2]
        
        #ignore command repeats
        if (sequence != "00"):
           return
        
        print(command)      
            

#define Global
conn = RawConnection()

print("Starting Up...")

while True:         

      ProcessIRRemote()