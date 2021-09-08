from tkinter import *
from frameProduto import FrameProduto

class Principal(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('1000x600')
        self.frameBotoes = Frame(self)
        self.btVenda = Button(self.frameBotoes, width=10, text='Venda')
        self.btProduto = Button(self.frameBotoes, width=10, text='Produto', command=self.show_frProduto)
        self.btFaturamento = Button(self.frameBotoes,width=10, text='Faturamento')
        self.btVenda.grid(row=0, sticky=N+W)
        self.btProduto.grid(row=1)
        self.btFaturamento.grid(row=2)
        
        self.frameBotoes.pack(side=LEFT, fill=BOTH)
        

        # =================================================================
        self.frameDireita = Frame(self)
        self.frProduto = FrameProduto(self.frameDireita)

        self.frameDireita.pack(side=LEFT, fill=BOTH)
        
    def show_frProduto(self):
        self.frProduto.pack()
        
        
        
root = Principal()
root.mainloop()