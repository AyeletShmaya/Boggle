from boggle_board_randomizer import *
import ex11_utils as utils

class BoggleModel:
    def __init__(self, board):
        self.board = board
        self.score = 0
        self.words = open_words_file("boggle_dict.txt")
        self.words_found = set()

    def check_valid_path(self, path):
        word = utils.is_valid_path(self.board, path, self.words)
        return word

    def add_word(self, word):
        self.words_found.add(word) # update words set
        self.score += len(word) ** 2 # update score


    def get_board(self):
        return self.board

    def get_words(self):
        return self.board

    def get_words_found(self):
        return self.board

def open_words_file(file_name):
    words = []
    with open(file_name) as Words_dict:
        for word in Words_dict:
            words.append(word.split()[0])
    
    return words

