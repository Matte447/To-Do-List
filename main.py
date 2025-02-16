import tkinter as tk
import customtkinter as ctk


class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("To Do List")
        self.geometry("500x500")
        self.resizable(False, False)

        # Widgets

        self.label = ctk.CTkLabel(self, text="To Do List", font=("Arial", 36))
        self.label.pack(pady = 10)

        self.frame = ctk.CTkFrame(self, 500, 100, fg_color=None)
        self.frame.pack(pady = 10)

        self.entry_var = tk.StringVar()
        self.entry = ctk.CTkEntry(self.frame, 300, 28, 10, textvariable=self.entry_var)
        self.entry.pack(pady = 10, side = "left")

        self.add = ctk.CTkButton(self.frame, 40,text="Add", command=lambda: self.add_todo(self.entry_var.get()))
        self.add.pack(side="left")

        self.todo_frame = ctk.CTkFrame(self, 500)
        self.todo_frame.pack()

    def add_todo(self, text):
        if text != "":
            self.new = ctk.CTkLabel(self.todo_frame, text=text)
            self.new.pack()
        else:
            pass
        
        





if __name__ == "__main__":
    app = main()
    ctk.set_appearance_mode("system")
    app.mainloop()