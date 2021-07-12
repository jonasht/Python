from tkinter import *
from interfaceStart import FrameStart
from frameMenu import Menu

class Principal(Tk):
    def __init__(self):
        super().__init__()
        
        self.title('FTabuada v5')
        self.geometry('500x400')
        
       
        # chamando classes
        
        self.menu = Menu(self)
        self.frameStart = FrameStart(self)
        
        # dizendo que frameStart ainda nao foi colocada na tela
        self.frameStart_on = False
                
        # numeros para apertas as teclas do teclado
        self.bind('1', self.tecla1)
        self.bind('2', self.tecla2)
        self.bind('3', self.tecla3)
        self.bind('4', self.tecla4)
        self.bind('5', self.tecla5)
        self.bind('6', self.tecla6)
        self.bind('7', self.tecla7)
        self.bind('8', self.tecla8)
        self.bind('9', self.tecla9)
        
        # numeros numPad para apertar
        self.bind('<KP_1>', self.tecla1)
        self.bind('<KP_2>', self.tecla2)
        self.bind('<KP_3>', self.tecla3)
        self.bind('<KP_4>', self.tecla4)
        self.bind('<KP_5>', self.tecla5)
        self.bind('<KP_6>', self.tecla6)
        self.bind('<KP_7>', self.tecla7)
        self.bind('<KP_8>', self.tecla8)
        self.bind('<KP_9>', self.tecla9)
        
        
        # tecla enter
        self.bind('<Return>', self.teclaEnter)
        
        self.bind('<KP_Enter>', self.teclaEnter)
        
        # botoes do topo da tela ====================================
        self.frameVoltarSair = Frame(self)
        
        self.bt_voltar = Button(self.frameVoltarSair, 
                                text='Voltar', width=15, font='arial 20 bold', 
                                command=self.esconderFrameStart)
        self.bt_sair = Button(self.frameVoltarSair, 
                              text='Fechar X', width=20, 
                              font='arial 20 bold',
                              command=exit
                              )

        self.bt_voltar.pack(side=RIGHT)
        self.bt_sair.pack(side=LEFT)

        self.frameVoltarSair.pack(side=TOP) 
        
        self.mostrarMenu()
        

    def tecla1(self, event):
        print('tecla1 apertada main')
        print('frame start on?:', self.frameStart_on)
        if self.frameStart_on:
            self.frameStart.tecla1(None)
        elif self.menu.frameStart_on:
            self.menu.frameStart.tecla1(None)
        else:
            self.menu.rbt1.select()
            
    def tecla2(self, event):
        if self.frameStart_on:
            self.frameStart.tecla2(None)
        elif self.menu.frameStart_on:
            self.menu.frameStart.tecla2(None)
        else:
            self.menu.rbt2.select()
            
    def tecla3(self, event):
        if self.frameStart_on:
            self.frameStart.tecla3(None)
        elif self.menu.frameStart_on: 
            self.menu.frameStart.tecla3(None)
        else:
            self.menu.rbt3.select()

    def tecla4(self, event):
        self.menu.rbt4.select()
    def tecla5(self, event):
        self.menu.rbt5.select()
    def tecla6(self, event):
        self.menu.rbt6.select()
    def tecla7(self, event):
        self.menu.rbt7.select()
    def tecla8(self, event):
        self.menu.rbt8.select()
    def tecla9(self, event):
        self.menu.rbt9.select()
    
    def teclaEnter(self, event):
        self.Start()
        
    def esconderMenu(self):
        self.menu.pack_forget()
        
    def esconderFrameStart(self):
        self.frameStart_on = False
        self.menu.frameStart_on = False
        self.frameStart.pack_forget()
        self.mostrarMenu()

    def mostrarMenu(self): 
        self.menu.pack()
        self.bt_voltar.config(state=DISABLED)   
    
    
    def Start(self):  
        self.esconderMenu()
        self.bt_voltar.config(state=NORMAL)
        self.frameStart.pack()
        self.frameStart_on = True
        self.frameStart.iniciar(self.menu.valor.get())
        


    
root = Principal()
root.mainloop()