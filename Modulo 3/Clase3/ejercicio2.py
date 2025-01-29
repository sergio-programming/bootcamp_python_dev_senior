class Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        
reservas = [
    Reserva("Juan", None),
    Reserva("Sergio", "2025-01-28"),
    Reserva("Flaquita", "2025-01-29")
]

for reserva in reservas:
    if not reserva.fecha:
        print(f"Error: Fecha no asignada por el cliente {reserva.cliente}")