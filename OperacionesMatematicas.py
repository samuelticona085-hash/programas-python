print ( " ********************************** " )
print ( " * == Operaciones Matematicas == * " )
print ( " ********************************** " )
print ( " " )
print ( " eliga una opcion " )
print ( " ● 1 → Sumar " )
print ( " ● 2 → Restar " )
print ( " ● 3 → Multiplicar " ) 
print ( " ● 4 → Divicion " ) 
print ( " ● 5 → Elevar numero " ) 
x = input ( " _ " )
if x == "1" :
    a = float ( input ( " ingrese un numero: " ) )
    b = float ( input ( " ingrese otro numero :" ) ) 
    suma = a + b
    print ( " la suma es: ", suma )
elif x == "2" :
    a = float ( input ( " ingrese un numero: " ) )
    b = float ( input ( " ingrese otro numero: " ) )
    res = a - b
    print ( " tu resta es de: ", res )
elif x == "3" :
    a = float ( input ( " ingrese un numero: " ) )
    b = float ( input ( " ingrese otro nuemero: " ) )
    mul = a * b
    print ( " la multiplicacion es: ", mul )
elif x == "4" :
    print ( " ● 1 → Divicion entera " )
    print ( " ● 2 → Divicion decimal " )
    x = input ( " _ " )
    if x == "1" :
        a = float ( input ( " ingrese un numero: " ) )
        b = float ( input ( " ingrese otro numero: " ) ) 
        if b == 0 :
            print ( " no existe divison entre 0 " )
        else :
            div = a / b
            print ( " tu division es de: ", div )
    elif x == "2" :
        a = float ( input ( " ingrese un numero: " ) )
        b = float ( input ( " ingrese otro numero: " ) ) 
        if b == 0 :
            print ( " no existe division entre cero " )
        else:
            div = a // b
            print ( " tu division es de: ", div )
    else :
        print ( " opcion no valida T-T " )
elif x == "5" :
    a = float ( input ( " ingrese un numero: " ) )
    b = float ( input ( " sobre cuantos lo quieres elevar: " ) )
    pot = a ** b
    print ( " la respuesta que esperabas es: ", pot )
else :
    print ( " no opcion no valoida T-T " )
