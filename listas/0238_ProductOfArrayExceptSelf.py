# Complejidad temporal: O(n).
# Complejidad espacial: O(1) extre sin contar la lista de salida
# Justificacion: recorremos la lista 2 veces y usamos 1 lista de salida para guardar los productoo y Solo necesitamos dos variadles para acumular los productos de izquierda y derecha.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        resultado = [1] * n

        izquierda = 1
        for i in range(n):
            resultado[i] = izquierda
            izquierda = izquierda * nums[i]

        derecha = 1
        for i in range(n - 1, -1, -1):
            resultado[i] = resultado[i] * derecha
            derecha = derecha * nums[i]

        return resultado
    
