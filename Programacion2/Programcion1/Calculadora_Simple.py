def calculadora():
    while True:
        print("\nCalculadora Simple")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Elija una operación (1-5): ")
        
        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")

calculadora()