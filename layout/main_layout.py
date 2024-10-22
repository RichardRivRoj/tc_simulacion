from fasthtml.common import *
from component.buttons import calculation_button

def main_layout():
    return Div(
        Div(
            "CALCULADORA DE TEORÍA DE COLAS", 
            cls="bg-[#0a5cb8] text-white font-bold py-4 px-6 rounded text-center text-[20px]"
        ),
        Div(
            # Fila de cálculos simples
            Div(
                Div("SIMPLE", cls="bg-[#2174d4] text-white text-center py-4 rounded-t-md font-bold"),
                    Div(
                        calculation_button("ℹ️", "M/M/1", "Población infinita canal simple", "bg-white", "text-black", "/calcularmm1"),
                        calculation_button("ℹ️", "M/M/1/DG/K/∞", "Población finita canal simple", "bg-white", "text-black", "/calcularmm1k"),
                        cls="grid grid-cols-2 gap-2"
                    ),
                cls="rounded-md overflow-hidden"
            ),
            # Fila de cálculos múltiples
            Div(
                Div("MULTIPLE", cls="bg-[#2174d4] text-white text-center py-4 rounded-t-md font-bold"),
                    Div(
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "#"),
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "#"),
                        cls="grid grid-cols-2 gap-2"
                    ),
                cls="rounded-md overflow-hidden mt-4"
            ),
            cls="space-y-4 mt-6"
        ),
        cls="container mx-auto p-6"
    )