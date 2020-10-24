#! /usr/bin/python3
from repositorio import Repositorio
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo

class RepositorioClientes(Repositorio):
    '''Gestiona el almacenamiento de los clientes en la Base de Datos.'''

    def get_one(self, id_cliente):
        '''Recibe un id de cliente (número entero). Retorna un objeto cliente,
        tanto sea Particular como Corporativo. Si no lo encuentra, retorna
        None.'''
        # Comprobamos si existe un cliente con ese id en cliente_corporativo:
        consulta2 = "SELECT EXISTS ( SELECT * FROM cliente_corporativo \
                    WHERE id_cliente = ?) as existe"
        result2 = self.cursor.execute(consulta2,[id_cliente]).fetchone()
        if result2[0] == 1:
            return self.get_one_corporativo(id_cliente)

        # Si no, consultamos si existe uno con ese id en cliente_particular:
        consulta2 = "SELECT EXISTS ( SELECT * FROM cliente_particular \
                    WHERE id_cliente = ?) as existe"
        result2 = self.cursor.execute(consulta2,[id_cliente]).fetchone()
        if result2[0] == 1:
            return self.get_one_particular(id_cliente)

        # Si no existe en ninguna de las dos tablas, retornamos None
        return None

    def get_one_corporativo(self, id_cliente):
        '''Recibe un id de cliente (número entero). Retorna un cliente
        Corporativo. Si no lo encuentra, retorna None.'''
        consulta = "SELECT  cc.nombre_empresa, cc.nombre_contacto, \
                            cc.telefono_contacto, c.telefono, c.mail\
                    FROM cliente c \
                    JOIN cliente_corporativo cc ON c.id = cc.id_cliente \
                    WHERE c.id = ?"
        result = self.cursor.execute(consulta,[id_cliente]).fetchone()
        if result == None:
            return None
        else:
            return ClienteCorporativo(result[0], 
                                      result[1], 
                                      result[2],
                                      result[3], 
                                      result[4], 
                                      id_cliente);

    def get_one_particular(self, id_cliente):
        '''Recibe un id de cliente (número entero). Retorna un cliente
        Particular. Si no lo encuentra, retorna None.'''
        consulta = "SELECT cp.nombre, cp.apellido, c.telefono, c.mail  \
                    FROM cliente c \
                    JOIN cliente_particular cp ON c.id = cp.id_cliente \
                    WHERE c.id = ?"
        result = self.cursor.execute(consulta,[id_cliente]).fetchone()
        if result == None:
            return None
        else:
            return ClienteParticular(result[0], result[1], result[2], 
                                      result[3], id_cliente);
        
    
    def get_all(self):
        '''Retorna una lista, compuesta por objetos Cliente, tanto particulares
        como corporativos'''
        return self.get_all_particulares() + self.get_all_corporativos()
    
    def get_all_particulares(self):
        '''Retorna una lista, compuesta por todos los objetos
        ClienteParticular'''
        lista_clientes = []
        # Consultamos primero los clientes c orporativos:
        consulta = "SELECT c.id, cp.nombre, cp.apellido, c.telefono, c.mail \
                    FROM cliente_particular cp \
                    JOIN cliente c ON c.id = cp.id_cliente";
        self.cursor.execute(consulta)
        todos_los_clientes = self.cursor.fetchall()
        for id_cliente, nombre, apellido, telefono, mail in todos_los_clientes:
            lista_clientes.append(
                ClienteParticular(nombre, apellido, telefono, mail, id_cliente)
                )
        return lista_clientes

    def get_all_corporativos(self):
        '''Retorna una lista, compuesta por todos los objetos
        ClienteCorporativo'''
        lista_clientes = []
        # Consultamos primero los clientes corporativos:
        consulta = "SELECT c.id, cc.nombre_empresa, cc.nombre_contacto, \
                    cc.telefono_contacto, c.telefono, c.mail \
                    FROM cliente_corporativo cc \
                    JOIN cliente c ON c.id = cc.id_cliente";
        self.cursor.execute(consulta)
        todos_los_clientes = self.cursor.fetchall()
        for id_cliente, empresa, contacto, telefono_contacto, \
                         telefono_empresa, mail_empresa in todos_los_clientes:
            lista_clientes.append(
                ClienteCorporativo(empresa,
                                  contacto,
                                  telefono_contacto,
                                  telefono_empresa,
                                  mail_empresa,
                                  id_cliente
                                  )
                )
        return lista_clientes

    def store(self, cliente):
        '''Recibe un objeto Cliente (particular o corporativo), representando un
        cliente nuevo, y lo guarda en la base de datos.
        En caso de éxito, retorna el id del cliente generado por la base de
        datos. En caso de fracaso, retorna 0 (cero).'''
        # Abrimos un bloque try, por si falla algo al operar con la BD:
        try:
            # Guardamos en la tabla cliente los datos comunes:
            consulta = "INSERT INTO cliente (telefono, mail) VALUES (?,?)"
            result=self.cursor.execute(consulta,[cliente.telefono,cliente.mail])
            # Preguntamos cuál fue el último id insertado:
            id_cliente = result.lastrowid
    
            # Preparamos la consulta a la tabla específica al tipo de cliente:
            if type(cliente).__name__ == "ClienteCorporativo":
                tabla = "cliente_corporativo"
                campos = ["id_cliente", "nombre_empresa", "telefono_contacto", \
                        "nombre_contacto"]

                # consulta2 = "INSERT INTO cliente_corporativo (id_cliente,\
                #              nombre_empresa, telefono_contacto, id_contacto) \
                #              VALUES (?,?,?,?)"
                parametros = [ id_cliente, cliente.nombre_empresa,
                            cliente.telefono_contacto,cliente.nombre_contacto ]

            elif type(cliente).__name__ == "ClienteParticular":
                tabla = "cliente_particular"
                campos = ['id_cliente','nombre','apellido']
                # consulta2 = "INSERT INTO cliente_particular (id_cliente,\
                #               nombre, apellido) VALUES (?,?,?)"
                parametros = [ id_cliente, cliente.nombre, cliente.apellido ]

            else:
                # Revertimos los cambios, porque desconocemos el tipo de cliente
                self.bd.rollback()
                # Retornamos 0, indicando fracaso:
                return 0
            
            signos = ','.join([ '?' for i in campos ])
            consulta2 = "INSERT INTO " + tabla + '(' + ','.join(campos)
            consulta2+= ") VALUES (" + signos + ")"  
            # Ejecutamos consulta2, con los parámetros creados en el if anterior
            result2=self.cursor.execute(consulta2, parametros)
            # Confirmamos los cambios:
            self.bd.commit()
            # Y retornamos el id del cliente recién insertado:
            return id_cliente
        except:
            # Si ocurrió algún error, revertimos los cambios...
            self.bd.rollback()
            # ... y retornamos cero
            return 0

    def delete(self, cliente):
        '''Recibe un objeto Cliente y lo elimina de la Base de Datos.
        Retorna True si tuvo éxito, False de lo contrario.'''
        if type(cliente).__name__ == "ClienteCorporativo":
            tabla = "cliente_corporativo"
        elif type(cliente).__name__ == "ClienteParticular": 
            tabla = "cliente_particular"
        else:
            return False
        try:
            consulta = "DELETE FROM " + tabla + " WHERE id_cliente = ?"
            self.cursor.execute(consulta, [cliente.id_cliente])
            c1 = self.cursor.rowcount
            consulta2 = "DELETE FROM cliente WHERE id  = ?"
            self.cursor.execute(consulta2, [cliente.id_cliente])
            c2 = self.cursor.rowcount
            if (c1 == 0 or c2 == 0):
                # Si no afectó a ninguna fila (es decir, no borró nada):
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False

    def update(self, cliente):
        '''Recibe un objeto cliente y actualiza sus datos en la base de datos
        (no se puede actualizar el id del cliente, pero sí el resto de sus
        datos). Retorna True si tuvo éxito, False de lo contrario.'''
        try:
            consulta = "UPDATE cliente SET telefono = ?, mail = ? WHERE id = ?"
            result = self.cursor.execute(consulta, [cliente.telefono, 
                                                    cliente.mail, 
                                                    cliente.id_cliente])
            if result.rowcount == 0:
                # Si no se encontró un cliente con ese id:
                self.bd.rollback()
                return False

            if type(cliente).__name__ == "ClienteParticular":
                consulta2 = "UPDATE cliente_particular \
                        SET nombre = ?, apellido = ? WHERE id_cliente = ?"
                parametros=[cliente.nombre,cliente.apellido,cliente.id_cliente]        
            elif type(cliente).__name__ == "ClienteCorporativo":
                consulta2 = "UPDATE cliente_corporativo SET nombre_empresa=?,\
                nombre_contacto=?, telefono_contacto=? WHERE id_cliente=?"
                parametros=[cliente.nombre_empresa,    cliente.nombre_contacto,
                            cliente.telefono_contacto, cliente.id_cliente] 
            else:
                self.bd.rollback()
                return False
            
            result2 = self.cursor.execute(consulta2,parametros)
            if result2.rowcount == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
                self.bd.rollback()
                return False

