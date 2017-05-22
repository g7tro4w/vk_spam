from tkinter import *
import vk

def showMainPanel():
    mainPanel = Tk()
    mainPanel.title(u'Работа с группами')
    mainPanel.geometry('400x300+40+80')

    def searchGroups():
            session = vk.Session(access_token='') #ВОТ ТУТ ДОЛЖЕН БЫТЬ ТОКЕН
            api = vk.API(session)
            groups = api.groups.search(q = group.get(), count = 1000)
            group_list.delete(0,END)
            group_count.config(text = 'Найдено ' + str(groups.pop(0)) + ' групп') #Удаляем первый элемент, в котором содержится количество найденных групп
            for i in groups:
                group_list.insert(END,i['name'])

                
    frame=Frame(mainPanel,bd=5)
    group_label = Label(mainPanel,text='Название группы', width=30)
    group = Entry(mainPanel, bd=2, text = 'Music')
    group_count = Label(frame,text='', width=30)
    group_list = Listbox(frame,height=10,width=50,selectmode=SINGLE)
    search = Button(mainPanel, text='Поиск', command = searchGroups)

    
    scrollbar = Scrollbar(frame)
    
    # первая привязка
    scrollbar['command'] = group_list.yview
    # вторая привязка
    group_list['yscrollcommand'] = scrollbar.set

    
    group_label.pack()
    group.pack()
    search.pack()
    frame.pack()
    group_count.pack()
    scrollbar.pack(side='right', fill=Y)
    group_list.pack()
    
    
    mainPanel.mainloop()
    
    auth_window.destroy()

    
            



    
auth_window = Tk()
auth_window.title(u'Авторизация')
auth_window.geometry('300x150+40+80')

login_label = Label(auth_window,text='E-mail')
login=Entry(auth_window, bd=2)
password_label = Label(auth_window,text='Пароль')
password=Entry(auth_window, bd=2, show='*')
send = Button(auth_window, text='Войти', command = showMainPanel)

login_label.pack()
login.pack()
password_label.pack()
password.pack()
send.pack()

auth_window.mainloop()

