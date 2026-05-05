# Actulizamos la version de nuestro sistema de inversiones.

# Agregamos un menú, para hacerlo interactivo.

lista_inversiones = []
lista_ganancias = []
lista_totales = []

total_invertido = 0
total_ganancias = 0
inversiones_realizadas = 0
# Creamos el menú.

while True:
    print("\n*** Sistema de Inversiones.***")
    print("1.-Inversión.")
    print("2.-Mostrar Tabla.")
    print("3.-Salir.")

    opcion = input("Elige una opcíon (1-3): ")
    
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        continue

    if opcion == "1":
        try:
            inversion = float(input("Ingrresa una inversión: "))
            if inversion < 0:
                print("Error: No se permiten números negativos.")
                continue

            ganancia = inversion * 0.1
            total_final = inversion + ganancia

            lista_inversiones.append(inversion)
            lista_ganancias.append(ganancia)
            lista_totales.append(total_final)

            total_invertido = total_invertido + inversion
            inversiones_realizadas += 1

        except:
            print("Error: Número inválido.")
    
    elif opcion == "2":
        if inversiones_realizadas == 0:
            print("No hay datos.")
        else:
            print("\nResumen:")
            print (f"{'Inversión':>12} | {'Ganancia':>12} | {'Total':>12}")
            print("-" * 50)

            for i in range(len(lista_inversiones)):
                inv = lista_inversiones[i]
                gan = lista_ganancias[i]
                tot = lista_totales[i]
                
                print(f"${inv:>10,.2f}   | ${gan:>10,.2f}   | ${tot:>10,.2f}   |")

            total_general = total_invertido + total_ganancias
            print("-" * 50)
            print(f"\nTotal final: ${total_general:,.2f}")
            print("-" * 50)
    
    elif opcion == "3":
        print("Gracias por usar el sistema.")
        break