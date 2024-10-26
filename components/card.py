from fasthtml.common import *

def card(content, title, c: Any = None):
    return Div(
        Div(
            H2(title, cls="text-xl font-bold text-lg"),
            cls=f"bg-primary text-white text-center py-2 rounded-t-md min-w-full",
        ),
        content,
        cls=f"bg-white border border-gray-200 rounded-lg shadow {c}"
    )