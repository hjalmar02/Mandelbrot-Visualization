import sys
from math import ceil
from datetime import timedelta
from keyboard import is_pressed
import time

class ProgressBar:
    def __init__(self, width, target, current=0):
        self.width = width
        self.target = target
        self.current = current
        self.avg_time = None

    def update(self, show_percentage=True, show_time=True):
        bars = ceil(self.width * self.current/self.target)
        percent = round(self.current/self.target*100, 1)
        sys.stdout.write("\r")
        if show_percentage:
            sys.stdout.write(str(percent)+" % ")
            if len(str(percent)) == 2:
                sys.stdout.write(" "*2)
        sys.stdout.write("[{}{}]".format("|"*bars, " "*(self.width-bars)))
        if self.avg_time and show_time:
            remaining_time = timedelta(seconds=int(self.avg_time*(self.target-self.current)))
            sys.stdout.write(f" Est. time: {remaining_time}")


class OptionMenu:
    def __init__(self, options, clear=True):
        self.options = options
        self.clear = clear
        self.selection = 0

    def input(self, prompt):
        while True:
            self.draw(prompt+" ")
            if is_pressed("right") or is_pressed("num 6"):
                if self.selection < len(self.options) - 1:
                    self.selection += 1
            if is_pressed("left") or is_pressed("num 4"):
                if self.selection > 0:
                    self.selection -= 1
            if is_pressed("return"):
                sys.stdout.write("\r")
                return self.options[self.selection]
            time.sleep(0.1)

    def draw(self, prompt):
        sys.stdout.write("\r")
        sys.stdout.write(prompt)
        sys.stdout.write(self.options[self.selection])


    def moveleft(self):
        self.selection += 1


if __name__ == "__main__":
    test = OptionMenu(['test1', 'test2', 'test3'])
    #test.input("Resolution [⮜⮞]:")
    print({'test1': 'hello', 'test2': 'hey', 'test3': 'whatsup'}[test.input("Resolution [⮜⮞]:")])


