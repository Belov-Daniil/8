from tkinter import *
from tkinter import ttk
from itertools import *
import numpy as np
import random


class Schedule:
    def __init__(self):
        self.fruit_basket = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']

    def count_iter(self, fruit_names):
        n = self.iter()
        answer = []
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if not (i.index(fruit_names[0]) < i.index(fruit_names[1]) < i.index(fruit_names[2])):
                    pass
                else:
                    p += 1
                    answer.append(i)
        return answer, p

    def iter(self):
        all_variants = []
        for i in permutations(self.fruit_basket, 7):
            all_variants.append(i)
        return all_variants


windowEntry = Tk()
windowEntry.title('Lab 8')


lbl = Label(windowEntry, width=80, text='Нажмите на кнопку чтобы полусить все возможные варианты меню на неделю')
txt = Text(windowEntry, width=100)
scrollbar = Scrollbar(windowEntry, orient="vertical", command=txt.yview)
fruts = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']
fruit1 = ttk.Combobox(windowEntry, values=fruts)
fruit2 = ttk.Combobox(windowEntry, values=fruts)
fruit3 = ttk.Combobox(windowEntry, values=fruts)
fruit1.set('apple')
fruit2.set('pineapple')
fruit3.set('orange')
info = Label(windowEntry, text=' У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню\n '
                               'полдника(1 фрукт) для ребенка на неделю. В качестве усложнения составления расписания\n'
                               ' напишите три фрукта из представленных на выбор:\n'
                               ' apple, pineapple, orange, banana, pear, kiwi, avocado\n'
                               ' Они будут стоять в меню таким обазом - Фрукт 1 будет всегда до фрукта 2,'
                               ' а фрукт 3 будет после фрукта 2')


def pressed():
    txt.delete('1.0', END)
    s = Schedule()
    if fruit1.get() == fruit2.get() or fruit1.get() == fruit3.get() or fruit2.get() == fruit3.get():
        txt.insert(END, 'Выберете разные фрукты')
    else:
        try:
            n = s.count_iter([fruit1.get(), fruit2.get(), fruit3.get()])
        except ValueError:
            txt.insert(END, 'Выберете из предложанных фруктов')
            return
        txt.insert('1.0', 'Кол-во вариантов ' + str(n[1]) + '\n')
        random.shuffle(n[0])
        for i in range(len(n[0])):
            txt.insert(END, (n[0][i]))
            txt.insert(END, ' - меню №' + str(i + 1))
            txt.insert(END, '\n')


button = Button(windowEntry, text='Продолжить', command=pressed)

button_exit = Button(windowEntry, text='Выход', command=lambda : exit())
fruit1.place(x=50, y=200)
fruit2.place(x=260, y=200)
fruit3.place(x=470, y=200)
lbl.place(x=30, y=170)
button.place(x=310, y=250)
button_exit.place(x=450, y=250)
txt.place(x=0, y=300)
scrollbar.place(x=785, y=300, height=400)
info.place(x=30, y=50)


txt["yscrollcommand"] = scrollbar.set
windowEntry.geometry('800x700')
windowEntry.mainloop()
