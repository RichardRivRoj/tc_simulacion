from fasthtml.common import *
from components.card import card
from layouts.guest_layout import guest_layout


def calc_mmsk():
    # Vista Calculadora M/M/1: Permite introducir las variables para calcular M/M/1
    form = card(
        Form(
            Label("λ Tasa de llegada: ", Input(name="v_lambda", type="number", cls="flex rounded-md border mt-4 p-2", min=0.0001, required=True), cls="block font-medium text-black text-lg"),
            Label("μ Tasa de servicio: ", Input(name="v_mu", type="number", cls="flex rounded-md border mt-4 p-2", min=0.0001, required=True), cls="block font-medium text-black text-lg"),
            Label("c Número de servidores: ", Input(name="v_c", type="number", cls="flex rounded-md border mt-2 p-2", min=1, required=True), cls="block font-medium text-black text-lg mx-8"),
            Label("K Limite: ", Input(name="v_k", type="number", cls="flex rounded-md border mt-2 p-2", min=1, required=True), cls="block font-medium text-black text-lg mx-8"),
            Button("Calcular", type="submit", hx_post='/result_mmsk', hx_target='#response', cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"),
            action = '/result_mmsk',
            method="POST",
            cls="flex flex-col items-center gap-4 p-4"
        ),
        title="Calcular M/M/c/DG/K/∞",
        c="max-h-1/2"
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
        title="Calculadora M/M/c/DG/K/∞"
    )