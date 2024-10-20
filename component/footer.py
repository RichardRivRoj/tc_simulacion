from fasthtml import FastHTML
from fasthtml.common import *

def footer():
    return Footer(
        Div(
            'HECHO CON AMOR POR QUEDAMOS ',
            cls="bg-blue-600 text-white text-center py-2"
        ),
        cls="w-full",
    )