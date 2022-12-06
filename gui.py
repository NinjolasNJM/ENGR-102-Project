# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Nicholas Mirabal
#               Eli Valentino
#               Chris Avila
# Section:      102-565
# Assignment:   Project
# Date:         6 December 2022
import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):
        """elivalentino@tamu.edu
        This function creates the gui by placing all the buttons and labels
        that people can interact with
        """
        self.window = tk.Tk('500x600')
        self.file = ''
        self.speed = 1
        self.check=0

        self.window.title('Map Your File!')

        self.label= tk.Label(self.window, text='Input file name and press Input', font=('Arial',14))
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.window, height=1)
        self.textbox.pack()

        self.button=tk.Button(self.window, text='Input', command=self.assign_message)
        self.button.pack(padx=10,pady=10)

        self.l2 = tk.Label()
        self.l2.pack(pady=5)
        self.speed_label=tk.Label(self.window, text='Speed of car: ', font=('Arial',14))
        self.speed_label.pack(pady=10)
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btnslow = tk.Button(self.buttonframe, text='Slow',bg='white', command=self.assign_speed_slow)
        self.btnslow.grid(row=0, column=0, sticky='ew')

        self.btnmed = tk.Button(self.buttonframe, text='Medium', bg='white', command=self.assign_speed_med)
        self.btnmed.grid(row=0, column=1, sticky='ew')

        self.btnfast = tk.Button(self.buttonframe, text='Fast', bg='white', command=self.assign_speed_fast)
        self.btnfast.grid(row=0, column=2, sticky='ew')

        self.buttonframe.pack(fill='x')



        self.l1 = tk.Label()
        self.l1.pack(pady=10)
        self.gobtn=tk.Button(text='Go',height=3,width=16,bg='white', command=self.go)
        self.gobtn.pack(pady=10)
        self.window.mainloop()

    def assign_message(self):
        """
        elivalentino @ tamu.edu
        This function assigns the text inputted by the user to a variable to save the file name
        """
        self.file=self.textbox.get('1.0',tk.END)
        print('File name received')
    def assign_speed_slow(self):
        """elivalentino@tamu.edu
        This function changes the color of the slow button when pressed and assigns the speed variable to slow
        """
        self.speed=1
        self.btnslow = tk.Button(self.buttonframe, text='Slow',bg='green', command=self.assign_speed_slow)
        self.btnslow.grid(row=0, column=0, sticky='ew')
        self.btnmed = tk.Button(self.buttonframe, text='Medium', bg='white', command=self.assign_speed_med)
        self.btnmed.grid(row=0, column=1, sticky='ew')
        self.btnfast = tk.Button(self.buttonframe, text='Fast', bg='white', command=self.assign_speed_fast)
        self.btnfast.grid(row=0, column=2, sticky='ew')

    def assign_speed_med(self):
        """elivalentino@tamu.edu
        This function changes the color of the med button when pressed and assigns the speed variable to med
         """
        self.speed=2
        self.btnslow = tk.Button(self.buttonframe, text='Slow', bg='white', command=self.assign_speed_slow)
        self.btnslow.grid(row=0, column=0, sticky='ew')
        self.btnmed = tk.Button(self.buttonframe, text='Medium', bg='green', command=self.assign_speed_med)
        self.btnmed.grid(row=0, column=1, sticky='ew')
        self.btnfast = tk.Button(self.buttonframe, text='Fast', bg='white', command=self.assign_speed_fast)
        self.btnfast.grid(row=0, column=2, sticky='ew')

    def assign_speed_fast(self):
        """elivalentino@tamu.edu
        This function changes the color of the fast button when pressed and assigns the speed variable to fast
        """
        self.speed=3
        self.btnslow = tk.Button(self.buttonframe, text='Slow', bg='white', command=self.assign_speed_slow)
        self.btnslow.grid(row=0, column=0, sticky='ew')
        self.btnmed = tk.Button(self.buttonframe, text='Medium', bg='white', command=self.assign_speed_med)
        self.btnmed.grid(row=0, column=1, sticky='ew')
        self.btnfast = tk.Button(self.buttonframe, text='Fast', bg='green', command=self.assign_speed_fast)
        self.btnfast.grid(row=0, column=2, sticky='ew')

    def go(self):
        """elivalentino@tamu.edu
        This function commands the go button to close the gui but only if the file can be found
        """
        self.check=0
        try:
            file=open(self.file.split()[0]).read()
        except:
            print('File not found')
            self.check=1

        if self.check==0:

            self.window.destroy()