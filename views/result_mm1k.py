from fasthtml.common import *
from fastapi.responses import HTMLResponse
from component.header import header
from component.footer import footer
from component.table import tabla_resultado
from component.graficas import crear_grafica
import numpy as np
import math

def resultado_mm1k(v_lambda: float, v_mu: float, v_k : int):
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
    
    n_values = [fila['n'] for fila in resultados]
    pn_values = [fila['Pn'] for fila in resultados]
    fn_values = [fila['Fn'] for fila in resultados]
    
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
    

    # Calcular n y almacenar los resultados
    
    
    grafica_pn = crear_grafica(n_values, pn_values, "n vs Pn", "n", "Pn")
    grafica_fn = crear_grafica(n_values, fn_values, "n vs Fn", "n", "Fn")

    # Generar la tabla con FastHTML
    return Div(
        Div(
            H2("Resultados M/M/1/DG/K/∞", cls="text-xl font-bold text-lg"),
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
                P(f"Factor de Utilización (pk): {v_pk:.4f}", cls="text-[16px] font-semibold text-black"),
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
            Div(
                P(f"Tasa efectiva de llegada (λefec): {v_lambda_efec:.2f}", cls="text-[16px] font-semibold text-black"),
                cls="bg-white p-4 rounded-lg shadow-md max-w-md mx-auto mt-4"
            ),
            Div(
                P(f"Pérdida de llegadas (λPl): {v_lambda_pn:.4f}", cls="text-[16px] font-semibold text-black"),
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
        cls="flex flex-col items-center rounded-bl-lg rounded-br-lg space-y-0 pb-12"
    )