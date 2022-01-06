from tkinter import ttk
from tkinter import *

class Product:
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Products Application')

        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()