from collections.abc import Generator, Iterator

from .exceptions import (
    InterpreterFunctionExecutionError,
    InterpreterInvalidColorError,
    InterpreterInvalidCommandError,
    InterpreterInvalidFunctionArgumentsError,
    InterpreterInvalidTreeError,
    InterpreterUnboundVariableError,
    InterpreterUnboundVariableListError,
    InterpreterUndefinedFunctionError,
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
        self._fuctions = {}
        self._lists = {}
        self._colors = ["white", "black", "red", "green", "blue", "cyan"]
        try:
            self._commands = tree["tokens"]
        except KeyError as err:
            raise InterpreterInvalidTreeError from err
        except TypeError as err:
            raise InterpreterInvalidTreeError from err

    def __iter__(self) -> Iterator[dict]:
        """Iterates over commands and interprets them.

        Returns:
            Iterator[dict]: Iterator of commands.
        """
        return self._interpret(self._commands)

    def _interpret(self, commands: list) -> Generator[dict, None, None]:  # noqa: C901, PLR0912
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
                    case "func_def":
                        self._handle_func_def(command)
                    case "func_call":
                        yield from self._handle_func_call(command)
                    case "make":
                        self._handle_make(command)
                    case "list_make":
                        self._handle_list_make(command)
                    case "list":
                        self._handle_list(command)
                    case "repeat":
                        yield from self._handle_repeat(command)
                    case "if":
                        yield from self._handle_if(command)
                    case "forward" | "backward" | "left" | "right":
                        yield from self._handle_movement(command)
                    case "hideturtle" | "showturtle" | "penup" | "pendown":
                        yield command
                    case "setpos":
                        command["x"] = self._evaluate(command["x"])
                        command["y"] = self._evaluate(command["y"])
                        yield command
                    case "setpencolor":
                        yield from self._handle_setpencolor(command)
                    case "setpensize":
                        yield from self._handle_setpensize(command)
                    case "print":
                        yield from self._handle_print(command)
                    case _:
                        raise InterpreterInvalidCommandError
        except KeyError as err:
            raise InterpreterInvalidTreeError from err

    # --------------------------------------------------------------------------
    # Handlers for specific commands
    # --------------------------------------------------------------------------

    def _handle_func_def(self, command: dict) -> Generator[dict, None, None]:
        """Handles function definition commands."""
        func_name = command["func_name"]
        arguments = command["arguments"]
        commands = command["commands"]

        self._fuctions[func_name] = {"arguments": {}, "commands": []}
        for argument in arguments:
            self._fuctions[func_name]["arguments"][argument] = ""
        self._fuctions[func_name]["commands"] = commands

    def _handle_func_call(self, command: dict) -> Generator[dict, None, None]:
        """Handles function call commands."""
        func_name = command["func_name"]
        arguments = command["arguments"]

        try:
            func_args_num = len(self._fuctions[func_name]["arguments"])
            input_args_num = len(arguments)

            if func_args_num != input_args_num:
                raise InterpreterInvalidFunctionArgumentsError(
                    func_name=func_name,
                    expected_args=func_args_num,
                    received_args=input_args_num,
                )

            keys = list(self._fuctions[func_name]["arguments"])
            for i in range(len(arguments)):
                arg_name = keys[i]
                evaluated_value = self._evaluate(arguments[i])
                self._fuctions[func_name]["arguments"][arg_name] = evaluated_value

            commands = self._fuctions[func_name]["commands"]
            try:
                yield from self._interpret(commands)
            except Exception as execution_err:
                raise InterpreterFunctionExecutionError(
                    func_name, str(execution_err)
                ) from execution_err

        except KeyError as err:
            raise InterpreterUndefinedFunctionError(func_name) from err

    def _handle_make(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'make' commands (variable assignment)."""
        var_name = command["var_name"]
        value = self._evaluate(command["value"])
        self._variables[var_name] = value

    def _handle_list_make(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'list_make' commands (list creation)."""
        list_name = command["list_name"]
        value = command["list"]
        if value == "empty":
            value = []
        for i in range(len(value)):
            value[i] = self._evaluate(value[i])
        self._lists[list_name] = value

    def _handle_repeat(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'repeat' commands."""
        value = self._evaluate(command["value"])
        for _ in range(int(value)):
            yield from self._interpret(command["commands"])

    def _handle_if(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'if' commands."""
        condition = self._evaluate(command["condition"])
        if condition:
            yield from self._interpret(command["commands"])
        else:
            yield from self._interpret(command["else_commands"])

    def _handle_movement(self, command: dict) -> Generator[dict, None, None]:
        """Handles movement commands like forward, backward, left, right."""
        new_command = {
            "name": command["name"],
            "value": self._evaluate(command["value"]),
        }
        yield new_command

    def _handle_setpencolor(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'setpencolor' commands."""
        if command["color"] not in self._colors:
            raise InterpreterInvalidColorError(
                color=command["color"],
                supported_colors=self._colors,
            )
        yield command

    def _handle_setpensize(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'setpensize' commands."""
        new_command = {
            "name": command["name"],
            "value": self._evaluate(command["value"]),
        }
        yield new_command

    def _handle_print(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'print' commands."""
        new_command = {
            "name": command["name"],
            "value": self._evaluate(command["value"]),
        }
        yield new_command

    def _handle_list(self, command: dict) -> Generator[dict, None, None]:
        """Handles 'list' commands."""
        try:
            if command["list_name"] in self._lists:
                xs = self._lists[command["list_name"]]
            match command["function"]:
                case "empty":
                    return bool(not xs)
                case "len":
                    return len(xs)
                case "get":
                    i = int(self._evaluate(command["index"]))
                    return xs[i]
                case "set":
                    xs[int(command["index"])] = self._evaluate(command["value"])
                    self._lists[command["list_name"]] = xs
                case "insert":
                    xs.insert(int(command["index"]), self._evaluate(command["value"]))
                    self._lists[command["list_name"]] = xs
                case "remove":
                    xs.pop(int(command["index"]))
                    self._lists[command["list_name"]] = xs
                case "remove_value":
                    xs.remove(self._evaluate(command["value"]))
                    self._lists[command["list_name"]] = xs
                case _:
                    raise InterpreterInvalidCommandError
        except KeyError as err:
            raise InterpreterUnboundVariableListError from err

    # --------------------------------------------------------------------------
    # Expression evaluation
    # --------------------------------------------------------------------------

    def _evaluate(self, value: float | str | dict) -> float:  # noqa: PLR0912, PLR0911, C901
        """Evaluates the value of the possible variable or expression."""
        # Value is a float
        if isinstance(value, float):
            return value

        # Value is a string -> could be a variable
        if isinstance(value, str):
            # Try local function arguments first
            for func_data in self._fuctions.values():
                if value in func_data["arguments"]:
                    return func_data["arguments"][value]

            if value == "true":
                return True
            if value == "false":
                return False

            # Then try global variables
            try:
                return self._variables[value]
            except KeyError as err:
                raise InterpreterUnboundVariableError(value) from err

        # Value is an expression (dict)
        if isinstance(value, dict):
            if "name" in value and value["name"] == "list":
                return self._handle_list(value)
            try:
                op = value["op"]
                match op:
                    case "+":
                        return self._evaluate(value["left"]) + self._evaluate(
                            value["right"]
                        )
                    case "-":
                        return self._evaluate(value["left"]) - self._evaluate(
                            value["right"]
                        )
                    case "*":
                        return self._evaluate(value["left"]) * self._evaluate(
                            value["right"]
                        )
                    case "/":
                        return self._evaluate(value["left"]) / self._evaluate(
                            value["right"]
                        )
                    case "^":
                        return self._evaluate(value["left"]) ** self._evaluate(
                            value["right"]
                        )
                    case "neg":
                        return -self._evaluate(value["value"])
                    case ">":
                        return self._evaluate(value["left"]) > self._evaluate(
                            value["right"]
                        )
                    case ">=":
                        return self._evaluate(value["left"]) >= self._evaluate(
                            value["right"]
                        )
                    case "<":
                        return self._evaluate(value["left"]) < self._evaluate(
                            value["right"]
                        )
                    case "<=":
                        return self._evaluate(value["left"]) <= self._evaluate(
                            value["right"]
                        )
                    case "=":
                        return self._evaluate(value["left"]) == self._evaluate(
                            value["right"]
                        )
                    case "<>":
                        return self._evaluate(value["left"]) != self._evaluate(
                            value["right"]
                        )
                    case "and":
                        return all(self._evaluate(expr) for expr in value["list"])
                    case "or":
                        return any(self._evaluate(expr) for expr in value["list"])
                    case "not":
                        return not self._evaluate(value["expr"])
                    case _:
                        raise InterpreterInvalidCommandError
            except KeyError as err:
                raise InterpreterInvalidTreeError from err

        # If none of the above matched, it's an invalid tree
        raise InterpreterInvalidTreeError
