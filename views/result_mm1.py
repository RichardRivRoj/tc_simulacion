from fasthtml.common import *
from component.header import header
from component.footer import footer


def resultado_mm1(tasa_llegada : float, tasa_servicio : float):
    
    # Cálculos de teoría de colas
    rho = tasa_llegada / (tasa_servicio)
    vacio = (1 - rho)
    
    return Div(
        H2(f"Factor de utilización (rho): {rho:.4f}", cls="text-lg text-green-500"), 
        H2(f"Factor que el servidor este vacio P0: {vacio:.4f}", cls="text-lg text-green-500"),
        Div(
            A('Volver', href='/', cls="text-red-300")
        ),
        cls="p-6 bg-white border border-gray-200 rounded-lg shadow space-y-10"
    )
    
    """
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
    """