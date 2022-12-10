import tkinter as tk
from tkinter import ttk
import math

class GameWindow(tk.Toplevel):
    def __init__(self, rows, cols, difficulty):

        super().__init__()
        
        self.title = "Minesweeper"
        
        self.mine_count_img = tk.PhotoImage(file="./assets/white_mine.png")
        tk.Label(self, image=self.mine_count_img).pack()
        
        
        # mine counter
        
        

class MinesweeperGrid():
    def __init__(self) -> None:
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