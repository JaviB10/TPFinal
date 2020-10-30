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
        print("""                                              ===============
                                               S I S T E M A 
                                              ===============
        MENU CLIENTES:                                                     MENU TRABAJOS:
        
        1. Ingresar un nuevo cliente                                       6. Cargar nuevo trabajo
        
        2. Mostrar todos los clientes                                      7. Mostrar todos los trabajos
        
        3. Buscar un cliente                                               8. Finalizar un trabajo
        
        4. Modificar los datos de un cliente                               9. Retirar un trabajo
        
        5. Borrar un cliente                                               10. Modificar los datos de un trabajo
        
                                                                           11. Historial de trabajos de un cliente
                                                                           
                                                                           12. Borrar un trabajo
                                                                           
        
        0. Salir del sistema
        """)

    def Ejecutar(self):
        "Mostrar y responder opciones"
        while True:
            self.MostrarMenu()
            opcion = input("INGRESA UNA OPCION: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida")

    def NuevoCliente(self):
        "Ingresa un nuevo cliente, ya sea corporativo o particular"
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("""
    Escogio la opcion para ingresar un nuevo cliente, por favor elija el tipo de cliente e ingreselo
    
    C: Corporativo
    P: Particular
    
    Ingrese el tipo de cliente: """)
        if tipo in ("C", "c"):
            print("\nA continuacion se pediran los datos correspondientes al nuevo cliente\n")
            NombreEmpresa = input("Ingrese el nombre de la empresa: ")
            NombreContacto = input("Ingrese el nombre del contacto: ")
            TelCont = input("Ingrese el telefono del contacto: ")
        else:
            print("\nA continuacion se pediran los datos correspondientes al nuevo cliente\n")
            Nombre = input("Ingrese el nombre: ")
            Apellido = input("Ingrese el apellido: ")
        Tel = input("Ingrese el telefono: ")
        Mail = input("Ingrese el mail: ")
        if tipo in ("C", "c"):
            C = self.ListaC.NuevoClienteCorp(NombreEmpresa, NombreContacto, TelCont, Tel, Mail)
        else:
            C = self.ListaC.NuevoClientePart(Nombre, Apellido, Tel, Mail)
        if C is None:
            print("===========================================")
            print("Ocurrio un error al cargar al nuevo cliente")
            print("===========================================")
        else:
            print("\n===========================================")
            print("El clientes fue cargado con exito")
            print("===========================================\n")
            print(C)
            print("===========================================")
        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def MostrarClientes(self):
        "Muestra todos los clientes"
        l = self.RC.get_all_corporativos()
        print("""         =====================""")
        print("""         CLIENTES CORPORATIVOS""")
        print("""         =====================""")
        if l:
            for i in l:
                print("========================================")
                print(i)
                print("========================================")
        t = self.RC.get_all_particulares()
        print("""         =====================""")
        print("""         CLIENTES PARTICULARES""")
        print("""         =====================""")
        if t:
            for i in t:
                print("========================================")
                print(i)
                print("========================================")
        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        if l and t == None:
            print("\nActualmente no se encuentra ningun cliente cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def BuscarCliente(self):
        "Solicita un ID, busca al cliente con ese ID y lo muestra"
        print("\nEscogio la opcion para buscar un cliente\n")
        while True:
            try:
                id_cliente = int(input("Ingrese el ID del cliente que desea buscar: "))
            except ValueError:
                print('Debe ingresar un numero')
                continue
            break
        C = self.ListaC.BuscarPorID(id_cliente)
        if C == None:
            print("\n=================================================================")
            print("El ID ingresado no pertenece a ningun cliente cargado actualmente")
            print("=================================================================\n")
        else:
            print("\n===============================================\n")
            print(C)
            print("=================================================")
        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def ModificarDatosC(self):
        "Modificar los datos de un cliente, ya sea cliente corporativo o particular"
        tipo = "N"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("""
    Escogio la opcion para modificar un cliente, por favor elija el tipo de cliente e ingreselo
    
    C: Corporativo
    P: Particular
    
    Ingrese el tipo de cliente que desea modificar: """)
        if tipo in ("C","c"):
            l = self.RC.get_all_corporativos()
            if l:
                print("\n""         =====================""")
                print("""         CLIENTES CORPORATIVOS""")
                print("""         =====================""")
                for I in l:
                    print("========================================\n")
                    print(I)
                    print("========================================\n")
                while True:
                    try:
                        id_cliente = int(input("Ingrese el ID del cliente: "))
                    except ValueError:
                        print('Debe ingresar un numero')
                        continue
                    break
                Cliente = self.ListaC.BuscarPorID(id_cliente)
                if Cliente:
                    print("========================================\n")
                    print(Cliente)
                    print("=================================================================================")
                    print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
                    print("=================================================================================\n")
                    NombreEmpresa = input("Ingrese el nombre de la empresa: ")
                    NombreContacto = input("Ingrese el nombre del contacto: ")
                    TelCont = input("Ingrese el telefono del contacto: ")
                    Tel = input("Ingrese el telefono: ")
                    Mail = input("Ingrese el mail: ")
                    C = self.ListaC.ModificarDatosCC(NombreEmpresa, NombreContacto, TelCont, Tel, Mail, id_cliente)
                    if C == None:
                        print("\n========================================\n")
                        print("Ocurrio un error al modificar los datos del cliente")
                        print("========================================\n")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                    else:
                        print("\n===============================================================\n")
                        print("""Los datos del cliente se modificaron con exito
A continuacion se podran ver los datos del cliente actualizados""")
                        print("\n===============================================================\n")
                        print("\n========================================")
                        print(Cliente)
                        print("========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\nEl ID ingresado no pertenece a ningun cliente corporativo guardado en el sistema")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\nActualmente no se encuentra ningun cliente corporativo guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            l = self.RC.get_all_particulares()
            if l:
                print("\n""         =====================""")
                print("""         CLIENTES PARTICULARES""")
                print("""         =====================""")
                for I in l:
                    print("========================================\n")
                    print(I)
                    print("========================================\n")
                while True:
                    try:
                        id_cliente = int(input("Ingrese el ID del cliente: "))
                    except ValueError:
                        print('Debe ingresar un numero')
                        continue
                    break
                Cliente = self.ListaC.BuscarPorID(id_cliente)
                if Cliente:
                    print("\n========================================\n")
                    print(Cliente)
                    print("========================================\n")
                    print("==============================================================================")
                    print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
                    print("==============================================================================\n")
                    Nombre = input("Ingrese el nombre: ")
                    Apellido = input("Ingrese el apellido: ")
                    Tel = input("Ingrese el telefono: ")
                    Mail = input("Ingrese el mail: ")
                    C = self.ListaC.ModificarDatosCP(Nombre, Apellido, Tel, Mail, id_cliente)
                    if C == None:
                        print("\n================================================\n")
                        print("Ocurrio un error al modificar los datos del cliente")
                        print("==================================================\n")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                    else:
                        print("\n===============================================================\n")
                        print("""Los datos del cliente fueron modificaros con exito
A continuacion se podran ver los datos del cliente actualizados""")
                        print("\n===============================================================\n")
                        print("========================================\n")
                        print(Cliente)
                        print("========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\nEl ID ingresado no pertenece a ningun cliente particular guardado en el sistema")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\nActualmente no se encuentra ningun cliente particular guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def BorrarCliente(self):
        "Solicita un ID y borra al cliente, en caso de que tenga trabajos pendientes, tambien los borra"
        l = self.RC.get_all_corporativos()
        if l:
            print("""         =====================""")
            print("""         CLIENTES CORPORATIVOS""")
            print("""         =====================""")
            for i in l:
                print("========================================")
                print("ID cliente: ",i.id_cliente,"- Nombre: ",i.nombre_empresa)
                print("========================================")
        t = self.RC.get_all_particulares()
        if t:
            print("""         =====================""")
            print("""         CLIENTES PARTICULARES""")
            print("""         =====================""")
            for i in t:
                print("========================================")
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre)
                print("========================================\n")
        if l or t:
            while True:
                try:
                    id_cliente = int(input("Ingrese el ID del cliente a borrar: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            D = self.ListaC.BuscarPorID(id_cliente)
            if D:
                print("\n========================================\n")
                print(D)
                print("========================================\n")
                U = "J"
                while U not in ("S","s","N","n"):
                    U = input("""¿Estas seguro que desea eliminar al cliente? 
    
    S: Si borrar al cliente
    N: No borrar al cliente
    
Ingrese una opcion: """)
                if U in ("S","s"):
                    B = self.ListaC.EliminarCliente(id_cliente)
                    if B == None:
                        print("========================================")
                        print("Ocurrio un error al querer borrar al cliente")
                        print("========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                    else:
                        print("\n========================================")
                        print("El cliente fue borrado con exito")
                        print("========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

                else:
                    print("\nHa decidido no borrar al cliente")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\nEl ID ingresado no pertenece a ningun cliente guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun cliente guardado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def CargarNuevoT(self):
        "Solicita el ID de un cliente y carga los datos de un nuevo trabajo"
        l = self.RC.get_all_corporativos()
        if l:
            print("""         =====================""")
            print("""         CLIENTES CORPORATIVOS""")
            print("""         =====================""")
            for i in l:
                print("========================================")
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre_empresa)
                print("========================================")
        t = self.RC.get_all_particulares()
        if t:
            print("""         =====================""")
            print("""         CLIENTES PARTICULARES""")
            print("""         =====================""")
            for i in t:
                print("========================================")
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre)
                print("========================================\n")
        if l or t:
            while True:
                try:
                    id_cliente = int(input("Ingrese el ID del cliente: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaC.BuscarPorID(id_cliente)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun cliente guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                fecha_ingreso = date.today()
                print("\nLa fecha de ingreso es: ", fecha_ingreso)
                print("\nA continuacion ingrese la fecha de entrega propuesta")
                while True:
                    try:
                        dia = int(input("Ingrese el dia (1 a 31): "))
                    except ValueError:
                        print('Debe ingresar un numero del 1 al 31')
                        continue
                    break
                while True:
                    try:
                        mes = int(input("Ingrese el mes (1 a 12): "))
                    except ValueError:
                        print('Debe ingresar un numero del 1 al 12')
                        continue
                    break
                while True:
                    try:
                        anio = int(input("Ingrese el año: "))
                    except ValueError:
                        print('Debe ingresar un numero')
                        continue
                    break
                fecha_entrega_propuesta = date(anio, mes, dia)
                descripcion = input("\nIngrese la descripcion del nuevo trabajo: ")
                T = self.ListaT.NuevoTrabajo(C, fecha_ingreso, fecha_entrega_propuesta, descripcion)
                if T == None:
                    print("\n========================================\n")
                    print("Ocurrio un error al cargar el nuevo trabajo")
                    print("========================================")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

                else:
                    print("\n========================================")
                    print("El nuevo trabajo se cargo con exito\n")
                    print(T)
                    print("========================================\n")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun cliente guardado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

    def MostrarTrabajos(self):
        "Muestra una lista con todos los trabajos"
        Lista = self.RT.get_all()
        if Lista:
            for Cliente in Lista:
                print("\n===========================================\n")
                print(Cliente)
                print("===========================================")
        else:
            print("\nActualmente no se encuentra ningun trabajo cargado en el sistema")
        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

    def FinalizarTrabajo(self):
        "Solicita un ID trabajo y modifica la fecha de entrega real"
        t = self.RT.get_all()
        if t:
            for i in t:
                print("========================================")
                print(i.cliente)
                print("ID trabajo: ",i.id_trabajo,"- Fecha entrega real: ",i.fecha_entrega_real)
                print("========================================")
            print("\n========================================")
            while True:
                try:
                    id_trabajo = int(input("Ingrese el ID del trabajo: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaT.BuscarPorID(id_trabajo)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun trabajo guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\n========================================\n")
                print (C)
                print("========================================")
                tipo = "n"
                while tipo not in ("F","f","c","C"):
                    print("============================================================================")
                    tipo = input("""¿Estas seguro que desea dar por finalizado el trabajo?
                        
    F: Finalizar trabajo
    C: No finalizar
        
    Ingresa una opcion: """)
                    print("============================================================================")
                if tipo in ("F","f"):
                    T = self.ListaT.TrabajoFinalizado(id_trabajo)
                    if T == None:
                        print("\n==============================================")
                        print("Error al modificar la entrega real del trabajo")
                        print("==============================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                    else:
                        print("\n====================================================")
                        print("\nLa entrega real del trabajo fue modificada con exito")
                        print("\n====================================================")
                        print(C)
                        print("====================================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\n=================================================================")
                    print("No se realizo ninguna modificacion en la finalizacion del trabajo")
                    print("=================================================================\n")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun trabajo cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def RetirarTrabajo(self):
        "Solicita un ID trabajo y lo marca como retirado"
        t = self.RT.get_all()
        if t:
            for i in t:
                print("\n========================================")
                print(i.cliente)
                print("ID trabajo: ",i.id_trabajo,"- Retirado: ",i.retirado)
                print("=========================================\n")
            while True:
                try:
                    id_trabajo = int(input("Ingrese el ID del trabajo: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaT.BuscarPorID(id_trabajo)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun trabajo guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\n========================================")
                print(C)
                print("========================================")
                tipo = "n"
                while tipo not in ("R","r","c","C"):
                    print("\n======================================================")
                    tipo = input("""¿Estas seguro que desea dar por finalizado el trabajo?
                    
    R: Retirar el trabajo
    C: No retirar el trabajo
    
    Ingresa una opcion: """)
                    print("======================================================")
                if tipo in ("R","r"):
                    T = self.ListaT.Trabajo_retirado(id_trabajo)
                    if T == None:
                        print("========================================")
                        print("Error al retirar el trabajo")
                        print("========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                    else:
                        print("\n========================================")
                        print("El trabajo fue retirado con exito")
                        print("========================================\n")
                        print(C)
                        print("\n========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\n===========================================================")
                    print("No se realizo ninguna modificacion en el retiro del trabajo")
                    print("===========================================================")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun trabajo cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def ModificarDatosT(self):
        "Solicita un ID trabajo y modifica los datos del trabajo"
        t = self.RT.get_all()
        if t:
            for i in t:
                print("\n========================================")
                print("ID trabajo: ",i.id_trabajo)
                print("Fecha de ingreso: ",i.fecha_ingreso)
                print("Fecha entrega propuesta: ",i.fecha_entrega_propuesta)
                print("Descripcion: ",i.descripcion)
                print("========================================\n")
            while True:
                try:
                    id_trabajo = int(input("Ingrese el ID del trabajo: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaT.BuscarPorID(id_trabajo)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun trabajo guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\n=========================================")
                print (C.cliente)
                print("Trabajo:")
                print("Fecha de ingreso: ",C.fecha_ingreso)
                print("Fecha entrega propuesta: ",C.fecha_entrega_propuesta)
                print("Descripcion: ",C.descripcion)
                print("\n=============================================================================")
                print("Modifique el campo que desee, de no querer modificar algun campo dejelo vacio")
                print("=============================================================================")
                tipo = "n"
                while tipo not in ("I", "i", "P", "p", "D", "d", "C", "c"):
                    while tipo not in ("C", "c"):
                        tipo = input("""\n¿Estas seguro que desea hacer alguna modificacion?
                        
    I: Fecha de ingreso
    P: Fecha entrega propuesta
    D: Descripcion
    C: No deseo realizar una modificacion
    
    Ingrese una opcion: """)
                        if tipo in ("I","i"):
                            print("==========================")
                            print("Modificar fecha de ingreso\n")
                            while True:
                                try:
                                    dia = int(input("Ingrese el dia (1 a 31): "))
                                except ValueError:
                                    print('Debe ingresar un numero del 1 al 31')
                                    continue
                                break
                            while True:
                                try:
                                    mes = int(input("Ingrese el mes (1 a 12): "))
                                except ValueError:
                                    print('Debe ingresar un numero del 1 al 12')
                                    continue
                                break
                            while True:
                                try:
                                    anio = int(input("Ingrese el año: "))
                                except ValueError:
                                    print('Debe ingresar un numero')
                                    continue
                                break
                            FechaIngreso = date(anio, mes, dia)
                            T = self.ListaT.ModificarDatosT(FechaIngreso, C.fecha_entrega_real, C.descripcion, id_trabajo)
                            if T == None:
                                print("=========================================")
                                print("Error al modificar el trabajo")
                                print("=========================================")
                                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                            else:
                                print("\n=========================================")
                                print("Los datos que decidio modificar se modificaron con exito")
                                print("=========================================\n")
                                print(C)
                                print("=========================================")
                        if tipo in ("P","p"):
                            print("=====================================")
                            print("Modificar fecha de entregra propuesta\n")
                            while True:
                                try:
                                    dia = int(input("Ingrese el dia (1 a 31): "))
                                except ValueError:
                                    print('Debe ingresar un numero del 1 al 31')
                                    continue
                                break
                            while True:
                                try:
                                    mes = int(input("Ingrese el mes (1 a 12): "))
                                except ValueError:
                                    print('Debe ingresar un numero del 1 al 12')
                                    continue
                                break
                            while True:
                                try:
                                    anio = int(input("Ingrese el año: "))
                                except ValueError:
                                    print('Debe ingresar un numero')
                                    continue
                                break
                            FechaEntregaPropuesta = date(anio, mes, dia)
                            T = self.ListaT.ModificarDatosT(C.fecha_ingreso, FechaEntregaPropuesta, C.descripcion, id_trabajo)
                            if T == None:
                                print("=========================================")
                                print("Error al modificar el trabajo")
                                print("=========================================")
                                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                            else:
                                print("\n=========================================")
                                print("Los datos que decidio modificar se modificaron con exito")
                                print("=========================================\n")
                                print(C)
                                print("=========================================")
                        if tipo in ("D","d"):
                            print("====================================")
                            print("Modificar la descripcion del trabajo\n")
                            Descripcion = input("Ingrese la descripcion del trabajo: ")
                            T = self.ListaT.ModificarDatosT(C.fecha_ingreso, C.fecha_entrega_real, Descripcion, id_trabajo)
                            if T == None:
                                print("=========================================")
                                print("Error al modificar el trabajo")
                                print("=========================================")
                                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                            else:
                                print("\n=========================================")
                                print("Los datos que decidio modificar se modificaron con exito")
                                print("=========================================\n")
                                print(C)
                                print("=========================================")
                    if tipo in ("C","c"):
                        self.Ejecutar()
        else:
            print("\nActualmente no se encuentra ningun trabajo cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

    def BorrarTrabajo(self):
        "Solicita un ID trabajo y borra un trabajo"
        t = self.RT.get_all()
        if t:
            for i in t:
                print("\n========================================")
                print("ID trabajo: ",i.id_trabajo)
                print("Fecha de ingreso: ",i.fecha_ingreso)
                print("Fecha entrega propuesta: ",i.fecha_entrega_propuesta)
                print("Fecha de entrega real: ",i.fecha_entrega_real)
                print("Descripcion: ",i.descripcion)
                print("Retirado: ",i.retirado)
                print("=========================================\n")
            while True:
                try:
                    id_trabajo = int(input("Ingrese el ID del trabajo: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaT.BuscarPorID(id_trabajo)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun trabajo guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\n=========================================")
                print(C)
                print("=========================================\n")
                tipo = "n"
                while tipo not in ("E","e","C","c"):
                    tipo = input("""¿Estas seguro que desea eliminar el trabajo?
                    
    E: Eliminar trabajo
    C: No eliminar trabajo
    
    Ingresa una opcion: """)
                if tipo in ("E","e"):
                    T = self.ListaT.EliminarTrabajo(id_trabajo)
                    if T == None:
                        print("=========================================")
                        print("Ocurrio un error al eliminar el trabajo")
                        print("=========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")

                    else:
                        print("\n=========================================")
                        print("El trabajo fue eliminado con exito")
                        print("=========================================")
                        input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\n==================================")
                    print("Ha decidido no eliminar el trabajo")
                    print("==================================")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun trabajo cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def HistorialTrabajosPorC(self):
        """Solicita un ID y muestra una lista con los trabajos encargados por el cliente"""
        l = self.RC.get_all_corporativos()
        if l:
            print("""         =====================""")
            print("""         CLIENTES CORPORATIVOS""")
            print("""         =====================""")
            for i in l:
                print("========================================")
                print("ID cliente: ",i.id_cliente,"- Nombre: ",i.nombre_empresa)
                print("========================================")
        t = self.RC.get_all_particulares()
        if t:
            print("""         =====================""")
            print("""         CLIENTES PARTICULARES""")
            print("""         =====================""")
            for i in t:
                print("========================================")
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre)
                print("========================================\n")
        if l or t:
            while True:
                try:
                    id = int(input("\nIngrese el ID del cliente: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            C = self.ListaC.BuscarPorID(id)
            if C == None:
                print("\nEl ID ingresado no pertenece a ningun cliente guardado en el sistema")
                input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
            else:
                print("\n========================================\n")
                print(C)
                print("========================================")
                t = self.ListaT.TrabajoL
                if t:
                    for I in t:
                        if I.cliente.id_cliente == id:
                            print("========================================\n")
                            print("ID trabajo: ",I.id_trabajo)
                            print("Fecha de ingreso: ",I.fecha_ingreso)
                            print("Fecha entrega propuesta: ",I.fecha_entrega_propuesta)
                            print("Fecha entrega real: ",I.fecha_entrega_real)
                            print("Descripcion: ",I.descripcion)
                            print("Retirado: ",I.retirado)
                            print("========================================")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
                else:
                    print("\nActualmente el cliente no cuenta con ningun trabajo cargado en el sistema")
                    input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")
        else:
            print("\nActualmente no se encuentra ningun cliente cargado en el sistema")
            input("\nPRESIONE CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL DEL SISTEMA")


    def salir(self):
        print("Muchas gracias por haber utilizado el sistema")
        sys.exit(0)

if __name__ == "__main__":
    m = Menu()
    m.Ejecutar()