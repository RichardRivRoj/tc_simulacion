from fasthtml.common import *
from layouts.guest_layout import guest_layout
from components.card import card

def calc_mms():
    # Vista Calculadora M/M/1: Permite introducir las variables para calcular M/M/1
    form = card(
        Form(
            Label("λ Tasa de llegada: ", Input(name="v_lambda", type="number", cls="flex rounded-md border mt-4 p-2", min=0.0001, required=True, hx_validate=True), cls="block font-medium text-black text-lg"),
            Label("μ Tasa de servicio: ", Input(name="v_mu", type="number", cls="flex rounded-md border mt-4 p-2", min=0.0001, required=True, hx_validate=True), cls="block font-medium text-black text-lg"),
            Label("c Número de servidores: ", Input(name="v_c", type="number", cls="flex rounded-md border mt-4 p-2", min=0.0001, required=True, hx_validate=True), cls="block font-medium text-black text-lg"),
            Button("Calcular", type="submit", hx_post='/result_mms', hx_target='#response', cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"),
            action = '/result_mms',
            method="POST",
            cls="flex flex-col items-center gap-4 p-4"
        ),
        title="Calcular M/M/c",
        c="max-h-1/3"
    )
    
    return guest_layout(
            Div(
                Div(
                form,
                Div(id="response"),
                cls="flex flex-row justify-center space-x-4 p-8"
            ),
            Div(
                Div(id="graph_pn"),
                Div(id="graph_fn"),
                cls="flex flex-row justify-center space-x-4 p-8"
            ),
            cls="w-full"
        ),
        title="Calculadora M/M/c"
    )