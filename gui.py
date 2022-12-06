import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):

        self.window=tk.Tk()
        self.file='gg'
        self.speed=1

        self.label= tk.Label(self.window, text='Input file name and press Input')
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.window, height=1)
        self.textbox.pack()

        self.button=tk.Button(self.window, text='Input', command=self.assign_message)
        self.button.pack(padx=10,pady=10)

        self.speed_label=tk.Label(self.window, text='Speed of car: ')
        self.speed_label.pack(pady=10)
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btnslow = tk.Button(self.buttonframe, text='Slow', command=self.assign_speed_slow)
        self.btnslow.grid(row=0, column=0, sticky='news')

        self.btnmed = tk.Button(self.buttonframe, text='Medium', command=self.assign_speed_med)
        self.btnmed.grid(row=0, column=1, sticky='news')

        self.btnfast = tk.Button(self.buttonframe, text='Fast', command=self.assign_speed_fast)
        self.btnfast.grid(row=0, column=2, sticky='news')

        self.buttonframe.pack(fill='x')


        self.window.mainloop()

    def assign_message(self):
        self.file=self.textbox.get('1.0',tk.END)
        print('File name received')
    def assign_speed_slow(self):
        self.speed=1
        self.window.destroy()

    def assign_speed_med(self):
        self.speed=2
        self.window.destroy()

    def assign_speed_fast(self):
        self.speed=3
        self.window.destroy()

