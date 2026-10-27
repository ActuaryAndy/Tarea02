# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: n es el número de elementos en la lista de correos.


import re


class Solution(object):

  def numUniqueEmails(self, emails):
    correos_unicos = set()

    for correo in emails:
      partes = correo.split("@")
      nombre_local = partes[0]
      dominio = partes[1]

      nombre_local = re.sub(r"\+.*", "", nombre_local)
      nombre_local = re.sub(r"\.", "", nombre_local)

      correo_normalizado = nombre_local + "@" + dominio
      correos_unicos.add(correo_normalizado)

    return len(correos_unicos)
  