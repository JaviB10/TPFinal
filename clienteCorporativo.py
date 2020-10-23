#! /usr/bin/env python3
from cliente import Cliente

class ClienteCorporativo(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre_empresa, nombre_contacto, telefono_contacto,
            telefono, mail, id_cliente = None):
        self.nombre_empresa = nombre_empresa
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        super().__init__(telefono, mail, id_cliente)
         
    def __str__(self):
        Cadena = f"{self.id_cliente}:{self.nombre_empresa} (Cliente Corporativo)\n"
        Cadena+= f"{self.telefono} - {self.mail}\n"
        Cadena+= f"Datos del contacto: {self.nombre_contacto} - {self.telefono_contacto}\n"
        return Cadena