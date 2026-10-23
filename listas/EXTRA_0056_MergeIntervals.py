# Complejidad temporal:O(n log n)
# Complejidad espacial:O(n)
# Justificacion: ordenar cuesta O(n log n) y recorremos los intervalos una viz, la lista de resultados puede guardar n intervalos y la ordenación puede usar O(n) de espacio.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        unidos = []

        for intervalo in intervals:
            inicio = intervalo[0]
            fin = intervalo[1]

            if not unidos or inicio > unidos[-1][1]:
                unidos.append([inicio, fin])
            else:
                unidos[-1][1] = max(unidos[-1][1], fin)

        return unidos 

