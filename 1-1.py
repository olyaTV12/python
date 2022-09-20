import argparse

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Take two integer values - ")
    parser.add_argument("input_value_1", type=int,
                help="Give a positive integer value for 1st veriable")
    parser.add_argument("input_operator", type=str,
                help="Give an operator", choices=["+", "-", "*", "/"])
    parser.add_argument("input_value_2", type=int,
                help="Give a positive integer value for 2nd variable")

    input_args = parser.parse_args()
    val_1 = input_args.input_value_1
    val_2 = input_args.input_value_2
    operator = input_args.input_operator

    if operator == "+":
        result = val_1 + val_2
    elif operator == "-":
        result = val_1 - val_2
    elif operator == "*":
        result = val_1 * val_2
    elif operator == "/":
        result = val_1 / val_2

    print("{0} {1} {2} = {3}".format(val_1, operator, val_2, result))