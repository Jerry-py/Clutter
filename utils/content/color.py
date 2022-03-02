import sys
from typing import Any, Callable, Union


def esc(*codes: Union[int, str]) -> str:
    return t_("\x1b[{}m").format(t_(";").join(t_(str(c)) for c in codes))


def t_(b: Union[bytes, Any]) -> str:
    return b.decode() if isinstance(b, bytes) else b


def make_color(start, end: str) -> Callable[[str], str]:
    def color_func(s: str) -> str:
        return s if not sys.stdout.isatty() else start + t_(s) + end

    return color_func


FG_END = esc(39)
BG_END = esc(49)
HL_END = esc(22, 27, 39)


class Color:
    black = make_color(esc(30), FG_END)
    red = make_color(esc(31), FG_END)
    green = make_color(esc(32), FG_END)
    yellow = make_color(esc(33), FG_END)
    blue = make_color(esc(34), FG_END)
    magenta = make_color(esc(35), FG_END)
    cyan = make_color(esc(36), FG_END)
    white = make_color(esc(37), FG_END)

    black_bg = make_color(esc(40), BG_END)
    red_bg = make_color(esc(41), BG_END)
    green_bg = make_color(esc(42), BG_END)
    yellow_bg = make_color(esc(43), BG_END)
    blue_bg = make_color(esc(44), BG_END)
    magenta_bg = make_color(esc(45), BG_END)
    cyan_bg = make_color(esc(46), BG_END)
    white_bg = make_color(esc(47), BG_END)

    black_hl = make_color(esc(1, 30, 7), HL_END)
    red_hl = make_color(esc(1, 31, 7), HL_END)
    green_hl = make_color(esc(1, 32, 7), HL_END)
    yellow_hl = make_color(esc(1, 33, 7), HL_END)
    blue_hl = make_color(esc(1, 34, 7), HL_END)
    magenta_hl = make_color(esc(1, 35, 7), HL_END)
    cyan_hl = make_color(esc(1, 36, 7), HL_END)
    white_hl = make_color(esc(1, 37, 7), HL_END)

    bold = make_color(esc(1), esc(22))
    italic = make_color(esc(3), esc(23))
    underline = make_color(esc(4), esc(24))
    strike = make_color(esc(9), esc(29))
    blink = make_color(esc(5), esc(25))
