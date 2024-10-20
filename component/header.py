from fasthtml import FastHTML
from fasthtml.common import *

def header():
    return Div(
        Header(
            Div("LOGO", cls="bg-blue-600 text-white px-4 py-2 rounded-full font-bold"),
            Nav(
                Ul(
                    Li(A("Inicio", href="/", cls="text-lg hover:text-blue-600 font-semibold")),
                    Li(A("Calculadora", href="#", cls="text-lg hover:text-blue-600 font-semibold")),
                    Li(A("Ayuda", href="#", cls="text-lg hover:text-blue-600 font-semibold")),
                    cls="flex space-x-16"
                ),
                cls="flex items-center space-x-8 pr-8"
            ),
            cls="flex justify-between items-center p-6 shadow"
        ),
        cls="w-full"
    )