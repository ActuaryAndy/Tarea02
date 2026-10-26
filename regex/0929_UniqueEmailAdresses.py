import re


class Solution(object):

  def numUniqueEmails(self, emails):
    correos_unicos = set()

    for correo in emails:
      # 1. Separar el correo usando split y guardarlo en una lista llamada 'partes'
      partes = correo.split("@")

      # 2. Asignar cada parte usando su índice numérico (nombre local y dominio)
      nombre_local = partes[0]
      dominio = partes[1]

      # 3. Descartar el signo más '+' y todo lo que le sigue
      nombre_local = re.sub(r"\+.*", "", nombre_local)

      # 4. Eliminar todos los puntos '.' del nombre local
      nombre_local = re.sub(r"\.", "", nombre_local)

      # 5. Unir el correo limpio y agregarlo al conjunto
      correo_normalizado = nombre_local + "@" + dominio
      correos_unicos.add(correo_normalizado)

    return len(correos_unicos)
