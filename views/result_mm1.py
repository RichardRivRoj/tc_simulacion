from fasthtml.common import *
from component.header import header
from component.footer import footer


def resultado_mm1(v_lambda: float, v_mu: float):
    v_rho = v_lambda / v_mu
    v_po = (1 - v_rho)
    v_ls = round(v_rho / v_po, 0)
    v_lq = (v_rho**2) / v_po
    v_ws = v_ls / v_lambda
    v_wq = v_lq / v_lambda

    def v_pn(n: int):
        return round(v_po*(v_rho**n), 4)

    def v_fn(n: int):
        v_pn_temp = 0
        for i in range(0, n+1):
            v_pn_temp += v_pn(i)
            print(i)
        return v_pn_temp

    def v_n():
        n = 0
        v_pn_temp = 1
        while v_pn_temp > 0:
            v_pn_temp = v_pn(n)
            if v_pn_temp > 0:
                n += 1
        return n

    # Deberia crearse una tabla, y ponerse al lado del la parte de la calculadora
    return Div(
        Table(
            Tr(
                Th("n"),
                Th("Pn"),
                Th("Fn"),
            ),
            # Resolver el for
            Tr(
                Td("1"),
                Td(v_pn(0)),
                Td(v_fn(0)),
            ),
            Tr(
                Td("1"),
                Td(v_pn(1)),
                Td(v_fn(1)),
            )
        ),
        H2(f"Factor de utilización (rho): {v_rho:.4f}", cls="text-lg text-green-500"), 
        H2(f"Factor que el servidor este vacio P0: {v_po:.4f}", cls="text-lg text-green-500"),
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