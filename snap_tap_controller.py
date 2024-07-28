import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

# Variáveis para armazenar o estado das teclas
keys_pressed = {}
snap_tap_active = False
listener = None

# Função para ativar/desativar o Snap Tap
def toggle_snap_tap():
    global snap_tap_active
    snap_tap_active = not snap_tap_active
    if snap_tap_active:
        activate_button.config(text="Desativar Snap Tap")
        start_listener()
    else:
        activate_button.config(text="Ativar Snap Tap")
        stop_listener()

# Funções para iniciar e parar o listener do teclado
def start_listener():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    monitor_keys()

def stop_listener():
    global listener
    if listener:
        listener.stop()
        listener = None

def on_press(key):
    if not snap_tap_active:
        return
    try:
        k = key.char
    except:
        k = key.name
    keys_pressed[k] = True

def on_release(key):
    if not snap_tap_active:
        return
    try:
        k = key.char
    except:
        k = key.name
    if k in keys_pressed:
        del keys_pressed[k]

def monitor_keys():
    if snap_tap_active:
        if 'a' in keys_pressed and 'd' in keys_pressed:
            controller.press('a')
            controller.release('a')
            controller.press('d')
            controller.release('d')
        elif 'w' in keys_pressed and 's' in keys_pressed:
            controller.press('w')
            controller.release('w')
            controller.press('s')
            controller.release('s')
    root.after(10, monitor_keys)

# Interface gráfica
root = tk.Tk()
root.title("Snap Tap Controller")

activate_button = tk.Button(root, text="Ativar Snap Tap", command=toggle_snap_tap)
activate_button.pack(pady=20)

controller = keyboard.Controller()

root.mainloop()
