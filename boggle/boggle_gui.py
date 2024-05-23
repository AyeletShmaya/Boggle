import tkinter as tk
from boggle_board_randomizer import *
from timer import *
from functools import partial
import winsound


class BoggleGui:
    button_font = "aharoni"
    general_font = "Comic Sans MS"
    background = "steel blue"
    font_color = "LightBlue1"

    def __init__(self, board):
        self.root = tk.Tk()
        self.board_letters = board
        self.board_buttons = []
        self.timer = None
        self.word = None
        self.words = None
        self.score = None
        self.check = None
        self.reset = None
        self.path = []

    def set_game(self):
        self.root.geometry("675x750")
        self.root.config(bg=self.background)
        title = tk.Frame(self.root)
        boggle_title = tk.Label(
            title,
            text="BOGGLE: THE GAME",
            bg=self.background,
            fg=self.font_color,
            font=(self.general_font, 24, "bold"),
        )
        boggle_title.pack()
        title.grid(row=0, column=0)

        timer_frame = tk.Frame(self.root)
        self.timer = Timer(timer_frame)
        timer_frame.grid(row=1, column=0)

        check_reset_frame = tk.Frame(self.root)
        self.check = tk.Button(
            check_reset_frame,
            text="CHECK",
            font=(self.button_font, 20),
            bg=self.font_color,
        )
        self.check.pack(side=tk.LEFT, padx=10)
        check_reset_frame.config(bg=self.background)
        check_reset_frame.grid(row=2, column=0)

        # reset_frame = tk.Frame(self.root)
        self.reset = tk.Button(
            check_reset_frame,
            text="RESET",
            font=(self.button_font, 20),
            bg=self.font_color,
        )
        self.reset.bind("<Button-1>", self.reset_action)
        self.reset.pack(side=tk.RIGHT, padx=10)
        # reset_frame.grid(row=2, column=1)

        current_word = tk.Frame(self.root)
        self.word = tk.Label(
            current_word,
            text="",
            font=(self.button_font, 18),
            bg=self.background,
            fg=self.font_color,
        )
        self.word.pack()
        current_word.grid(row=3, column=0, pady=10)

        # score_frame = tk.Frame(self.root)
        # score_title = tk.Label(score_frame, text="score:", font=BoggleGui.text_font)
        # score_title.config(width=10, height=2)
        # score_title.pack()

        score_frame = tk.Frame(self.root)
        self.score = tk.Label(
            score_frame,
            text="0",
            font=(self.button_font, 26),
            fg=self.font_color,
            bg=self.background,
        )
        score_title = tk.Label(
            score_frame,
            text="SCORE: ",
            fg=self.font_color,
            bg=self.background,
            font=(self.button_font, 18, "bold"),
        )
        # self.score.config(width=10, height=2)
        self.score.pack(side=tk.BOTTOM)
        score_title.pack(side=tk.TOP)
        score_frame.config(bg=self.background)
        score_frame.grid(row=1, column=1)

        words_frame = tk.Frame(self.root)
        self.words = tk.Label(
            words_frame,
            font=(self.button_font, 15, "italic"),
            fg="SteelBlue4",
            bg="LightSkyBlue1",
            height=20,
            width=10,
        )
        word_title = tk.Label(
            self.root,
            text="WORDS FOUND:",
            fg=self.font_color,
            bg=self.background,
            font=(self.button_font, 16, "bold"),
        )

        text = tk.Text(words_frame)
        scrollbar = tk.Scrollbar(words_frame, orient="vertical", command=text.yview)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.words.pack(side=tk.TOP, anchor="s")
        text.config(yscrollcommand=scrollbar.set)
        word_title.grid(row=3, column=1, columnspan=2)
        words_frame.config(height=17, width=10)
        words_frame.grid(row=4, column=1, padx=15)

        board = tk.Frame(self.root)
        for row in range(len(self.board_letters)):
            self.board_buttons.append([])
            for col in range(len(self.board_letters[0])):
                button = tk.Button(
                    board,
                    text=self.board_letters[row][col],
                    font=(self.button_font, 18),
                    activeforeground="DarkOrange3",
                )
                # button.bind("<Button-1>", self.on_press)
                press = partial(self.on_press, row, col)
                button.bind("<Button-1>", press, add="+")
                button.config(bg="LightSkyBlue1", fg="navy")
                button.config(width=7, height=3, relief="flat")
                button.grid(row=row, column=col, padx=5, pady=5)
                self.board_buttons[row].append(button)
        board.config(bg="tan1")
        board.grid(row=4, column=0)

    def run_game(self):
        self.root.mainloop()

    def possible_moves(self):
        POSSIBLE_MOVES = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        x, y = self.path[-1]
        return [
            (x + move[0], y + move[1])
            for move in POSSIBLE_MOVES
            if (x + move[0], y + move[1]) not in self.path
        ]

    def on_press(self, row, col, e):
        if len(self.path) == 0 or (row, col) in self.possible_moves():
            if e.widget.cget("bg") == "gray91":
                e.widget.config(bg="LightSkyBlue1")
                e.widget.config(fg="navy")
                return

            e.widget.config(bg="grey91")
            e.widget.config(fg="tan4")

            winsound.PlaySound("sounds/button_press.WAV", winsound.SND_FILENAME)
            __word = self.word.cget("text") + e.widget.cget("text")
            self.word.config(text=__word)
            self.path.append((row, col))
            # print(self.path)
        else:
            self.reset_action()

    def reset_action(self, e=None):
        for row in range(len(self.board_buttons)):
            for col in range(len(self.board_buttons[0])):
                self.board_buttons[row][col].config(bg="LightSkyBlue1")
                self.board_buttons[row][col].config(fg="navy")

        self.word.config(text="")
        self.word.config(fg=self.font_color)
        self.path = []

