from tkinter import *
from itertools import *
import numpy as np

class Schedule:
    def __init__(self):
        self.fruit_basket = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']


    def count_iter(self):
        n = self.iter()
        answer = []
        p = 0
        for i in n:
            if len(i) == 7 and len(np.unique(i)) == 7:
                if i.index('kiwi') < i.index('apple') > i.index('pineapple'):
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
scrollbar = Scrollbar(orient="vertical", command=txt.yview)
info = Label(windowEntry, text=' У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню\n '
                               'полдника(1 фрукт) для ребенка на неделю. Доп. условие киви должно стоять в неделе\n'
                               'раньше яблока а ананас позже')


def pressed():
    txt.delete('1.0', END)
    s = Schedule()
    n = s.count_iter()
    txt.insert('1.0', 'Кол-во вариантов ' + str(n[1]) + '\n')
    for i in range(len(n[0])):
        txt.insert(END, (n[0][i]))
        txt.insert(END, ' - меню №' + str(i + 1))
        txt.insert(END, '\n')


button = Button(windowEntry, text='Продолжить', command=pressed)

button_exit = Button(windowEntry, text='Выход', command=lambda : exit())
lbl.place(x=30, y=150)
button.place(x=310, y=250)
button_exit.place(x=450, y=250)
txt.place(x=0, y=300)
scrollbar.place(x=785, y=300, height=400)
info.place(x=30, y=50)


txt["yscrollcommand"] = scrollbar.set
windowEntry.geometry('800x700')
windowEntry.mainloop()