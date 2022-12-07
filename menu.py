import tkinter as tk


class Menu(tk.Tk):

    def __init__(self) -> None:

        super().__init__()
        
        self.difficulty = tk.StringVar
        
        menu_instructions = tk.Label(self, text="Choose game options")
        menu_instructions.pack()
        rows_slider = tk.Scale(self, from_=5, to=100, orient="horizontal",
                               length=400, label="Choose the number of rows")
        rows_slider.pack()
        cols_slider = tk.Scale(self, from_=5, to=100, orient="horizontal",
                               length=400, label="Choose the number of columns")
        cols_slider.pack()
        difficulty_frame = tk.Frame(self)
        difficulty_instructions = tk.Label(difficulty_frame, text="Choose a difficulty")
        difficulty_instructions.pack()
        easy_radiobutton = tk.Radiobutton(difficulty_frame, text="Easy",
                                          value="easy", variable=self.difficulty)
        easy_radiobutton.pack(side="left")
        medium_radiobutton = tk.Radiobutton(difficulty_frame, text="Medium",
                                            value="medium",
                                            variable=self.difficulty)
        medium_radiobutton.pack(side="left")
        hard_radiobutton = tk.Radiobutton(difficulty_frame, text="Hard",
                                          value="hard", variable=self.difficulty)
        hard_radiobutton.pack(side="left")
        hell_radiobutton = tk.Radiobutton(difficulty_frame, text="Hell",
                                          value="hell", variable=self.difficulty)
        hell_radiobutton.pack(side="left")
        difficulty_frame.pack()
        

