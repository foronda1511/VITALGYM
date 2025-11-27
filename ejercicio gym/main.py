from app import asistencias,entrenamientos,miembros,pagos,reportes,usuario

def menu():

    while True:

        print("\n===> MENÚ <===")
        print("Opción 1 -Miembros.")
        print("Opción 2 -Entrenamientos.")
        print("Opción 3 -Asistencias.")
        print("Opción 4 -Pagos de membresías.")
        print("Opción 5 -Reportes mensuales.")
        print("Opción 6 -SALIR.")

        try:
            opcion = int(input("ingresa la opcion deseada: "))
        except:
            print("No se permiten caracteres especiales.")
            continue

        if opcion == 1:
            miembros.agregar_miembro()

        elif opcion == 2:
            entrenamientos.print("f")
        elif opcion == 3:
            asistencias.print("f")
        elif opcion == 4:
            pagos.print("f")
        elif opcion == 5:
            reportes.print("f")
        elif opcion == 6:
            break
        else: 
            print("Opcion no existe.")

login_exitoso = usuario.inicio_sistema()

if login_exitoso:
    menu()