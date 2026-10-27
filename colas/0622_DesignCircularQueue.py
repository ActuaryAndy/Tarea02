class MyCircularQueue:
    def __init__(self, k: int):
        self.tamaño = k       # establecemos el tamaño k de la cola
        self.cola = [0] * k   # una cola inicial con el tamaño establecido k
        self.ocupados = 0     # lugares de la cola ocupados inicialmente en 0
        self.rear = -1        # indicador de indice del ultimo elemento de la cola
        self.front = 0        # indicador de indice del primer elemento de la cola

    def enQueue(self, value: int) -> bool:
        if self.isFull():     # si la cola esta llena no se puede agregar otro elemento
            return False
        else: 
            self.cola[(self.rear + 1) % self.tamaño] = value  # agregamos value a la posicion resultante    #                                                   posterior a el ultimo de la cola
        self.rear += 1        # actualizamos el indice del ultimo elemento
        self.ocupados += 1    # actualizamos la cantidad de elementos en la cola
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():    # Si la pila esta vacia no se puede eliminar elementos
            return False
        else: 
            self.cola[self.front % self.tamaño] = 0  # reiniciamos el elemento resultante al inicio de la   #                                          cola a 0 por comodidad inicial, mas no es necesario
        self.front += 1       # Ahora el elemnto inicial de la cola es el siguiente
        self.ocupados -= 1    # Actualizamos la cantidad de elementos en la cola
        return True
    def Front(self) -> int:
        if self.isEmpty():    # Si la cola esta vacia solo regresamos -1
            return -1
        else: 
            return self.cola[self.front % self.tamaño]  # regresamos el elemento elemento congruente bajo #                                             modulo k, representando a el elemento inicial de #                                             la cola
            

    def Rear(self) -> int:
        if self.isEmpty():    #  Si la cola esta vacia regresamos -1
            return -1
        else:
            return self.cola[self.rear % self.tamaño]   # regresamos el elemento representante a el ultimo #                                             de la cola

    def isEmpty(self) -> bool:
        return self.ocupados == 0      # esta vacia si no hay ocupados 

    def isFull(self) -> bool:
        return self.ocupados == self.tamaño  # esta llena si los ocupados es el total k

