from tkinter import *


def concatenate_to_calculation(character):
    global calculation
    calculation += str(character)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    text_result.delete(1.0, "end")
    calculation = ""


def create_window():
    btns = [None for _ in range(10)]

    for i in range(1, 10, 3):
        for j in range(3):
            btns[i + j] = Button(root, text=str(i + j), command=lambda r=i + j: concatenate_to_calculation(r), width=5,
                                 font=("Arial", 24))
            btns[i + j].grid(row=(i // 3) + 1, column=j + 1)
    btns[0] = Button(root, text=str(0), command=lambda: concatenate_to_calculation(0), width=5, font=("Arial", 24))
    btns[0].grid(row=4, column=2)
    btn_plus = Button(root, text=str("+"), command=lambda: concatenate_to_calculation("+"), width=5, font=("Arial", 24))
    btn_plus.grid(row=1, column=4)
    btn_minus = Button(root, text=str("-"), command=lambda: concatenate_to_calculation("-"), width=5,
                       font=("Arial", 24))
    btn_minus.grid(row=2, column=4)
    btn_multiply = Button(root, text=str("*"), command=lambda: concatenate_to_calculation("*"), width=5,
                          font=("Arial", 24))
    btn_multiply.grid(row=3, column=4)
    btn_divide = Button(root, text=str("/"), command=lambda: concatenate_to_calculation("/"), width=5,
                        font=("Arial", 24))
    btn_divide.grid(row=4, column=4)
    btn_open = Button(root, text=str("("), command=lambda: concatenate_to_calculation("("), width=5, font=("Arial", 24))
    btn_open.grid(row=4, column=1)
    btn_close = Button(root, text=str(")"), command=lambda: concatenate_to_calculation(")"), width=5,
                       font=("Arial", 24))
    btn_close.grid(row=4, column=3)
    btn_equals = Button(root, text=str("="), command=lambda: evaluate(), width=12, font=("Arial", 24))
    btn_equals.grid(row=5, column=3, columnspan=2)
    btn_clear = Button(root, text=str("C"), command=lambda: clear_field(), width=12, font=("Arial", 24))
    btn_clear.grid(row=5, column=1, columnspan=2)


calculation = ""
root = Tk()
root.geometry("428x255")
root.title("Calculator")
text_result = Text(root, height=2, width=30, font=("Arial", 24))
text_result.grid(columnspan=5)
create_window()

root.mainloop()
