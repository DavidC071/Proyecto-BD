archivoDatos = "src/Persistencia/agenda.agp"  #ruta del archivo donde se guardan los registros

def guardarRegistro(id, nombre, apellido, fecha, sexo, telefono):
    
    registro = f"{id};{nombre};{apellido};{fecha};{sexo};{telefono}\n"  #crea una linea con los datos separados por ;

    with open(archivoDatos, "a") as archivo:  #abre el archivo en modo agregar
        archivo.write(registro)  #escribe el registro en el archivo


def leerRegistros():

    registros = []  

    try:
        with open(archivoDatos, "r") as archivo:  #abre el archivo en modo lectura

            for linea in archivo:  #recorre cada linea del archivo
                datos = linea.strip().split(";")  #elimina salto de linea y separa los datos por ;
                registros.append(datos)  #guarda el registro en la lista

    except FileNotFoundError:  
        pass  

    return registros  


def buscarRegistro(id_buscar):

    registros = leerRegistros()  #obtiene todos los registros

    for r in registros:  #recorre cada registro
        if r[0] == id_buscar:  #compara el ID
            return r  # retorna el registro encontrado

    return None  #si no encuentra nada


def eliminarRegistros(id_eliminar):

    registros = leerRegistros()  #obtiene todos los registros
    nuevos = []  #lista para guardar registros que no se eliminarán

    eliminado = False  #bandera para saber si se eliminó algo

    for r in registros:  #recorre registros
        if r[0] != id_eliminar:  #si el ID no coincide
            nuevos.append(r)  #lo guarda
        else:
            eliminado = True  #indica que el registro fue eliminado

    with open(archivoDatos, "w") as archivo:  #abre el archivo en modo sobrescritura
        for r in nuevos:  #recorre los registros restantes
            linea = ";".join(r) + "\n"  #vuelve a crear la linea
            archivo.write(linea)  #escribe el registro

    return eliminado 