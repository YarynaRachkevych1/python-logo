import lark.exceptions
from lark import Lark, Transformer

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

_LOGO_GRAMMAR = """
start: command+
command: (no_arg_command) | (one_arg_command) \
         | (repeat) | (if_command) | (make)

showturtle: "showturtle" | "st"
hideturtle: "hideturtle" | "ht"
penup: "penup" | "pu"
pendown: "pendown" | "pd"
no_arg_command: showturtle | hideturtle | penup | pendown
forward: "forward" | "fd"
backward: "backward" | "bk"
left: "left" | "lt"
right: "right" | "rt"
one_arg_command: (forward | backward | left | right) (number | variable)
repeat: "repeat" (number | variable) "[" command+ "]"
if_command: "if" (true | false) "[" command+ "]" ((else_command) "[" command+ "]")?
make: "make" var (number | variable)
var: WORD
variable: ":" var
else_command: "else"
true: "true" | "True"
false: "false" | "False"
number: SIGNED_INT

%import common.SIGNED_INT
%import common.WORD
%import common.WS
%ignore WS
"""


class _LogoJsonTransformer(Transformer):
    """Transforms Logo language code into JSON format."""

    def start(self, items: list) -> dict:
        return {"tokens": items}

    def command(self, items: list) -> dict:
        return items[0]

    def showturtle(self, items: list) -> str:  # noqa: ARG002
        return "showturtle"

    def hideturtle(self, items: list) -> str:  # noqa: ARG002
        return "hideturtle"

    def penup(self, items: list) -> str:  # noqa: ARG002
        return "penup"

    def pendown(self, items: list) -> str:  # noqa: ARG002
        return "pendown"

    def no_arg_command(self, items: list) -> str:
        return {"name": items[0]}

    def forward(self, items: list) -> str:  # noqa: ARG002
        return "forward"

    def backward(self, items: list) -> str:  # noqa: ARG002
        return "backward"

    def left(self, items: list) -> str:  # noqa: ARG002
        return "left"

    def right(self, items: list) -> str:  # noqa: ARG002
        return "right"

    def one_arg_command(self, items: list) -> str:
        name = items[0]
        value = items[1]
        return {"name": name, "value": value}

    def repeat(self, items: list) -> str:
        value = items[0]
        commands = items[1:]
        return {"name": "repeat", "value": value, "commands": commands}

    def if_command(self, items: list) -> str:
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

    def make(self, items: list) -> str:
        var_name = items[0]
        value = items[1]
        return {"name": "make", "var_name": var_name, "value": value}

    def else_command(self, items: list) -> str:  # noqa: ARG002
        return "else"

    def true(self, items: list) -> str:  # noqa: ARG002
        return "true"

    def false(self, items: list) -> str:  # noqa: ARG002
        return "false"

    def number(self, items: list) -> int:
        return int(items[0])

    def var(self, items: list) -> str:
        return str(items[0])

    def variable(self, items: list) -> str:
        return str(items[0])


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
