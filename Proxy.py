from Interfaz import interfaz
from Servicio import servicio

class proxy(interfaz):
    def __init__(self, solicitud: servicio) -> None:
        self.solicitud = solicitud
        
    def revisar_autorizacion(self)-> bool:
        print("Acceso al servicio concendido (Proxy)")
        return True
    
    def acceso(self) -> None:
        print("Peticion registrada (Proxy)")
        
    def solicitud_pago(self) -> None:
        if self.revisar_autorizacion():
            self.solicitud.solicitud_pago()
            self.acceso()
            