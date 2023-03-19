import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from validate_docbr import CNS
import pyperclip as pc

class Fr_CNS(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.CNS = CNS()
        self.CNS_num = ''
        self.var = ttk.BooleanVar()

        #   CNS =================================================
        self.lbfr = ttk.Labelframe(self, text='CNS', padding=20)
        self.etd = ttk.Entry(self.lbfr)
        self.bt_gerar = ttk.Button(self.lbfr, text='Gerar', command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self.lbfr, text='mask',variable=self.var, command=self.chbt_Evento)
        self.bt_copy = ttk.Button(self.lbfr, text='Copiar', command=self.copiar)
        self.etd.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        self.chbt_mask.grid(row=1, column=2, padx=2, pady=5)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        
        self.lbfr.pack()
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()

        
    def gerar(self):
        self.etd.delete(0, END)
        self.CNS_num = self.CNS.generate()
        self.etd.insert(0, self.CNS_num)
        if self.var.get():
            self.chbt_Evento()

    def copiar(self):
        pc.copy(self.etd.get())

    def chbt_Evento(self):
        if self.var.get():
            self.etd.delete(0, END)
            self.etd.insert(0, self.CNS.mask(self.CNS_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.CNS_num)

