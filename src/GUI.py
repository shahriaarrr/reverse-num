from tkinter import *

def main(n, lbl):
    x = n
    y = 0
    while(x > 0):
        y = y * 10 + (x % 10)
        x = x // 10
    lbl.config(text=str(y))

class WINDOW():
    def __init__(self):
        self.win = Tk()

        self.config_title = 'reverse number'
        self.config_width = 250
        self.confing_heigt = 250
        self.config_resizable = [False, False]
        self.config_background = '#00FC39'

        self.Load_Configs()
        self.Load_objects()



        mainloop()

    def  Load_Configs(self):
        self.win.title(self.config_title)
        self.win.geometry(str(self.config_width) + 'x' + str(self.confing_heigt))
        self.win.resizable(self.config_resizable[0], self.config_resizable[1])
        self.win.config(bg = self.config_background)

    def reverse(self):
        a = self.number_in.get()
        main(a)

    def Load_objects(self):
        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 10)
        ).pack()

        Label(
            self.win,
            text = "your number: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10, 'bold') ,
        ).pack()

        number_in = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 34,
        )
        self.number_in = number_in
        number_in.pack()

        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 5)
        ).pack()

        reverse_button = Button(
            self.win,
            text = 'reverse',
            background = '#FC7E00',
            foreground = 'black',
            border = 5,
        )
        reverse_button.config(command = self.reverse)
        reverse_button.pack()

        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 30)
        ).pack()

        Label(
            self.win,
            text = "reverse: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10, 'bold') ,
        ).pack()

        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 5)
        ).pack()

        number_in = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 34,
        )
        self.number_in = number_in
        number_in.pack()

app = WINDOW()