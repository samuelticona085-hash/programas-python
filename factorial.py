print ( " ********************* " )
print ( " * == Factoriales == * " )
print ( " ********************* " )
print ( " " )
n = int ( input ( " ingrese un nuemro: " ) )
fac = 1
for i in range ( 1, n + 1 ):
    fac *= i    
    print ( fac )
print ( " el factorial de ", n, " es de: ", fac )
