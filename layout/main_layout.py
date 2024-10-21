from fasthtml.common import *
from component.buttons import calculation_button

def main_layout():
    return Div(
        Div(
            "CALCULADORA DE TEORÍA DE COLAS", 
            cls="bg-blue-600 text-white font-bold py-2 px-6 rounded-full text-center"
        ),
        Div(
            # Fila de cálculos simples
            Div(
                Div("SIMPLE", cls="bg-red-600 text-white text-center py-2 rounded-t-md font-bold"),
                    Div(
                        calculation_button("ℹ️", "M/M/1", "Población infinita canal simple", "bg-white", "text-black", "/calcularmm1"),
                        calculation_button("ℹ️", "M/M/1/M/M", "Población finita canal simple", "bg-white", "text-black", "#"),
                        cls="grid grid-cols-2 gap-4"
                    ),
                cls="rounded-md overflow-hidden"
            ),
            # Fila de cálculos múltiples
            Div(
                Div("MULTIPLE", cls="bg-yellow-500 text-black text-center py-2 rounded-t-md font-bold"),
                    Div(
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "#"),
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "#"),
                        cls="grid grid-cols-2 gap-4"
                    ),
                cls="rounded-md overflow-hidden mt-4"
            ),
            cls="space-y-4 mt-6"
        ),
        cls="container mx-auto p-6"
    )