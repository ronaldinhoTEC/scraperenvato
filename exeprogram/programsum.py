import tkinter as tk
from tkinter import messagebox

# Función para sumar los dos números
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sumador de Números")

# Crear y colocar etiquetas y entradas de texto
label_num1 = tk.Label(root, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Crear y colocar el botón de sumar
boton_sumar = tk.Button(root, text="Sumar", command=sumar)
boton_sumar.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
