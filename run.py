import tkinter as tk
from get_info import Word

window = tk.Tk()

def run():
    label = tk.Label(text='Enter Word:')
    label.pack()

    entry = tk.Entry()
    entry.pack()

    def callback():
        word = entry.get()
        word = Word(word.upper())
        meaning = word.get_info()[0][0]

        label = tk.Label(text='Meaning(s): {0}'.format(meaning))
        label.pack()

        again = tk.Button(window, text='Again', width=10, command=run)
        again.pack()

    button = tk.Button(window, text='Get Meaning', width=10, command=callback)
    button.pack()

    window.mainloop()

run()


# Better GUI
# Fix when no meanings