#Patron de diseño Singleton
class SingleCreationInstancia:
    
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(SingleCreationInstancia, cls)._new_(cls)
        return cls._instancia
    
    