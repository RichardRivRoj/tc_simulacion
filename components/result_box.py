from fasthtml.common import *

def result_box(title, result):
    return Div(
        P(f"{title}: {result}", cls="text-base font-semibold text-black text-center"),
        cls="bg-white rounded-lg shadow-md border flex justify-center items-center h-24 px-4"
    ),