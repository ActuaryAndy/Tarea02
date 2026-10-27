# Complejidad temporal: O(n)
# Complejidad espacial: O(1)
# Justificación: n es la longitud de la cadena s, 
# la cual se evalúa de forma lineal con la expresión regular utilizando un espacio auxiliar constante.
import re

class Solution:
    def isNumber(self, s):
       
        patron = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"
        return bool(re.match(patron, s))

