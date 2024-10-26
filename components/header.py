from fasthtml import FastHTML
from fasthtml.common import *

def header():
    return Header(
        Nav(
            Div(
                A(
                    # Editar el logo para evitar margenes negativos
                    Img(src="static/img/logo_white.svg", alt="logo", cls="h-16 -mt-2 -mb-3"),
                    href="/"
                ),
                Div(
                    Ul(
                        Li(A("Inicio", href="/", cls="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0")),
                        Li(A("Calculadora", href="#", cls="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0")),
                        Li(A("Ayuda", href="#", cls="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0")),
                        id="navbar-default",
                        cls="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white"
                    ),
                    cls="w-full md:block md:w-auto"
                ),
            cls="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
            ),
            cls="bg-white border-b border-gray-200"
        ),
        cls="w-full"
    )