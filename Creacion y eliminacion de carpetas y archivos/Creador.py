# -*- coding: utf-8 -*-
import os
  
def __init__():
    print("*****Administrar archivos y carpetas*****")
    opcion = input("Seleccione una opcion c= crear e= eliminar:")
    if(opcion == "c"):
        ruta = input(chr(27)+"[1;33m"+"Indique la ruta, si no indica la ruta. Sera la actual")
        if(ruta == ""): ruta = os.getcwd() + "\\"
        #Comprobacion de la rusa (si la ruta existe o no)
        if(os.path.isdir(ruta)):
            tipo = input(chr(27)+"[1;33m"+"Indique el tipo a=archivo y c=carpeta:")
            if(tipo =="a"):
                arc= input(chr(27)+"[1;33m"+"Indique el nombre del archivo:")
                #Creacion de archivo
                seleccion1=input("\033[4;35m"+"Ingrese el ID del item:")
                seleccion2=input("\033[4;35m"+"Ingrese el titulo del item:")
                seleccion3=input("\033[4;35m"+"Ingrese la categoria del item")
                seleccion4=input("\033[4;35m"+"Ingrese el nombre de la categoria del item:")
                archivo = open(ruta+arc, "w+")
                contenido=archivo.read()
                archivo.write(seleccion1+ "      "+seleccion2+"      "+seleccion3+"      "+seleccion4)
                archivo.close()
                print("archivo", archivo, "creado con exito")
                print("Y su contenido", contenido, "Creado con exito")
                
            elif(tipo=="c"):
                carpeta= input("Indique el nombre de la carpeta: ")
                #Crear la carpeta
                os.mkdir(ruta+carpeta)
                print("Carpeta", carpeta, "creada con exito")
            else: __init__()   #Reiniciamos el programa
            
    elif(opcion == "e"):
        ruta= input("Indique la ruta, si no indica la ruta. Sera la actual")
        if (ruta == ""): ruta = os.getcwd() + "\\"
        eliminar = input("Indique el nombre de la carpeta a eliminar")
        if(os.path.isfile(ruta+eliminar)):
            os.remove(ruta+eliminar)
            print("Archivo",eliminar, "eliminado con exito")
        elif(os.path.isdir(ruta+eliminar)):
            os.rmdir(ruta+eliminar)
            print("Carpeta", eliminar, "eliminada con exito")
        else: __init__()
    else: __init__()
    
__init__()