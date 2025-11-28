from datetime import datetime, timedelta
import csv
import os

archivo = "csv/miembros.csv"

def obtener_fecha_inicio():
    return datetime.today().strftime("%Y-%m-%d")

def obtener_fecha_fin(plan):
    hoy = datetime.today()

    if plan == "básico":
        dias = 30
    elif plan == "premium":
        dias = 60
    elif plan == "full":
        dias = 90
    else:
        dias = 30  # por si acaso

    fecha_fin = hoy + timedelta(days=dias)
    return fecha_fin.strftime("%Y-%m-%d")

def obtener_estado(fecha_fin_plan):
    hoy = datetime.today().strftime("%Y-%m-%d")
    return "ACTIVO" if fecha_fin_plan >= hoy else "INACTIVO"

def asignar_id():
    if not os.path.exists(archivo):
        return 0

    with open(archivo, "r", encoding="utf-8")as f:
        lector = csv.DictReader(f)
        ultimo_id = 0

        for fila in lector:
            ultimo_id = int(fila["id"])

        return ultimo_id

def agregar_miembro():

    print("\nagregar miembro.")

    ultimo_id = asignar_id()
    nuevo_id = ultimo_id + 1

    nombre = input("Nombre del usuario: ")

    while True:
        try:
            documento = float(input("Documento del usuario: "))
            if documento < 0:
                print("ERROR: Número de documento negativo.")
                continue
            break
        except:
            print("Tú documento no puede ser letras.")
            continue
    while True:
        try:
            telefono = float(input("Telefono del usuario: "))
            if telefono < 0:
                print("ERROR: Número de telefono negativo.")
                continue
            break
        except:
            print("Tú numero de telefono no puede ser letras.")
            continue
        
    correo = input("Correo electronico del usuario: ")

    plan = input("Plan escogido por el usuario (BÁSICO | PREMIUM | FULL)").strip().lower()

    fecha_inicio = obtener_fecha_inicio()
    fecha_fin_plan = obtener_fecha_fin(plan)
    estado = obtener_estado(fecha_fin_plan)

    archivo_existe = os.path.exists(archivo)

    with open(archivo, "a", encoding="utf-8")as f:
        writer = csv.writer(f)

        if not archivo_existe:
            writer.writerow(["id","nombre","documento","telefono","correo","plan","fecha_inicio","fecha_fin_plan","estado"])

        writer.writerow([nuevo_id,nombre,documento,telefono,correo,plan,fecha_inicio,fecha_fin_plan,estado])

    print(f"\nMiembro agregado con ID: {nuevo_id}\n")

def listar_miembro():

    with open("csv/miembros.csv", "r", encoding="utf-8")as f:
        lector = csv.DictReader(f)
        for fila in lector:
            print(f"\nmiembro con id:{fila["id"]}")
            print(f"nombre: {fila["nombre"]}")
            print(f"documento: {fila["documento"]}")
            print(f"telefono: {fila["telefono"]}")
            print(f"correo: {fila["correo"]}")
            print(f"plan: {fila["plan"]}")
            print(f"fecha de inicio: {fila["fecha_inicio"]}")
            print(f"fecha final del plan: {fila["fecha_fin_plan"]}")
            print(f"estado del miembro: {fila["estado"]}")
            print("---------------------\n")

def buscar_miembro():
    while True:

        buscar = input("\nNombre del usuario o escribe salir: ").strip().lower()
        if buscar == "salir":
            print("saliendo al menú.")
            return

        with open(archivo, newline="",encoding="utf-8")as f:
            lector = csv.DictReader(f)
            encontrado = False

            for fila in lector:
                if buscar ==  fila["nombre"].lower():
                    print("Registro encontrado.\n")
                    for clave, valor in fila.items():
                        print(f"{clave}: {valor}")
                    print()
                    encontrado = True

            if not encontrado:
                print("No se encontro el miembro con ese nombre.")

def renovar_plan():
    print("\n--Renovar plan con pago. --")

    while True:
        print("Escribe (salir) para cancelar y volver al menú.")
        buscar = input("Usuario a renovar plan: ").strip().lower()
        if buscar == "salir":
            print("Renovacion cancelada.")
            return
        with open(archivo,"r", newline="", encoding="utf-8")as f:
            lector = csv.DictReader(f)
            miembro_encontrado = False

            for fila in lector:
                if buscar == fila["nombre"].lower() or buscar == fila["id"]:
                    miembro_encontrado = True
                    print(f"\nMiembro encontrado: {fila['nombre']}")
                    print(f"Plan actual: {fila['plan']}")
                    print(f"Fecha de finalización actual: {fila['fecha_fin_plan']}")
                    print(f"Estado actual: {fila['estado']}")

                    dias_restantes = (datetime.strptime(fila['fecha_fin_plan'], "%Y-%m-%d") - datetime.today()).days
                    
                    if dias_restantes > 0:
                        print(f"\nQuedan {dias_restantes} días para que se venza el plan actual.")
                    
                    opcion_renovar = input("\n¿Deseas renovar el plan? (si/no): ").strip().lower()
                    
                    if opcion_renovar == "si":
                        plan_nuevo = input("\nNuevo plan (BÁSICO | PREMIUM | FULL): ").strip().lower()
                        if plan_nuevo not in ["básico", "premium", "full"]:
                            print("Plan no válido. Debes elegir entre BÁSICO, PREMIUM o FULL.\n")
                            continue
                        
                        nueva_fecha_fin = obtener_fecha_fin(plan_nuevo)
                        estado = "ACTIVO"  

                        miembros = []

                        with open(archivo, "r", encoding="utf-8") as f_read:
                            lector = csv.DictReader(f_read)
                            for fila in lector:
                                if fila["id"] == fila["id"]:
                                    fila["plan"] = plan_nuevo
                                    fila["fecha_fin_plan"] = nueva_fecha_fin
                                    fila["estado"] = estado
                                miembros.append(fila)

                        with open(archivo, "w", encoding="utf-8", newline="") as f_write:
                            writer = csv.DictWriter(f_write, fieldnames=miembros[0].keys())
                            writer.writeheader()
                            writer.writerows(miembros)

                        print(f"\nPlan renovado exitosamente para {fila['nombre']}. Nuevo plan: {plan_nuevo}, fecha de finalización: {nueva_fecha_fin}.")
                    else:
                        print("No se ha renovado el plan.")
                    break

            if not miembro_encontrado:
                print("No se encontró un miembro con ese nombre o ID.")

def menu_miembro():

    while True:

        print("\n---- MENÚ DE MIEMBRO.----")
        print("Opción 1 -Registrar miembro")
        print("Opcion 2 -Listar miembros(estado).")
        print("Opción 3 -Buscar miembro.")
        print("Opción 4 -Renovar plan con pago.")
        print("Opción 5 -Regresar al menú.")

        try:
            opcion = int(input("Qué opción deseas realizar: "))
        except:
            print("No se permiten caracteres especiales.")
            continue

        if opcion == 1:
            agregar_miembro()
        elif opcion == 2:
            listar_miembro()
        elif opcion == 3:
            buscar_miembro()
        elif opcion == 4:
            renovar_plan()
        elif opcion == 5:
            return
        else:
            print("Opcion no existe.")