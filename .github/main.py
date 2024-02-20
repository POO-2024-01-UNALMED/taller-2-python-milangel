class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, color, registro):
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.registro = registro
        self.asientos = []
        Auto.cantidadCreados += 1

    def cambiarColor(self, color):
        colores_validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_validos:
            self.color = color
        else:
            print("Color no válido.")

    def cantidadAsientos(self):
        return len(self.asientos)

    def verificarIntegridad(self):
        registro_auto = self.registro
        for asiento in self.asientos:
            if asiento.registro != registro_auto:
                return "Las piezas no son originales"
        if self.motor.registro != registro_auto:
            return "Las piezas no son originales"
        return "Auto original"


class Asiento:
    def __init__(self, numeroAsientos, color, registro):
        self.numeroAsientos = numeroAsientos
        self.color = color
        self.registro = registro


class Motor:
    def __init__(self, marca, tipo, numeroCilindros, registro):
        self.marca = marca
        self.tipo = tipo
        self.numeroCilindros = numeroCilindros
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo
        else:
            print("Tipo de motor no válido.")
