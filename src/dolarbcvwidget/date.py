from datetime import datetime
from unidecode import unidecode
import locale

"""
This module provides a function to obtain the current date formatted in Spanish.
Functions:
    get_datetime_current():
        Returns the current date as a string in Spanish locale, formatted as
        "Day, DD de Month de YYYY". If the Spanish locale cannot be set, it
        prints a warning and falls back to the system's default locale.
"""


def get_datetime_current():
    """Return the current date in Spanish."""
    try:
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, "Spanish_Spain")
        except locale.Error:
            print(
                "Advertencia: No se pudo establecer la configuración regional a español.")

    now = datetime.now()
    spanish_date = now.strftime("%A, %d de %B de %Y")
    return unidecode(spanish_date.capitalize())
