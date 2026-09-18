print ( "  ************************************************************** " ) 
print ( " *== Programa para saber si los numeros son iguales ==* " )
print ( "  ************************************************************** " )
print ( " " )
a = int ( input ( " ingrese un numero entero: " ) )
b = int ( input ( " ingrese otro numero entero: " ) )
c = int ( input ( " ingrese otro numero entero: " ) )
if a == b and a == c :
    print ( " los tres numero son iguales " )
elif a == b or a == c or b == c :
    print ( " solo hay dos numeros iguales " )
else :
    print ( " ninguno es igual " )
