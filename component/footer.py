from fasthtml import FastHTML
from fasthtml.common import *

def footer():
    return Footer(
        Div(
            'Repositotio de GITHUB u otra informacion de interes de los autores del software',
            cls="bg-blue-600 text-white text-center py-2"
        ),
        cls="fixed bottom-0 left-0 z-50 w-full",
    )