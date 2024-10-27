from fasthtml.common import *
from components.card import card
from components.result_box import result_box
from components.table import tabla_resultado
import json
import math
from scipy.special import factorial

def result_mms(v_lambda: float, v_mu: float, v_c : int):
   
    n = 0
    v_pn_temp = 1
    fn_acumulado = 0
   
    v_rho = v_lambda / v_mu
    
    # Calcular P0
    sumatoria = sum((v_lambda/v_mu) ** n / factorial(n) for n in range(v_c))
    v_po = 1 / (sumatoria + ((v_lambda/v_mu) ** v_c / (factorial(v_c) * (1 - (v_rho/ v_c)))))
    
    resultados = []

    # Calcular n y almacenar los resultados
    while v_pn_temp > 0:
        if 0 <= n <= v_c:
            v_pn_temp = round(((v_lambda / v_mu) ** n / factorial(n)) * v_po, 4)
            print(v_pn_temp)
        else:
            v_pn_temp = round(((v_lambda / v_mu) ** n / (factorial(v_c) * v_c ** (n - v_c))) * v_po, 4)
            print(v_pn_temp)
        if v_pn_temp > 0:
            fn_acumulado += v_pn_temp
            resultados.append({
                'n': n,
                'Pn': v_pn_temp,
                'Fn': round(fn_acumulado, 4)
            })
            n += 1
    
    v_lq = ((v_lambda / v_mu) ** (v_c + 1)) / (factorial(v_c - 1) * (v_c - v_rho) ** 2) * v_po
    v_ls = v_lq + (v_lambda / v_mu)
    v_wq = v_lq / v_lambda
    v_ws = v_wq + (1 / v_mu)
    #v_pw = ((v_lambda / v_mu) ** v_c / (factorial(v_c) * (1 - v_rho))) * v_po
            
    x_data = [fila['n'] for fila in resultados]
    y_data = [fila['Pn'] for fila in resultados]
    title = f"Gráfica de M/M/c (λ={v_lambda}, μ={v_mu}, c={v_c})"
    x_label = "n"
    x_label = str(x_label)
    y_label = "Pn"
    y_label = str(y_label)
    y_label2 = str("Fn")
    y_data2 = [fila['Fn'] for fila in resultados]

    graph_pn = Form(
        Input(type="hidden", name="x_data", value=json.dumps(x_data)),
        Input(type="hidden", name="y_data", value=json.dumps(y_data)),
        Input(type="hidden", name="title", value=title),
        Input(type="hidden", name="x_label", value=x_label),
        Input(type="hidden", name="y_label", value=y_label),
        Button("Gráfica M/M/c n x Pn", type="submit",
            cls="text-center focus:outline-none text-white bg-blue-500 hover:bg-blue-600 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5",
            hx_post="/graph",  # Realiza una solicitud POST
            hx_target="#graph_pn",  # Contenedor donde se cargará el HTML
            hx_swap="innerHTML",  # Reemplazar el contenido del contenedor
        ),
        action='/graph',
        method="POST",
    )

    graph_fn = Form(
        Input(type="hidden", name="x_data", value=json.dumps(x_data)),
        Input(type="hidden", name="y_data", value=json.dumps(y_data2)),
        Input(type="hidden", name="title", value=title),
        Input(type="hidden", name="x_label", value=x_label),
        Input(type="hidden", name="y_label", value=y_label2),
        Button("Gráfica M/M/c n x Fn", type="submit",
            cls="text-center focus:outline-none text-white bg-blue-500 hover:bg-blue-600 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5",
            hx_post="/graph",  # Realiza una solicitud POST
            hx_target="#graph_fn",  # Contenedor donde se cargará el HTML
            hx_swap="innerHTML",  # Reemplazar el contenido del contenedor
        ),
        action='/graph',
        method="POST",
    ),

    result = card(
        Div(
            Div(
                Div(
                    result_box("Factor de Utilización (ρ)", f"{v_rho:.4}"),
                    result_box("Probabilidad de que el servidor esté ocupado (Po)", f"{v_po:.4}"),
                    cls="grid grid-rows-subgrid gap-4 row-span-2"
                ),
                Div(
                    result_box("Número esperado de clientes en el sistema (Ls)", f"{v_ls:.4}"),
                    result_box("Número esperado de clientes en la cola (Lq)", f"{v_lq:.4}"),
                    cls="grid grid-rows-subgrid gap-4 row-span-2"
                ),
                Div(
                    result_box("Tiempo esperado en el sistema por cliente (Ws)", f"{v_ws:.4}"),
                    result_box("Tiempo esperado en la cola (Wq)", f"{v_wq:.4}"),
                    cls="grid grid-rows-subgrid gap-4 row-span-2"
                ),
                cls="flex flex-row items-center gap-4"
            ),
            Div(
                tabla_resultado(
                    headers=['n', 'Pn', 'Fn'],
                    data=resultados
                ),
                cls="w-1/2"
            ),
            Div(
                graph_pn,
                graph_fn,
                cls="flex flex-row space-x-4"
            ),
            Div(
                A('Volver', href='/calc_mms', cls="text-white"),
                cls="w-1/2 text-center focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5"
            ),
            cls="flex flex-col items-center gap-4 p-4"
        ),
        title="Resultado M/M/c",
    )

    # Generar la tabla con FastHTML
    return result