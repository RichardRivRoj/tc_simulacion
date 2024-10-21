from fasthtml import FastHTML
from fasthtml.common import *
from component.header import header
from component.footer import footer
from component.main import main_layout

app, rt = fast_app()

@rt("/")
def index():
    # Crear el formulario directamente con clases de Python
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
    
    form = Form(
        Label("Tasa de llegada: ", Input(name="tasa_llegada", type="number", cls="border p-2")),
        Div("Tasa de servicio: ", Input(name="tasa_servicio", type="number", cls="border p-2")),
        Div("Servidores: ", Input(name="servidores", type="number", cls="border p-2")),
        Button("Calcular", type="submit", cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"),
        action = '/result_MM1',
        method="POST",
        cls= "pl-5 space-y-4"
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
                    cls="container mx-auto p-6 flex-grow"
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