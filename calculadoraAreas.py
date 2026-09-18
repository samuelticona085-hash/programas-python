import math
print ( " ********************************** " )
print ( " * == Calculadora de areas == * " )
print ( " ********************************** " )
print ( " " )
print ( " ¿eliga una opcion? " )
print ( " a) Area del Triangulo " )
print ( " b) Area del Circulo " )
x = input ( " _ " )
if x == "a" :
    a = float ( input ( " dame el al valor de la base: " ) )
    b = float ( input ( " dame le valor de la altura: " ) )
    area = ( a * b ) / 2
    print ( " el area de tu triangulo es: ", area )
elif x == "b" :
    a = float ( input ( " dame el valor del radio " ) )
    area = math.pow( a, 2 ) * math.pi
    print ( " el area de tiu circulos es: ", area )
else :
    print ( " opcion no valida " )
