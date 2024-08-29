usuarios = []
montos = []

def menu():
    print("\nBienvenida al sistema de banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Salir")
    
def Registrar_usuario():
    nombre = input("Ingrese el nombre de usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado")
    else:
        usuarios.append(nombre)
        montos.append(0)  
        print("Usuario registrado con éxito")
        
def deposito():
    nombre = input("Ingrese el usuario: ")
    if nombre in usuarios:
        monto = float(input("Ingrese el monto deseado: "))
        indice = usuarios.index(nombre)
        montos[indice] += monto
        print(f"Depósito de {monto} realizado con éxito en la cuenta de {nombre}")
    else:
        print("Usuario no válido")
    
def retiro():
    nombre = input("Ingrese el usuario: ")
    if nombre in usuarios:
        monto = float(input("Ingrese el monto deseado: "))
        indice = usuarios.index(nombre)
        if monto <= montos[indice]:
            montos[indice] -= monto
            print(f"Retiro de {monto} realizado con éxito en la cuenta de {nombre}")
        else:
            print("Fondos insuficientes")
    else:
        print("Usuario no válido")
                
def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Registrar_usuario()
        elif opcion == "2":
            deposito()
        elif opcion == "3":
            retiro()
        elif opcion == "4":
            print("Gracias por usar nuestro sistema")
            break
        else:
            print("Opción no válida")

main()
