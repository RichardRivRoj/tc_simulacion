from fasthtml.common import *
from component.header import header
from component.footer import footer


def calcular_cola():
    # Vista Calculadora M/M/1: Permite introducir las variables para calcular M/M/1
    form = Div(
        Form(
            H2("M/M/1", cls="font-medium text-black text-center text-lg"),
            Label("λ Tasa de llegada: ", Input(name="tasa_llegada", type="number", cls="flex rounded-md border mt-2 px-3 py-1"), cls="block font-medium text-black"),
            Label("μ Tasa de servicio: ", Input(name="tasa_servicio", type="number", cls="flex rounded-md border mt-2 px-3 py-1"), cls="block font-medium text-black"),
            Button("Calcular", type="submit", cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"),
            action = '/result_MM1',
            method="POST",
            cls= "space-y-10"
        ),
        cls="p-6 bg-white border border-gray-200 rounded-lg shadow"
    )
    
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Calculadora de Teoria de Colas")
        ),
        Body(
            Div(
                header(),
                    Div(
                        form,
                        cls="container flex justify-center mx-auto p-6 flex-grow"
                    ), 
            footer(),
            cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )
    
