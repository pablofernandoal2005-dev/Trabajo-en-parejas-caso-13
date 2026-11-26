#Alvarado Pablo - Ortiz Steven 
#M3A
#TSUDS

class Evento:
    def __init__(self, codigo, nombre, precio, aforo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.aforo = aforo

    def a_linea(self):
        return f"{self.codigo},{self.nombre},{self.precio},{self.aforo}"


class Inscripcion:
    def __init__(self, numero, codigo_evento, cantidad, es_estudiante, total, fecha, estado):
        self.numero = numero
        self.codigo_evento = codigo_evento
        self.cantidad = cantidad
        self.es_estudiante = es_estudiante   
        self.total = total
        self.fecha = fecha
        self.estado = estado                 

    def a_linea(self):
        if self.es_estudiante:
            est = "si"
        else:
            est = "no"
        return (f"{self.numero},{self.codigo_evento},{self.cantidad},{est},"
                f"{self.total},{self.fecha},{self.estado}")

class eventos: