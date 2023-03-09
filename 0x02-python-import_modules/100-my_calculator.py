#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as cal
    operators = ["+", "-", "*", "/"]
    print(len(argv))
    print(argv)
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif argv[2] == "+":
            print("{} {} {} = {}".format(a, argv[2], b, cal.add(a, b)))
        elif argv[2] == "-":
            print("{} {} {} = {}".format(a, argv[2], b, cal.sub(a, b)))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(a, argv[2], b, cal.mul(a, b)))
        elif argv[2] == "/":
            print("{} {} {} = {}".format(a, argv[2], b, cal.div(a, b)))
