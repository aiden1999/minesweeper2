import tkinter as tk


class Menu(tk.Tk):
    
    def __init__(self):

        super().__init__()
        
        self.difficulty = tk.StringVar
        self.title("Minesweeper - Game Setup")
        self.configure(bg="#282a36")
        
        menu_instructions = tk.Label(self, text="Choose game options",
            bg="#282a36", fg="#f8f8f2")
        menu_instructions.pack()
        
        rows_slider = tk.Scale(self, from_=5, to=100, orient="horizontal",
            length=400, label="Rows", bg="#282a36", fg="#f8f8f2")
        rows_slider.pack()
        
        cols_slider = tk.Scale(self, from_=5, to=100, orient="horizontal",
            length=400, label="Columns", bg="#282a36", fg="#f8f8f2")
        cols_slider.pack()
        
        difficulty_frame = tk.Frame(self, bg="#282a36")
        difficulty_instructions = tk.Label(difficulty_frame, text="Difficulty",fg="#f8f8f2", bg="#282a36")
        difficulty_instructions.pack()
        
        easy_radiobutton = tk.Radiobutton(difficulty_frame, text="Easy",
            value="easy", variable=self.difficulty)
        easy_radiobutton.pack(side="left")
        
        medium_radiobutton = tk.Radiobutton(difficulty_frame, text="Medium",
            value="medium", variable=self.difficulty)
        medium_radiobutton.pack(side="left")
        
        hard_radiobutton = tk.Radiobutton(difficulty_frame, text="Hard",
            value="hard", variable=self.difficulty)
        hard_radiobutton.pack(side="left")
        
        hell_radiobutton = tk.Radiobutton(difficulty_frame, text="Hell",
            value="hell", variable=self.difficulty)
        hell_radiobutton.pack(side="left")
        difficulty_frame.pack()
        
        ok_button = tk.Button(self, text="OK", command=self.ok_button_clicked)
        ok_button.pack(side="left")

    def ok_button_clicked():
        print("wow")