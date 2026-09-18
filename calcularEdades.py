print ( " *************************************************************** " )
print ( " * == BIENVENIDO A NUESTRA SALA DE JUEGOS == * " )
print ( " *************************************************************** " )
print ( " " )
edad = int ( input ( " ¿cunatos años tienes? " ) )
if edad < 4 :
    print ( " vaya puedes jugar gratis baby " )
elif edad >= 4 and edad <= 18 :
    print ( " antes de ingresar deberas de pagar un monto de 5 $ " )
else :
    print ( " deberas de pagar 10 $ " )
