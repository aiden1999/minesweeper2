import tkinter as tk
import math
import random

class GameWindow(tk.Toplevel):
    def __init__(self, rows: int, cols: int, difficulty: str):

        super().__init__()
        
        self.title = "Minesweeper"
        self.configure(bg = "#282a36")
        self.rows = rows
        self.cols = cols
        self.difficulty = difficulty
        self.cleared_colour = "#282a36"
        self.solution = None
        
        mine_count_frame = tk.Frame(self, bg="#282a36")
        self.mine_count_img = tk.PhotoImage(file="./assets/white_mine.png")
        mine_count_img_label = tk.Label(mine_count_frame, image=self.mine_count_img, bg="#282a36")
        mine_count_img_label.grid(row=0, column=0)
        
        self.mine_total = calculate_mines(self.rows, self.cols, self.difficulty)
        self.mine_counter = tk.Label(mine_count_frame, text=self.mine_total, fg="#f8f8f2", bg="#282a36", font=("Comic Sans MS", "20"))
        self.mine_counter.grid(row=0, column=1)
        mine_count_frame.pack()

        game_grid = tk.Frame(self, bg="#282a36")
        self.game_cells = [[tk.Label(game_grid) for i in range(self.cols)] for i in range(self.rows)]
        for x in range(self.cols):
            for y in range(self.rows):
                btn_text = row_col_to_rc(y, x, cols)  # testing
                self.game_cells[y][x].configure(text=btn_text)  # testing
                self.game_cells[y][x].configure(height=1, width=2, bg="#21222b")
                self.game_cells[y][x].grid(row=y, column=x, padx=1, pady=1)
                self.game_cells[y][x].bind("<Button-1>", lambda event, col=x, row=y: self.left_click(row, col))
                self.game_cells[y][x].bind("<Button-2>", lambda event, col=x, row=y: self.right_click(row, col))
                self.game_cells[y][x].bind("<Button-3>", lambda event, col=x, row=y: self.right_click(row, col))
        game_grid.pack(padx=5, pady=5)
        
        self.initial_click = True
        
    def left_click(self, row: int, col: int):
        if self.initial_click:
            self.solution = generate_puzzle(row, col, self.rows, self.cols, self.mine_total)
            self.game_cells[col][row].configure(bg=self.cleared_colour)
            self.blank_clear()
            self.initial_click = False
    
    def right_click(self, row: int, col: int):
        print("right click")
        
    def blank_clear(self):
        check_again = True
        while check_again:
            check_again = False
            for x in range(self.rows):
                for y in range(self.cols):
                    if (self.game_cells[y][x].cget("bg") == self.cleared_colour)and (self.game_cells[y][x].cget("image") == None):
                        adj_cells = adj_rc(y, x, self.rows, self.cols)
                        for cell in adj_cells:
                            adj_row, adj_col = rc_to_row_col(cell, self.cols)
                            self.game_cells[adj_col][adj_row].configure(bg=self.cleared_colour)
                            rc_adj = row_col_to_rc(adj_row, adj_col, self.cols)
                            if self.solution[rc_adj] == 0:
                                check_again = True
                            else:
                                self.show_number(adj_row, adj_col, self.solution[rc_adj])
                                
    
    def show_number(self, row, col, value):
        match value:
            case 1:
                num_img = tk.PhotoImage(file="./assets/number_1.png")
            case 2:
                num_img = tk.PhotoImage(file="./assets/number_2.png")
            case 3:
                num_img = tk.PhotoImage(file="./assets/number_3.png")
            case 4:
                num_img = tk.PhotoImage(file="./assets/number_4.png")
            case 5:
                num_img = tk.PhotoImage(file="./assets/number_5.png")
            case 6:
                num_img = tk.PhotoImage(file="./assets/number_6.png")
            case 7:
                num_img = tk.PhotoImage(file="./assets/number_7.png")
            case 8:
                num_img = tk.PhotoImage(file="./assets/number_8.png")
        self.game_cells[col][row].configure(image=num_img)
                            
    
def calculate_mines(rows: int, cols: int, difficulty: str) -> int:
    mine_percentage = 0
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


def generate_puzzle(initial_row: int, initial_col: int, rows: int, cols: int, mine_total: int) -> list[int]:
    sln = [0 for i in range(cols * rows)]
    initial_adj = adj_rc(initial_row, initial_col, rows, cols)
    initial_rc = row_col_to_rc(initial_row, initial_col, cols)
    initial_adj.append(initial_rc)
    while mine_total > 0:
        rc_random = random.randrange(0, rows * cols)
        print(sln[rc_random])  # testing
        print(rc_random)
        if rc_random in initial_adj:
            pass
        elif sln[rc_random] == 9:
            pass
        else:
            sln[rc_random] = 9
            mine_total = mine_total - 1
    for x in range(cols):
        for y in range(rows):
            current_rc = row_col_to_rc(y, x, cols)
            if sln[current_rc] != 9:
                adj_cells = adj_rc(y, x, rows, cols)
                for cell in adj_cells:
                    if sln[cell] == 9:
                        sln[current_rc] = sln[current_rc] + 1
    return sln
 
 
def row_col_to_rc(row: int, col: int, cols: int) -> int:
    return (row * cols) + col


def rc_to_row_col(rc: int, cols: int) -> tuple[int, int]:
    row = rc // cols
    col = rc % cols
    return row, col


def adj_rc(row: int, col: int, rows: int, cols: int) -> list[int]:
    adj_cells = []
    row_max = rows - 1
    col_max = cols - 1
    if row == 0:  # top row
        adj_cells.append(row_col_to_rc(row + 1, col, cols))
        if col == 0:  # top left corner
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col + 1, cols))
        elif col == col_max:  # top right corner
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col - 1, cols))
        else:
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col + 1, cols))
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col - 1, cols))    
    elif row == row_max:  # bottom row
        adj_cells.append(row_col_to_rc(row - 1, col, cols))
        if col == 0:  # bottom left corner
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col + 1, cols))
        elif col == col_max:  # bottom right corner
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col - 1, cols))
        else:
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col + 1, cols))
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col - 1, cols)) 
    else:
        adj_cells.append(row_col_to_rc(row + 1, col, cols))
        adj_cells.append(row_col_to_rc(row - 1, col, cols))
        if col == 0:  # left column
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col + 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col + 1, cols))
        elif col == col_max:  # right column
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col - 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col - 1, cols))
        else:
            adj_cells.append(row_col_to_rc(row, col + 1, cols))
            adj_cells.append(row_col_to_rc(row, col - 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col + 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col + 1, cols))
            adj_cells.append(row_col_to_rc(row + 1, col - 1, cols))
            adj_cells.append(row_col_to_rc(row - 1, col - 1, cols))
    return adj_cells

