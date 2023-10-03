import tkinter as tk
import requests
from datetime import datetime
import os
import threading
import sys
import atexit

# Comprobar si ya existe un archivo de bloqueo
lockfile = 'lockfile.lock'
if os.path.isfile(lockfile):
    print("La aplicación ya está en ejecución.")
    sys.exit()

# Crear el archivo de bloqueo
open(lockfile, 'w').close()

# Eliminar el archivo de bloqueo al salir del programa
def eliminar_lockfile():
    if os.path.isfile(lockfile):
        os.remove(lockfile)

atexit.register(eliminar_lockfile)

# Función para obtener la IP pública IPv4
def obtener_ip_publica_ipv4():
    try:
        response = requests.get("https://ipv4.icanhazip.com")
        return response.text.strip()
    except Exception as e:
        return "Error al obtener la IP pública"

# Función para obtener el historial de IP desde el archivo de historial
def obtener_historial():
    historial = ""
    if os.path.exists("ip_historial.txt"):
        with open("ip_historial.txt", "r") as file:
            historial = file.read()
    return historial

# Función para actualizar la información y mostrarla en la interfaz gráfica
def actualizar_y_mostrar():
    ip_actual_ipv4 = obtener_ip_publica_ipv4()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Obtener la IP antigua desde el historial
    ip_antigua = obtener_historial().split("Ip actualizada:")[-1].strip()

    if ip_actual_ipv4 != ip_antigua:
        # Guardar la nueva IP en el archivo de historial
        with open("ip_historial.txt", "a") as file:
            file.write(f"Fecha: {fecha}\nIp antigua: {ip_antigua}\nIp actualizada: {ip_actual_ipv4}\n\n")

    # Actualizar la etiqueta en la interfaz gráfica
    ip_actual_label.config(text=f"Ip actual:\n{ip_actual_ipv4}\n{fecha}")

    # Hacer que el cuadro de texto sea editable temporalmente para actualizarlo
    historial_text.configure(state="normal")

    # Actualizar el cuadro de texto con el historial
    historial_text.delete("1.0", tk.END)  # Borrar el contenido actual
    historial_text.insert(tk.END, obtener_historial())  # Insertar el nuevo historial

    # Volver a configurar el cuadro de texto en modo de solo lectura
    historial_text.configure(state="disabled")

# Función para ejecutar la actualización en segundo plano
def ejecutar_actualizacion_en_segundo_plano():
    while True:
        actualizar_y_mostrar()
        # Ajusta el tiempo de espera aquí (por ejemplo, 5 minutos)
        threading.Event().wait(15)  # 300 segundos = 5 minutos

# Configuración de la ventana tkinter
window = tk.Tk()
window.title("Detector de IP Pública")
window.geometry("400x400")  # Tamaño fijo

# Hacer que la ventana no sea redimensionable
window.resizable(False, False)

# Etiqueta para mostrar la IP actual
ip_actual_label = tk.Label(window, text="", padx=10, pady=10)
ip_actual_label.pack()

# Cuadro de texto para mostrar el historial (solo lectura)
historial_text = tk.Text(window, height=15, width=40)
historial_text.pack()

# Hacer que el cuadro de texto sea de solo lectura inicialmente
historial_text.configure(state="disabled")

# Lanzar el hilo para ejecutar la actualización en segundo plano
background_thread = threading.Thread(target=ejecutar_actualizacion_en_segundo_plano)
background_thread.daemon = True
background_thread.start()

# Llamar a la función para actualizar y mostrar la IP al abrir el programa
actualizar_y_mostrar()

# Iniciar la aplicación
window.mainloop()
