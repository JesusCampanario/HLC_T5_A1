

def entada_numeros():
    num1 = int(input("Introduce un número :"))
    num2 = int(input("Introduce un número :"))
    return num1 + num2

def mostrar_resultado():
    resultado = entada_numeros()
    print("La suma de los dos numeros es : ", resultado)

mostrar_resultado()