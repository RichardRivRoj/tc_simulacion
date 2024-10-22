from fasthtml.common import *
from component.table import tabla_resultado
import json

def resultado_mm1(v_lambda: float, v_mu: float):
    v_rho = v_lambda / v_mu
    v_po = (1 - v_rho)
    v_ls = v_rho /(1 - v_rho)
    v_lq = (v_rho**2) / (1 - v_rho)
    v_ws = v_ls / v_lambda
    v_wq = v_lq / v_lambda
    
    n = 0
    v_pn_temp = 1
    fn_acumulado = 0

    resultados = []

    # Calcular n y almacenar los resultados
    while v_pn_temp > 0:
        v_pn_temp = round(v_po * (v_rho**n), 4)
        if v_pn_temp > 0:
            fn_acumulado += v_pn_temp
            resultados.append({
                'n': n,
                'Pn': v_pn_temp,
                'Fn': round(fn_acumulado, 4)
            })
            n += 1
            
    x_data = [fila['n'] for fila in resultados]
    y_data = [fila['Pn'] for fila in resultados]
    title = f"Gráfica de M/M/1/ (λ={v_lambda}, μ={v_mu})"
    x_label = "n"
    x_label = str(x_label)
    y_label = "Pn"
    y_label = str(y_label)
    fn_values = [fila['Fn'] for fila in resultados]
        

    # Generar la tabla con FastHTML
    return Div(
        Div(
            H2("Resultados M/M/1", cls="text-xl font-bold text-lg"),
            cls="bg-blue-600 text-white text-center py-4 rounded-t-md min-w-full",
            ),
        Div(
            Div(
                P(f"Factor de Utilización (ρ): {v_rho:.4f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md border max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Probabilidad de que el servidor esté ocupado (Po): {v_po:.4f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Número esperado de clientes en el sistema (Ls): {v_ls:.2f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md border max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Número esperado de clientes en la cola (Lq): {v_lq:.2f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Tiempo esperado en el sistema por cliente (Ws): {v_ws:.2f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Tiempo esperado en la cola (Wq): {v_wq:.2f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mt-4"
            ),
            Div(cls="mt-6"),
            tabla_resultado(
                headers=['n', 'Pn', 'Fn'],
                data=resultados
            ),
            Div(
                A('Volver', href='/', cls="text-white"),
                cls="mt-4 bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg px-5 py-2.5 text-center"
            ),
            cls="p-12 mb-8 bg-white border border-gray-200 shadow space-y-8"
        ),
        Div(
        Form(
            H1("Resultados M/M/1/K"),
            Input(type="hidden", name="x_data", value=json.dumps(x_data)),
            Input(type="hidden", name="y_data", value=json.dumps(y_data)),
            Input(type="hidden", name="title", value=title),
            Input(type="hidden", name="x_label", value=x_label),
            Input(type="hidden", name="y_label", value=y_label),
            Button("Cargar Gráfica", type="submit",
                cls="bg-blue-500 text-white p-2 rounded",
                hx_post="/grafica",  # Realiza una solicitud POST
                hx_target="#grafica-container",  # Contenedor donde se cargará el HTML
                hx_swap="innerHTML",  # Reemplazar el contenido del contenedor
            ),
            action='/grafica',
            method="POST",
            cls="flex flex-col items-center space-y-10 pb-12"
        ),
        Div(id="grafica-container", cls="mt-4"),
        cls="flex flex-col items-center rounded-bl-lg rounded-br-lg space-y-0 pb-12"
        ),    
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
    

        Para implementar despues
        Div(
            Div(
                cls="graph", _inner_html=grafica_fn # Ancho al 50% y espaciado
            ),
            Div(
                cls="graph", _inner_html=grafica_pn # Ancho al 50% y espaciado
            ),
            cls="flex justify-between items-center"  # Organiza las gráficas de manera horizontal
        ),
        cls="p-6 bg-white border border-gray-200 rounded-lg shadow space-y-10"
    """