import tkinter as tk
from tkinter import ttk
import math

class GameWindow(tk.Toplevel):
    def __init__(self, rows, cols, difficulty):

        super().__init__()
        
        self.title = "Minesweeper"
        self.configure(bg = "#282a36")
        
        mine_count_frame = tk.Frame(self, bg="#282a36")
        self.mine_count_img = tk.PhotoImage(file="./assets/white_mine.png")
        mine_count_img_label = tk.Label(mine_count_frame, image=self.mine_count_img, bg="#282a36")
        mine_count_img_label.grid(row=0, column=0)
        self.mine_count = tk.Label(mine_count_frame, text="this will be a number", fg="#f8f8f2", bg="#282a36")
        self.mine_count.grid(row=0, column=1)
        mine_count_frame.pack()
        # mine counter
        
        

class MinesweeperGrid():
    def __init__(self, rows, cols) -> None:
        pass
    

class MinesweeperCell(tk.Button):
    def __init__(self) -> None:
        pass
    
    
class MinesweeperSolution(list[list]):
    def __init__(self) -> None:
        pass
    
    
def calculate_mines(rows, cols, difficulty):
    mine_percentage = None
    match difficulty:
        case "easy":
            mine_percentage = 0.1
        case "medium":
            mine_percentage = 0.3
        case "hard":
            mine_percentage = 0.5
        case "hell":
            mine_percentage = 0.7
    total_cells = rows * cols
    total_mines = math.floor(mine_percentage * total_cells)
    return total_mines