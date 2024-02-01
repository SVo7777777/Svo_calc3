from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import math
from kivy.uix.popup import Popup

layout0 = BoxLayout(orientation="horizontal", padding=10, )
layout1 = BoxLayout(orientation="vertical", padding=10, size_hint=(.5, 1))
layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
root.add_widget(layout)
clear = Button(text='Очистить', font_size=62, markup=True)
solution = Label(text='0.0p.', font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
summer = Button(text='Сумма', markup=True, font_size=82, size_hint=(1, 2), color=[1, 1, 0, 1])
change = Button(text='Сдача с суммы:', font_size=22, size_hint=(1, .7))
ch = TextInput(text='', halign="center", font_size=45, size_hint=(1, .7))
digkey = Button(text='', font_size=42, )
rew = Button(text='', font_size=42)
proc = Button(text='%', font_size=42, )
# multiline=False, readonly=True, )
layout1.add_widget(summer)
layout1.add_widget(solution)
layout1.add_widget(clear)
layout1.add_widget(change)
layout1.add_widget(ch)
layout1.add_widget(proc)
layout1.add_widget(digkey)
layout1.add_widget(rew)
# Make sure the height is such that there is something to scroll.
# для прокрутки
layout.bind(minimum_height=layout.setter('height'))
# layout.add_widget(layout1)
layout0.add_widget(root)
layout0.add_widget(layout1)
but = {}
entry = {}
for i in range(50):
    h_layout = BoxLayout(height=60, size_hint=(None, None))
    for j in range(6):
        if j == 5:
            but[i, j] = Button(text='del', halign="left", font_size=28, size_hint=(None, None), height=80)
            h_layout.add_widget(but[i, j])
        else:
            entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=48, size_hint=(None, None),
                                    height=80, width=80, multiline=False)
            h_layout.add_widget(entry[i, j])
            if j == 1:
                entry[i, j].text = 'x'
                entry[i, j].markup = True
            if j == 3:
                entry[i, j].text = '='
                entry[i, j].markup = True
            if j == 0:
                entry[i, j].halign = 'right'
                entry[i, j].width = 120

            if j == 2:
                entry[i, j].halign = 'left'
                entry[i, j].width = 120
            if j == 4:
                entry[i, j].width = 220
                entry[i, j].foreground_color = [1, 0, 1, 1]
    layout.add_widget(h_layout)

chek_full = False
pust_chek = True
# очищаем калькулятор
def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek, vvod_not, ito, entry_focus
    if pust_chek == True:
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])
        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 120))
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        print('here')
        for i in range(zapisej2 + 1):
            print('here2')
            if entry[i, 0].text != '':
                entry[i, 0].text = ''
                entry[i, 2].text = ''
                entry[i, 4].text = ''
                print('here3')
    sum_sp = []
    print('список сумм пуст - ', sum_sp)
    vvod(0)
    pust_chek = True
    vvod_not = False  # выбор растния в поиске возможенTypeError
    summer.text = 'сумма'
    solution.text = '0.0 p.'
    change.text = 'Сдача с суммы'
    ch.text = ''
    entry[0, 0].unfocus_on_touch = False
    entry[0, 0].focus = True

def skidka():
    global vvodi, pust_chek
    if pust_chek == True:
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])
        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 120))
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        label = Label(text='введите скидку:', font_size=42, color=[1, 1, 0, 1])
        vvodi = TextInput(text='', halign="center", font_size=45, size_hint=(None, None), width=100, height=70)
        vivod = Button(text='скидка', halign="center", font_size=28, size_hint=(None, None), width=120, height=70)
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
        vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
        popupWindow = Popup(title="скидка", size_hint=(None, None), size=(600, 200))
        vvod_layout.add_widget(label)
        vvod_layout.add_widget(vvodi)
        vvod_layout.add_widget(vivod)
        h_layout.add_widget(vvod_layout)
        vvodi.unfocus_on_touch = False
        vvodi.focus = True
        def vivo():
            procent = vvodi.text
            sum = summer.text
            s = sum.split('.')
            print(s[0])
            p = int(s[0]) * int(procent) * 0.01
            ot = int(s[0]) - p
            print(p)
            vivod.text = str(p)
            summer.text = str(ot)
        vivod.on_press = lambda: vivo()
        popupWindow.add_widget(h_layout)
        popupWindow.open()

sum_sp = []
def chek_stoimost(t):
    global chek_full, name_tara, pust_chek, sum_sp
    try:
        price = entry[t, 0].text
        colich = entry[t, 2].text
        print(price)
        print(colich)
        stoim = int(price) * int(colich)
        if entry[t, 4].text == '':
            entry[t, 4].text = str(stoim)
            chek_full = False
            sum_sp.append(stoim)
            print(sum_sp)
            print(math.fsum(sum_sp))
            summer.text = str(math.fsum(sum_sp))
            solution.text = str(math.fsum(sum_sp))
        else:
            entry[t, 4].text = ''
            sum_sp.pop(t)
            print(sum_sp)
            print(math.fsum(sum_sp))
            entry[t, 4].text = str(stoim)
            summer.text = str(math.fsum(sum_sp))
            solution.text = str(math.fsum(sum_sp))
            chek_full = False
            # удалить сумму из списка
            print(sum_sp)
        pust_chek = False
        vvod(t + 1)
    except ValueError:
        if entry[t, 0].text == '':
            entry[t, 0].focus = True
            vvod(t)

def sum():
    global sum_sp
    if pust_chek == True:
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])
        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 120))
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        summer.text = str(math.fsum(sum_sp))

def sdacha():
    global sum_sp
    if pust_chek == True or ch.text == '':
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])
        popupWindow = Popup(title='внимание!', size_hint=(None, None), size=(700, 120))
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        oplata = ch.text
        sum = summer.text
        s = sum.split('.')
        print(s[0])
        sd = int(oplata) - int(s[0])
        change.text = str(sd)
# для кнопок удалить
def del_str(z):
    global zapisej2, vvod_not
    vvod_not = False  # выбор растения в поиске возможен
    try:
        print('удаляем ' + str(z) + ' строку')
        print('удаляем ' + str(sum_sp[z]))
        entry[z, 0].text = ''
        entry[z, 2].text = ''
        entry[z, 4].text = ''
        sum_sp.pop(z)
        summer.text = str(math.fsum(sum_sp))
        solution.text = str(math.fsum(sum_sp))
        print(zapisej2)
        d = zapisej2
        for n in range(zapisej2):
            print('проверяем строку ' + str(n))
            if entry[n, 0].text == '':
                print('строка ' + str(n) + ' пустая')
                if entry[n + 1, 0].text != '':
                    print('строка ' + str(n + 1) + ' непустая')
                    m0 = entry[n + 1, 0].text
                    print(m0)
                    m2 = entry[n + 1, 2].text
                    m4 = entry[n + 1, 4].text
                    entry[n, 0].text = m0
                    entry[n, 2].text = m2
                    entry[n, 4].text = m4
                    entry[n + 1, 0].text = ''
                    entry[n + 1, 2].text = ''
                    entry[n + 1, 4].text = ''
                else:
                    entry[d, 0].unfocus_on_touch = False
                    entry[d, 0].focus = True
                    vvod(d)
                    d = d - 1
    except IndexError:
        entry[z, 0].texr = ''
        entry[z, 2].text = ''
        entry[z, 4].text = ''
        entry[z, 0].unfocus_on_touch = False
        entry[z, 0].focus = True
        vvod(z)

def un_bind(t):
    global zapisej2
    zapisej2 = t
    but[t, 5].on_press = lambda: del_str(t)
    entry[t, 2].on_text_validate = lambda: chek_stoimost(t)

def perehod1(t):
    entry[t, 2].focus = True
    un_bind(t)

entry[0, 0].focus = True
entry[0, 0].on_text_validate = lambda: perehod1(0)

def vvod(t):
    entry[t, 0].focus = True
    entry[t, 0].on_text_validate = lambda: perehod1(t)

proc.on_press = lambda: skidka()
clear.on_press = lambda: chek_up()
summer.on_press = lambda: sum()
change.on_press = lambda: sdacha()
runTouchApp(layout0)
