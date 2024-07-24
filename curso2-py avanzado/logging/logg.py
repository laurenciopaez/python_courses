""" LOGGING """

""" 
Proceso para obtener logs del programa,
permiten entender el comportamiento del programa,
ayudan en la deteccion de errores

libreria  built-in

Niveles de Severidad:

DEBUG: informacion detallada, se usa cuando se esta desarrollando.

INFO: reporte de eventos de los cuales se quiere obtener informacion

WARNING: reporte de algo inesperado, no genera ningun error

ERROR: algo que no se pudo ejecutar

CRITICAL: reporte de un error grave. Se puede llegar a interrumpir la ejecucion de un programa
 """

import logging

logging.basicConfig(level=logging.DEBUG, filename="curso2-py avanzado\logging\ejemplo_logs.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")

logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

try:
    division = 2/0
except:
    logging.exception('Division por cero') # La exception tambien informa del error. No solo el mensaje que escribimos dentro del parentesis.