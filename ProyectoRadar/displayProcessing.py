def numberDisplay(number):
    if(number == 0):
        return 0xc0 #192 in decimal
    if(number == 1):
        return 0xf9 #249 in decimal
    if(number == 2):
        return 0xa4 #164 in decimal
    if(number == 3):
        return 0xb0 #176 in decimal
    if(number == 4):
        return 0x99
    if(number == 5):
        return 0x92
    if(number == 6):
        return 0x82
    if(number == 7):
        return 0xf8
    if(number == 8):
        return 0x80
    if(number == 9):
        return 0x90

def separadorNumeros(dist):
    distInt = int(dist)
    num = str(distInt) #convierto in string
    list_num = [] #creo un array para armacenar los numeros
    listNumberInDisplay = []
    list_num.append(0)
    if(len(num) == 0):
        for i in range(4):
            list_num.append(0)            
    elif(len(num) == 1):
        list_num.append(0)
        list_num.append(0)
        for n in num:       
            n = int(n)
            list_num.append(n) #F(127) =[1,2,7]
        
    elif(len(num) == 2):
        list_num.append(0)
        for n in num:       
            n = int(n)
            list_num.append(n) #F(127) =[1,2,7]
    else:
        for n in num:       
            n = int(n)
            list_num.append(n) #F(127) =[1,2,7]

    for n in list_num:        
        eachNumberInHexa = numberDisplay(n)
        listNumberInDisplay.append(eachNumberInHexa)
    return listNumberInDisplay



    