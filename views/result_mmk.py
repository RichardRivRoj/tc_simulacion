from fasthtml.common import *
from components.card import card
from components.result_box import result_box
from components.table import tabla_resultado
import json

def result_mmk(v_lambda: float, v_mu: float, v_k: int):
    n = 0
    v_pn_temp = 1
    fn_acumulado = 0
    
    # Calculo de rho
    v_rho = v_lambda / v_mu
    
    # Calculo de Po
    if v_rho == 1:
        v_po = 1 / (v_k + 1)
    else:
        v_po = (1 - v_rho) / (1-(v_rho**(v_k+1)))
        
    # Calculo de Pn
    resultados = []
    # Ciclo para calcular Pn para cada valor de n (hasta K)
    while n <= v_k:
        # Cálculo de Pn utilizando la fórmula
        v_pn_temp = round(((v_rho**n) * v_po), 4)
        
        # Acumulamos la función de distribución acumulada Fn
        fn_acumulado += v_pn_temp
        
        # Guardamos los resultados en la lista
        resultados.append({
            'n': n,
            'Pn': v_pn_temp,
            'Fn': round(fn_acumulado, 4)
        })
        
        # Incrementamos n para la siguiente iteración
        n += 1
    
    x_data = [fila['n'] for fila in resultados]
    y_data = [fila['Pn'] for fila in resultados]
    title = f"Gráfica de M/M/1/K/DG/∞ (λ={v_lambda}, μ={v_mu}, k={v_k})"
    x_label = str("n")
    y_label = str("Pn")
    y_label2 = str("Fn")
    
    y_data2 = [fila['Fn'] for fila in resultados]
    
    # Calculo de Ls
    v_ls = 0
    for fila in resultados:
        v_ls += fila['n'] * fila['Pn']
    
    # Calculo de pk
    v_pk = 0
    for n in range(v_k + 1):
        for fila in resultados:
            v_pk = fila['Pn']
    
    # Calculo de tasa de efectividad
    v_lambda_efec = v_lambda*(1 - v_pk)
    
    #Calculo de lambdaPn
    v_lambda_pn = v_lambda - v_lambda_efec
    
    # Calculo de Lq
    v_lq = v_ls - (v_lambda_efec/v_mu)
    
    # Calculo de Ws
    v_ws = v_ls / (v_lambda * (1 - v_pk))
    
    # Calculo de Wq
    v_wq = v_lq / (v_lambda * (1 - v_pk))

    graph_pn = Form(
        Input(type="hidden", name="x_data", value=json.dumps(x_data)),
        Input(type="hidden", name="y_data", value=json.dumps(y_data)),
        Input(type="hidden", name="title", value=title),
        Input(type="hidden", name="x_label", value=x_label),
        Input(type="hidden", name="y_label", value=y_label),
        Button("Gráfica M/M/k n x Pn", type="submit",
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
        Button("Gráfica M/M/k n x Fn", type="submit",
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
                Div(
                    result_box("Tasa efectiva de llegada (λefec)", f"{v_lambda_efec:.2f}"),
                    result_box("Pérdida de llegadas (λPl)", f"{v_lambda_pn:.4f}"),
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
                A('Volver', href='/calc_mmk', cls="text-white"),
                cls="w-1/2 text-center focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5"
            ),
            cls="flex flex-col items-center gap-4 p-4"
        ),
        title="Resultados M/M/1/DG/K/∞",
    )

    # Generar la tabla con FastHTML
    return result