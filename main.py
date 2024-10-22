from fasthtml import FastHTML
from fasthtml.common import *
from views.home import home
from views.calcular_cola import calcular_cola
from views.result_mm1 import resultado_mm1
from views.calcular_colak import calcular_colak
from views.result_mm1k import resultado_mm1k

app, rt = fast_app()

# Rutas 

@rt("/")
def index():
    return home()

@rt("/calcularmm1", methods=["GET"])
def mm1():
    return calcular_cola()

@rt("/result_MM1", methods=["POST"])
def result_mm1(v_lambda : float, v_mu : float):
    return resultado_mm1(v_lambda, v_mu)

@rt("/calcularmm1k", methods=["GET"])
def mm1k():
    return calcular_colak()

@rt("/result_MM1K", methods=["POST"])
def result_mm1(v_lambda : float, v_mu : float, v_k : int):
    return resultado_mm1k(v_lambda, v_mu, v_k)

serve()