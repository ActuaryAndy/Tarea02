# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificacion: La cadena se va recorrer una sola vez con el ciclo y la pila va a almacenar hasta n elementos.
class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                pila.append(c)
            else:
                if not pila:
                    return False
                tope = pila.pop()
                if c == ')' and tope != '(':
                    return False
                if c == ']' and tope != '[':
                    return False
                if c == '}' and tope != '{':
                    return False
        return len(pila) == 0
