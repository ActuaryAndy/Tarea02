#coplejidad temporal: O(n) en promedio
#complejidad espacial: O(n)
# Justificacion: usamos un diccionario para guardar los numeros y los indices y recorremos la lista esto puede guardar n elelemntos  y al momento de buscar y guardar en el diccionario es de O(1) en promedio 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vistos = {}

        for i in range(len(nums)):
            faltante = target - nums[i]

            if faltante in vistos:
                return [vistos[faltante], i]

            vistos[nums[i]] = i

