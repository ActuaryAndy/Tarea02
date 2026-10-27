class MyQueue: 
    def __init__(self):
        self.pila1 = []   # creamos la pila 1, inicialmente vacia, su funcion es tal cual una pila
        self.pila2 = []   # la pila 2 tendra la funcion principal de ser la inversa de la pila 1, dandonos
                          # el orden correcto de una cola

    def push(self, x: int) -> None:
        self.pila1.append(x)  # la funcion .append respeta el orden de una cola, considerando un orden de
                              # izquierda a derecha

    def pop(self) -> int:
        if not self.pila2:    # Si no hay elementos en la pila 2, tendremos que:
            while self.pila1:    # mientras haya elementos en la pila 1 
                self.pila2.append(self.pila1.pop()) # creamos la lista con orden inverso con la funcion  
        return(self.pila2.pop())    # .pop en la pila 2 y vaciamos la pila 1 para finalmente
                                    # regresar y eliminamos el ultimo elemento siendo el primero en haber  # entrado a la pila 1 cumpliendo con ser el primero de la cola,        # cumpliendo de la  # misma manera si ya habia elementos existentes

            
    def peek(self) -> int:
        if not self.pila2:
            while self.pila1:
                self.pila2.append(self.pila1.pop())
        return(self.pila2[-1])  # se usa el mismo metodo de pop, solo regresando el elemento sin eliminarlo

    def empty(self) -> bool:
        if not self.pila2 and not self.pila1: # Si no hay elementos en ambas pilas
            return True
        else:
            return False     # Si hay elemento en alguna pila 
    
