from model import Agendamodelo 
from view import Agendavista  


def iniciar ():
    while True:  #ciclo infinito del programa
        Agendavista.mostrar_menu()  #muestra menu
        opcion = input("Seleccione opcion: ")  #pide opcion
        if opcion == "1":  #guardar contacto
            datos = Agendavista.pedir_datos()  #pide datos a la vista
            Agendamodelo.guardarRegistro(*datos)  #guarda los datos en el modelo

            print("Contacto guardado") 
        elif opcion == "2":  #buscar contacto

            id = Agendavista.pedir_id()  #pide ID
            r = Agendamodelo.buscarRegistro(id)  #busca registro
            Agendavista.mostrarContacto(r)  #muestra resultado
        elif opcion == "3":  #eliminar contacto

            id = Agendavista.pedir_id()  #pide ID
            eliminado = Agendamodelo.eliminarRegistros(id)  #elimina registro

            if eliminado:  #si se eliminó
                print("Contacto eliminado")
            else:
                print("No se encontró el contacto")
        elif opcion == "4": #mostrar todos

            registros = Agendamodelo.leerRegistros()  #obtiene registros
            Agendavista.mostrar_lista(registros)  #muestra lista
        elif opcion == "5":  #salir

            print("Saliendo del programa")  #mensaje
            break  #termina programa
        else:
            print("Opcion invalida")  #error