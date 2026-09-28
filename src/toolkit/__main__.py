import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ToolkitError


def main():
    par = argparse.ArgumentParser(prog="toolkit")
    sub = par.add_subparsers(dest="command", required=True)

    p_calc = sub.add_parser("calc", help="Вычислить выражение")
    p_conv = sub.add_parser("convert", help="Конвертировать величину")
    p_calc.add_argument("expression")
    p_conv.add_argument("value", type=float)
    p_conv.add_argument("--from", dest="from_unit", required=True)
    p_conv.add_argument("--to", dest="to_unit", required=True)

    args = par.parse_args()

    try:
        if args.command == "calc":
            print(calculate(args.expression))
        elif args.command == "convert":
            print(convert(args.value, args.from_unit, args.to_unit))
    except ToolkitError as e:
        print(e, file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()