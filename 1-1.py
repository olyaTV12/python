import argparse

def process(val_1, op, val_2):
    if not val_2:
        raise ZeroDivisionError("Division by 0")

    if op == "+":
        return val_1 + val_2
    elif op == "-":
        return val_1 - val_2
    elif op == "*":
        return val_1 * val_2
    elif op == "/":
        return val_1 / val_2
    else:
        raise AttributeError("Invalid operator")

        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Take two integer values - ")

    parser.add_argument("input_value_1", type=int)
    parser.add_argument("input_operator", type=str, choices=["+", "-", "*", "/"])
    parser.add_argument("input_value_2", type=int)


    input_args = parser.parse_args()
    val_1 = input_args.input_value_1
    val_2 = input_args.input_value_2
    operator = input_args.input_operator

    result = process(val_1, operator, val_2)

    print("{0} {1} {2} = {3}".format(val_1, operator, val_2, result))
