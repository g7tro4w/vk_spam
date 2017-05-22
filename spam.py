from tkinter import *
import vk

def showMainPanel():
    mainPanel = Tk()
    mainPanel.title(u'Работа с группами')
    mainPanel.geometry('720x400+40+80')

    def searchGroups():
            session = vk.Session(access_token='d8773f36b3431af6c4fb32f3c84bf1d3c2e0883ed6acc94bc150b47ede94ecb521064a98732900074de0d')
            api = vk.API(session)
            groups = api.groups.search(q = group.get()) //Удаляем первый элемент, в котором содержится количество найденных групп
            group_list.delete(0,END)
            group_count.config(text = 'Найдено ' + str(groups.pop(0)) + ' групп')
            for i in groups:
                group_list.insert(END,i['name'])
    
    group_label = Label(mainPanel,text='Название группы', width=30)
    group = Entry(mainPanel, bd=2, text = 'Music')
    group_count = Label(mainPanel,text='', width=30)
    group_list = Listbox(mainPanel,height=10,width=100,selectmode=SINGLE)
    search = Button(mainPanel, text='Поиск', command = searchGroups)
    
    group_label.pack()
    group.pack()
    search.pack()
    group_count.pack()
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

