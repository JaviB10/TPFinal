#! /usr/bin/env python3

import sys
from datetime import date
from Metodosclientes import ListaClientes
from Metodostrabajos import ListaTrabajos
from repositorioClientes import RepositorioClientes
from trabajo import Trabajo

class Menu:
    "Muestra ocpiones"
    def __init__(self):
        self.ListaC = ListaClientes()
        self.ListaT = ListaTrabajos()
        self.RC = RepositorioClientes()
        self.opciones = {
                 "1": self.NuevoCliente,
                 "2": self.MostrarClientes,
                 "3": self.BuscarCliente,
                 "4": self.ModificarDatosC,
                 "5": self.BorrarCliente,
                 "6": self.CargarNuevoT,
                 "7": self.MostrarTrabajos,
                 "8": self.FinalizarTrabajo,
                 "9": self.RetirarTrabajo,
                "10": self.ModificarDatosT,
                "11": self.BorrarTrabajo,
                "12": self.HistorialTrabajosPorC,
                 "0": self.salir
        }

    def MostrarMenu(self):
        print("""
        Menu del sistema: 
        1. Ingrese un nuevo cliente
        2. Mostrar todos los clientes
        3. Buscar un cliente por su ID
        4. Modificar los datos de un cliente       
        5. Borrar un cliente
        6. Cargar nuevo trabajo
        7. Mostrar los trabajos
        8. Finalizar un trabajo
        9. Retirar un trabajo
        10. Modificar los datos de un trabajo
        11. Borrar un trabajo
        12. Mostrar el historial de trabajos de un cliente
        0. Salir
        """)

    def Ejecutar(self):
        "Mostrar y responder opciones"
        while True:
            self.MostrarMenu()
            opcion = input("Ingresar una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida")

    def NuevoCliente(self):
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C: Corporativo / P: Particular:")
        if tipo in ("C", "c"):
            NombreEmpresa = input("Ingrese el nombre de la empresa: ")
            NombreContacto = input("Ingrese el nombre del contacto: ")
            TelCont = input("Ingrese el telefono del contacto: ")
        else:
            Nombre = input("Ingrese el nombre: ")
            Apellido = input("Ingrese el apellido: ")
        Tel = input("Ingrese el telefono: ")
        Mail = input("Ingrese el mail: ")
        if tipo in ("C", "c"):
            C = self.ListaC.NuevoClienteCorp(NombreEmpresa, NombreContacto, TelCont, Tel, Mail)
        else:
            C = self.ListaC.NuevoClientePart(Nombre, Apellido, Tel, Mail)
        if C is None:
            print("Error en la carga del nuevo cliente")
        else:
            print("========================================")
            print(C)
            print("========================================")
            print("Carga exitosa")

    def MostrarClientes(self, Lista = None):
        if Lista == None:
            Lista = self.ListaC.ClienteL
        for Cliente in Lista:
            print(Cliente)
            print("========================================")

    def BuscarCliente(self):
        IDC = int(input("ingrese el ID del cliente a buscar: "))
        C = self.ListaC.BuscarPorID(IDC)
        if C == None:
            print("Cliente no encontrado")
        else:
            print(C)

    def ModificarDatosC(self):
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente que desea modificar: C: Corporativo / P: Particular:")
        if tipo in ("C","c"):
            print("Estos son los clientes corporativos: ")
            for I in self.RC.get_all_corporativos():
                print(I)
        else:
            print("Estos son los clientes particulares: ")
            c = self.RC.get_all_particulares()
            print(c)
        id_cliente = int(input("Ingrese el ID del cliente: "))
        Cliente = self.ListaC.BuscarPorID(id_cliente)
        print (Cliente)
        print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
        if tipo in ("C","c"):
            NombreEmpresa = input("Ingrese el nombre de la empresa: ")
            NombreContacto = input("Ingrese el nombre del contacto: ")
            TelCont = input("Ingrese el telefono del contacto: ")
        else:
            Nombre = input("Ingrese el nombre: ")
            Apellido = input("Ingrese el apellido: ")
        Tel = input("Ingrese el telefono: ")
        Mail = input("Ingrese el mail: ")
        if tipo in ("C","c"):
            C = self.ListaC.ModificarDatosCC(NombreEmpresa, NombreContacto, TelCont, Tel, Mail, id_cliente)
        else:
            C = self.ListaC.ModificarDatosCP(Nombre, Apellido, Tel, Mail, id_cliente)
        if C is None:
            print("Error al modificar los datos del cliente")
        else:
            print("========================================")
            print(Cliente)
            print("========================================")
            print("Modificacion exitosa")

    def BorrarCliente(self):
        id_cliente = int(input("ingrese el ID del cliente a borrar: "))
        C = self.ListaC.EliminarCliente(id_cliente)
        self.ListaC = ListaClientes()
        if C == None:
            print("Error al borrar el cliente")
        else:
            print("Cliente borrado con exito")

    def CargarNuevoT(self):
        id_cliente = int(input("Ingrese el ID del cliente: "))
        C = self.ListaC.BuscarPorID(id_cliente)
        if C == None:
            print("No se encontro al cliente")
        else:
            fecha_ingreso = date.today()
            print("La fecha de ingreso es: ", fecha_ingreso)
            print("A continuacion ingrese la fecha de entrega propuesta")
            dia = int(input("Ingrese el dia (1 a 31): "))
            mes = int(input("Ingrese el mes (1 a 12): "))
            anio = int(input("Ingrese el año: "))
            fecha_entrega_propuesta = date(anio, mes, dia)
            descripcion = input("Ingrese la descripcion del nuevo trabajo: ")
            T = self.ListaT.NuevoTrabajo(C, fecha_ingreso, fecha_entrega_propuesta, descripcion)
        if T == None:
            print("Ocurrio un error al cargar el nuevo trabajo")
        else:
            print("========================================")
            print("El nuevo trabajo se cargo con exito")
            print(T)
            print("========================================")

    def MostrarTrabajos(self, listat=None):
        if listat == None:
            listat = self.ListaT.TrabajoL
        for trabajo in listat:
            print(trabajo)
            print("========================================")

    def FinalizarTrabajo(self):
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        print (C)
        tipo = "n"
        while tipo not in ("F","f","c","C"):
            tipo = input("Desea dar por finalizado el trabajo: F: Finalizado / C: No finalizar")
        if tipo in ("F","f"):
            T = self.ListaT.TrabajoFinalizado(id_trabajo)
            if T == None:
                print("Error al modificar la entrega real del trabajo")
            else:
                print("La entrega real del trabajo fue modificada con exito")
                print(C)
        else:
            print("No se realizo ninguna modificacion en el trabajo")
            print(C)

    def RetirarTrabajo(self):
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        print(C)
        tipo = "n"
        while tipo not in ("R","r","c","C"):
            tipo = input("Desea dar por finalizado el trabajo: R: Retirar el trabajo / C: No retirar el trabajo")
        if tipo in ("R","r"):
            T = self.ListaT.Trabajo_retirado(id_trabajo)
            if T == None:
                print("Error al retirar el trabajo")
            else:
                print("El trabajo fue retirado con exito")
                print(C)
        else:
            print("No se realizo ninguna modificacion en el trabajo")
            print(C)

    def ModificarDatosT(self):
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        print (C)
        print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
        tipo = "n"
        while tipo not in ("I", "i", "P", "p", "D", "d", "C", "c"):
            while tipo not in ("C", "c"):
                tipo = input("Si desea hacer alguna modificacion ingrese: I: Fecha de ingreso / P: Fecha entrega propuesta / D: Descripcion / C: Volver al menu principal")
                if tipo in ("I","i"):
                    print("Modificar fecha de ingreso")
                    dia = int(input("Ingrese el dia (1 a 31): "))
                    mes = int(input("Ingrese el mes (1 a 12): "))
                    anio = int(input("Ingrese el año: "))
                    FechaIngreso = date(anio, mes, dia)
                    T = self.ListaT.ModificarDatosT(FechaIngreso, C.fecha_entrega_real, C.descripcion, id_trabajo)
                if tipo in ("P","p"):
                    print("Modificar fecha de entregra propuesta")
                    dia = int(input("Ingrese el dia (1 a 31): "))
                    mes = int(input("Ingrese el mes (1 a 12): "))
                    anio = int(input("Ingrese el año: "))
                    FechaEntregaPropuesta = date(anio, mes, dia)
                    T = self.ListaT.ModificarDatosT(C.fecha_ingreso, FechaEntregaPropuesta, C.descripcion, id_trabajo)
                if tipo in ("D","d"):
                    print("Modificar la descripcion del trabajo")
                    Descripcion = input("Ingrese la descripcion del trabajo: ")
                    T = self.ListaT.ModificarDatosT(C.fecha_ingreso, C.fecha_entrega_real, Descripcion, id_trabajo)
        if tipo in ("C","c"):
            self.Ejecutar()
        if T == None:
            print("Error al modificar el trabajo")
        else:
            print("El trabajo fue modificado con exito")
            print(C)

    def BorrarTrabajo(self):
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        print(C)
        tipo = "n"
        while tipo not in ("E","e","C","c"):
            tipo = input("Opciones: E: Eliminar trabajo / C: No eliminar trabajo")
        if tipo in ("E","e"):
            T = self.ListaT.EliminarTrabajo(id_trabajo)
            if T == None:
                print("Error al borrar el trabajo")
            else:
                print("El trabajo se elimino con exito")
        else:
            print("No se borro ningun trabajo")
            print(C)

    def HistorialTrabajosPorC(self):
        """Solicita un ID y muestra una lista con los trabajos encargados por el cliente"""
        id_cliente = int(input("Ingrese el ID del cliente: "))
        C = self.ListaC.BuscarPorID(id_cliente)
        print(C)
        for I in self.ListaT.TrabajoL:
            if I.cliente.id_cliente == id_cliente:
                print("=======================================================")
                print("ID trabajo: ",I.id_trabajo)
                print("Fecha de ingreso: ",I.fecha_ingreso)
                print("Fecha entrega propuesta: ",I.fecha_entrega_propuesta)
                print("Fecha entrega real: ",I.fecha_entrega_real)
                print("Descripcion: ",I.descripcion)
                print("Retirado: ",I.retirado)
                print("=======================================================")
            else:
                print("No se encontraron trabajos")

    def salir(self):
        print("Gracias por utilizar el sistema")
        sys.exit(0)

if __name__ == "__main__":
    m = Menu()
    m.Ejecutar()