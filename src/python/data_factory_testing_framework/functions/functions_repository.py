from typing import Dict, Callable, List, Iterable, Union
import json
from datetime import datetime
from collections.abc import Iterable as IterableType


class FunctionsRepository:
    functions: Dict[str, Callable] = {
        "concat": lambda arguments: "".join(arguments),
        "trim": lambda text, trim_argument: text.strip(trim_argument[0]),
        "equals": lambda argument0, argument1: argument0 == argument1,
        "json": lambda argument: argument,
        "contains": lambda obj, value: (
            value in obj if isinstance(obj, dict) else
            value in obj if isinstance(obj, IterableType) else
            value in obj if isinstance(obj, str) else
            False
        ),
        "replace": lambda input_str, pattern, replacement: input_str.replace(pattern, replacement),
        "string": lambda input_str: input_str,
        "union": lambda arg0, arg1: json.dumps(list(set(json.loads(arg0) + json.loads(arg1)))),
        "coalesce": lambda args: next((arg for arg in args if arg is not None), None),
        "or": lambda a, b: a or b,
        "utcnow": lambda: datetime.utcnow().isoformat(),
        "ticks": lambda date_time: datetime.fromisoformat(date_time).timestamp(),
        "sub": lambda a, b: a - b,
        "div": lambda a, b: a / b,
        "greaterOrEquals": lambda a, b: a >= b,
        "not": lambda value: not value,
        "empty": lambda array: len(array) == 0,
        "split": lambda input_str, delimiter: input_str.split(delimiter),
    }

    @staticmethod
    def register(function_name: str, function: Callable):
        FunctionsRepository.functions[function_name] = function

    @staticmethod
    def func_equals(argument0, argument1):
        if type(argument0) != type(argument1):
            raise ValueError("Equals function requires arguments of the same type.")
        return argument0 == argument1

    @staticmethod
    def trim(text, trim_argument):
        return text.strip(trim_argument[0])

    @staticmethod
    def json(argument):
        return argument

    @staticmethod
    def contains(obj, value):
        if isinstance(obj, dict):
            return value in obj
        elif isinstance(obj, IterableType):
            return value in obj
        elif isinstance(obj, str):
            return value in obj
        raise ValueError("Contains function requires an object of type Dictionary, IEnumerable, or string.")
