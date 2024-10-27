from fasthtml import FastHTML
from fasthtml.common import *


def footer():
    return Footer(
        Div(
            Div(
                A(
                    Img(src="static/img/github.svg", alt="logo", cls="h-6 mr-2"),
                    'Repositorio del proyecto', href='https://github.com/RichardRivRoj/tc_simulacion',
                    cls="flex items-center font-bold"
                ),
                Div(
                    P('Desarrolladores:', cls='font-semibold'),
                    P('Rodrigo Oliveira'),
                    P('Richard Rivera'),
                    P('Sahenndry Carreño'),
                    cls="flex flex-col items-center mt-4"
                ),
                cls="flex flex-col items-center mt-2"
            ),
            cls="flex justify-center items-center bg-primary-variant text-white text-center py-2"
        ),
        cls="bottom-0 left-0 z-70 w-full",
    )
