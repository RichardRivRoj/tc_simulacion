from fasthtml.common import *
from layout.main_layout import main_layout
from component.header import header
from component.footer import footer


def home():
    # Vista Principal: Muestra las opciones que se pueden calcular
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Inicio")
        ),
        Body(
            Div(
                header(),
                    Div(
                        main_layout(),
                        cls="container mx-auto p-6 flex-grow"
                    ), 
                footer(),
                cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )