n=int(input("""¿Que operación matematica desea hacer?
Elija 1 para suma
Elija 2 para resta """))

def suma ():
    a=int(input("Ingrese un numero "))
    b=int(input("Ingrese otro número "))
    print ("La suma del primer numero con el segundo numero va a dar",(a+b),"como resultado")
    
def resta ():
    a=int(input("Ingrese un numero "))
    b=int(input("Ingrese otro número "))
    print ("La resta del primer nnumero con el segundo numero va a dar ", (a-b),"como resultado" )


if n==1:
    suma()
else:
    if n==2:
        resta()
