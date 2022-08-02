from abc import ABC, abstractmethod

class interfaz(ABC):
    @abstractmethod
    def solicitud_pago(self) -> None:
        pass
    