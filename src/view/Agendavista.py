
def mostrar_menu():

    print("      AGENDA     ") 
    print("1. Guardar contacto") 
    print("2. Buscar contacto")  
    print("3. Eliminar contacto") 
    print("4. Mostrar contactos") 
    print("5. Salir")


def pedir_datos():

    print("Nuevo Contacto: ")  

    id = input("ID: ")  
    nombre = input("Nombre: ") 
    apellido = input("Apellido: ")  
    fecha = input("Fecha nacimiento: ") 
    sexo = input("Sexo: ")  
    telefono = input("Telefono: ") 

    return id, nombre, apellido, fecha, sexo, telefono  # retorna todos los datos


def pedir_id():

    id = input("Ingrese ID: ")  
    return id 


def mostrar_contacto(r):

    if r:  #si existe registro
        print("ID:", r[0])  
        print("Nombre:", r[1])  
        print("Apellido:", r[2])  
        print("Fecha:", r[3])  
        print("Sexo:", r[4])  
        print("Telefono:", r[5])  
    else:
        print("Contacto no encontrado") 


def mostrar_lista(registros):

    for r in registros:  # recorre todos los registros
        print("")
        print("ID:", r[0])  
        print("Nombre:", r[1])  
        print("Apellido:", r[2])  
        print("Telefono:", r[5])  


