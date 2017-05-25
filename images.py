#! /usr/bin/env python3
import vk
import vk_auth
client_id = '5732579'
scope = 'wall'

token, user_id = vk_auth.auth('', '', client_id, scope)
session = vk.Session(access_token=token) #ВОТ ТУТ ДОЛЖЕН БЫТЬ ТОКЕН
api = vk.API(session)
OWNER_ID = '53320096'
href = 'photo26749604_456240990'
r=api.users.get(user_ids = OWNER_ID, fields="can_post")
messages = "Hi @username"
messages = messages.replace('@username', r[0]['first_name'])
print(messages)
#messages = "Привет " + r[0]['first_name'] + ", я хочу поиграть с тобой в игру...."
#can = r[0]["can_post"]
#if can == 1:
	#api.wall.post(owner_id=OWNER_ID, message=messages, attachments=href)