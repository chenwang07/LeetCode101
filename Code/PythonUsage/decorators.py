""" https://www.programiz.com/python-programming/decorator
"""

# decorators wrap a function, modifying its behavior.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def odinary():
    print("I am oridnary")


def smart_divide(func):
    # 似乎写法就是用一个inner function包装下，变量个数与func一致即可
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("I cannot divide")
            return
        return func(a, b)
    
    return inner

@smart_divide
def divide(a, b):
    return a/b



def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    # 这个写法好像是inner不用知道printer用什么参数，call的人负责传正确的参数，因为inner里面并不用任何参数，传
    # 进来什么就传出去什么
    # wrapper
    def inner(msg):
        print("%" * 30)
        func(msg)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


def main():
    printer("Hello")
    #divide(4, 3)
    #divide(1, 0)

main()


