import tkinter
import boggle_gui
import winsound


class Timer:
    background = "steel blue"
    font_color = "LightBlue1"

    def __init__(self, root):
        self.__timer = root
        self.sec_label = tkinter.Label(self.__timer, text="00", font=("aharoni", 32))
        self.sep_label = tkinter.Label(self.__timer, text=":", font=("aharoni", 32))
        self.min_label = tkinter.Label(self.__timer, text="02", font=("aharoni", 32))
        self.min_label.config(bg=self.background, fg="gray95")
        self.sep_label.config(bg=self.background, fg="gray95")
        self.sec_label.config(bg=self.background, fg="gray95")

        self.min_label.grid(row=2, column=1)
        self.sep_label.grid(row=2, column=2)
        self.sec_label.grid(row=2, column=3)
        self.minutes = 2
        self.seconds = 0
        self.__timer.after(1000, self.timer_handler)

    def timer_handler(self):
        # logic
        if self.minutes == 0 and self.seconds == 10:
            self.min_label.config(fg="orange red")
            self.sep_label.config(fg="orange red")
            self.sec_label.config(fg="orange red")
        if self.minutes == 0 and self.seconds == 0:  # End of timer
            self.min_label.configure(text="E")
            self.sep_label.configure(text="N")
            self.sec_label.configure(text="D")
            winsound.PlaySound("sounds/game_over.WAV", winsound.SND_FILENAME)
            return
        if self.seconds == 0 and self.minutes > 0:  # Minute change
            self.minutes -= 1
            self.seconds = 59
        else:  # Regular second change
            self.seconds -= 1
        self.paint_timer()
        self.__timer.after(1000, self.timer_handler)

    def paint_timer(self):
        self.min_label.configure(text="0" + str(self.minutes))
        if len(str(self.seconds)) == 1:
            self.sec_label.configure(text="0" + str(self.seconds))
        else:
            self.sec_label.configure(text=self.seconds)

