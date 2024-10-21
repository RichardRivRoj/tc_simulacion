from fasthtml import FastHTML
from fasthtml.common import *
from component.header import header
from component.footer import footer
from layout.main_layout import main_layout

app, rt = fast_app()

@rt("/")
def index():
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

@rt("/calcularmm1", methods=["GET"])
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
        cls="p-12 bg-white border border-gray-200 rounded-lg shadow"
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

@rt("/result_MM1", methods=["POST"])
def resultado(tasa_llegada : float, tasa_servicio : float, servidores : int):
    
    # Cálculos de teoría de colas
    rho = tasa_llegada / (servidores * tasa_servicio)
    vacio = (1 - rho)
    
    resultado = Div(
        Div(f"Factor de utilización (rho): {rho:.2f}", cls="text-lg text-green-500"), 
        H2(f"Factor que el servidor este vacio P0: {vacio:.2f}", cls="text-lg text-green-500"),
        Div(
            A('Volver', href='/', cls="text-red-300")
        )
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
                        resultado,
                        cls="container mx-auto p-6 flex-grow"
                    ), 
            footer(),
            cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )
    

serve()