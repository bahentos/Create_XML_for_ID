from tkinter import Tk, RIGHT, BOTH, RAISED, X, Y
from tkinter.ttk import Frame, Button, Style, Label, Entry


class AppWindow(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Создание XML для спуска")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self)
        frame.pack(fill=BOTH, expand=True)
        label = Label(frame, background="red")
        label.pack(fill=BOTH)


        frame1 = Frame(self, padding=[10, 10, 10, 10])
        frame1.pack(fill=BOTH, expand=True) 

        label1 = Label(frame1, text="Количество макетов на спуске", background="green")
        label1.pack(fill=BOTH)

        input1 = Entry(frame1)
        input1.pack(fill=BOTH)

        self.pack(fill=BOTH, expand=True)


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = AppWindow()
    root.mainloop()


if __name__ == '__main__':
    main()