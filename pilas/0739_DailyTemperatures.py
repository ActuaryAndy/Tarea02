# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificacion: Cada elemento entra y sale de la pila hasta una vez, recorriendo el arreglo de temperaturas de forma lineal.
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        resultados = [0] * n
        pila = []
        
        for i in range(n):
            while pila and temperatures[i] > temperatures[pila[-1]]:
                dia_anterior = pila.pop()
                resultados[dia_anterior] = i - dia_anterior
            pila.append(i)
        return resultados
