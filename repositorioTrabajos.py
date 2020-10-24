#! /usr/bin/python3
from repositorio import Repositorio
from repositorioClientes import RepositorioClientes
from trabajo import Trabajo
from cliente import Cliente
import datetime

class RepositorioTrabajos(Repositorio):
    '''Gestiona el almacenamiento de los clientes en la Base de Datos.'''

    def get_one(self, id_trabajo):
        '''Recibe un id (número entero), y retorna un objeto Trabajo. Si no lo
        encuentra, retorna None'''
        consulta = "SELECT id_cliente, fecha_ingreso, fecha_entrega_propuesta, \
          fecha_entrega_real, descripcion, retirado FROM trabajos WHERE id = ?"
        result = self.cursor.execute(consulta, [ id_trabajo ]).fetchone()
        if result == None:
            return None
        else:
            return self._obtener_trabajo_de_result(result, id_trabajo)

    def get_all(self):
        '''Retorna una lista compuesta por todos los objetos Trabajo'''
        consulta = "SELECT id_cliente, fecha_ingreso, fecha_entrega_propuesta, \
          fecha_entrega_real, descripcion, retirado, id FROM trabajos"
        result = self.cursor.execute(consulta).fetchall()
        lista_trabajos = []
        for t in result:
            lista_trabajos.append(self._obtener_trabajo_de_result(t))
        return lista_trabajos

    def store(self, trabajo):
        '''Recibe un objeto Trabajo, representando un nuevo Trabajo, y lo guarda
        en la base de datos.
        En caso de éxito, retorna el id del trabajo, generado por la base de
        datos. En caso de fracaso, retorna 0 (cero).'''
        # Abrimos un bloque try, por si falla algo al operar con la BD:
        try:
            consulta = "INSERT INTO trabajos (id_cliente, fecha_ingreso, \
            fecha_entrega_propuesta,fecha_entrega_real, descripcion, retirado) \
            VALUES (?,?,?,?,?,?)"
            parametros = [ trabajo.cliente.id_cliente ]
            
            parametros.append(trabajo.fecha_ingreso.strftime("%Y-%m-%d"))

            if trabajo.fecha_entrega_propuesta == None:
                parametros.append(None)
            else:
                parametros.append(
                    trabajo.fecha_entrega_propuesta.strftime("%Y-%m-%d") )

            if trabajo.fecha_entrega_real == None:
                parametros.append(None)
            else:
                parametros.append(
                    trabajo.fecha_entrega_real.strftime("%Y-%m-%d"))

            parametros.append(trabajo.descripcion)

            if trabajo.retirado:
                parametros.append(1)
            else:
                parametros.append(0)

            result=self.cursor.execute(consulta,parametros)
            # Preguntamos cuál fue el último id insertado:
            id_trabajo = result.lastrowid

            # Confirmamos los cambios:
            self.bd.commit()
            # Y retornamos el id del cliente recién insertado:
            return id_trabajo
        except:
            # Si ocurrió algún error, revertimos los cambios...
            self.bd.rollback()
            # ... y retornamos cero
            return 0

    def update(self, trabajo):
        '''Recibe un objeto Trabajo, y actualiza sus datos en la BD. No se puede
        actualizar el id del trabajo ni cambiar el cliente. 
        Retorna True si tuvo éxito, False de lo contrario'''
        fi = trabajo.fecha_ingreso.strftime("%Y-%m-%d")
        if trabajo.fecha_entrega_propuesta == None:
            fep = None
        else:
            fep = trabajo.fecha_entrega_propuesta.strftime("%Y-%m-%d")
        if trabajo.fecha_entrega_real == None:
            fer = None
        else:
            fer = trabajo.fecha_entrega_real.strftime("%Y-%m-%d")
        r = 1 if trabajo.retirado else 0
        consulta = "UPDATE trabajos SET fecha_ingreso = ?, \
                fecha_entrega_propuesta = ?, fecha_entrega_real = ?, \
                descripcion = ?, retirado = ? WHERE id = ?"
        try:
            result = self.cursor.execute(consulta, [ fi, fep, fer, 
                                                 trabajo.descripcion, r, 
                                                 trabajo.id_trabajo ])
            if result.rowcount > 0:
                self.bd.commit()
                return True
            else:
                self.bd.rollback()
                return False
        except:
            self.bd.rollback()
            return False

    def delete(self, trabajo):
        ''' Recibe un objeto Trabajo y lo elimina de la base de datos. Retorna
        True si tuvo éxito; False de lo contrario'''
        consulta = "DELETE FROM trabajos WHERE id = ?"
        try:
            result =self.cursor.execute(consulta, [ trabajo.id_trabajo ])
            if result.rowcount == 1:
                self.bd.commit()
                return True
            else:
                self.bd.rollback()
                return False
        except:
            self.bd.rollback()
            return False 

    def _obtener_trabajo_de_result(self, result, id_trabajo = None):
        '''Retorna un objeto Trabajo a partir del resultado de un SELECT'''
        # A partir del id_cliente, obtenemos el cliente correspondiente:
        rc = RepositorioClientes()
        cliente = rc.get_one(result[0])
        if cliente == None:
            return None

        # A partir de la fecha en formato "2020-31-12", creamos un datetime:
        fecha_ingreso = datetime.date.fromisoformat(result[1])

        #Hacemos lo mismo con las otras fechas, siempre que no sean nulas:
        if result[2] == None:
            fecha_entrega_propuesta = None
        else:
            fecha_entrega_propuesta = datetime.date.fromisoformat(result[2])
    
        if result[3] == None:
            fecha_entrega_real = None
        else:
            fecha_entrega_real = datetime.date.fromisoformat(result[3])

        # Guardamos la descripcion:
        descripcion = result[4]

        # Guardamos el valor booleano retirado: 0->False, 1->True
        retirado = result[5] == 1
        
        if id_trabajo == None:
            id_trabajo = result[6]

        return Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta,
                fecha_entrega_real, descripcion, retirado, id_trabajo)

