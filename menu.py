#! /usr/bin/env python3

import sys
from datetime import date
from Metodosclientes import ListaClientes
from Metodostrabajos import ListaTrabajos
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo

class Menu:
    "Muestra ocpiones"
    def __init__(self):
        self.RC = RepositorioClientes()
        self.RT = RepositorioTrabajos()
        self.ListaC = ListaClientes()
        self.ListaT = ListaTrabajos()
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
                "11": self.HistorialTrabajosPorC,
                "12": self.BorrarTrabajo,
                 "0": self.salir
        }



    def MostrarMenu(self):
        print("""
        MENU DEL SISTEMA:
         
        CLIENTES:
        1. Ingresar un nuevo cliente
        2. Mostrar todos los clientes
        3. Buscar un cliente
        4. Modificar los datos de un cliente
        5. Borrar un cliente
        
        TRABAJOS:
        6. Cargar nuevo trabajo
        7. Mostrar todos los trabajos
        8. Finalizar un trabajo
        9. Retirar un trabajo
        10. Modificar los datos de un trabajo
        11. Historial de trabajos de un cliente
        12. Borrar un trabajo
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
        "Ingresa un nuevo cliente, ya sea corporativo o particular"
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
            print("========================================")
            print("Error en la carga del nuevo cliente")
            print("========================================")
        else:
            print("========================================")
            print("El clientes se cargo con exito")
            print("========================================")
            print(C)
            print("========================================")


    def MostrarClientes(self, Lista = None):
        "Muestra todos los clientes"
        if Lista == None:
            Lista = self.ListaC.ClienteL
        for Cliente in Lista:
            print("========================================")
            print(Cliente)
            print("========================================")

    def BuscarCliente(self):
        "Solicita un ID y muestre el cliente"
        print("========================================")
        IDC = int(input("ingrese el ID del cliente a buscar: "))
        print("========================================")
        C = self.ListaC.BuscarPorID(IDC)
        if C == None:
            print("========================================")
            print("Ocurrio un error al buscar al cliente")
            print("========================================")
        else:
            print("========================================")
            print(C)
            print("========================================")

    def ModificarDatosC(self):
        "Modificar los datos de un cliente, ya sea cliente corporativo o particular"
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            print("======================================================================================")
            tipo = input("Ingrese el tipo de cliente que desea modificar: C: Corporativo / P: Particular:")
            print("======================================================================================")
        if tipo in ("C","c"):
            print("========================================")
            print("CLIENTES CORPORATIVOS")
            print("========================================")
            for I in self.RC.get_all_corporativos():
                print("========================================")
                print(I)
                print("========================================")
        else:
            print("========================================")
            print("CLIENTES PARTICULARES")
            print("========================================")
            for I in self.RC.get_all_particulares():
                print("========================================")
                print(I)
                print("========================================")
        print("========================================")
        id_cliente = int(input("Ingrese el ID del cliente: "))
        print("========================================")
        Cliente = self.ListaC.BuscarPorID(id_cliente)
        if Cliente:
            print("========================================")
            print(Cliente)
            print("========================================")
            print("======================================================================================")
            print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
            print("======================================================================================")
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
                print("========================================")
                print("Ocurrio un error al modificar los datos del cliente")
                print("========================================")
            else:
                print("========================================")
                print("Los datos del cliente se modificaron con exito")
                print("========================================")
                print(Cliente)
                print("========================================")

    def BorrarCliente(self):
        "Solicita un ID y borra al cliente, en caso de que tenga trabajos pendientes, tambien los borra"
        for i in self.RC.get_all_particulares():
            print("========================================")
            print("ID cliente: ",i.id_cliente,"- Nombre: ",i.nombre)
            print("========================================")
        for i in self.RC.get_all_corporativos():
            print("========================================")
            print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre_empresa)
            print("========================================")
        id_cliente = int(input("ingrese el ID del cliente a borrar: "))
        D = self.ListaC.BuscarPorID(id_cliente)
        if D:
            print("========================================")
            print(D)
            print("========================================")
            U = "J"
            while U not in ("S","s","N","n"):
                print("======================================================================================")
                U = input("¿Estas seguro que desea eliminar al cliente? S: Si / N: No")
                print("======================================================================================")
            if U in ("S","s"):
                B = self.ListaC.EliminarCliente(id_cliente)
                if B == None:
                    print("========================================")
                    print("Ocurrio un error al querer borrar al cliente")
                    print("========================================")
                else:
                    print("========================================")
                    print("El cliente fue borrado con exito")
                    print("========================================")
            else:
                self.Ejecutar()

    def CargarNuevoT(self):
        "Solicita el ID de un cliente y carga los datos de un nuevo trabajo"
        for i in self.RC.get_all_particulares():
            print("========================================")
            print("ID cliente: ",i.id_cliente,"- Nombre: ",i.nombre)
            print("========================================")
        for i in self.RC.get_all_corporativos():
            print("========================================")
            print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre_empresa)
            print("========================================")
        id_cliente = int(input("Ingrese el ID del cliente: "))
        C = self.ListaC.BuscarPorID(id_cliente)
        if C == None:
            print()
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
                print("========================================")
                print("Ocurrio un error al cargar el nuevo trabajo")
                print("========================================")
            else:
                print("========================================")
                print("El nuevo trabajo se cargo con exito")
                print(T)
                print("========================================")

    def MostrarTrabajos(self, listat=None):
        "Muestra una lista con todos los trabajos"
        if listat == None:
            listat = self.ListaT.TrabajoL
        for trabajo in listat:
            print("========================================")
            print(trabajo)
            print("========================================")

    def FinalizarTrabajo(self):
        "Solicita un ID trabajo y modifica la fecha de entrega real"
        for i in self.RT.get_all():
            print("========================================")
            print(i.cliente)
            print("ID trabajo: ",i.id_trabajo,"- Fecha entrega real: ",i.fecha_entrega_real)
            print("========================================")
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        if C == None:
            print()
        else:
            print("========================================")
            print (C)
            print("========================================")
            tipo = "n"
            while tipo not in ("F","f","c","C"):
                print("============================================================================")
                tipo = input("Desea dar por finalizado el trabajo: F: Finalizado / C: No finalizar")
                print("============================================================================")
            if tipo in ("F","f"):
                T = self.ListaT.TrabajoFinalizado(id_trabajo)
                if T == None:
                    print("==============================================")
                    print("Error al modificar la entrega real del trabajo")
                    print("==============================================")
                else:
                    print("====================================================")
                    print("La entrega real del trabajo fue modificada con exito")
                    print("====================================================")
                    print(C)
                    print("====================================================")
            else:
                print("================================================")
                print("No se realizo ninguna modificacion en el trabajo")
                print("================================================")
                print(C)
                print("================================================")

    def RetirarTrabajo(self):
        "Solicita un ID trabajo y lo marca como retirado"
        for i in self.RT.get_all():
            print("========================================")
            print(i.cliente)
            print("ID trabajo: ",i.id_trabajo,"- Retirado: ",i.retirado)
            print("=========================================")
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        if C == None:
            print()
        else:
            print("========================================")
            print(C)
            print("========================================")
            tipo = "n"
            while tipo not in ("R","r","c","C"):
                print("============================================================================================")
                tipo = input("Desea dar por finalizado el trabajo: R: Retirar el trabajo / C: No retirar el trabajo")
                print("============================================================================================")
            if tipo in ("R","r"):
                T = self.ListaT.Trabajo_retirado(id_trabajo)
                if T == None:
                    print("========================================")
                    print("Error al retirar el trabajo")
                    print("========================================")
                else:
                    print("========================================")
                    print("El trabajo fue retirado con exito")
                    print("========================================")
                    print(C)
                    print("========================================")
            else:
                print("================================================")
                print("No se realizo ninguna modificacion en el trabajo")
                print("================================================")
                print(C)
                print("================================================")

    def ModificarDatosT(self):
        "Solicita un ID trabajo y modifica los datos del trabajo"
        for i in self.RT.get_all():
            print("========================================")
            print("ID trabajo: ",i.id_trabajo)
            print("Fecha de ingreso: ",i.fecha_ingreso)
            print("Fecha entrega propuesta: ",i.fecha_entrega_propuesta)
            print("Descripcion: ",i.descripcion)
            print("=========================================")
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        if C == None:
            print()
        else:
            print("=========================================")
            print (C)
            print("=========================================")
            print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
            print("=========================================")
            tipo = "n"
            while tipo not in ("I", "i", "P", "p", "D", "d", "C", "c"):
                while tipo not in ("C", "c"):
                    print("==================================================================================================================================================")
                    tipo = input("Si desea hacer alguna modificacion ingrese: I: Fecha de ingreso / P: Fecha entrega propuesta / D: Descripcion / C: Volver al menu principal")
                    print("==================================================================================================================================================")
                    if tipo in ("I","i"):
                        print("=========================================")
                        print("Modificar fecha de ingreso")
                        dia = int(input("Ingrese el dia (1 a 31): "))
                        mes = int(input("Ingrese el mes (1 a 12): "))
                        anio = int(input("Ingrese el año: "))
                        FechaIngreso = date(anio, mes, dia)
                        T = self.ListaT.ModificarDatosT(FechaIngreso, C.fecha_entrega_real, C.descripcion, id_trabajo)
                    if tipo in ("P","p"):
                        print("=========================================")
                        print("Modificar fecha de entregra propuesta")
                        dia = int(input("Ingrese el dia (1 a 31): "))
                        mes = int(input("Ingrese el mes (1 a 12): "))
                        anio = int(input("Ingrese el año: "))
                        FechaEntregaPropuesta = date(anio, mes, dia)
                        T = self.ListaT.ModificarDatosT(C.fecha_ingreso, FechaEntregaPropuesta, C.descripcion, id_trabajo)
                    if tipo in ("D","d"):
                        print("=========================================")
                        print("Modificar la descripcion del trabajo")
                        Descripcion = input("Ingrese la descripcion del trabajo: ")
                        T = self.ListaT.ModificarDatosT(C.fecha_ingreso, C.fecha_entrega_real, Descripcion, id_trabajo)
            if tipo in ("C","c"):
                self.Ejecutar()
            if T == None:
                print("=========================================")
                print("Error al modificar el trabajo")
                print("=========================================")
            else:
                print("=========================================")
                print("El trabajo fue modificado con exito")
                print("=========================================")
                print(C)
                print("=========================================")

    def BorrarTrabajo(self):
        "Solicita un ID trabajo y borra un trabajo"
        for i in self.RT.get_all():
            print("========================================")
            print("ID trabajo: ",i.id_trabajo)
            print("Fecha de ingreso: ",i.fecha_ingreso)
            print("Fecha entrega propuesta: ",i.fecha_entrega_propuesta)
            print("Fecha de entrega real: ",i.fecha_entrega_real)
            print("Descripcion: ",i.descripcion)
            print("Retirado: ",i.retirado)
            print("=========================================")
        id_trabajo = int(input("Ingrese el ID del trabajo: "))
        C = self.ListaT.BuscarPorID(id_trabajo)
        if C == None:
            print()
        else:
            print("=========================================")
            print(C)
            print("=========================================")
            tipo = "n"
            while tipo not in ("E","e","C","c"):
                print("=========================================")
                tipo = input("Opciones: E: Eliminar trabajo / C: No eliminar trabajo")
            if tipo in ("E","e"):
                T = self.ListaT.EliminarTrabajo(id_trabajo)
                if T == None:
                    print("=========================================")
                    print("Error al borrar el trabajo")
                    print("=========================================")
                else:
                    print("=========================================")
                    print("El trabajo se elimino con exito")
                    print("=========================================")
            else:
                print("=========================================")
                print("No se borro ningun trabajo")
                print("=========================================")

    def HistorialTrabajosPorC(self):
        """Solicita un ID y muestra una lista con los trabajos encargados por el cliente"""
        for i in self.RC.get_all_particulares():
            print("========================================")
            print("ID cliente: ",i.id_cliente,"- Nombre: ",i.nombre)
            print("========================================")
        for i in self.RC.get_all_corporativos():
            print("========================================")
            print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre_empresa)
            print("========================================")
        id = int(input("Ingrese el ID del cliente: "))
        C = self.ListaC.BuscarPorID(id)
        if C == None:
            print()
        else:
            print("========================================")
            print(C)
            print("========================================")
            for I in self.ListaT.TrabajoL:
                if I.cliente.id_cliente == id:
                    print("=======================================================")
                    print("ID trabajo: ",I.id_trabajo)
                    print("Fecha de ingreso: ",I.fecha_ingreso)
                    print("Fecha entrega propuesta: ",I.fecha_entrega_propuesta)
                    print("Fecha entrega real: ",I.fecha_entrega_real)
                    print("Descripcion: ",I.descripcion)
                    print("Retirado: ",I.retirado)
                    print("=======================================================")
                else:
                    print("========================================")
                    print("No se encontraron trabajos")
                    print("========================================")


    def salir(self):
        print("Gracias por utilizar el sistema")
        sys.exit(0)

if __name__ == "__main__":
    m = Menu()
    m.Ejecutar()