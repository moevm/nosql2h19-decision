import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from pymemcache.client import base
import re
import random
def get_values(string):
    values = client.get(string)
    values = values.decode()
    values = values.replace("[", '')
    values = values.replace("]", '')
    values = values.replace("'", '')
    values = values.replace(",", '')
    values = values.split(" ")
    return values
def fill():
    global car_header
    global car_header1
    global car_header2
    global car_list
    global car_list1
    global car_list2
    global specialities
    global inf_sys
    global inf
    global comp_sci
    global specialities
    car_header = ['№', 'КУРС', 'ФАКУЛЬТЕТ', 'СПЕЦИАЛЬНОСТЬ']
    car_header1 = ['ИМЯ ПРЕПОДАВАТЕЛЯ', 'ПРЕДМЕТ', 'СРЕДНИЙ БАЛЛ']
    car_header2 = ['ПРЕДМЕТ', 'РЕЙТИНГ']
    car_list1 = [['Anatoly Zagupalovich','78',],['Andrey Tatishenko','87'],['Kurman Zubaev','63'],['Vladimir Dnishev','91'],
                 ["Sergey Ermolenko","26"],["Vadim Zalokoysky","46"],["Anton Zabe","59"],["Viktor Kolomoysky","89"],
                 ["Sergey Dnepropetrenko","95"],["Petr Zakhudalov","95.8"],["Alexey Starozhilov","75"],["Daniil Poperechnyi","75"]]


    car_list1 = [['Anatoly Zagupalovich','Basics of Numerical Analysis', '89'], ['Andrey Tatishenko','Information theory', '55'], ['Kurman Zubaev','Programming basics', '78'],
                 ['Vladimir Dnishev','Java programming', '96'],
                 ["Sergey Ermolenko","Basics of Computer Science", "100"], ["Vadim Zalokoysky","3D modelling", "55"], ["Anton Zabe","C++ Programming", "87"],
                 ["Viktor Kolomoysky","Algorithms", "99"],
                 ["Sergey Dnepropetrenko","Basics of Information systems", "74"], ["Petr Zakhudalov","Fundamentals of Numerical Methods", "89"],
                 ["Alexey Starozhilov","Cisco programming", "95"], ["Daniil Poperechnyi","Object-oriented programming", "51"]]


    specialities = get_values('list_of_specs')
    print(specialities)
    l = specialities
    n = 4
    specialities = [l[i:i + n] for i in range(0, len(l), n)]
    print(specialities)
    car_list = specialities
    car_list2 = [['Basics of Numerical Analysis','89'],['Information theory','55'],['Programming basics','78'],['Java programming','96'],
                 ["Basics of Computer Science","100"],["3D modelling","55"],["C++ Programming","87"],["Algorithms","99"],
                 ["Basics of Information systems","74"],["Fundamentals of Numerical Methods","89"],["Cisco programming","95"],["Object-oriented programming","51"]]
class MultiColumnListbox2(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 14))
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=car_header2, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in car_header2:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in car_list2:
            self.tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header2[ix],width=None)<col_w:
                    self.tree.column(car_header2[ix], width=col_w)

def add_student_to_mem(surname_but_ent,faculty_but_ent,name_but_ent,group_but_ent,otchestvo_but_ent,specialnost_but_ent):
    ar = get_values(specialnost_but_ent)
    ar.append(surname_but_ent+"_"+name_but_ent+"_"+otchestvo_but_ent)
    client.set(specialnost_but_ent,ar)
    print(client.get(specialnost_but_ent))
def memcache_work():
    global client
    client = base.Client(('localhost', 11211))
    client.set('list_of_specs', [["1", "4", "Computer_systems", "Information_systems"],
                                 ["2", "4", "Professional_education", "Informatica"],
                                 ["3", "3", "Computer_systems", "Computer_Science"],
                                 ])
    client.set('Information_systems', [["1.Ivanov_Ivan_Ivanovich"],
                                    ["2.Petrov_Petr_Petrovich"],
                                    ["3.Vasiliev_Vasiliy_Vasilievich"],
                                    ["4.Koshkina_Yulia_Andreevna"],
                                    ["5.Tsvetkova_Anastasia_Aleksandrovna"]])

    client.set("Informatica", [["1.Andreev_Andrey_Andreevich"],
                                ["2.Alexeyev_Alexey_Alexeyevich"],
                                ["3.Dmitriev_Dmitriy_Dmitriyevich"]])

    client.set("Computer_Science", [["1.Vasilieva_Vasilisa_Vasilievna"],
                                    ["2.Vasiliyev_Vasliliy_Vasiliyevich"],
                                    ["3.Dozhko_Andrey_Kolkovich"]])
    a = get_values("Information_systems")
    for i in a:
        client.set(i,["Basics of Information systems - "+str(random.randint(0,100)),"--Fundamentals of Numerical Methods - "+str(random.randint(0,100)), "--Cisco programming - "+str(random.randint(0,100)), "--Object-oriented programming - "+str(random.randint(0,100))])

    b = get_values("Informatica")
    print(b)
    for i in b:
        client.set(i, ["Basics of Numerical Analysis - " + str(random.randint(0,100)),
                       "--Information theory - " + str(random.randint(0,100)),
                       "--Programming basics - " + str(random.randint(0,100)),
                       "--Java programming - " + str(random.randint(0,100))])


    c = get_values("Computer_Science")
    print("this"+str(c))
    for i in c:
        client.set(i, ["Basics of Computer Science - " + str(random.randint(0,100)),
                       "--3D modelling - " + str(random.randint(0,100)),
                       "--C++ Programming - " + str(random.randint(0,100)),
                       "--Algorithms - " + str(random.randint(0,100))])



class MultiColumnListbox1(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 14))
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=car_header1, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in car_header1:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in car_list1:
            self.tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header1[ix],width=None)<col_w:
                    self.tree.column(car_header1[ix], width=col_w)


class MultiColumnListbox(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 14))
        style.configure("Treeview", font=("Helvetica", 14))
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=car_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in car_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in car_list:
            self.tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def on_tree_select(self, event):
        self.selected = event.widget.selection()
        for idx in self.selected:
            print(self.tree.item(idx)['values'])
            group_list(self.tree.item(idx)['values'])
def sortby(tree, col, descending):
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))


def onselect(evt,selection):
    print(evt)
    print(selection)

    selection = re.sub("\d+.", "", selection)
    word = selection
    selection = selection.split("_")

    print(selection)
    student_info(None,selection[1],selection[0],selection[2],evt[2],evt[0],evt[3],word)

def group_list(list,root=None):
    print(list)
    try:
        root.destroy()
    except AttributeError:
        print()
    group_list_root = tk.Tk()
    group_list_root.geometry("600x300")
    group_list_root.configure(background='#f79317')

    scrollbar = tk.Scrollbar(group_list_root)
    scrollbar.pack(side="right", fill="y")
    mylist = tk.Listbox(group_list_root,yscrollcommand = scrollbar.set,height=10,font=tkFont.Font(size=16))
    #mylist.bind('<<ListboxSelect>>', onselect)


    group = get_values(list[3])

    for line in group:
        mylist.insert("end", str(line))

    mylist.pack(side="bottom", fill = "both")
    spisok = tk.Label(group_list_root,background="#3ccbd2", text="СПИСОК ГРУППЫ",font=("Helvetica",16))
    button = tk.Button(group_list_root, text="Выбрать", font=("Helvetica", 14),background="#16de7f",command=lambda: onselect(list,mylist.get(mylist.curselection())))
    button.pack(side="bottom",fill="both")

    spisok.pack()


    group_list_root.mainloop()

def hard_subjects():
    listbox2 = MultiColumnListbox2()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
def soot():
    names = ['Basics of Information systems','Fundamentals of Numerical Methods','Cisco programming','Object-oriented programming',
             'Basics of Numerical Analysis','Information theory','Programming basics','Java programming','Basics of Computer Science',
             '3D modelling','C++ Programming','Algorithms']
    values = [random.randint(0,100) for i in range(len(names))]
    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(2, 2)
    ax = fig.add_subplot(gs[0, :])
    ax.plot()
    ax.bar(names, values)
    print(values)
    for tick in ax.get_xticklabels():
        tick.set_rotation(55)
    plt.show()

def counting2(spec):
    b = get_values(spec)
    name_b = ""
    sum_b = 0
    for i in b:
        sum = 0
        values = client.get(i)
        values = values.decode()
        values = values.replace("[", '')
        values = values.replace("]", '')
        values = values.replace("'", '')
        values = values.replace(",", '')
        values = values.split("--")
        print(values)
        for y in values:
            sum += int(y[-2:])
            print(sum)
        sum_b+=sum
    return sum_b/len(b)



def counting(spec):
    b = get_values(spec)
    name_b = ""
    sum_b = 0
    for i in b:
        sum = 0
        values = client.get(i)
        values = values.decode()
        values = values.replace("[", '')
        values = values.replace("]", '')
        values = values.replace("'", '')
        values = values.replace(",", '')
        values = values.split("--")
        print(values)
        for y in values:
            sum += int(y[-2:])
            print(sum)
        if sum / len(values) > sum_b:
            sum_b = sum
            name_b = i
    return name_b, sum_b

def sred_bal_group():
    sum_a = counting2("Information_systems")
    sum_b = counting2("Informatica")
    sum_c = counting2("Computer_Science")
    names = ["1", "2", "3"]
    values = [sum_a, sum_b, sum_c]
    plt.figure(figsize=(9, 3))
    plt.plot()
    plt.bar(names, values)
    plt.show()


def otlichniki():
    name_a,sum_a = counting("Information_systems")
    name_b,sum_b = counting("Informatica")
    name_c,sum_c = counting("Computer_Science")
    names = [name_a,name_b,name_c]
    values = [sum_a,sum_b,sum_c]
    plt.figure(figsize=(9, 3))
    plt.plot()
    plt.bar(names, values)
    plt.show()
def sred_fac():
    names = ['Information systems', 'Informatica', 'Computer Science']
    values = [25.5, 37.2, 37.3]
    plt.figure(figsize=(5, 3))
    plt.plot()
    plt.bar(names, values)
    plt.show()

def statistics(root=None):
    try:
        root.destroy()
    except AttributeError:
        print()
    statistics_root = tk.Tk()
    statistics_root.geometry("600x550")
    statistics_root.configure(background='#f79317')
    statistic_label = tk.Label(statistics_root,text="СТАТИСТИКИ",background="#3ccbd2", font=("Helvetica",14))
    hardis_rating = tk.Button(statistics_root,text="РЕЙТИНГ СЛОЖНОСТИ ПРЕДМЕТОВ",background="#16de7f",font=("Helvetica",14),width=35,command=hard_subjects)
    prepod_rating = tk.Button(statistics_root,text="РЕЙТИНГ ПРЕПОДАВАТЕЛЕЙ",background="#16de7f",font=("Helvetica",14),width=35,command=lambda: prepods(statistics_root))
    otlichnicks_fac = tk.Button(statistics_root,text="ОТЛИЧНИКИ НА ФАКУЛЬЕТЕТАХ",background="#16de7f",font=("Helvetica",14),width=35,command=otlichniki)
    sootnoshenie = tk.Button(statistics_root,text="СООТНОШЕНИЕ ОЦЕНОК ПО КУРСАМ",background="#16de7f",font=("Helvetica",14),width=35,command=soot)
    avg_ball = tk.Button(statistics_root,text="СРЕДНИЙ БАЛЛ НА ФАКУЛЬТЕТЕ",background="#16de7f",font=("Helvetica",14),width=35,command=sred_fac)
    avg_group = tk.Button(statistics_root,text="СРЕДНИЙ БАЛ В ГРУППЕ",background="#16de7f",font=("Helvetica",14),width=35,command=sred_bal_group)

    statistic_label.place(x=230,y=50)

    hardis_rating.place(x=100,y=100)
    prepod_rating.place(x=100,y=150)
    otlichnicks_fac.place(x=100,y=200)
    sootnoshenie.place(x=100,y=250)
    avg_ball.place(x=100,y=300)
    avg_group.place(x=100,y=350)
    back_but = tk.Button(statistics_root, text="Назад",background="#16de7f", font=("Helvetica", 18), width=10,
                         command=lambda: main_page(statistics_root))
    back_but.pack()
    back_but.place(x=20, y=480)
    statistics_root.mainloop()


def prepods(root=None):
    try:
        root.destroy()
    except AttributeError:
        print()

    prepods_root = tk.Tk()
    prepods_root.geometry("650x550")
    prepods_root.configure(background='#f79317')
    prepods_root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox1()
    back_but = tk.Button(prepods_root, text="Назад",background="#16de7f", font=("Helvetica", 18), width=10,
                         command=lambda: main_page(prepods_root))
    back_but.pack()
    back_but.place(x=20, y=480)
    prepods_root.mainloop()


def list_of_groups(root=None):
    try:
        root.destroy()
    except AttributeError:
        print()


    list_of_groups_root = tk.Tk()
    list_of_groups_root.geometry("500x550")
    list_of_groups_root.configure(background='#f79317')
    list_of_groups_root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox()
    #listbox._build_tree(combo_faculty.get(),combo_course.get(),combo_specialnost.get(),combo_nomer_gruppy.get())
    back_but = tk.Button(list_of_groups_root, text="Назад",background="#16de7f", font=("Helvetica", 18), width=10,
                         command=lambda: main_page(list_of_groups_root))
    back_but.pack()
    back_but.place(x=20,y=480)
    list_of_groups_root.mainloop()


def find_student(root=None):
    global combo_faculty
    global combo_course
    global combo_specialnost
    global combo_nomer_gruppy
    try:
        root.destroy()
    except AttributeError:
        print()

    find_student_root = tk.Tk()
    find_student_root.title("Поиск студента")
    find_student_root.geometry("600x500")
    find_student_root.configure(background='#f79317')

    combo_faculty = ttk.Combobox(find_student_root,values=["Факультет"],font=("Helvetica",20))
    combo_faculty.current(0)
    combo_course = ttk.Combobox(find_student_root,values=["Курс"],font=("Helvetica",20))
    combo_course.current(0)
    combo_specialnost = ttk.Combobox(find_student_root,values=["Специальность"],font=("Helvetica",20))
    combo_specialnost.current(0)
    combo_nomer_gruppy = ttk.Combobox(find_student_root,values=["Номер гурппы"],font=("Helvetica",20))
    combo_nomer_gruppy.current(0)

    find_button = tk.Button(find_student_root, text="Поиск",font=("Helvetica",20),background="#16de7f",command=lambda: list_of_groups(find_student_root))
    find_button.place(x=280,y=380)
    combo_faculty.place(x=170,y=100)
    combo_course.place(x=170,y=170)
    combo_specialnost.place(x=170,y=240)
    combo_nomer_gruppy.place(x=170,y=310)
    back_but = tk.Button(find_student_root, text="Назад",background="#16de7f", font=("Helvetica", 18), width=10,
                         command=lambda: main_page(find_student_root))
    find_stud_lab = tk.Label(text="Поиск студента",background="#3ccbd2", font=("Helvetica",20))

    find_stud_lab.place(x=250,y=50)
    back_but.place(x=25,y=430)
    find_student_root.mainloop()


def student_info(root=None,name=None,surname=None,otchestvo=None, faculty=None, group=None, speciality=None,word=None):
    try:
        root.destroy()
    except AttributeError:
        print()

    student_info_root = tk.Tk()
    student_info_root.title("Сведения о студенте")
    student_info_root.geometry("700x600")
    student_info_root.configure(background='#f79317')

    uspevaemost = tk.Label(student_info_root, background="#3ccbd2",text="Успеваемость", font=("Helvetica", 14))

    if name is None:
        surname_but_ent = tk.Entry()
        faculty_but_ent = tk.Entry()
        name_but_ent = tk.Entry()
        group_but_ent = tk.Entry()
        otchestvo_but_ent = tk.Entry()
        specialnost_but_ent = tk.Entry()

        surname_but = tk.Label(student_info_root, text="Фамилия",background="#3ccbd2", font=("Helvetica", 12), width=13)
        faculty_but = tk.Label(student_info_root, text="Факультет",background="#3ccbd2", font=("Helvetica", 12), width=13)
        name_but = tk.Label(student_info_root, text="Имя",background="#3ccbd2", font=("Helvetica", 12), width=13)
        group_but = tk.Label(student_info_root, text="Группа",background="#3ccbd2", font=("Helvetica", 12), width=13)
        otchestvo_but = tk.Label(student_info_root, text="Отчество",background="#3ccbd2", font=("Helvetica", 12), width=13)
        specialnost_but = tk.Label(student_info_root, text="Специальность",background="#3ccbd2", font=("Helvetica", 12), width=13)
        add_but = tk.Button(student_info_root, text="Добавить",background="#16de7f", font=("Helvetica", 12), width=10,
                             command=lambda: add_student_to_mem(surname_but_ent.get(),
                                                                faculty_but_ent.get(),
                                                                name_but_ent.get(),
                                                                group_but_ent.get(),
                                                                otchestvo_but_ent.get(),
                                                                specialnost_but_ent.get()))
        back_but = tk.Button(student_info_root, text="Назад",background="#16de7f", font=("Helvetica", 12), width=10,
                             command=lambda: main_page(student_info_root))
        surname_but_ent.place(x=200, y=100)
        faculty_but_ent.place(x=450, y=100)
        name_but_ent.place(x=200, y=200)
        group_but_ent.place(x=450, y=200)
        otchestvo_but_ent.place(x=200, y=300)
        specialnost_but_ent.place(x=450, y=300)


        surname_but.place(x=200, y=50)
        faculty_but.place(x=450, y=50)
        name_but.place(x=200, y=150)
        group_but.place(x=450, y=150)
        otchestvo_but.place(x=200, y=250)
        specialnost_but.place(x=450, y=250)
        add_but.place(x=350,y=500)

        back_but.place(x=25, y=500)
        student_info_root.mainloop()
    else:
        surname_but = tk.Label(student_info_root, text="Фамилия:\n"+surname,background="#3ccbd2", font=("Helvetica", 16), width=13)
        faculty_but = tk.Label(student_info_root, text="Факультет:\n"+faculty,background="#3ccbd2", font=("Helvetica", 16), width=20)
        name_but = tk.Label(student_info_root, text="Имя:\n"+name, font=("Helvetica", 16),background="#3ccbd2", width=13)
        group_but = tk.Label(student_info_root, text="Группа:\n"+str(group),background="#3ccbd2", font=("Helvetica", 16), width=13)
        otchestvo_but = tk.Label(student_info_root, text="Отчество:\n"+otchestvo,background="#3ccbd2", font=("Helvetica", 16), width=13)
        specialnost_but = tk.Label(student_info_root, text="Специальность\n"+speciality,background="#3ccbd2", font=("Helvetica", 16), width=20)
        back_but = tk.Button(student_info_root, text="Назад",background="#16de7f", font=("Helvetica", 20), width=10,
                             command=lambda: main_page(student_info_root))

        scrollbar = tk.Scrollbar(student_info_root)
        scrollbar.pack(side="right", fill="y")
        mylist = tk.Listbox(student_info_root, yscrollcommand=scrollbar.set, height=10, font=tkFont.Font(size=16))
        # mylist.bind('<<ListboxSelect>>', onselect)
        print(word)
        group = client.get(word)
        group = group.decode()
        group = group.replace("[", '')
        group = group.replace("]", '')
        group = group.replace("'", '')
        group = group.replace(",", '')
        group = group.split("--")
        print(group)

        for line in group:
            mylist.insert("end", str(line))

        mylist.pack(side="bottom", fill="both")

        surname_but.place(x=200, y=50)
        faculty_but.place(x=420, y=50)
        name_but.place(x=200, y=120)
        group_but.place(x=420, y=120)
        otchestvo_but.place(x=200, y=190)
        specialnost_but.place(x=420, y=190)

        uspevaemost.place(x=10, y=250)
        back_but.place(x=25, y=500)
        student_info_root.mainloop()




def add_student(root=None):
    try:
        root.destroy()
    except AttributeError:
        print()

    add_student_root = tk.Tk()
    add_student_root.title("Добавить студента")
    add_student_root.geometry("600x500")
    add_student_root.configure(background='#f79317')

    add_student_label = tk.Label(add_student_root,background="#3ccbd2", text="Добавить студента",font=("Helvetica",20))

    open_file_but = tk.Button(add_student_root, text="Открыть файл",background="#16de7f", font=("Helvetica", 20), width=20)
    photo_but = tk.Button(add_student_root, text="Фото",background="#16de7f", font=("Helvetica", 20), width=20)
    add_but = tk.Button(add_student_root, text="Добавить",background="#16de7f", font=("Helvetica", 20), width=10,command=lambda: student_info(add_student_root))
    back_but = tk.Button(add_student_root, text="Назад",background="#16de7f", font=("Helvetica", 20), width=10,command=lambda: main_page(add_student_root))

    add_student_label.place(x=200,y=20)
    open_file_but.place(x=150, y=100)
    photo_but.place(x=150, y=180)
    add_but.place(x=240, y=260)
    back_but.place(x=10, y=420)
    add_student_root.mainloop()


def main_page(root=None):
    try:
        root.destroy()
    except AttributeError:
        print()

    global main_page_root
    main_page_root = tk.Tk()
    main_page_root.title("Поиск студента")
    main_page_root.geometry("600x500")
    main_page_root.configure(background='#f79317')

    find_student_but = tk.Button(main_page_root,text="Найти студента",font=("Helvetica",20),width=20,background="#16de7f",command=lambda: find_student(main_page_root))
    statistic_but = tk.Button(main_page_root,text="Статистики",font=("Helvetica",20),width=20,background="#16de7f",command=lambda: statistics(main_page_root))
    add_student_but = tk.Button(main_page_root,text="Добавить студента",font=("Helvetica",20),background="#16de7f",width=20,command=lambda: add_student(main_page_root))
    base_export_but = tk.Button(main_page_root,text="Экспорт базы",font=("Helvetica",20),background="#16de7f",width=20)

    find_student_but.place(x=150,y=100)
    statistic_but.place(x=150,y=180)
    add_student_but.place(x=150,y=260)
    base_export_but.place(x=150,y=340)

    main_page_root.mainloop()

memcache_work()
fill()
main_page()