from boggle_gui import *
from boggle_board_randomizer import *
from boggle_model import *
import winsound


class BoggleController:
    def __init__(self):
        board_1 = [
            ["A", "D", "O", "B"],
            ["D", "S", "U", "R"],
            ["O", "T", "A", "N"],
            ["O", "R", "I", "W"],
        ]
        self.model = BoggleModel(board_1)

        self.gui = BoggleGui(self.model.get_board())

    def start_game(self):
        self.gui.set_game()
        self.gui.check.bind("<Button-1>", lambda e: self.check(e))
        self.gui.run_game()

    def check(self, e):
        word = self.model.check_valid_path(self.gui.path)
        if word and word not in self.model.words_found:
            self.gui.words.configure(
                text=self.gui.words.cget("text") + "\n" + word, anchor="n"
            )
            self.gui.word.configure(fg="pale green")
            self.gui.score.config(
                text=int(self.gui.score.cget("text")) + (len(self.gui.path) ** 2)
            )
            self.model.add_word(word)
            winsound.PlaySound("right_short.WAV", winsound.SND_FILENAME)

        elif word in self.model.words_found:
            self.gui.word.configure(fg="gold")
            winsound.PlaySound("already_guessed.WAV", winsound.SND_FILENAME)

        else:
            self.gui.word.configure(fg="orange red")
            winsound.PlaySound("wrong_short.WAV", winsound.SND_FILENAME)

        self.gui.root.after(500, self.gui.reset_action)

    # def check(self, e):
    #     __word = self.__actions["check_valid_path"](self.__path)
    #     if __word:
    #         self.__words.configure(text = self.__words.cget("text") + "\n" + __word)
    #         self.__word.configure(fg="green")
    #         self.__score.config(text = int(self.__score.cget("text")) + (len(self.__path)**2))
    #     else:
    #         self.__word.configure(fg="red")

    #     self.root.after(500, self.reset)


def main():
    controller = BoggleController()
    controller.start_game()


if __name__ == "__main__":
    main()
