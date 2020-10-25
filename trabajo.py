#! /usr/bin/python3

import datetime

class Trabajo:
    '''Representa un trabajo de reparación que realizará el taller'''
    def __init__(self, cliente, fecha_ingreso, fecha_entrega_propuesta,
        fecha_entrega_real, descripcion, retirado, id_trabajo = None):
        ''' Recibe un objeto cliente, una fecha de ingreso (objeto datetime),
        otros dos objetos datetime con la fecha de entrega propuesta y real, 
        una descripción, un valor "retirado" (True o False) y un id opcional'''
        self.cliente = cliente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_entrega_propuesta = fecha_entrega_propuesta
        self.fecha_entrega_real = fecha_entrega_real
        self.descripcion = descripcion
        self.retirado = retirado
        self.id_trabajo = id_trabajo

    def __str__(self):
        cadena = f"Cliente: \n"
        cadena+= f"{self.cliente}\n"
        cadena+= f"Trabajos: \n"
        cadena+= f"ID del trabajo: {self.id_trabajo}\n"
        cadena+= f"Fecha de ingreso: {self.fecha_ingreso}\n"
        cadena+= f"Fecha de entrega propuesta: {self.fecha_entrega_propuesta}\n"
        cadena+= f"Fecha de entrega real: {self.fecha_entrega_real}\n"
        cadena+= f"Descripción: {self.descripcion}\n"
        cadena+= f"Retirado: {self.retirado}"
        return cadena

