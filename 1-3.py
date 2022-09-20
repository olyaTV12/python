import argparse

def process(accum, op, number):
    if op == '+':
        return accum + number
    elif op == '-':
        return accum - number
    elif op == '0':
        return number

def parse(expression):
    if not expression:
        return (False, None)
    accum = 0
    number = 0
    pending = '0'
    for c in expression:
        if c.isdigit():
            if number is None:
                number = 0
            number = number * 10 + int(c)
        elif c in "+-":
            if number is None:
                return False, None
            accum = process( accum, pending, number )
            pending = c
            number = None
        else:
            return False, None
    return True, process(accum, pending, number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Take expression")
    parser.add_argument("input_expression", type=str,
            help="Give an expression")

    input_args = parser.parse_args()
    expr = input_args.input_expression

    print(parse(expr))