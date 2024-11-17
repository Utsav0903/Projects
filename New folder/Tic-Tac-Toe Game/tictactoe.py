import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.canvas = tk.Canvas(master, width=300, height=300, bg="lightblue")
        self.canvas.pack()

        self.player1_name = simpledialog.askstring("Player 1", "Enter Player 1's name:")
        self.player2_name = simpledialog.askstring("Player 2", "Enter Player 2's name:")
        
        self.current_player = "X"
        self.board = [""] * 9

        self.draw_board()
        self.canvas.bind("<Button-1>", self.make_move)

    def draw_board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, fill="lightblue")
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=2)
            self.canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=2)

    def make_move(self, event):
        x = event.x // 100
        y = event.y // 100
        index = y * 3 + x

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.draw_symbol(x, y)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.get_current_player_name()} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_symbol(self, x, y):
        if self.current_player == "X":
            self.canvas.create_line(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, fill="red", width=5)
            self.canvas.create_line(x * 100 + 90, y * 100 + 10, x * 100 + 10, y * 100 + 90, fill="red", width=5)
        else:
            self.canvas.create_oval(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, outline="blue", width=5)

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def get_current_player_name(self):
        return self.player1_name if self.current_player == "X" else self.player2_name

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.canvas.delete("all")
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

    