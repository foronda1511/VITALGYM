import csv

def verificar():
    usuarios = set()
    contraseñas = {}  
    roles = {}  
    
    with open("csv/usuarios.csv", "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        for fila in lector:
            usuario = fila["usuario"].strip().lower()
            contraseña = fila["contraseña"]  
            rol = fila["rol"].strip().lower()
            usuarios.add(usuario)
            contraseñas[usuario] = contraseña
            roles[usuario] = rol

    return usuarios, contraseñas, roles

def inicio_usuario(usuarios):

    while True:
        usuario = input("Ingresa nombre de usuario: ").strip().lower()
        if usuario in usuarios:
            return usuario
        else:
            print("Usuario no existe. Intenta de nuevo.")

def inicio_contraseña(usuario, contraseñas):

    while True:
        contraseña = input("Ingresa la contraseña: ")
        if contraseña == contraseñas[usuario]:
            return True
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")

def inicio_sistema():

    usuarios, contraseñas, roles = verificar()
    
    print("Bienvenido a VitalGYM.")
    
    usuario = inicio_usuario(usuarios)
    
    if inicio_contraseña(usuario, contraseñas):
        print(f"Bienvenido/a {roles[usuario].capitalize()}--{usuario.capitalize()}\n")
        return True
    else:
        return False