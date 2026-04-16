'''CalcuTodo es un miniprograma que puede calcular las operaciones básicas (suma - resta - multiplicación - división
porcentaje)'''

def main():
    calculadora = str(input("Qué Desea Escoger: Sumar -  Restar - Multiplicar - Dividir - Porcentaje - Potencia: "))
    a = int(input("Escriba el valor de a: "))
    b = int(input("Escriba el valor de b: "))
    resultado = calculadora
    print(f"Hemos calculado el/la {resultado}")

#Al usar una de las palabras clave el código ejecuta su respectiva operación matemática


    if calculadora == "Sumar":
        print(a + b)   
    elif calculadora == "Restar":
        print(a - b)
    elif calculadora == "Multiplicar":
        print(a * b)
    elif calculadora == "Dividir":
        print(a / b)
    elif calculadora == "Potencia":
        print(a ** b)
    elif calculadora == "Porcentaje":
        print(b / a * 100, str("%"))
    if calculadora == "Comprobación":   
        a / b  % 2 == 0
        print("Es un número par")
           
main()
