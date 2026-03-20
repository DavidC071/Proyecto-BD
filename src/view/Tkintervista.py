import tkinter as tk
from tkinter import messagebox   # para mostrar mensajes en pantalla
from model import Agendamodelo  


# Funcion de la vista principal
def iniciarVista():

    # variables globales para usar en todas las funciones
    global entrada_nombre
    global entrada_apellido
    global entrada_fecha
    global entrada_sexo
    global entrada_telefono
    global entrada_id


    # Limpia los campos 
    def limpiar_campos():

        entrada_id.delete(0, tk.END)
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_fecha.delete(0, tk.END)
        entrada_sexo.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)


    # Guarda
    def guardar():

        id = entrada_id.get()
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        fecha = entrada_fecha.get()
        sexo = entrada_sexo.get()
        telefono = entrada_telefono.get()

        # validar campos vacios
        if id == "" or nombre == "":
            messagebox.showwarning("Error", "Faltan datos")
            return

        # llamar al modelo
        Agendamodelo.guardarRegistro(
            id,
            nombre,
            apellido,
            fecha,
            sexo,
            telefono
        )

        # mensaje
        messagebox.showinfo("OK", "Persona guardada con exito")

        # limpiar
        limpiar_campos()


    # Busca
    def buscar():

        id = entrada_id.get()

        # validar
        if id == "":
            messagebox.showwarning(
                "Error",
                "Ingrese el ID de la persona"
            )
            return

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

        else:
            messagebox.showerror(
                "Error",
                "ID no registrado"
            )


    # Funcion eliminar
    def eliminar():

        id = entrada_id.get()

        if id == "":
            messagebox.showwarning(
                "Error",
                "Ingrese ID"
            )
            return

        eliminado = Agendamodelo.eliminarRegistros(id)

        if eliminado:
            messagebox.showinfo(
                "OK",
                "Persona eliminada"
            )
            limpiar_campos()
        else:
            messagebox.showerror(
                "Error",
                "No existe ese ID"
            )


    # Funcion Mostrar 
    def mostrar():

        registros = Agendamodelo.leerRegistros()

        ventana2 = tk.Toplevel()
        ventana2.title("Contactos")

        texto = tk.Text(
            ventana2,
            width=50,
            height=20
        )

        texto.pack()

        for r in registros:

            linea = (
                "ID: " + r[0]
                + " Nombre: " + r[1]
                + " Apellido: " + r[2]
                + " Tel: " + r[5]
                + "\n"
            )

            texto.insert(
                tk.END,
                linea
            )


    # Crea la ventana 
    ventana = tk.Tk()

    ventana.title("AGENDA")
    ventana.geometry("250x250")

    titulo = tk.Label(
    ventana,
    text="AGENDA",
    font=("Arial", 16)
)

    titulo.grid(
    row=0,
    column=0,
    columnspan=2
)

    # Campos a llenar

    tk.Label(
        ventana,
        text="Nombre"
    ).grid(row=1, column=0)

    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.grid(row=1, column=1)


    tk.Label(
        ventana,
        text="Apellido"
    ).grid(row=2, column=0)

    entrada_apellido = tk.Entry(ventana)
    entrada_apellido.grid(row=2, column=1)


    tk.Label(
        ventana,
        text="Fecha"
    ).grid(row=3, column=0)

    entrada_fecha = tk.Entry(ventana)
    entrada_fecha.grid(row=3, column=1)


    tk.Label(
        ventana,
        text="Sexo"
    ).grid(row=4, column=0)

    entrada_sexo = tk.Entry(ventana)
    entrada_sexo.grid(row=4, column=1)


    tk.Label(
        ventana,
        text="Telefono"
    ).grid(row=5, column=0)

    entrada_telefono = tk.Entry(ventana)
    entrada_telefono.grid(row=5, column=1)


    tk.Label(
        ventana,
        text="ID"
    ).grid(row=6, column=0)

    entrada_id = tk.Entry(ventana)
    entrada_id.grid(row=6, column=1)


    # "Contenedor" de botones
    frame = tk.Frame(ventana)

    frame.grid(
        row=7,
        column=0,
        columnspan=2,
        pady=10
    )


    # Netamente botones 

    tk.Button(
        frame,
        text="Buscar",
        command=buscar
    ).grid(row=1, column=0)


    tk.Button(
        frame,
        text="Guardar",
        command=guardar
    ).grid(row=1, column=1)


    tk.Button(
        frame,
        text="Eliminar",
        command=eliminar
    ).grid(row=1, column=2)


    tk.Button(
        frame,
        text="Mostrar",
        command=mostrar
    ).grid(row=1, column=3)


    tk.Button(
        frame,
        text="Salir",
        command=ventana.destroy
    ).grid(row=1, column=4)


    # Iniciar la ventana
    ventana.mainloop()