from Servicio import servicio
from Cliente import cliente
from Proxy import proxy

if __name__ == '__main__':
    print("Ejecucion mediante servicio real")
    servicio_real = servicio()
    cliente(servicio_real)
    
    print(  " --- ")
    
    print("Ejecucion mediante proxy")
    Proxxy = proxy(servicio_real)
    cliente(Proxxy)