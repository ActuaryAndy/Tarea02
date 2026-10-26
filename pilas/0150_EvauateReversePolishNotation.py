# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificacion: La lista de tokens se recorrera una sola vez y la pila almacena como máximo n números.
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pila = []
        
        for e in tokens:
            if e == '+':
                b = pila.pop()
                a = pila.pop()
                pila.append(a + b)
            elif e == '-':
                b = pila.pop()
                a = pila.pop()
                pila.append(a - b)
            elif e == '*':
                b = pila.pop()
                a = pila.pop()
                pila.append(a * b)
            elif e == '/':
                b = pila.pop()
                a = pila.pop()
                pila.append(int(a / b))
            else:
                pila.append(int(e))   
        return pila[0]
