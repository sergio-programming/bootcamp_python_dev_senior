import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class Vehiculo:
    def __init__(self, placa, horaEntrada):
        self.placa = placa
        self.horaEntrada = horaEntrada
        
    def calcularTiempo(self):
        horaSalida = datetime.datetime.now()
        tiempoTotal = horaSalida - self.horaEntrada
        return tiempoTotal.total_seconds() / 60 #total_seconds devuelve los segundos de la funcion datetime.datetime.now()
    
class ParqueaderoApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Control de Parqueadero")
        self.ventana.geometry("500x400")
        
        self.vehiculos = {}
        
        #Entrada de la placa
        tk.Label(ventana, text="Ingrese la placa del vehiculo: ").pack(pady=5) # Texto para la caja de texto
        self.entryPlaca = tk.Entry(ventana) # Caja de texto
        self.entryPlaca.pack(pady=5)
        
        #Botones
        tk.Button(ventana, text="Registro Entrada", command=self.registroEntrada).pack(pady=5)
        tk.Button(ventana, text="Registro Salida", command=self.registroSalida).pack(pady=5)
        
        #Tabla de vehiculos
        self.tree = ttk.Treeview(ventana, columns=("Placa", "Hora de Entrada"), show="headings")
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Hora de Entrada", text="Hora de Entrada")
        self.tree.pack(pady=10, fill="both", expand=True)
        
    def registroEntrada(self):
        placa = self.entryPlaca.get().upper()
        if placa and placa not in self.vehiculos:
            horaActual = datetime.datetime.now().strftime("%H:%M:%S")
            self.vehiculos[placa] = Vehiculo(placa, datetime.datetime.now())
            
            self.tree.insert("", "end", iid=placa, values=(placa, horaActual))
        else:
            messagebox.showerror("Error", "Placa invalida o ya registrada")
        
            
    def registroSalida(self):
        placa = self.entryPlaca.get().upper()
        if placa in self.vehiculos:
            Vehiculo = self.vehiculos.pop(placa)
            tiempoParque = Vehiculo.calcularTiempo()
            print(tiempoParque)
            self.tree.delete(placa)
            
            messagebox.showinfo("Salida", f"Vehiculo {placa} ha salido del parqueadero \nTiempo: {tiempoParque:.2f} minutos")
        else:
            messagebox.showerror("Error", "Vehiculo no encontrado")    
    
                   
root = tk.Tk()
app = ParqueaderoApp(root)
root.mainloop()