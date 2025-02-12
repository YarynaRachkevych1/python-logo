import lark.exceptions
from lark import Lark, Transformer, v_args

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

_LOGO_GRAMMAR = """
start: command+
?command: hideturtle | showturtle | penup | pendown
    | setpencolor | setpensize | print
    | forward | backward | left | right
    | repeat | if_command | make | list_operations | func_def | func_call
    | setpos

number: NUMBER
var_name: /[a-zA-Z_-]+/
func_name: /[a-zA-Z_-]+/
color: /[a-zA-Z_-]+/
variable: ":" var_name

?logic_expr: compare_expr
            | "AND" "[" (logic_expr)* "]" -> logic_and
            | "OR" "[" (logic_expr)* "]" -> logic_or
            | "NOT" "[" logic_expr "]" -> logic_not
?compare_expr: expr
            | expr ">" expr -> greater
            | expr ">=" expr -> greater_equal
            | expr "<" expr -> less
            | expr "<=" expr -> less_equal
            | expr "=" expr -> equal
            | expr "<>" expr -> not_equal
?expr: term
    | expr "+" term -> add
    | expr "-" term -> sub
?term: power
    | term "*" power -> mul
    | term "/" power -> div
?power: factor
    | power "^" factor -> pow
?factor: atom
    | "-" factor -> neg
    | "(" expr ")"
?atom: number
    | variable
    | list_get | list_len | list_empty

?list_operations : list_make | list_empty | list_len | list_set
                | list_get | list_insert | list_remove | list_remove_value

hideturtle: "hideturtle" | "ht"
showturtle: "showturtle" | "st"
setpos: "setpos" term term
penup: "penup" | "pu"
pendown: "pendown" | "pd"
setpencolor: "setpencolor" color
setpensize: "setpensize" expr
print: "print" "[" logic_expr "]"

forward: ("forward" | "fd") expr
backward: ("backward" | "bk") expr
left: ("left" | "lt") expr
right: ("right" | "rt") expr

repeat: "repeat" expr "[" command+ "]"

if_command: "if" (true | false | logic_expr) "[" command+ "]" \
            ((else_command) "[" command+ "]")?
else_command: "else"
true: "true" | "True"
false: "false" | "False"

make: "make" var_name logic_expr
list_make: "list" var_name "[" logic_expr* "]"
list_set: "set" variable number expr
list_get: "get" variable expr
list_insert: "insert" variable number expr
list_remove: "remove" variable number
list_remove_value: "remove_value" variable logic_expr
list_len: "len" variable
list_empty: "empty" variable
func_def: "to" func_name arguments command+ "end"
func_call: func_name (expr)*

arguments: (variable)*

%import common.NUMBER
%import common.WS
%ignore WS
"""


class _LogoJsonTransformer(Transformer):
    """Transforms Logo language code into JSON format."""

    def start(self, items: list) -> dict:
        return {"tokens": items}

    @v_args(inline=True)
    def number(self, value: str) -> float:
        return float(value)

    @v_args(inline=True)
    def var_name(self, value: str) -> str:
        return str(value)

    @v_args(inline=True)
    def func_name(self, value: str) -> str:
        return str(value)

    @v_args(inline=True)
    def color(self, value: str) -> str:
        return str(value)

    @v_args(inline=True)
    def variable(self, value: str) -> str:
        return str(value)

    def add(self, items: list) -> dict:
        return {"op": "+", "left": items[0], "right": items[1]}

    def sub(self, items: list) -> dict:
        return {"op": "-", "left": items[0], "right": items[1]}

    def mul(self, items: list) -> dict:
        return {"op": "*", "left": items[0], "right": items[1]}

    def div(self, items: list) -> dict:
        return {"op": "/", "left": items[0], "right": items[1]}

    def pow(self, items: list) -> dict:
        return {"op": "^", "left": items[0], "right": items[1]}

    def neg(self, items: list) -> dict:
        return {"op": "neg", "value": items[0]}

    def greater(self, items: list) -> dict:
        return {"op": ">", "left": items[0], "right": items[1]}

    def greater_equal(self, items: list) -> dict:
        return {"op": ">=", "left": items[0], "right": items[1]}

    def less(self, items: list) -> dict:
        return {"op": "<", "left": items[0], "right": items[1]}

    def less_equal(self, items: list) -> dict:
        return {"op": "<=", "left": items[0], "right": items[1]}

    def equal(self, items: list) -> dict:
        return {"op": "=", "left": items[0], "right": items[1]}

    def not_equal(self, items: list) -> dict:
        return {"op": "<>", "left": items[0], "right": items[1]}

    def logic_and(self, items: list) -> dict:
        return {"op": "and", "list": items[0:]}

    def logic_or(self, items: list) -> dict:
        return {"op": "or", "list": items[0:]}

    def logic_not(self, items: list) -> dict:
        return {"op": "not", "expr": items[0]}

    def hideturtle(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "hideturtle"}

    def showturtle(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "showturtle"}

    def setpos(self, items: list) -> dict:
        return {"name": "setpos", "x": items[0], "y": items[1]}

    def penup(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "penup"}

    def pendown(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "pendown"}

    def setpencolor(self, items: list) -> dict:
        return {"name": "setpencolor", "color": items[0]}

    def setpensize(self, items: list) -> dict:
        return {"name": "setpensize", "value": items[0]}

    def print(self, items: list) -> dict:
        return {"name": "print", "value": items[0]}

    def forward(self, items: list) -> dict:
        return {"name": "forward", "value": items[0]}

    def backward(self, items: list) -> dict:
        return {"name": "backward", "value": items[0]}

    def left(self, items: list) -> dict:
        return {"name": "left", "value": items[0]}

    def right(self, items: list) -> dict:
        return {"name": "right", "value": items[0]}

    def repeat(self, items: list) -> dict:
        return {"name": "repeat", "value": items[0], "commands": items[1:]}

    def if_command(self, items: list) -> dict:
        condition = items[0]
        if "else" in items:
            separator_index = items.index("else")
            commands = items[1:separator_index]
            else_commands = items[separator_index + 1 :]
        else:
            commands = items[1:]
            else_commands = []
        return {
            "name": "if",
            "condition": condition,
            "commands": commands,
            "else_commands": else_commands,
        }

    def else_command(self, items: list) -> str:  # noqa: ARG002
        return "else"

    def true(self, items: list) -> str:  # noqa: ARG002
        return "true"

    def false(self, items: list) -> str:  # noqa: ARG002
        return "false"

    def arguments(self, items: list) -> str:
        return items

    def make(self, items: list) -> dict:
        return {"name": "make", "var_name": items[0], "value": items[1]}

    def list_make(self, items: list) -> dict:
        xs = "empty" if len(items) <= 1 else items[1:]
        return {"name": "list_make", "list_name": items[0], "list": xs}

    def list_len(self, items: list) -> dict:
        return {"name": "list", "function": "len", "list_name": items[0]}

    def list_empty(self, items: list) -> dict:
        return {"name": "list", "function": "empty", "list_name": items[0]}

    def list_get(self, items: list) -> dict:
        return {
            "name": "list",
            "function": "get",
            "list_name": items[0],
            "index": items[1],
        }

    def list_set(self, items: list) -> dict:
        return {
            "name": "list",
            "function": "set",
            "list_name": items[0],
            "index": items[1],
            "value": items[2],
        }

    def list_insert(self, items: list) -> dict:
        return {
            "name": "list",
            "function": "insert",
            "list_name": items[0],
            "index": items[1],
            "value": items[2],
        }

    def list_remove(self, items: list) -> dict:
        return {
            "name": "list",
            "function": "remove",
            "list_name": items[0],
            "index": items[1],
        }

    def list_remove_value(self, items: list) -> dict:
        return {
            "name": "list",
            "function": "remove_value",
            "list_name": items[0],
            "value": items[1],
        }

    def func_def(self, items: list) -> dict:
        return {
            "name": "func_def",
            "func_name": items[0],
            "arguments": items[1],
            "commands": items[2:],
        }

    def func_call(self, items: list) -> dict:
        return {"name": "func_call", "func_name": items[0], "arguments": items[1:]}


def parse(code: str) -> dict:
    """Parses the given Logo code and returns its JSON representation.

    Args:
        code (str): The Logo code to be parsed.

    Returns:
        dict: Code tree representation in JSON format.
    """
    code = code.strip()
    if code == "":
        return {"tokens": []}

    parser = Lark(_LOGO_GRAMMAR, parser="lalr", transformer=_LogoJsonTransformer())

    try:
        return parser.parse(code)
    except lark.exceptions.UnexpectedCharacters as err:
        raise ParserInvalidCommandError from err
    except lark.exceptions.UnexpectedToken as err:
        raise ParserUnexpectedTokenError from err
