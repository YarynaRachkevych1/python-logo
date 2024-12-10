from collections.abc import Generator, Iterator

from .exceptions import (
    InterpreterInvalidCommandError,
    InterpreterInvalidTreeError,
    InterpreterUnboundVariableError,
)


class Interpreter:
    """Class to interpret parsed Logo programming language commands.
    Interpreted commands include only commands that affects the turtle directly.
    It doesn't include variables, functions or commands that are used for control flow.

    Args:
        tree (dict): Parsed Logo tree with parse() function.
    """

    def __init__(self, tree: dict) -> None:
        """Initializes the Interpreter instance."""
        self._variables = {}
        try:
            self._commands = tree["tokens"]
        except KeyError as err:
            raise InterpreterInvalidTreeError from err
        except TypeError as err:
            raise InterpreterInvalidTreeError from err

    def _interpret(self, commands: list) -> Generator[dict, None, None]:
        """Generates and interprets commands.

        Args:
            commands (list): List of parsed commands.

        Returns:
            Generator[dict, None, None]: Generator of commands.
        """
        try:
            for command in commands:
                name = command["name"]
                match name:
                    case "make":
                        name = command["var_name"]
                        value = self._evaluate(command["value"])
                        self._variables[name] = value
                    case "repeat":
                        value = self._evaluate(command["value"])
                        for _ in range(value):
                            yield from self._interpret(command["commands"])
                    case "if":
                        condition = command["condition"]
                        if condition == "true":
                            yield from self._interpret(command["commands"])
                        else:
                            yield from self._interpret(command["else_commands"])
                    case "forward" | "backward" | "left" | "right":
                        evaluated_value = self._evaluate(command["value"])
                        yield {**command, "value": evaluated_value}
                    case "hideturtle" | "showturtle" | "penup" | "pendown":
                        yield command
                    case _:
                        raise InterpreterInvalidCommandError
        except KeyError as err:
            raise InterpreterInvalidTreeError from err

    def _evaluate(self, value: int | str) -> int | None:
        """Evaluates the value of the possible variable.

        Args:
            value (int | str): Value or variable to evaluate.

        Returns:
            int: Value of the possible variable.
        """
        # Value is  just a number
        if isinstance(value, int):
            return value

        # Value is a single variable from dictionary
        if not isinstance(value, list):
            try:
                return self._variables[value]
            except KeyError as err:
                raise InterpreterUnboundVariableError(value) from err

        # Value is an expression
        value = value[0]
        for command in value:
            match command:
                case "arithmetic_op":
                    operator = value["arithmetic_op"]
                    operand1 = value["operands"][0]
                    operand2 = value["operands"][1]
                    if operator == "+":
                        return self._evaluate(self._evaluate(operand1)
                                              + self._evaluate(operand2))
                    if operator == "-":
                        return self._evaluate(self._evaluate(operand1)
                                              - self._evaluate(operand2))
        return None

    def __iter__(self) -> Iterator[dict]:
        """Iterates over commands and interprets them.

        Returns:
            Iterator[dict]: Iterator of commands.
        """
        return self._interpret(self._commands)
