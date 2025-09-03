import tkinter as tk

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f"Resultado: {fahrenheit:.2f}°")
    except:
        resultado.config(text="Ingrese un número valido")

root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("300x200")


# Widgets
tk.Label(root, text="Por favor ingrese los grados Celsius: ").pack(padx=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convertir", command=convertir).pack(pady=5)
resultado = tk.Label(root, text="Resultado: ")
resultado.pack(pady=5)

root.mainloop()