import tkinter as Tk
from view.login_view import LoginView

if __name__ == "__main__":
    root = Tk()
    app = LoginView(root)
    root.mainloop()