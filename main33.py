from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import math
import os
from kivy.uix.popup import Popup
from datetime import datetime
#from kivymd.uix.list import OneLineListItem

layout0 = BoxLayout(orientation="horizontal", padding=10)
layout1 = BoxLayout(orientation="vertical", padding=10, size_hint=(.5, 1))
layout2 = BoxLayout(orientation="horizontal", padding=0)
layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
root.add_widget(layout)

clear = Button(text='Очистить', font_size=62, markup=True)
solution = Label(text='0.0p.', font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
summer = Button(text='Сумма', markup=True, font_size=82, size_hint=(1, 2), color=[1, 1, 0, 1])
change = Button(text='Сдача с суммы:', font_size=22, size_hint=(1, .7))
ch = TextInput(text='', halign="center", font_size=45, size_hint=(1, .7))
spisok_summ = Button(text='all', font_size=22)
spisok_summ_today= Button(text='today', font_size=22)
col_people = Button(text='buyers', font_size=22)
rew = Button(text='rew', font_size=42)
proc = Button(text='%', font_size=42,)
            #multiline=False, readonly=True, )
layout1.add_widget(summer)
layout1.add_widget(solution)
layout1.add_widget(clear)
layout1.add_widget(change)
layout1.add_widget(ch)
layout1.add_widget(proc)
layout1.add_widget(rew)
layout2.add_widget(spisok_summ)
layout2.add_widget(spisok_summ_today)
layout2.add_widget(col_people)
layout1.add_widget(layout2)


        # Make sure the height is such that there is something to scroll.
#для прокрутки
layout.bind(minimum_height=layout.setter('height'))
#layout.add_widget(layout1)
layout0.add_widget(root)
layout0.add_widget(layout1)
but = {}
entry = {}
for i in range(50):
    h_layout = BoxLayout(height=60, size_hint=(None, None))
    for j in range(6):
        if j == 5:
            but[i, j] = Button(text='del', halign="center", font_size=28, size_hint=(None, None), height=80)
            h_layout.add_widget(but[i, j])
        else:
            entry[i, j] = TextInput(halign="center", cursor_color=[0, 0, 1, 1], font_size=48, size_hint=(None, None), height=80, width=80, multiline=False)
            h_layout.add_widget(entry[i, j])
            if j == 1:
                entry[i, j].text = 'x'
                entry[i, j].markup=True
            if j == 3:
                entry[i, j].text = '='
                entry[i, j].markup=True
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
#сохраняем суммы в 'kalkulator.txt'
def save(s):
    now_chek = datetime.now()
    data = now_chek.strftime("%d-%m-%Y %H:%M")
    print(data)
    with open('kalkulator.txt', 'a+') as k:
        k.write('\n' + data + ': ' + s)
        label = Label(text='сумма успешно сохранена!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
        popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 350.0 / Window.width, 'y': 500.0 / Window.height})
        popupWindow.add_widget(label)
        popupWindow.open()

chek_full = False
def clear_calk():
    global pust_chek
    if pust_chek == True:
            label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
            popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
            popupWindow.add_widget(label)
            popupWindow.open()
    else:
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(None, None))
      #  q_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
        an_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
        yes = Button(text='да', halign="center", font_size=28, size_hint=(None, .5), width=160, height=80)
        no = Button(text='нет', halign="center", font_size=28, size_hint=(None, .5), width=160, height=80)
        #label = Label(text='Хотите сохранить?', size_hint=(None, None), color=[1, 0, 0, 1])
        #q_layout.add_widget(label)
        an_layout.add_widget(yes)
        an_layout.add_widget(no)
        no.on_press=lambda: (chek_up(), close())
        yes.on_press=lambda: (perevod(), close())
        def close():
            popupWindow.dismiss()
        def perevod():
            an_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
            yes = Button(text='да', halign="center", font_size=28, size_hint=(None, .5), width=160, height=80)
            no = Button(text='нет', halign="center", font_size=28, size_hint=(None, .5), width=160, height=80)
            # label = Label(text='Хотите сохранить?', size_hint=(None, None), color=[1, 0, 0, 1])
            # q_layout.add_widget(label)
            an_layout.add_widget(yes)
            an_layout.add_widget(no)
            no.on_press = lambda: (save(summer.text[:-2]), close(), chek_up())
            yes.on_press = lambda: (save(summer.text[:-2] + 'perevod' ), close(), chek_up())
            def close():
                popupWindow.dismiss()
            #label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])
            popupWindow = Popup(title='ЭТО ПЕРЕВОД?', size_hint=(None, None), size=(400, 200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
            popupWindow.add_widget(an_layout)
            popupWindow.open()
        popupWindow = Popup(title="Хотите сохранить сумму? "+str(summer.text[:-2]), size_hint=(None,None),size=(500,200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
       # h_layout.add_widget(q_layout)
        h_layout.add_widget(an_layout)
        popupWindow.add_widget(h_layout)
        popupWindow.open()
        
def rew_sum():
    #show = P()
    now_chek = datetime.now()
    data = now_chek.strftime("%d-%m") #-%Y
    h_layout = BoxLayout(orientation="vertical", padding=10, spacing=-20, size_hint=(None, None))
    q_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(2, None))
    an_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
    itog_today = Button(text='за сегодня', halign="center", font_size=28, size_hint=(None, .5), width=160, height=80)
    itog_month = Button(text='за месяц', halign="center", padding=20, font_size=28, size_hint=(None, .5), width=160, height=80)
    itog_all = Button(text='общий', halign="center", font_size=28, size_hint=(None, .5),width=160,  height=80)
    rew_file = Button(text='за год', halign="center", font_size=28, size_hint=(None, .5),width=160,  height=80)
    label1 = Label(text='всего наличными за  ', font_size=22, size_hint=(4, 1), color=[1, 0, 1, 1])
    label2 = Label(text='всего переводов за  ', font_size=22, size_hint=(4, 1), color=[1, 0, 1, 1])
    label3 = Label(text='итого за  ', font_size=22, size_hint=(4, 1), color=[1, 0, 1, 1])
    q_layout.add_widget(label1)
    q_layout.add_widget(label2)
    q_layout.add_widget(label3)
    an_layout.add_widget(itog_today)
    an_layout.add_widget(itog_month)
    an_layout.add_widget(itog_all)
    an_layout.add_widget(rew_file)
    itog_today.on_press=lambda: it_tod(data)
    itog_all.on_press=lambda: it_all()
    rew_file.on_press=lambda: it_ye()
    itog_month.on_press = lambda: itog_m()
    
    #popupWindow = Popup(title="ИТОГИ", size_hint=(None,None),size=(400,200))
    h_layout.add_widget(q_layout)
    h_layout.add_widget(an_layout)
    

    def it_ye():

        label = Label(text='введите год ', font_size=32, color=[1, 1, 0, 1])
        vvodi = TextInput(text='', halign="center", font_size=35, size_hint=(None, None), width=100, height=60)
        vivod = Button(text='ok', halign="center", font_size=28, size_hint=(None, None), width=80, height=60)
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
        vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
        popupWindow = Popup(title="итог за год", size_hint=(None, None), size=(500, 150))
        vvod_layout.add_widget(label)
        vvod_layout.add_widget(vvodi)
        vvod_layout.add_widget(vivod)
        h_layout.add_widget(vvod_layout)
        vvodi.unfocus_on_touch = False
        vvodi.focus = True

        def it_y():
            popupWindow.dismiss()
            m = vvodi.text
            
           # data = month.get(m)
            print(m)
            label2.text = 'всего переводов за ' + m
            label1.text = 'всего наличными за ' + m
            label3.text = 'итого за ' + m
            per = []
            nal = []
            with open('kalkulator.txt', 'r', encoding='utf-8') as f:
                all = f.read()
                sp_all = all.splitlines()
                for i in range(len(sp_all)):
                    s = sp_all[i].split()
                    print(s[0][6:10])
                    if len(s) == 4:
                        if s[0][6:10] == m and s[3] == 'perevod': #'перевод':
                            #print(s[0][6:10])
                            per.append(int(s[2]))
                    else:
                        if s[0][6:10] == m:
                            nal.append(int(s[2]))
            #q_layout.size_hint = (2, None)
            label2.text = 'всего переводов за ' + m + 'год : ' + str(math.fsum(per))
            label1.text = 'всего наличными за ' + m + 'год : ' + str(math.fsum(nal))
            label3.text = 'итого за ' + m + 'год : ' + str(math.fsum(nal) + math.fsum(per))

        vivod.on_press = lambda: (it_y(), popupWindow.dismiss())
        popupWindow.add_widget(h_layout)
        popupWindow.open()
    def it_tod(data):
        #popupWindow.dismiss()
        try:
            label2.text ='всего переводов за ' + data
            label1.text ='всего наличными за ' + data
            label3.text ='итого за ' + data
            per = []
            nal = []
            with open('kalkulator.txt', 'r', encoding='utf-8') as f: # encoding='utf-8'
                all = f.read()
                sp_all = all.splitlines()
                for i in range(len(sp_all)):
                    s = sp_all[i].split()
                    da = data.split()
                    if len(s) == 4:
                        if s[0][0:5] == da[0] and s[3] == 'perevod': #'перевод':
                            per.append(int(s[2]))
                    else:
                        if s[0][0:5] == da[0]:
                            nal.append(int(s[2]))
            print(math.fsum(per))
            print(math.fsum(nal))
            #q_layout.size_hint = (2, None)
            label2.text='всего переводов за ' + data + ': ' + str(math.fsum(per))
            label1.text='всего наличными за ' + data + ': ' + str(math.fsum(nal))
            label3.text='итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per))
        except IndexError:
            print('IndexError', ' удалите пустую строку в "kalkulator.txt"')

        
    def it_all():
        #popupWindow.dismiss()
        label2.text = 'всего переводов за '
        label1.text = 'всего наличными за '
        label3.text = 'итого за '
        per = []
        nal = []
        with open('kalkulator.txt', 'r', encoding='utf-8') as f:
            all = f.read()
            sp_all = all.splitlines()
            s_kakogo = sp_all[0].split()[0]
            po_kakoe = sp_all[-1].split()[0]
            for i in range(len(sp_all)):
                s = sp_all[i].split()
                if len(s) == 4:
                    if s[3] == 'perevod': #'перевод':
                        per.append(int(s[2]))
                else:
                    nal.append(int(s[2]))
        # print(math.fsum(per))
        # print(math.fsum(nal))
        #q_layout.size_hint = (2, None)
        label2.text='всего переводов c ' + s_kakogo + ' по ' + po_kakoe + ': ' + str(math.fsum(per))
        label1.text='всего наличными c ' + s_kakogo + ' по ' + po_kakoe + ': ' + str(math.fsum(nal))
        label3.text='итого c ' + s_kakogo + ' по ' + po_kakoe + ': ' + str(math.fsum(nal) + math.fsum(per))

    def itog_m():

        label = Label(text='введите номер месяца:', font_size=32, color=[1, 1, 0, 1])
        vvodi = TextInput(text='', halign="center", font_size=35, size_hint=(None, None), width=70, height=60)
        vivod = Button(text='ok', halign="center", font_size=28, size_hint=(None, None), width=80, height=60)
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
        vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
        popupWindow = Popup(title="итог за месяц", size_hint=(None, None), size=(600, 150))
        vvod_layout.add_widget(label)
        vvod_layout.add_widget(vvodi)
        vvod_layout.add_widget(vivod)
        h_layout.add_widget(vvod_layout)
        vvodi.unfocus_on_touch = False
        vvodi.focus = True

        def it_mon():
            popupWindow.dismiss()
            m = vvodi.text
            month = {'01': 'ЯНВАРЬ',
                     '02': 'ФЕВРАЛЬ',
                     '03': 'МАРТ',
                     '04': 'АПРЕЛЬ',
                     '05': 'МАЙ',
                     '06': 'ИЮНЬ',
                     '07': 'ИЮЛЬ',
                     '08': 'АВГУСТ',
                     '09': 'СЕНТЯБРЬ',
                     '10': 'ОКТЯБРЬ',
                     '11': 'НОЯБРЬ',
                     '12': 'ДЕКАБРЬ'}
            data = month.get(m)
            print(data)
            label2.text = 'всего переводов за ' + data
            label1.text = 'всего наличными за ' + data
            label3.text = 'итого за ' + data
            per = []
            nal = []
            with open('kalkulator.txt', 'r', encoding='utf-8') as f:
                all = f.read()
                sp_all = all.splitlines()
                for i in range(len(sp_all)):
                    s = sp_all[i].split()
                    
                    if len(s) == 4:
                        if s[0][3:5] == m and s[3] == 'perevod': #'перевод':
                            per.append(int(s[2]))
                    else:
                        if s[0][3:5] == m:
                            nal.append(int(s[2]))
            #q_layout.size_hint = (2, None)
            label2.text = 'всего переводов за ' + data + ': ' + str(math.fsum(per))
            label1.text = 'всего наличными за ' + data + ': ' + str(math.fsum(nal))
            label3.text = 'итого за ' + data + ': ' + str(math.fsum(nal) + math.fsum(per))

        vivod.on_press = lambda: (it_mon(), popupWindow.dismiss())
        popupWindow.add_widget(h_layout)
        popupWindow.open()




    popupWindow = Popup(title="ИТОГИ", size_hint=(None,None),size=(700,300), pos_hint={'x': 320.0 / Window.width, 'y': 400.0 / Window.height})
    #popupWindow.add_widget(label)
    popupWindow.add_widget(h_layout)
    popupWindow.open() 
    
pust_chek = True
#очищаем калькулятор
def chek_up():
    global zapisej2, tabl_full, sum_sp, vvod_search2, pust_chek,vvod_not, ito, entry_focus
    if pust_chek == True:
            label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
            popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
            popupWindow.add_widget(label)
            popupWindow.open()
    else:
             print('here')
             for i in range(zapisej2+1):
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
    summer.text='сумма'
    solution.text='0.0 p.'
    change.text='Сдача с суммы'
    ch.text=''
    entry[0,0].unfocus_on_touch = False
    entry[0, 0].focus = True
    #popupWindow.dismiss()
       
def skidka():
    global vvodi, pust_chek
    if pust_chek == True:
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
        popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        label = Label(text='введите скидку:', font_size=42, color=[1, 1, 0, 1])
        vvodi= TextInput(text='', halign="center", font_size=45, size_hint=(None, None), width=100, height=70)
        vivod = Button(text='скидка', halign="center", font_size=28, size_hint=(None, None), width=120, height=70)
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
        vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
        popupWindow = Popup(title="скидка", size_hint=(None,None),size=(600,200), pos_hint={'x': 350.0 / Window.width, 'y': 500.0 / Window.height})
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
            p = int(s[0])*int(procent)*0.01
            ot = int(s[0])-p
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
        stoim = int(price)*int(colich)
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
            #удалить сумму из списка
            print(sum_sp)
        pust_chek = False
        vvod(t + 1)
        
    except ValueError:
        if entry[t, 0].text== '':
            entry[t, 0].focus = True
            vvod(t)
def sum():
    global sum_sp
    if pust_chek == True:
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
        popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        summer.text = str(math.fsum(sum_sp))

def sdacha():
    global sum_sp
    if pust_chek == True or ch.text == '':
        label = Label(text='действие выполнить нельзя!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
        popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
        popupWindow.add_widget(label)
        popupWindow.open()
    else:
        oplata = ch.text
        sum = summer.text
        s = sum.split('.')
        print(s[0])
        sd = int(oplata)-int(s[0])
        change.text = str(sd)
#для кнопок удалить
def del_str(z):
    global zapisej2, vvod_not
    vvod_not = False  # выбор растения в поиске возможен

    try:
        print('удаляем ' + str(z) + ' строку')
        print('удаляем ' + str(sum_sp[z]))
        entry[z, 0].text=''
        entry[z, 2].text=''
        entry[z, 4].text=''
        sum_sp.pop(z)
        summer.text = str(math.fsum(sum_sp))
        solution.text = str(math.fsum(sum_sp))
        print(zapisej2)
        d = zapisej2
        for n in range(zapisej2):
            print('проверяем строку ' + str(n))
            if entry[n, 0].text == '':
                print('строка ' + str(n) + ' пустая')
                if entry[n+1, 0].text != '':
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
                    d = d-1
                    entry[d, 0].unfocus_on_touch = False
                    entry[d, 0].focus = True
                    
                    vvod(d)
                    #d = d-1
                    
    except IndexError:
        entry[z, 0].texr = ''
        entry[z, 2].text = ''
        entry[z, 4].text = ''
        entry[z, 0].unfocus_on_touch = False
        entry[z, 0].focus = True
        vvod(z)
        
def people():
    vvodi = TextInput(text='', halign="center", font_size=35, size_hint=(None, None), width=200, height=60)
    vivod = Button(text='ok', halign="center", font_size=28, size_hint=(None, None), width=80, height=60)
    h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
    vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
    popupWindow = Popup(title="ВВЕДИТЕ ПАРОЛЬ", size_hint=(None, None), size=(400, 200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
    #vvod_layout.add_widget(label)
    vvod_layout.add_widget(vvodi)
    vvod_layout.add_widget(vivod)
    h_layout.add_widget(vvod_layout)
    vvodi.unfocus_on_touch = False
    vvodi.focus = True    
    def people2():
            m = vvodi.text
            now_chek = datetime.now()
            day = now_chek.strftime("%d-%m-%Y")
            day1 = '04-03-2024'
            if m == 'fazenda':
                popupWindow.dismiss()
                popupWindow1 = Popup(title='количество покупателей ',  size_hint=(None,None),size=(700,520))
                h_layout = BoxLayout(orientation="vertical", padding=10, spacing=40)
                f_stroka = BoxLayout(orientation="horizontal", padding=10, spacing=40, size_hint=(1, .1))
                lab = Label(text='количество покупателей по дням:', font_size=32, color=[1, 0, 0, 1])
                layout = GridLayout(cols=1, spacing=1, size_hint = (1, None))
                root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
                #для прокрутки
                layout.bind(minimum_height=layout.setter('height'))
                root.add_widget(layout)
                f_stroka.add_widget(lab)
                h_layout.add_widget(f_stroka)
                h_layout.add_widget(root)
                data = {}
                def vivod(k, line):
                    str_layout = BoxLayout(height=60, size_hint=(1, None))
                    data[k] =Button(text=line, markup=True, font_size=32, size_hint=(1, None), color=[1, 1, 0, 1])# Label(text=line,font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
                    
                    str_layout.add_widget(data[k])
                    layout.add_widget(str_layout)
                    #data[k].on_press = lambda: del_st(line)
                with open('kalkulator.txt') as f:
                    lines = f.read()
                    sp = lines.splitlines()
                    n = 0
                    day = sp[0][:10]
                    for i  in range(len(sp)):
                         if sp[i][:10] == day:
                             n = n + 1
                             if i == len(sp)-1:
                                 vivod(i, sp[i][:10] + ': ' + str(n) + ' чел.')
                         else:
                             vivod(i, sp[i-1][:10] + ': ' + str(n) + ' чел.')
                             day = sp[i][:10]
                             n = 1
                    
                popupWindow1.add_widget(h_layout)
                popupWindow1.open() 
            else:
                popupWindow2 = Popup(title='',  size_hint=(None,None),size=(400,200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
                label = Label(text='пароль неверный!!!', font_size=32, color=[1, 0, 0, 1])
                vvodi.text=''
                vvodi.unfocus_on_touch = False
                vvodi.focus = True
                popupWindow2.add_widget(label)
                popupWindow2.open() 
    vivod.on_press = lambda: (people2()) #, popupWindow.dismiss())
    popupWindow.add_widget(h_layout)
    popupWindow.open()      
def rew_kalk(t):
    #label = Label(text='чтобы проссмотреть список', font_size=32, color=[1, 1, 0, 1])
    vvodi = TextInput(text='', halign="center", font_size=35, size_hint=(None, None), width=200, height=60)
    vivod = Button(text='ok', halign="center", font_size=28, size_hint=(None, None), width=80, height=60)
    h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(1, 1))
    vvod_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(1, 1))
    popupWindow = Popup(title="ВВЕДИТЕ ПАРОЛЬ", size_hint=(None, None), size=(400, 200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
    #vvod_layout.add_widget(label)
    vvod_layout.add_widget(vvodi)
    vvod_layout.add_widget(vivod)
    h_layout.add_widget(vvod_layout)
    vvodi.unfocus_on_touch = False
    vvodi.focus = True
    def del_st(k):
        print(k)
        popupWindow2 = Popup(title='ХОТИТЕ УДАЛИТЬ ЗАПИСЬ: ' + k, size_hint=(None, None), size=(500, 200), pos_hint={'x': 400.0 / Window.width, 'y': 500.0 / Window.height})
        h_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(None, None))
      #  q_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
        an_layout = BoxLayout(orientation="horizontal", padding=10, size_hint=(None, None))
        yes = Button(text='да', halign="center", font_size=28, size_hint=(None, .5), width=200, height=80)
        no = Button(text='нет', halign="center", font_size=28, size_hint=(None, .5), width=200, height=80)
        #label = Label(text='Хотите сохранить?', size_hint=(None, None), color=[1, 0, 0, 1])
        #q_layout.add_widget(label)
        an_layout.add_widget(yes)
        an_layout.add_widget(no)
        no.on_press=lambda: (close())
        yes.on_press=lambda: (delete(k), close())
        def close():
            popupWindow2.dismiss()
        def delete(s):
            with open('kalkulator.txt', "r") as f:
                lines = f.readlines()
            with open("kalkulator.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != s:
                        f.write(line)
            close()
            popupWindow1.dismiss()
            label = Label(text='строка успешно удалена!', font_size=42, size_hint=(1, .6), color=[1, 0, 0, 1])      
            popupWindow = Popup(title='внимание!',  size_hint=(None,None),size=(700,120), pos_hint={'x': 320.0 / Window.width, 'y': 550.0 / Window.height})
            popupWindow.add_widget(label)
            popupWindow.open()
            
        h_layout.add_widget(an_layout)
        popupWindow2.add_widget(h_layout)
        popupWindow2.open()    
    def rew_kalk2(t):
            m = vvodi.text
            now_chek = datetime.now()
            day = now_chek.strftime("%d-%m-%Y")
            day1 = '04-03-2024'
            if m == 'fazenda':
                popupWindow.dismiss()
                popupWindow1 = Popup(title='список сумм',  size_hint=(None,None),size=(700,520))
                h_layout = BoxLayout(orientation="vertical", padding=10, spacing=40)
                f_stroka = BoxLayout(orientation="horizontal", padding=10, spacing=40, size_hint=(1, .1))
                lab = Label(text='', font_size=32, color=[1, 0, 0, 1])
                layout = GridLayout(cols=1, spacing=1, size_hint = (1, None))
                root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
                #для прокрутки
                layout.bind(minimum_height=layout.setter('height'))
                root.add_widget(layout)
                f_stroka.add_widget(lab)
                h_layout.add_widget(f_stroka)
                h_layout.add_widget(root)
                #popupWindow.dismiss()
               # os.startfile('kalkulator.txt')
                data = {}
                def vivod(k, line):
                    str_layout = BoxLayout(height=60, size_hint=(1, None))
                    data[k] =Button(text=line, markup=True, font_size=32, size_hint=(1, None), color=[1, 1, 0, 1])# Label(text=line,font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
                    
                    str_layout.add_widget(data[k])
                    layout.add_widget(str_layout)
                    data[k].on_press = lambda: del_st(line)
                with open('kalkulator.txt') as f:
                    lines = f.read()
                    sp = lines.splitlines()
                    n = 0
                    for i  in range(len(sp)):
                       if t:
                            lab.text = 'список сумм по дням и часам:'
                            vivod(i, sp[i])
                       if not t:
                            #print(sp[i][:10])
                            lab.text = 'список сумм за сегодня:'
                            if sp[i][:10] == day:
                                n = n + 1
                                vivod(i, sp[i])
                    if n == 0:
                        str_layout = BoxLayout(height=60, size_hint=(1, None))
                        dat=Button(text='сегодня ничего не продали!!!', markup=True, font_size=32, size_hint=(1, None), color=[1, 1, 0, 1])# Label(text=line,font_size=32, size_hint=(1, .6), color=[1, 0, 1, 1])
                    
                        str_layout.add_widget(dat)
                        layout.add_widget(str_layout)
                    
                popupWindow1.add_widget(h_layout)
                popupWindow1.open() 
            else:
                popupWindow2 = Popup(title='',  size_hint=(None,None),size=(400,200), pos_hint={'x': 450.0 / Window.width, 'y': 500.0 / Window.height})
                label = Label(text='пароль неверный!!!', font_size=32, color=[1, 0, 0, 1])
                vvodi.text=''
                vvodi.unfocus_on_touch = False
                vvodi.focus = True
                popupWindow2.add_widget(label)
                popupWindow2.open() 
                
            
    vivod.on_press = lambda: (rew_kalk2(t)) #, popupWindow.dismiss())
    popupWindow.add_widget(h_layout)
    popupWindow.open()    
def un_bind(t):
    global zapisej2
    zapisej2 = t
    but[t, 5].on_press=lambda: del_str(t)
    entry[t, 2].on_text_validate= lambda:  chek_stoimost(t)
    
def perehod1(t):
    entry[t,2].focus = True
    un_bind(t)
entry[0,0].focus = True
entry[0, 0].on_text_validate= lambda:  perehod1(0)

def vvod(t):
    entry[t,0].focus = True
    entry[t, 0].on_text_validate= lambda: perehod1(t)
all = True
proc.on_press=lambda:  skidka()
#clear.on_press=lambda: chek_up()
rew.on_press=lambda:  rew_sum()
clear.on_press=lambda: clear_calk()
summer.on_press=lambda: sum()
change.on_press=lambda: sdacha()
spisok_summ.on_press=lambda: rew_kalk(all)
spisok_summ_today.on_press=lambda: rew_kalk(not all)
col_people.on_press=lambda: people()
runTouchApp(layout0)