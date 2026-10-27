# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: n es la longitud de la cadena de la expresión, 
# la cual se procesa linealmente extrayendo los tokens en una lista que consume espacio proporcional a la entrada.
import re

class Solution:

  def fractionAddition(self, expression):
    def mcd(a, b):
      return a if b == 0 else mcd(b, a % b)

    tokens = re.findall(r'[+-]?\d+/\d+', expression)

    num_resultado = 0
    den_resultado = 1

    for token in tokens:
      partes = re.split(r'/', token)
      numerador = int(partes[0])
      denominador = int(partes[1])

      num_resultado = (
          num_resultado * denominador + numerador * den_resultado
      )
      den_resultado = den_resultado * denominador

      divisor = mcd(abs(num_resultado), den_resultado)
      num_resultado //= divisor
      den_resultado //= divisor

    return '{}/{}'.format(num_resultado, den_resultado)
