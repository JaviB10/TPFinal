#! /usr/bin/env python3

from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from Metodostrabajos import ListaTrabajos


class ListaClientes:
    def __init__(self):
        self.RC = RepositorioClientes()
        self.RT = RepositorioTrabajos()
        self.ClienteL = self.RC.get_all()
        self.ListaT = ListaTrabajos()



    def NuevoClienteCorp(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        """Recibe los datos de un cliente corporativo, crea un nuevo cliente corporativo y lo agrega a lista de clientes"""
        C = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        C.id_cliente = self.RC.store(C)
        if C.id_cliente == 0:
            return None
        else:
            self.ClienteL.append(C)
            return C

    def NuevoClientePart(self, nombre, apellido, telefono, mail):
        """Recibe los datos de un cliente particular, crea un nuevo cliente particular y lo agrega a la lista de clientes"""
        C = ClienteParticular(nombre, apellido, telefono, mail)
        C.id_cliente = self.RC.store(C)
        if C.id_cliente == 0:
            return None
        else:
            self.ClienteL.append(C)
            return C

    def BuscarPorID(self, id_cliente):
        """Recibe un ID y retorna un cliente"""
        for T in self.ClienteL:
            if T.id_cliente == int(id_cliente):
                return (T)
        print("El ID ingresado no pertenece a ningun cliente")
        return None


    def ModificarDatosCP(self, nombre, apellido, telefono ,mail, id_cliente):
        """Recibe los datos modificados y actualiza los datos del cliente particular"""
        C = self.BuscarPorID(id_cliente)
        if C:
            if nombre == '':
                nombre = C.Nombre
            else:
                C.nombre = nombre
            if apellido == '':
                apellido = C.apellido
            else:
                C.apellido = apellido
            if telefono == '':
                telefono = C.telefono
            else:
                C.telefono = telefono
            if mail == '':
                mail = C.mail
            else:
                C.mail = mail
            return self.RC.update(C)
        return None

    def ModificarDatosCC(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail, id_cliente):
        """Recibe los datos modificados y actualiza los datos del cliente corporativo"""
        C = self.BuscarPorID(id_cliente)
        if C:
            if nombre_empresa == '':
                nombre_empresa = C.nombre_empresa
            else:
                C.nombre_empresa = nombre_empresa
            if nombre_contacto == '':
                nombre_contacto = C.nombre_contacto
            else:
                C.nombre_contacto = nombre_contacto
            if telefono_contacto == '':
                telefono_contacto = C.telefono_contacto
            else:
                C.telefono_contacto = telefono_contacto
            if telefono == '':
                telefono = C.telefono
            else:
                C.telefono = telefono
            if mail == '':
                mail = C.mail
            else:
                C.mail = mail
            return self.RC.update(C)
        return None

    def EliminarCliente(self, id_cliente):
        """"Recibe el ID de un cliente y lo elimina, en caso de contener trabajos, tambien los elimina"""
        C = self.BuscarPorID(id_cliente)
        if C == self.ListaT.TrabajoL:
            for I in self.ListaT.TrabajoL:
                if I.cliente.id_cliente == id_cliente:
                    self.RT.delete(I)
                    self.ListaT = ListaTrabajos()
                    B = self.RC.delete(C)
                    self.ListaC = ListaClientes()
                    return C
        else:
            B = self.RC.delete(C)
            self.ListaC = ListaClientes()
            return C
        return None