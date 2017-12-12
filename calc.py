from tkinter import *

window = Tk()
a = StringVar()
b = StringVar()


def inToPost(exp):
    precedence = {1: ["(", ")"], 2: ["*", "/"],
                  3: ["+", "-"]}  # dictionary representing the precedence of the operators

    stack_operator = []  # a stack to keep operands

    exp += ")"
    stack_operator.append("(")

    exp_post = ""

    for ch in exp:

        #  for the braces
        if ch in precedence[1]:
            if ch == ")":
                while stack_operator[-1] != "(":
                    c = stack_operator.pop()
                    exp_post += c
                else:
                    stack_operator.pop()
            else:
                stack_operator.append("(")

        # for * and /
        elif ch in precedence[2]:
            while stack_operator[-1] in precedence[2]:
                c = stack_operator.pop()
                exp_post += c
            stack_operator.append(ch)

        # for + and _
        elif ch in precedence[3]:
            while stack_operator[-1] in precedence[2] or stack_operator[-1] in precedence[3]:
                c = stack_operator.pop()
                exp_post += c
            stack_operator.append(ch)

        # for the operands
        else:
            exp_post += ch

    return exp_post


def evalPost(exp):
    stack_operand = []

    operators = ['+', '-', '*', '/']

    for ch in exp:
        if ch not in operators:
            stack_operand.append(ch)
        elif ch in operators:
            a = int(stack_operand.pop())
            b = int(stack_operand.pop())
            if ch == '+':
                stack_operand.append(a + b)
            elif ch == '-':
                stack_operand.append(a - b)
            elif ch == '*':
                stack_operand.append(a * b)
            else:
                stack_operand.append(a / b)
    return stack_operand.pop()

def equalf():
    c = inToPost(a.get())
    b.set(evalPost(c))


def concat_op(p):
    global a
    a.set(a.get() + p)


def ac():
    a.set("")
    b.set("")


def clr():
    a.set(a.get()[0:-1])


window.geometry("350x180+300+300")

# defining the buttons, text field and label
text1 = Entry(window, width=18, textvariable=a, font=20).grid(row=0, column=0, columnspan=3)
Label(window,  textvariable=b, width=12, font=20).grid(row=0, column=3, columnspan=2)
Button(window, width=6, text="1", font=20, command=lambda: concat_op('1')).grid(row=1, column=0, sticky="w")
Button(window, width=6, text="2", font=20, command=lambda: concat_op('2')).grid(row=1, column=1, sticky="w")
Button(window, width=6, text="3", font=20, command=lambda: concat_op('3')).grid(row=1, column=2, sticky="w")
Button(window, width=6, text="4", font=20, command=lambda: concat_op('4')).grid(row=2, column=0, sticky="w")
Button(window, width=6, text="5", font=20, command=lambda: concat_op('5')).grid(row=2, column=1, sticky="w")
Button(window, width=6, text="6", font=20, command=lambda: concat_op('6')).grid(row=2, column=2, sticky="w")
Button(window, width=6, text="7", font=20, command=lambda: concat_op('7')).grid(row=3, column=0, sticky="w")
Button(window, width=6, text="8", font=20, command=lambda: concat_op('8')).grid(row=3, column=1, sticky="w")
Button(window, width=6, text="9", font=20, command=lambda: concat_op('9')).grid(row=3, column=2, sticky="w")
Button(window, width=6, text="0", font=20, command=lambda: concat_op('0')).grid(row=4, column=1, sticky="w")
Button(window, width=6, text="+", font=20, command=lambda: concat_op('+')).grid(row=1, column=3, sticky="w")
Button(window, width=6, text="-", font=20, command=lambda: concat_op('-')).grid(row=2, column=3, sticky="w")
Button(window, width=6, text="*", font=20, command=lambda: concat_op('*')).grid(row=3, column=3, sticky="w")
Button(window, width=6, text="/", font=20, command=lambda: concat_op('/')).grid(row=4, column=3, sticky="w")
Button(window, width=6, text="(", font=20, command=lambda: concat_op('(')).grid(row=4, column=0, sticky="w")
Button(window, width=6, text=")", font=20, command=lambda: concat_op(')')).grid(row=4, column=2, sticky="w")
Button(window, width=6, text="AC", font=20, command=ac).grid(row=1, column=4, sticky="w")
Button(window, width=6, text="C", font=20, command=clr).grid(row=2, column=4, sticky="w")
Button(window, width=6, height=3, text="=", font=20, command=equalf).grid(row=3, column=4, rowspan=2, sticky="w")

window.mainloop()
