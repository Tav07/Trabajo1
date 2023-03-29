tarifa_base = 2000
total_espacios = 100


class Cliente:
    def __init__(self, nombre: str, placa: str):
        self.nombre = nombre
        self.placa = placa
        self.tiempo = 0

    def calcular_costo(self) -> int:
        costo = self.tiempo * tarifa_base
        return costo


class Administrador:
    def __init__(self):
        self.ingresos = 0
        self.egresos = 0
        self.espacios_disponibles = total_espacios
        self.espacios_ocupados = 0

    def registrar_ingreso(self, cliente: Cliente) -> None:
        self.ingresos += cliente.calcular_costo()
        self.espacios_disponibles -= 1
        self.espacios_ocupados += 1

    def registrar_egreso(self, cliente: Cliente) -> None:
        self.egresos += cliente.calcular_costo()
        self.espacios_disponibles += 1
        self.espacios_ocupados -= 1

    def generar_reporte(self) -> str:
        reporte = f"Ingresos: {self.ingresos}\nEgresos: {self.egresos}\nEspacios disponibles: {self.espacios_disponibles}"
        return reporte


class Parqueadero:
    def __init__(self):
        self.administrador = Administrador()
        self.clientes = []

    def ingresar_cliente(self, nombre: str, placa: str) -> None:
        cliente = Cliente(nombre, placa)
        self.clientes.append(cliente)
        self.administrador.registrar_ingreso(cliente)

    def retirar_cliente(self, placa: str) -> None:
        for cliente in self.clientes:
            if cliente.placa == placa:
                self.clientes.remove(cliente)
                self.administrador.registrar_egreso(cliente)

    def generar_reporte(self) -> str:
        reporte = self.administrador.generar_reporte()
        return reporte


parqueadero = Parqueadero()

while True:
    print("\n1. Registrar Ingreso")
    print("2. Calcular Costo")
    print("3. Registrar Egreso")
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del cliente: ")
        placa = input("Ingrese la placa del vehículo: ")
        parqueadero.ingresar_cliente(nombre, placa)
        print("Ingreso registrado exitosamente.")

    elif opcion == 2:
        placa = input("Ingrese la placa del vehículo: ")
        tiempo = int(input("Ingrese el tiempo de estacionamiento en horas: "))
        for cliente in parqueadero.clientes:
            if cliente.placa == placa:
                cliente.tiempo = tiempo
                costo = cliente.calcular_costo()
                print("Pague", costo)

    elif opcion == 3:
        placa = input("Ingrese la placa del vehículo: ")
        parqueadero.retirar_cliente(placa)
        print("Egreso registrado exitosamente.")
