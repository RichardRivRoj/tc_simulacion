from fasthtml import FastHTML
from fasthtml.common import *

def footer():
    return Footer(
        Div(
            'HECHO CON AMOR POR QUEDAMOS ',
            cls="bg-blue-700 text—center text-white p-8")
    )