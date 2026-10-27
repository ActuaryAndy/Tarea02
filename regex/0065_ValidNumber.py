import re

class Solution:
    def isNumber(self, s):
        # Usamos re.match con $ al final para simular fullmatch en versiones anteriores de Python
        patron = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"
        return bool(re.match(patron, s))

