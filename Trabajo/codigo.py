import tkinter as tk
from datetime import datetime

def calcular_tarifa(tipo_vehiculo, tiempo):
    if tipo_vehiculo == 'carro':
        tarifa_hora = 4700
        tarifa_dia = 19000
        tarifa_mes = 276000
    elif tipo_vehiculo == 'moto':
        tarifa_hora = 2100
        tarifa_dia = 9500
        tarifa_mes = 89500

    dias = tiempo.days
    horas = tiempo.seconds // 3600
    minutos = (tiempo.seconds % 3600) // 60

    # Si el tiempo no supera una hora, se cobra la tarifa completa de una hora
    if dias == 0 and horas == 0 and minutos <= 60:
        return tarifa_hora

    total = (dias * tarifa_dia) + (horas * tarifa_hora)
    if dias >= 31:
        total = tarifa_mes

    return total

def registrar_entrada():
    placa = placa_entry.get()
    tipo_vehiculo = tipo_vehiculo_var.get()
    hora_entrada = datetime.now()
    vehiculos_registrados[placa] = hora_entrada
    entrada_label.config(text=f"Registro de entrada exitoso. Hora de entrada: {hora_entrada}")

def generar_factura():
    placa = placa_entry.get()
    tipo_vehiculo = tipo_vehiculo_var.get()
    hora_salida = datetime.now()
    if placa in vehiculos_registrados:
        hora_entrada = vehiculos_registrados[placa]
        tiempo_estacionado = hora_salida - hora_entrada
        tarifa_total = calcular_tarifa(tipo_vehiculo, tiempo_estacionado)
        factura = f"--- FACTURA ---\n"
        factura += f"Placa: {placa}\n"
        factura += f"Tipo de vehículo: {tipo_vehiculo}\n"
        factura += f"Hora de entrada: {hora_entrada}\n"
        factura += f"Hora de salida: {hora_salida}\n"
        factura += f"Tiempo estacionado: {tiempo_estacionado}\n"
        factura += f"Tarifa total: {tarifa_total} pesos\n"
        factura_text.configure(state='normal')
        factura_text.delete("1.0", tk.END)
        factura_text.insert(tk.END, factura)
        factura_text.configure(state='disabled')
        del vehiculos_registrados[placa]
    else:
        factura_text.configure(state='normal')
        factura_text.delete("1.0", tk.END)
        factura_text.insert(tk.END, "El vehículo no ha sido registrado.")
        factura_text.configure(state='disabled')

vehiculos_registrados = {}

window = tk.Tk()
window.title("Sistema de Facturación de Estacionamiento")

# Crear los elementos de la interfaz
placa_label = tk.Label(window, text="Placa del vehículo:")
placa_entry = tk.Entry(window)
tipo_vehiculo_label = tk.Label(window, text="Tipo de vehículo:")
tipo_vehiculo_var = tk.StringVar(window)
tipo_vehiculo_var.set("carro")
tipo_vehiculo_optionmenu = tk.OptionMenu(window, tipo_vehiculo_var, "carro", "moto")
registrar_entrada_btn = tk.Button(window, text="Registrar Entrada", command=registrar_entrada)
generar_factura_btn = tk.Button(window, text="Generar Factura", command=generar_factura)
entrada_label = tk.Label(window, text="")
factura_text = tk.Text(window, height=10, width=50)
factura_text.configure(state='disabled')

# Posicionar los elementos en la interfaz
placa_label.pack()
placa_entry.pack()
tipo_vehiculo_label.pack()
tipo_vehiculo_optionmenu.pack()
registrar_entrada_btn.pack()
entrada_label.pack()
generar_factura_btn.pack()
factura_text.pack()

window.mainloop()