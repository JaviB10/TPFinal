#! /usr/bin/env python3
from cliente import Cliente

class ClienteParticular(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)
         
    def __str__(self):
        Cadena = f"ID cliente: {self.id_cliente}\n"
        Cadena+= f"{self.nombre} {self.apellido} (Cliente Particular)\n"
        Cadena+= f"Tel: {self.telefono} - Email: {self.mail}\n"
        return Cadena