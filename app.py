from fasthtml import FastHTML
from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def index():
    # Crear el formulario directamente con clases de Python
    form = Form(
        Label("Tasa de llegada: ", Input(name="tasa_llegada", type="number", cls="border p-2")),
        Div("Tasa de servicio: ", Input(name="tasa_servicio", type="number", cls="border p-2")),
        Div("Servidores: ", Input(name="servidores", type="number", cls="border p-2")),
        Button("Calcular", type="submit", cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"),
        action = '/calcular',
        method="POST",
        cls= "space-y-4"
    )
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Calculadora de Teoria de Colas")
        ),
        Body(
            Div(
                form,
                cls="container mx-auto p-6"
            ) 
        ),      
    )

@rt("/calcular", methods=["POST"])
def calcular_cola(tasa_llegada : float, tasa_servicio : float, servidores : int):
    
    # Cálculos de teoría de colas
    rho = tasa_llegada / (servidores * tasa_servicio)
    vacio = (1 - rho)
    
    # Mostrar resultado
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
                resultado,
                cls="container mx-auto p-6"
            ) 
        ),      
    )

serve()