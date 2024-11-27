from tkinter import *
from tkinter import ttk

root = Tk()

class Aplicacao():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Calculadora")
        self.root.configure(bg = "#44467f")
        self.root.geometry("300x450")
        self.root.minsize(width = 300, height = 450)
        self.root.maxsize(width = 500, height = 700)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg='black')
        self.frame_1.place(relx=0.025, rely=0.025, 
                            relwidth=0.95, relheight=0.2)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.025, rely=0.25, 
                            relwidth=0.95, relheight=0.7)

    def criando_botoes(self):
        # Botões add
        self.btn_parleft = Button(self.frame_2, text='(')
        self.btn_parleft.place(relx=0, rely=0, 
                            relwidth=0.25, relheight=0.2)

        self.btn_parright = Button(self.frame_2, text=')')
        self.btn_parright.place(relx=0.25, rely=0, 
                            relwidth=0.25, relheight=0.2)

        self.btn_backspace = Button(self.frame_2, text='⌫')
        self.btn_backspace.place(relx=0.5, rely=0, 
                            relwidth=0.25, relheight=0.2)

        self.btn_virg = Button(self.frame_2, text=',')
        self.btn_virg.place(relx=0.5, rely=0.8, 
                            relwidth=0.25, relheight=0.2)

        self.btn_cc = Button(self.frame_2, text='C')
        self.btn_cc.place(relx=0, rely=0.8, 
                            relwidth=0.25, relheight=0.2)

        # Botões numéricos
        self.btn_9 = Button(self.frame_2, text='9')
        self.btn_9.place(relx=0.5, rely=0.2, 
                            relwidth=0.25, relheight=0.2)

        self.btn_8 = Button(self.frame_2, text='8')
        self.btn_8.place(relx=0.25, rely=0.2, 
                            relwidth=0.25, relheight=0.2)
        
        self.btn_7 = Button(self.frame_2, text='7')
        self.btn_7.place(relx=0, rely=0.2, 
                            relwidth=0.25, relheight=0.2)

        self.btn_6 = Button(self.frame_2, text='6')
        self.btn_6.place(relx=0.5, rely=0.4, 
                            relwidth=0.25, relheight=0.2)

        self.btn_5 = Button(self.frame_2, text='5')
        self.btn_5.place(relx=0.25, rely=0.4, 
                            relwidth=0.25, relheight=0.2)

        self.btn_4 = Button(self.frame_2, text='4')
        self.btn_4.place(relx=0, rely=0.4, 
                            relwidth=0.25, relheight=0.2)
        
        self.btn_3 = Button(self.frame_2, text='3')
        self.btn_3.place(relx=0.5, rely=0.6, 
                            relwidth=0.25, relheight=0.2)

        self.btn_2 = Button(self.frame_2, text='2')
        self.btn_2.place(relx=0.25, rely=0.6, 
                            relwidth=0.25, relheight=0.2)
        
        self.btn_1 = Button(self.frame_2, text='1')
        self.btn_1.place(relx=0, rely=0.6, 
                            relwidth=0.25, relheight=0.2)

        self.btn_0 = Button(self.frame_2, text='0')
        self.btn_0.place(relx=0.25, rely=0.8, 
                            relwidth=0.25, relheight=0.2)

        # Botões de opreação
        self.btn_soma = Button(self.frame_2, text='+')
        self.btn_soma.place(relx=0.75, rely=0.6, 
                            relwidth=0.25, relheight=0.2)

        self.btn_sub = Button(self.frame_2, text='-')
        self.btn_sub.place(relx=0.75, rely=0.4, 
                            relwidth=0.25, relheight=0.2)

        self.btn_prod = Button(self.frame_2, text='x')
        self.btn_prod.place(relx=0.75, rely=0.2, 
                            relwidth=0.25, relheight=0.2)

        self.btn_div = Button(self.frame_2, text='÷')
        self.btn_div.place(relx=0.75, rely=0, 
                            relwidth=0.25, relheight=0.2)
        
        self.btn_igual = Button(self.frame_2, text='=')
        self.btn_igual.place(relx=0.75, rely=0.8, 
                            relwidth=0.25, relheight=0.2)
        
Aplicacao()