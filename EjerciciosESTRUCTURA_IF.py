def ej1():
    num=int(input("Ingrese un numero "))
    if num>=0 and num%2==0:
        print("El numero es positivo y par")
    elif num>=0 and num%2!=0:
        print("El numero es positivo y es impar")
    elif num<=0 and num%2!=0:
        print("El numero es negativo e impar")
    else:
        print("El numero es negativo y par")
#ej1()

def ej2():
    sueldo=int(input("Ingresar sueldo "))
    if sueldo<600:
        sueldo=sueldo+(sueldo*0.1)
        print("El sueldo se encuentra dentro de rango, el nuevo sueldo es de  ",sueldo)
    else:
        print("EL sueldo esta fuera del rango, no recibe bono, el sueldo es de ", sueldo)
#ej2()
def ej3():
    ht=int(input("Ingresar horas trabajadas "))
    ph=int(input("Ingresar el pago por hora "))
    sueldo=0
    if ht<=40:
        sueldo=ht*ph
        print("El sueldo es de ",sueldo)
    elif ht<=48:
        hex=ht-40
        sueldo=((ht-hex)*ph)+hex*2*ph
        print("El sueldo es de ",sueldo )
    else:
        hex=ht-48
        sueldo=((ht-(hex+8))*ph)+(8*2*ph)+((hex)*3*ph)
        print("El sueldo es de ",sueldo)
#ej3()
def ej4():
    a=int(input("Ingresar año "))
    if a%4==0 and a%100!=0 or a%400==0:
        print("El año es bisiesto ")
    else:
        print("No es año bisiesto ")
#ej4()
def ej5():
    print("Elegir operacion ")
    print("1) Retirar ")
    print("2) Depositar ")
    saldo=2000
    op=int(input("Ingresar Opcion: "))
    cantidad=int(input("Ingresar el monto "))
    if op==1:
        print("AVISO: Solo puede retirar menos de 1000")
        if cantidad<1000 and cantidad<=saldo:
            saldo=saldo-cantidad
            print("Se retiro",cantidad," Su nuevo saldo es de ",saldo)
        else:
            print("se excedio la cantidad a retirar, su saldo actual es de ",saldo)
    elif op==2:
        print("AVISO: El deposito no debe exceder los 1500")
        if cantidad<1500:
            saldo=saldo+cantidad
            print("Se deposito ",cantidad, "Su nuevo saldo es de ",saldo)
        else:
            print("Error, la cantidad ",cantidad," excede el limite a depositar, su saldo actual es ",saldo)
    else:
        print("Ingreso una opcion equivocada")
#ej5()
def ej6():
    cs=0
    n=0
    print("Sintomas del covid: Escribir 1 para afirmar y 0 para negar")
    ss=int(input("¿Tiene fiebre? "))
    if ss==1:
        cs=cs+0.5
        n=n+1
    ss=int(input("¿Tiene dolor de cabeza? "))
    if ss==1:
        cs=cs+0.5
        n=n+1
    ss=int(input("¿Tiene dificultad para respirar? "))
    if ss==1:
        cs=cs+5
        n=n+1
    ss=int(input("¿Tiene dolor en el pecho? "))
    if ss==1:
        cs=cs+5
        n=n+1
    print("Calculando resultados....")    
    if cs>6:
        print("Tiene covid y muestra ",n ," sintomas graves, requiere hospitalizar y requiere UCI")
    elif cs>0 and cs<=1:
        print("Tiene ",n ," sintomas leves, podria ser un resfriado")
    elif cs==5.5:
        print("Requiere observacion, presenta almenos ",n ," sintomas, uno comun y otro grave")
    elif cs==6:
        print("Requiere hospitalizacion, presenta ",n ,"sintomas, 2 comunes y uno grave")
    else:
        print("No presenta los sintomas del covid.")
#ej6()
def ej7():
    print("OBTENCION DE LICENCIA DE CONDUCIR, INGRESAR LOS DATOS PEDIDOS")
    pt=0
    EV=int(input("¿Aprobo el examen de vision? Responder 1 para confirmar  o  0 para negar "))
    if EV==1:
        pt=pt+0.5
    print("Hola")
    Ert=int(input("Ingresar puntaje del examen de reglas de transito  "))
    if Ert>69 and Ert<=100:
        pt=pt+1
    EM=int(input("Ingresar puntaje del examen de manejo  "))
    if EM>=85:
        pt=pt+2
    print("Calculando resultados ")
    print("Puntaje obtenido ",pt)
    if pt==2.5:
        print("Tienes una segunda oportunidad de dar el examen fallido ")
    elif pt==0.5 or pt==1 or pt==2:
        print("Aprobaste solo un examen, puedes volver a dar el examen dentro de 6 meses ")
    elif pt==3:
        print("Obtienes una licencia temporal de 1 año")
    elif pt==1.5:
        print("No obtienes licencia ")
    elif pt==3.5:
        print("Aprobaste todo, obtienes una licencia de 10 años")
    else:
        print("Reprobaste todos los examenes, no obtienes licencia")
#ej7()
def ej8():
    ciclo=int(input("Ingresar el ciclo actual del estudiante "))
    cc=int(input("Ingresar cantidad de creditos que se llevaran "))
    cpc=0
    if ciclo>=2 and ciclo<=5:
        cpc=36
    elif ciclo>=6 and ciclo<=10:
        cpc=35
    elif ciclo==1:
        cpc=40
    else:
        print("Se ingreso un numero incorrecto ")
    print("Se calculara el costo de la matricula...")
    if cc<=12:
        cm=12*cpc
    elif cc>12 and cc<=18:
        cm=18*cpc
    else:
        cm=cc*cpc
    print("El estudiante se encuentra en ",ciclo," ciclo, llevara ",cc," creditos y pagara la cantidad de ",cm," soles ")
#ej8()