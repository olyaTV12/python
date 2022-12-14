import argparse
import operator
import math

def process(a, op_name, b):
    if op_name == 'truediv' and b == 0:
        return None

    op = getattr(operator, op_name, None)
    if op:
        return op(a, b)

    op = getattr(math, op_name, None)
    if op:
        return op(a, b)

    raise AttributeError("Invalid operator")

    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Take two integer values and operator")

    parser.add_argument("input_operator_name", type=str)
    parser.add_argument("input_value_1", type=int)
    parser.add_argument("input_value_2", type=int)


    input_args = parser.parse_args()

    val_1 = input_args.input_value_1
    val_2 = input_args.input_value_2
    operator_name = input_args.input_operator_name

    print(process(val_1, operator_name, val_2))
