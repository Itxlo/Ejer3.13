class Calificacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def obtener_letra(self):

        if self.calificacion > 9.0:
            return "A"
        elif self.calificacion > 8.0:
            return "B"
        elif self.calificacion >= 7.5:
            return "C"
        else:
            return "R"

    def mostrar_calificacion(self):
        print(f"La calificación es {self.obtener_letra()}")


calificacion_numerica = float(input("Introduce tu calificación: "))
mi_calificacion = Calificacion(calificacion_numerica)
mi_calificacion.mostrar_calificacion()
