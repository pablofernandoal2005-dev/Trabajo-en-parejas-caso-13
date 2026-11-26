#Alvarado Pablo - Ortiz Steven 
#M3A
#TSUDS

class vistaEvento:
    def menu(self):
        print("-------Eventos del instituto------")
        print("1. Registrar Evento")
        print("2.Mostrar Eventos")
        print("3.Inscribir")
        print("4. Buscar por su nombre")
        print("5. Anular inscripcion")
        print("6. Mostrar inscripciones")
        print("6. Mostrar inscripciones")
        print("7. Reporte General")
        print("8. Salir")

    def pedir_texto(self, mensaje):
        return input(mensaje).srip()

    def pedir_entero(self, mensaje):
        try:
            return int(input(mensaje))
        except ValueError:
            raise ValueError("Debe ser un numero entero")

    def pedir_decimales(self, mensaje):
        try:
            return float(
                input(mensaje).replace(
                    ",",
                    ".",
                )
            )
        except ValueError:
            raise ValueError("Debe ser en decimal")

    def pedir_si_o_no(self, mensaje):
        return input(mensaje + "s/n").strip().lower() in ("s", "si", "sí")

    def mensajes(self, texto):
        print(texto)
