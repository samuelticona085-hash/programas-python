print ( " ********************************************** " )
print ( " *== Programa para convertir medidas ==* " )
print ( " ********************************************** " )
print ( " " )
print ( " ¿que deseas convertir ? " )
print ( " a) m a cm o cm a m" )
print ( " b) mm a mi o mi a mm " )
text = input ( " _ " )
if text == "a" :
    print ( " 1) m a cm " )
    print ( " 2) cm a m " )
    text = input ( " _ " )
    if text == "1":
        num = float ( input ( " ingrese el valor para convertir: " ) )
        conver = num * 100
        print ( " la conversion es: ", conver, " cm " )
    elif text == "2" :
        num = float ( input ( " ingrese el valor para convertir: " ) )
        conver = num / 100
        print ( " la conversion es: ", conver, " m " )
    else :
        print ( " opcion no valida T-T  " )
elif text == "b" :
    print ( " 1) mm a mi " )
    print ( " 2) mi a mm " )
    text = input ( " _ " ) 
    if text == "1" :
        num = float ( input ( " ingrese el valor para convertir: " ) )
        conver = num / 1609344
        print ( " la conversion es: ", conver, " mi " )
    elif text == "2" :
        num = float ( input ( " ingrese el valor para convertir: " ) )
        conver = num * 1609344
        print ( " la conversion es: " , conver, " mm " )
else :
    print ( " opcion invalida T-T " )
