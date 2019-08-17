from Creador import
print(archivo)

while True:
    try:
        a= int("1: Cuantas lineas quiere agregar a su archivo? (maximo 3)?"))
        
        if a == "1":
            linea1=0
            linea1=input("Ingrese datos para la primera linea")
            print("Los datos de la primera linea son: "+ linea1)
            print("Linea agregada con exito")
            f=open(archivo, "w+")
            f.write(linea1)
            f.close()
        
        
        elif a== "2":
            linea1=0
            linea2=0
            linea1=input("Ingrese datos para la primera linea")
            linea2=input("Ingrese datos para la segunda linea")
            print("Los datos de la primera linea son: "+ linea1)
            print("Los datos de la segunda linea son: "+ linea2)
            print("Lineas agregadas con exito")
            f=open(archivo, "w+")
            f.write(linea1)
            f.write(linea2)
            f.close()
              
        elif a == "3":
            linea1=0
            linea2=0
            linea3=0
            linea1=input("Ingrese datos para la primera linea")
            linea2=input("Ingrese datos para la segunda linea")
            linea3=input("Ingrese datos para la tercera linea")
            print("Los datos de la primera linea son: "+ linea1)
            print("Los datos de la segunda linea son: "+ linea1)
            print("Los datos de la tercera linea son: "+ linea1)
            print("Lineas agregadas con exito")
            f=open(archivo, "w+")
            f.write(linea1)
            f.write(linea2)
            f.write(linea3)
            f.close()
    
        else: