from fasthtml import FastHTML
from fasthtml.common import *

def header():
    return Div(
        Header(
            Div(
                Img(src="static/img/logo_white.svg", alt="logo", cls="w-[178px] h-[70px] mx-4 my-2"),
                cls="w-[200px] h-[70px] flex items-center"
            ),
            Nav(
                Ul(
                    Li(A("Inicio", href="/", cls="text-lg hover:text-blue-600 font-semibold")),
                    Li(A("Calculadora", href="#", cls="text-lg hover:text-blue-600 font-semibold")),
                    Li(A("Ayuda", href="#", cls="text-lg hover:text-blue-600 font-semibold")),
                    cls="flex space-x-16 mx-6"
                ),
                cls="flex items-center space-x-8 pr-6"
            ),
            cls="flex justify-between items-center shadow"
        ),
        cls="w-full"
    )