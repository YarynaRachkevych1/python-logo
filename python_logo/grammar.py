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
one_arg_command: (forward | backward | left | right) (number | variable | expression)
repeat: "repeat" (number | variable | expression) "[" command+ "]"
if_command: "if" (true | false) "[" command+ "]" ((else_command) "[" command+ "]")?
make: "make" var (number | variable | expression)
var: WORD
variable: ":" var
else_command: "else"
true: "true" | "True"
false: "false" | "False"
number: SIGNED_INT

expression: term operator term
term: number | variable | expression | "(" expression ")"

plus: "+"
minus: "-"
operator: plus | minus

%import common.SIGNED_INT
%import common.WORD
%import common.WS
%ignore WS
"""
