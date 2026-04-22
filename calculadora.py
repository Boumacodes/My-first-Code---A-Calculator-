'''CalcuTodo es un miniprograma que puede calcular las operaciones básicas (suma - resta - multiplicación - división
porcentaje)'''

def main():
    calcu = str(input("Qué Desea Escoger: Sumar -  Restar - Multiplicar - Dividir - Porcentaje - Potencia: "))
    a = int(input("Escriba el valor de a: "))
    b = int(input("Escriba el valor de b: "))
    resultado = calcu
    print(f"El resultado de la {resultado} es: ")

#Al usar una de las palabras clave el código ejecuta su respectiva operación matemática

    if calcu == "Sumar":
        print(a + b)   
    elif calcu == "Restar":
        print(a - b)
    elif calcu == "Multiplicar":
        print(a * b)
    elif calcu == "Dividir":
        print(a / b)
    elif calcu == "Potencia":
        print(a ** b)
    elif calcu == "Porcentaje":
        print(b / a * 100, str("%"))
    if calcu == "Comprobación":   
        a / b  % 2 == 0
        print("Es un número par")
           
main()
