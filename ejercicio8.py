
base = int(input("Introduce la base : "))
altura = int(input("Introduce una altura : "))
precio = int(input("Introduce un precio : "))
    

def area():

    return base*altura

resultadoArea = area()
print("El area es : ", resultadoArea, "Metros cuadrados")

def CosteTotal():

    return resultadoArea*precio

resultadoPrecio = CosteTotal()
print("El coste total es de : ",resultadoPrecio, "euros")
