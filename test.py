from tkinter import *
from tkinter import ttk

# Operações

def addition(*args):
    a = float(number1.get())
    b = float(number2.get())
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return print('Division by zero is not allowed. Choose another number.')
     
    return a / b

# GUI (Graphical User Interface)
window = Tk()
window.title("Calculator")
window.geometry("500x500")

# Separa minha janela em uma matriz
mainframe = ttk.Frame(window, padding=(20, 20, 20, 20))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Colocar números

ttk.Label(mainframe, text='Digite um número').grid(column=1, row=1)
number1 = StringVar()
num1 = ttk.Entry(mainframe, textvariable=number1).grid(column=2, row=1)

ttk.Label(mainframe, text='Digite outro numero').grid(column=1, row=2)
number2 = StringVar()
num2 = ttk.Entry(mainframe, textvariable=number2).grid(column=2, row=2)


# Botões de cálculo
ttk.Button(mainframe, text="Addition", command=addition).grid(column=1, row=3)

ttk.Button(mainframe, text="Subtraction", command=subtraction).grid(column=2, row=3)

ttk.Button(mainframe, text='Multiplication', command=multiplication).grid(column=3, row=3)

ttk.Button(mainframe, text='Division', command=division).grid(column=4, row=3)

ttk.Button(mainframe, text='Quit', command=window.destroy).grid(column=4, row=4)

window.mainloop()

# numero 1
# numero 2
# 4 botões com as operações
# janela de resultado
