import csv
import os 
from datetime import datetime

archivo = "csv/asistencias.csv"

def buscar_miembro(miembro_id):
    archivo_miembros = "csv/miembros.csv"

    if not os.path.exists(archivo_miembros):
        print("El archivo miembros.csv no existe.")
        return None

    with open(archivo_miembros, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila["id"] == miembro_id:
                return fila
    
    return None

def inicializar_archivo():
    if not os.path.exists(archivo):
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["asistencia_id", "miembro_id", "nombre", "fecha", "hora", "tipo"])
            f.write("\n")
        print("Archivo asistencias.csv creado.")

def asignar_asistencia_id():
    if not os.path.exists(archivo):
        return 1020
    
    with open(archivo, "r", encoding="utf-8")as f:
        lector = csv.DictReader(f)
        ultimo_id = 1020

        for fila in lector:
            ultimo_id = int(fila["asistencia_id"])

        return ultimo_id

def buscar_miembro_por_id_o_nombre(valor):
    archivo_miembros = "csv/miembros.csv"

    if not os.path.exists(archivo_miembros):
        print("El archivo miembros.csv no existe.")
        return None

    valor = valor.lower().strip()

    with open(archivo_miembros, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila["id"].lower() == valor or fila["nombre"].lower() == valor:
                return fila

    return None

def registrar_asistencia():

    inicializar_archivo()

    ultimo_id = asignar_asistencia_id()
    nuevo_id = ultimo_id + 1

    print("\n--- Registrar Asistencia ---")
    entrada = input("Ingrese ID o nombre del miembro: ").strip()

    miembro = buscar_miembro_por_id_o_nombre(entrada)

    if miembro is None:
        print(" No existe un miembro con ese nombre o ID.")
        return

    # Datos reales desde miembros.csv
    miembro_id = miembro["id"]
    nombre = miembro["nombre"]

    tipo = ""
    while tipo not in ["ENTRADA", "SALIDA"]:
        tipo = input("¿Tipo (ENTRADA/SALIDA)?: ").upper().strip()

    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nuevo_id, miembro_id, nombre, fecha, hora, tipo])

    print(f"✔ Asistencia registrada correctamente para {nombre} (ID {miembro_id}).\n")

def historial_por_miembro():
    inicializar_archivo()

    buscar = input("Ingrese ID o nombre del miembro: ").strip().lower()

    print("\n--- Historial de Asistencias ---")

    encontrado = False
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if (buscar == fila["miembro_id"].lower()) or (buscar == fila["nombre"].lower()):
                encontrado = True
                print(
                    f"ID {fila['asistencia_id']} | "
                    f"{fila['nombre']} | "
                    f"{fila['fecha']} {fila['hora']} | "
                    f"{fila['tipo']}"
                )
    
    if not encontrado:
        print("No se encontraron registros para ese miembro.\n")

def menu_asistencias():
    while True:
        print("""\n---Menú asistencias.---
1) -registrar asistencia.
2) -historial por miembro.
3) -Regresar al menú""")
        try:
            opcion = int(input("Que opción deseas realizar: "))
            if opcion < 0:
                print("ERROR: Número negativo.")
        except:
            print("ERROR: No ingresastes un número.")

        if opcion == 1:
            registrar_asistencia()
        if opcion == 2:
            historial_por_miembro()
        if opcion == 3:
            return