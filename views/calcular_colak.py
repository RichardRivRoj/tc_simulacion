from fasthtml.common import *
from component.header import header
from component.footer import footer


def calcular_colak():
    # Vista Calculadora M/M/1: Permite introducir las variables para calcular M/M/1
    form = Div(
        Form(
            Div(
                H2("M/M/1/DG/K/∞", cls="text-xl font-bold text-lg"),
                cls="bg-blue-600 text-white text-center py-2 rounded-t-md min-w-full",
            ),
            Label("λ Tasa de llegada: ", Input(name="v_lambda", type="number", min=0.0001, cls="flex rounded-md border mt-2 p-2", required=True), cls="block font-medium text-black text-lg mx-8"),
            Label("μ Tasa de servicio: ", Input(name="v_mu", type="number", min=0.0001, cls="flex rounded-md border mt-2 p-2", required=True), cls="block font-medium text-black text-lg mx-8"),
            Label("K Capacidad máxima del sistema: ", Input(name="v_k", type="number", min=1,cls="flex rounded-md border mt-2 p-2", required=True), cls="block font-medium text-black text-lg mx-8"),
            Button("Calcular", type="submit", hx_post='/result_MM1K', hx_target='#response', cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"),
            action = '/result_MM1K',
            method="POST",
            cls="flex flex-col items-center space-y-10 pb-12"
        ),
        cls="overflow-hidden mb-auto bg-white border border-gray-200 rounded-lg shadow"
    )
    
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Link(rel="icon", type="image/ico", href="static/img/icono_linesim.ico"),
            Script(src="https://unpkg.com/htmx.org@1.5.0"),
            Script(src="https://cdn.plot.ly/plotly-latest.min.js"),
            Title("Calculadora de Teoria de Colas")
        ),
        Body(
            Div(
                header(),
                    Div(
                        Div(
                            form,
                            cls="flex mx-auto p-8 max-w-sm"
                        ),
                        Div(
                            id="response",
                            cls="flex mx-auto p-8"
                        ),
                        cls="flex flex-row"
                    ), 
                footer(),
                cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )