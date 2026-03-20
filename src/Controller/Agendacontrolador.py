from model import Agendamodelo 
from view import Agendavista  
from view import Tkintervista


def iniciarTerminal ():
    while True:  
        Agendavista.mostrar_menu()  
        opcion = input("Seleccione opcion: ")  
        if opcion == "1":  #guardar contacto
            datos = Agendavista.pedir_datos()  
            Agendamodelo.guardarRegistro(*datos)  #guarda los datos en el modelo

            print("Contacto guardado") 
        elif opcion == "2":  #buscar contacto

            id = Agendavista.pedir_id()  
            r = Agendamodelo.buscarRegistro(id)  #busca 
            Agendavista.mostrar_contacto(r)  #muestra resultado
        elif opcion == "3":  #eliminar contacto

            id = Agendavista.pedir_id()  
            eliminado = Agendamodelo.eliminarRegistros(id)  #elimina registro

            if eliminado: 
                print("Contacto eliminado")
            else:
                print("No se encontró el contacto")
        elif opcion == "4": #mostrar todos

            registros = Agendamodelo.leerRegistros()  #obtiene registros
            Agendavista.mostrar_lista(registros)  #muestra lista
        elif opcion == "5":  #salir

            print("Saliendo del programa")  
            break 
        else:
            print("Opcion invalida")  

#Para aplicar MVC con el apartado de Tkinter

def guardar(id, nombre, apellido, fecha, sexo, telefono):

    return Agendamodelo.guardarRegistro(
        id,
        nombre,
        apellido,
        fecha,
        sexo,
        telefono
    )


def buscar(id):

    return Agendamodelo.buscarRegistro(id)


def eliminar(id):

    return Agendamodelo.eliminarRegistros(id)


def mostrar():

    return Agendamodelo.leerRegistros()

#Inciar con Tkinter
def iniciar():
    Tkintervista.iniciarVista()
 
