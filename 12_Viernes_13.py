#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.

from datetime import datetime


def es_viernes(anio: int, mes: int):
    fecha = datetime.date(anio, mes, 13)
    return fecha.weekday() == 4


print(es_viernes(2023, 3))
