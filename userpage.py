from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class Application:
    def __init__(self, master=None):
        pass
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Pagina de utilizador')

panelOpçoes = PanedWindow(window, bg = "gray", width=250, height=500)
panelOpçoes.place(x=0, y=0)

mainloop()