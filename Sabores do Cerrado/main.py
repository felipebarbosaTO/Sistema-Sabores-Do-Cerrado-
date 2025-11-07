from tkinter import Tk
from view.login_principal_view import Application

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    print("Iniciarndo aplicação...")
    root.mainloop()