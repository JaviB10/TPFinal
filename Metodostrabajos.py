from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime


class ListaTrabajos:

    def __init__(self):
        self.RT = RepositorioTrabajos()
        self.TrabajoL = self.RT.get_all()

    def NuevoTrabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        """Recibe los datos de un trabajo, crea un nuevo trabajo y lo agrega a la lista trabajos"""
        T = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        T.id_trabajo = self.RT.store(T)
        if T.id_trabajo == 0:
            return None
        else:
            self.TrabajoL.append(T)
            return T

    def BuscarPorID(self, id_trabajo):
        """Recibe un ID y retorna un trabajo"""
        for T in self.TrabajoL:
            if T.id_trabajo == int(id_trabajo):
                return (T)
        return None

    def TrabajoFinalizado(self, id_trabajo):
        """Recibe un trabajo y le modifica la fecha de entrega"""
        T = self.BuscarPorID(id_trabajo)
        if T:
            T.fecha_entrega_real = datetime.date.today()
            return self.RT.update(T)
        return None

    def Trabajo_retirado(self, id_trabajo):
        """Recibe un trabajo y modifica el trabajo como retirado"""
        T = self.BuscarPorID(id_trabajo)
        if T:
            if T.fecha_entrega_real == None:
                T.retirado = True
                self.TrabajoFinalizado(id_trabajo)
            else:
                T.retirado = True
            return self.RT.update(T)
        return None

    def ModificarDatosT(self, fecha_ingreso, fecha_entrega_propuesta, descripcion, id_trabajo):
        """Recibe un trabajo y modifica sus datos"""
        T = self.BuscarPorID(id_trabajo)
        if T:
            T.fecha_ingreso = fecha_ingreso
            T.fecha_entrega_propuesta = fecha_entrega_propuesta
            T.descripcion = descripcion
            return self.RT.update(T)
        return None

    def EliminarTrabajo(self, id_trabajo):
        T = self.BuscarPorID(id_trabajo)
        if T:
            self.RT.delete(T)
            self.TrabajoL = self.RT.get_all()
            return True
        return None



