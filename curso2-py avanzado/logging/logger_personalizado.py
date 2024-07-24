import logging
# Aca se esta definiendo un logger personalizado
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Aca decimos que handler_consola va a ser un handler
handler_consola = logging.StreamHandler()
# Aca definimos el formato de los logs
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# Aca le decimos al handler como va a ser el formato
handler_consola.setFormatter(formato_logs)
# Luego se añade al logger la informacion mediante el handler
logger.addHandler(handler_consola)

# Permite generar un handler que permita manegar los files
handler_archivo = logging.FileHandler(".\curso2-py avanzado\\logging\\archivo.log")
# Hay que definir el nivel minimo a mostrar
handler_archivo.setLevel(logging.ERROR)
# Añadimos el formato al archivo
handler_archivo.setFormatter(formato_logs)
# Añadimos mediante el handler, el formato y el nivel para el file handler al logger
logger.addHandler(handler_archivo)

logger.info("registro informativo")
