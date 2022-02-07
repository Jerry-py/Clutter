from typing import Union, List, Any


def assemble(path: list, value: Any) -> dict:
    to_asm, i = {}, 0
    ref = to_asm
    if path == []:
        return value
    for _ in path:
        i += 1
        if i == len(path):
            to_asm[_] = value
            break
        to_asm[_] = {}
        to_asm = to_asm[_]
    return ref


def find(get_from: dict, path: str, *, default=None) -> Any:
    key = path.pop(-1)
    for _ in path:
        try:
            get_from = get_from[_]
        except (KeyError, TypeError, AttributeError):
            return default
    return get_from.get(key, default)
