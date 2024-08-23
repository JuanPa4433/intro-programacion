Nombre = input("Ingrese su nombre")
Nacimiento = int(input("ingrese su año de nacimiento"))
edad = 2024-Nacimiento
print("Hola", Nombre, "Tienes", edad, "years")

if Nacimiento> 1994:
    print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación z")
elif Nacimiento< 1948:
    print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación niños de la posguerra")
elif Nacimiento< 1968 and Nacimiento> 1949:
    print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación baby boomer")
elif Nacimiento< 1980 and Nacimiento> 1969:
    print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación x")

elif Nacimiento< 1993 and Nacimiento>1981:
    print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación millenials")
elif Nacimiento> 2011:
   print("Hola", Nombre, "tienes", edad, "años, y perteneces a la generación Alfa")


    
