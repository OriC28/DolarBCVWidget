import requests
import http
import json

"""
This module provides functionality to fetch the current price of the dollar from BCV using Dolarapi.
Functions:
    get_bcv_price(): Fetches the current dollar price from the BCV via an API request.
Dependencies:
    - requests: For making HTTP requests.
    - http: For HTTP status codes.
    - json: For parsing JSON responses.
"""


def get_bcv_price():
    """Make a request to Dolarapi to obtain the current price of the dollar in BCV."""
    response = requests.get("https://ve.dolarapi.com/v1/dolares")
    if response.status_code == 200:
        content = json.loads(response.content)
        return {'price': content[0]['promedio'], 'status': http.HTTPStatus.OK}
    return {'error': 'No se pudo obtener el precio del dólar.', 'status': http.HTTPStatus.NOT_FOUND}
