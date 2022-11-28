import os #limpia la pantalla IMPORTANTE
import matplotlib.pyplot as plt
import numpy as np #importas numpy y lo asignas como np

def puntoequilibrio(a,b,c):
    #PUNTO EQUILIBRIO ES BENEFICIO = 0
    costesT=a+b
    #PARA SABER LOS INGRESOS EL PUNTO DE EQUILIBRIO QUE ES 0 = I - CT -> I = CT
    ingresos=costesT
    #CANTIDAD
    cantidad=ingresos/c
    #BENEFICIO
    beneficio=ingresos-cantidad
    if eleccion==1:
        print("Datos: ", costesT ," ", ingresos," ", round(cantidad,2))
    if eleccion==2:
        print("El beneficio es: ",round(beneficio,2))
    #OBJETIVO
    if eleccion==3:
        nBeneficio=(float(input("Introduce el nuevo beneficio")))
        nCantidad=ingresos-nBeneficio
        print("La cantidad que tienes que vender para obtener ",nBeneficio, "de beneficio es: ",nCantidad)
    #PRECIOTECNICO
    if eleccion==4:
        nIngresos=cantidad
        print("El precio tecnico es: ",round(nIngresos,2))
    if eleccion==5:
        x1 = np.array([0, cantidad])
        y1 = np.array([ingresos, ingresos])
        x2 = np.array([0, cantidad])
        y2 = np.array([ingresos, ingresos])
        plt.plot(x1, y1, x2, y2)
        plt.show()

fin=False
while fin==False:
    try:
        print(" \n ---- PUNTO DE EQUILIBRIO ----")
        print("0-Introducir datos")
        print("1-Calcular punto de equilibrio")
        print("2-Calcular el beneficio")
        print("3-Calcular el objetivo")
        print("4-Calcular el precio tecnico")
        print("5-Crear grafico")
        print("6-Salir")
        print("------------------------------ \n")
        eleccion=int(input("Elige una opcion del menu: "))

        if eleccion==0:
            os.system('cls')
            costeF=float(input("Introduce el coste fijo: "))
            costeV=float(input("Introduce el coste variable unitario: "))
            precioU=float(input("Introduce el precio de venta unitario: "))
        if eleccion==1:
            os.system('cls')
            puntoequilibrio(costeF,costeV,precioU)
        if eleccion==2:
            os.system('cls')
            puntoequilibrio(costeF,costeV,precioU)
        if eleccion==3:
           os.system('cls')
           puntoequilibrio(costeF,costeV,precioU)
        if eleccion==4:
            os.system('cls')
            puntoequilibrio(costeF,costeV,precioU)
        if eleccion==5:
            os.system('cls')
            puntoequilibrio(costeF,costeV,precioU)
        if eleccion==6:
            os.system('cls')
            print("Has salido")
            fin=True

    except ValueError:
        os.system('cls')
        print("ERROR, SOLO SE PUEDEN INTRODUCIR NUMEROS")

    except NameError:
        os.system('cls')
        print("ERROR, DEBES INTRODUCIR ANTES LOS DATOS (0)")
    