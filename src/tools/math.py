import py_expression_eval as pe
parser = pe.Parser()

def calculate(expression: str) -> int | float | None:
    """Evaluate a mathematical expression"""

    try:
        # Attempt to evaluate the math expression
        result = parser.parse(expression).evaluate({})
        return result
    except:
        # Return an error message if the math expression is invalid
        return None