#! /usr/bin/env python3
from tkinter import *
import vk
import vk_auth

def showMainPanel():
    mainPanel = Tk()
    mainPanel.title('Работа с группами')
    mainPanel.geometry('400x300+40+80')
    client_id = '5732579'
    scope = 'wall'

    token, user_id = vk_auth.auth('79152986805','andranik111291a', client_id, scope)
    session = vk.Session(access_token=token) #ВОТ ТУТ ДОЛЖЕН БЫТЬ ТОКЕН
    api = vk.API(session)
    def filterUsers(owner_id):
        r=api.users.get(user_ids = OWNER_ID, fields="can_post")
        if r[0]["can_post"] == 1:
            #фильтруем базар и если подходит отправляем пост на стену

            send_messages(owner_id, r[0]['first_name'])
            sleep(100)
        else
            sys.exit()
    def getUsersFromGroup():
            #Получили список участников заданной группы
            groups = api.groups.getMembers(group_id = group_id.get(), fields='can_post')
            for i in groups['users']:
                #Получаем айди подписчика и отправляем в функцию для проверки по критериям
    def send_messages(OWNER_ID, name):
            #принимаем айдишник и имя чувака
            #r=api.users.get(user_ids = OWNER_ID, fields="can_post")
            messages = messages.get().replace('$username', name)
            api.wall.post(owner_id=OWNER_ID, message=messages, attachments=href_image.get())         
    frame=Frame(mainPanel,bd=5)
    #frame.grid(row=5,column=1)
    group_label = Label(mainPanel,text='ID группы', width=30)
    #group_label.grid(row=1,column=1)
    group_id = Entry(mainPanel, bd=2, text = 'Music')
    #group_id.grid(row=2,column=1)
    href_image_label = Label(mainPanel,text='Ссылка на картинку', width=30)
    #href_image_label.grid(row=3,column=1)
    href_image = Entry(mainPanel, bd=2)
    #href_image.grid(row=4,column=1)
    messages_label = Label(mainPanel,text='Сообщение', width=30)
    scrollbar = Scrollbar(frame)
    messages = Text(
        frame,
        yscrollcommand = scrollbar.set,
        height=10,
        width=50,
        )
    scrollbar.config(command=messages.yview)
    #group_count = Label(frame,text='', width=30)
    #group_list = Listbox(frame,height=10,width=50,selectmode=SINGLE)
    search = Button(mainPanel, text='Поиск', command = getUsersFromGroup)
    #scrollbar = Scrollbar(frame)
    # первая привязка
    #scrollbar['command'] = group_list.yview
    # вторая привязка
    #group_list['yscrollcommand'] = scrollbar.set
    group_label.pack()
    group_id.pack()
    href_image_label.pack()
    href_image.pack()
    messages_label.pack()
    frame.pack()
    messages.pack()
    search.pack()
    
    #group_count.pack()
    #scrollbar.pack(side='right', fill=Y)
    #group_list.pack()  
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

