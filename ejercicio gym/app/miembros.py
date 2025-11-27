import csv
import os

archivo = "csv/miembros.csv"

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
    documento = float(input("Documento del usuario: "))
    telefono = float(input("Telefono del usuario: "))
    correo = input("Correo electronico del usuario: ")
    plan = input("Plan escogido por el usuario (BÁSICO | PREMIUM | FULL)").strip().lower()

    archivo_existe = os.path.exists(archivo)

    with open("csv/miembros.csv", "a", encoding="utf-8")as f:
        writer = csv.writer(f)

        if not archivo_existe:
            writer.writerow(["id","nombre","documento","telefono","correo","plan"])

        writer.writerow([nuevo_id,nombre,documento,telefono,correo,plan])

    print(f"\nMiembro agregado con ID: {nuevo_id}\n")

def menu_miembro():

    while True:

        print("=> MENÚ DE MIEMBRO.")
        print("Opción 1 -Registrar miembro")
        print("Opcion 2 -Listar miembros(estado).")
        print("Opción 3 -Buscar miembro.")
        print("Opción 4 -Renovar plan con pago.")

        try:
            opcion = int(input("Qué opción deseas realizar: "))
        except:
            print("No se permiten caracteres especiales.")
            continue

        else: 
            print("Opcion no existe.")