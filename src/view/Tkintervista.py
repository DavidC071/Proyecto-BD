import tkinter as tk
from model import Agendamodelo


def iniciarVista():

    global entrada_nombre
    global entrada_apellido
    global entrada_fecha
    global entrada_sexo
    global entrada_telefono
    global entrada_id


    def guardar():

        id = entrada_id.get()
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        fecha = entrada_fecha.get()
        sexo = entrada_sexo.get()
        telefono = entrada_telefono.get()

        Agendamodelo.guardarRegistro(id, nombre, apellido, fecha, sexo, telefono)


    def buscar():

        id = entrada_id.get()

        r = Agendamodelo.buscarRegistro(id)

        if r:

            entrada_nombre.delete(0, tk.END)
            entrada_nombre.insert(0, r[1])

            entrada_apellido.delete(0, tk.END)
            entrada_apellido.insert(0, r[2])

            entrada_fecha.delete(0, tk.END)
            entrada_fecha.insert(0, r[3])

            entrada_sexo.delete(0, tk.END)
            entrada_sexo.insert(0, r[4])

            entrada_telefono.delete(0, tk.END)
            entrada_telefono.insert(0, r[5])


    def eliminar():

        id = entrada_id.get()
        Agendamodelo.eliminarRegistros(id)


    ventana = tk.Tk()
    ventana.title("AGENDA")
    ventana.geometry("400x400")


    tk.Label(ventana, text="Nombre").grid(row=0, column=0)
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Apellido").grid(row=1, column=0)
    entrada_apellido = tk.Entry(ventana)
    entrada_apellido.grid(row=1, column=1)

    tk.Label(ventana, text="Fecha").grid(row=2, column=0)
    entrada_fecha = tk.Entry(ventana)
    entrada_fecha.grid(row=2, column=1)

    tk.Label(ventana, text="Sexo").grid(row=3, column=0)
    entrada_sexo = tk.Entry(ventana)
    entrada_sexo.grid(row=3, column=1)

    tk.Label(ventana, text="Telefono").grid(row=4, column=0)
    entrada_telefono = tk.Entry(ventana)
    entrada_telefono.grid(row=4, column=1)

    tk.Label(ventana, text="ID").grid(row=5, column=0)
    entrada_id = tk.Entry(ventana)
    entrada_id.grid(row=5, column=1)


    frame = tk.Frame(ventana)
    frame.grid(row=6, column=0, columnspan=2)


    tk.Button(frame, text="Buscar", command=buscar).grid(row=0, column=0)
    tk.Button(frame, text="Guardar", command=guardar).grid(row=0, column=1)
    tk.Button(frame, text="Eliminar", command=eliminar).grid(row=0, column=2)
    tk.Button(frame, text="Salir", command=ventana.destroy).grid(row=0, column=3)


    ventana.mainloop()