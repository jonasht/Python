import tkinter as tk
from tkinter import ttk
from tkinter.constants import END

class Fr2(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller


        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

        # insert a the end
        tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

        # insert at the beginning
        tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

        tree.insert('', END, values=('Jonas', 'Teixeira', 'Jonas.Teixeira@email.com.br'))
        
        return tree


if __name__ == '__main__':
    root = tk.Tk()
    fr = Fr2(root, root)
    fr.pack()
    root.mainloop()
    # from main import Principal
    