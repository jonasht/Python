import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT
from frameCadastroCliente import FrameCadastroCliente
from frameVenda import FrameVenda
from frameCadastroProduto import FrameProduto
from framePesquisarProduto import FrPesquisarProduto
from FramePesquisarClientes import FrPesquisarCliente

class Principal(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry('1000x600')
        self.frameBotoes = ttk.Frame(self)
        
        # label frame venda =============================================================
        self.lbfr_venda = ttk.LabelFrame(self.frameBotoes, text='Venda')
        self.btVenda = ttk.Button(self.lbfr_venda, width=10, text='Venda')
        self.bt_entregas = ttk.Button(self.lbfr_venda, text='Entregas', width=10)
        self.btVenda.grid(row=0)
        self.bt_entregas.grid(row=1)
        self.lbfr_venda.grid(row=0)
        
        # label frame produto =============================================================
        self.lbfr_produto = ttk.LabelFrame(self.frameBotoes, text='Produto')
        self.bt_cadastrarProduto = ttk.Button(self.lbfr_produto, width=10, text='Cadastrar', command=self.show_fr_CadastrarProduto)
        self.bt_pesquisarProduto = ttk.Button(self.lbfr_produto, width=10, text='Pesquisar', command=self.show_fr_pesquisarProduto)

        self.bt_cadastrarProduto.grid(row=0)
        self.bt_pesquisarProduto.grid(row=1)
        self.lbfr_produto.grid(row=1)

        # label frame cliente =============================================================
        self.lbfr_cliente = ttk.LabelFrame(self.frameBotoes, text='Clientes')
        self.bt_cadastrarCliente = ttk.Button(self.lbfr_cliente, text='Cadastrar', width=10, command=self.show_fr_CadstroCliente)
        self.bt_pesquisarCliente = ttk.Button(self.lbfr_cliente, text='Pesquisar', width=10, command=self.show_fr_pesquisarCliente)

        self.bt_cadastrarCliente.grid(row=0)
        self.bt_pesquisarCliente.grid(row=1)
        self.lbfr_cliente.grid(row=2)
        
        self.btFaturamento = ttk.Button(self.frameBotoes,width=10, text='Faturamento')
        

        self.btFaturamento.grid(row=3)
        
        self.frameBotoes.pack(side=LEFT, fill=BOTH)
        

        # =================================================================
        self.frameDireita = ttk.Frame(self)
        self.frameCadastroProduto = FrameProduto(self.frameDireita)
        self.frameCadastroCliente = FrameCadastroCliente(self.frameDireita)
        self.framePesquisarProduto = FrPesquisarProduto(self.frameDireita)
        self.framePesquisarCliente = FrPesquisarCliente(self.frameDireita)

        self.frameDireita.pack(side=LEFT, fill=BOTH)
    
    def apagar_frames(self):
        self.frameCadastroCliente.forget()
        self.frameCadastroProduto.forget()
        self.framePesquisarProduto.forget()
        self.framePesquisarCliente.forget()
        
    def show_fr_CadastrarProduto(self):
        self.apagar_frames()
        self.frameCadastroProduto.pack()
        
    def show_fr_CadstroCliente(self):
        self.apagar_frames()
        self.frameCadastroCliente.pack()
    def show_fr_pesquisarProduto(self):
        self.apagar_frames()
        
        self.framePesquisarProduto.pack()
        
    def show_fr_pesquisarCliente(self):
        self.apagar_frames()
        
        self.framePesquisarCliente.pack()
        
        
        
        
root = Principal()
root.mainloop()