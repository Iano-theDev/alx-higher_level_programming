#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    
    ops = ['+', '-', '*', '/']
    a = int(argv[1])
    b = int(argv[3])
    input_op = str(argv[2])
    funcs = [add, sub, mul, div]
    
    for index, op in enumerate(ops):
        print(input_op)
        if op == input_op:
            print("{} {} {} = {}".format(a, input_op, b, funcs[index](a, b)))
            exit(1)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
