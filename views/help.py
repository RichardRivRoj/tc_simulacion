from fasthtml.common import *
from layouts.guest_layout import guest_layout

def help():
    # Vista Principal: Muestra las opciones que se pueden calcular
    return guest_layout(
        Div(
            H2(
                "Ayudas", 
                cls="bg-primary-variant text-white font-bold p-4 rounded text-center text-base"
            ),
            Div(
                Div(
                    "⚠️ En desarrollo",
                    cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-2",
                ),
                cls="space-y-8 my-8"
            ),
            cls="container mx-auto py-6 px-16 min-h-screen flex flex-col"
        ),
        title="Inicio"
    )
