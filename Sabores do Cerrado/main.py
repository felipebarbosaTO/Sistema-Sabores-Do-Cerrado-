import tkinter as Tk
from view.login_view import PrincipalView

if __name__ == "__main__":
    root = Tk()
    app = PrincipalView(root)
    root.mainloop()