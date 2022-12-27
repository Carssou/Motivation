import tkinter as tk
from tkinter import ttk, StringVar
from random import randint



main = tk.Tk()

main.geometry('800x300')
main.config(background='#c6c5ef')
main.title('Motivation')

tabs = ttk.Notebook(main)

quotes = ttk.Frame(tabs)
journal = ttk.Frame(tabs)

tabs.add(quotes, text='Quotes')
tabs.add(journal, text='Journal')

tabs.pack(expand=True, fill='both')
# label



citations = StringVar()
 



l1 = tk.Label(main,text='Motivation Alpha ver 0.01',
            font=('Verdana',30,'bold'),
            bg='#c6c5ef').pack(expand=True, fill='both')

l2 = tk.Label(quotes,
            textvariable=citations,
            font=('Verdana',15,'bold'),
            bg='#c6c5ef'
            ).pack(expand=True, fill='both')

b1 = tk.Button(l2,
                text='Another quote',
                command=(lambda: quote()),
                font=('Arial', 15),
                bg='#c6c5ef').pack()

l3 = tk.Label(journal,
            text='Journal placeholder',
            font=('Verdana',20,'bold', 'italic'),
            bg='#c6c5ef',
            pady=50,
            padx=20).pack(expand=True, fill='both')



# ADD TEXT WIDGET FOR JOURNALING/THOUGHT INPUT





# l1.pack()
# l2.pack()
# l3.pack()
# b1.pack()
def quote():
    f = open('/Users/ludo/Python Scripts/citations.txt', 'r')

    citations_list = []

    for text in f:
        citations_list.append(text)
    citations.set(citations_list[randint(0,len(citations_list))])

quote()

main.mainloop() # display the window