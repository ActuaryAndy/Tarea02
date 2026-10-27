from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        self.coladoble = deque()                                  #  Creamos una cola de doble salida       
        self.salida = []                                            
        for i in range(len(nums)):                                # Comparamos indices
            if self.coladoble and self.coladoble[0] < i - k + 1:  # Si el indice al final de la cola es   #                        menor a el indice inicial de la ventana, los eliminamos de la cola
                self.coladoble.popleft()
                                                        # Los numeros menores en la cola a el numero
            while self.coladoble and nums[self.coladoble[-1]] <= nums[i]:  # siguiente, ya no pueden ser    #                                             maximos por tanto
                self.coladoble.pop()                    # se pueden eliminar
            self.coladoble.append(i)                    # agregamos el nuevo elemento a la cola
            if i >= k - 1:                          # agregamos los numeros maximos a la lista de salida 
                self.salida.append(nums[self.coladoble[0]])
        return self.salida
