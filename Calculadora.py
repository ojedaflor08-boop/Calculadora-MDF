n=int(input("""¿Que operación matemática desea hacer?
Elija 1 para suma
Elija 2 para resta 
Elija 3 para multiplicacion
Elija 4 para division """))


def suma ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    print ("La suma del primer número con el segundo numero va a dar",(a+b),"como resultado")
    
def resta ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    print ("La resta del primer número con el segundo numero va a dar ", (a-b),"como resultado")
          
def multiplicacion ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    print ("El resultado es: ", (a*b))

def division ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    if a==0 or b==0:
        print ("No se puede dividir por 0")
    print ("El resultado es: ", (a/b))       

if n==1:
    suma()
else:
    if n==2:
        resta()
    else:
        if n==3:
            multiplicacion()
        else:
            if n==4:
                division()
