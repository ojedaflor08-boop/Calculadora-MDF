n=int(input("""¿Que operación matemática desea hacer?
Elija 3 para multiplicacion
Elija 4 para division """))


def multiplicación ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    print ("El resultado es: ", (a*b))

def division ():
    a=int(input("Ingrese un número "))
    b=int(input("Ingrese otro número "))
    if a==0 or b==0:
        print ("No se puede dividir por 0")
    print ("El resultado es: ", (a/b))        


if n==3:
    multiplicación()
else:
    if n==4:
        division()
