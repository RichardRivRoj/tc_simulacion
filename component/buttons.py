from fasthtml.common import *

def calculation_button(icon, title, subtitle, bg_color, text_color, dir):
    return A(
        Div(icon, cls="text-4xl"),
        Div(
            Div(title, cls="text-lg font-bold"),
            Div(subtitle, cls="text-sm text-gray-600"),
            cls="flex flex-col justify-center"
        ),
        cls=f"flex items-center space-x-4 {bg_color} {text_color} p-4 rounded-md shadow",
        href=f'{dir}'
    )