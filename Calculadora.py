n=int(input("""¿Que operación matematica desea hacer?
Elija 1 para suma
Elija 2 para resta
Elija 3 para multiplicacion
Elija 4 para division"""))
    

def suma ():
    a=float(input("Ingrese un numero "))
    b=float(input("Ingrese otro número "))
    print ("El resultado es: ", (a+b))

def resta ():
    a=float(input("Ingrese un numero "))
    b=float(input("Ingrese otro número "))
    print ("El resultado es: ", (a-b))

def multiplicación ():
    a=float(input("Ingrese un numero "))
    b=float(input("Ingrese otro número "))
    print ("El resultado es: ", (a*b))

def division ():
    print ("Esta operación sigue en proceso")
    

if n==1:
    suma()
if n==2:
    resta()
if n==3:
    multiplicación()
if n==4:
    division()
