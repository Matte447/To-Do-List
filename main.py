import tkinter as tk
import customtkinter as ctk


class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("To Do List")
        self.geometry("500x500")
        self.resizable(False, False)




if __name__ == "__main__":
    app = main()
    ctk.set_appearance_mode("system")
    app.mainloop()