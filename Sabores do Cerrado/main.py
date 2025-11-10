'''from tkinter import Tk
from view.login_principal_view import Application

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    print("Iniciando aplicação...")
    root.mainloop()'''

from tkinter import Tk, Toplevel
from view.login_principal_view import Application

if __name__ == "__main__":
    # Janela 1 (principal)
    root1 = Tk()
    app1 = Application(root1)
    root1.title("Janela 1 - Principal")
    
    # Janela 2 (secundária)
    root2 = Toplevel(root1)  # Toplevel depende da principal
    app2 = Application(root2)
    root2.title("Janela 2 - Secundária")
    
    print("Duas janelas iniciadas!")
    root1.mainloop()
    
