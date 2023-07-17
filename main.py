import vk_api, traceback, threading, random,math,time,os,json
from datetime import datetime, timedelta
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime

import socket
threadCount = 0
threadForId = []
threadForCommUs = []


ServiceToken1 = 'b115d9a5b115d9a5b115d9a5bfb207e21bbb115b115d9a5d2d63d72eca97b73a59da34c'
ServiceToken2 = 'e51f6cc3e51f6cc3e51f6cc313e5630d51ee51fe51f6cc38776053b4afe81fc29de2890'
ServiceToken3 = '21f4181621f4181621f418166c22e5d00e221f421f41816426457688139458300c796fe'
ServiceToken4 = '8c4d16958c4d16958c4d1695bb8f5cdd8d88c4d8c4d1695efdc2d5520978aa39eb59ed6'
ServiceToken5 = 'a9b0c790a9b0c790a9b0c7905daaa10c89aa9b0a9b0c790ca21fc607f75bb761717d594'
ServiceToken6 = 'b89e9959b89e9959b89e995912bb8f5243bb89eb89e9959db0fa5467fb47fae87d507bb'
sessionSrv1 = vk_api.VkApi(token=ServiceToken1)
vkSrv1 = sessionSrv1.get_api()
sessionSrv2 = vk_api.VkApi(token=ServiceToken2)
vkSrv2 = sessionSrv2.get_api()
sessionSrv3 = vk_api.VkApi(token=ServiceToken3)
vkSrv3 = sessionSrv3.get_api()
sessionSrv4 = vk_api.VkApi(token=ServiceToken4)
vkSrv4 = sessionSrv3.get_api()
sessionSrv5 = vk_api.VkApi(token=ServiceToken5)
vkSrv5 = sessionSrv3.get_api()
sessionSrv6 = vk_api.VkApi(token=ServiceToken6)
vkSrv6 = sessionSrv3.get_api()


goshatok = "vk1.a.qUJokxhrzpz-bQ5F4MgCejIe_KPdCrFm0G4WT37yBefY8K08UWZ5uIVkWjSoXnKHJvQyfVHXCx4tKuIgM1oifxpCzFiCeIgMBFHY74UehNNW9HxGJpB4Yg9vjtyQqPs4yiantYXM1TEe7VmJIRzJGhIbVDLbVmyC-0D9gTDnailcRGmkHmR_n0fJsOTBhOhxgMjz5Nvo_rkzuUwhXQ8r8g"
sessionG = vk_api.VkApi(token=goshatok)
vkG = sessionG.get_api()

#token = "vk1.a.6XnjJyHsFrZuU-Hg4ZdQxd8bZNgDhU4pdCtkb_Y5Sa46BYyWG_4ymNeYAQh9Mw3Oau5cgJfNSekPKJZUSEjtxcKrz2v_KIZf9L3UwVmfp9Z2uQN6uT5QmyxUtUYRUh-eUgNjYYq-MKc0l7iYyA-8uvgbwRd4aoZpcnl4W4lk_PzxVgXV5naZirBhH4t0fXh-FElL3fwkrDkoVS261UG8dQ"
GroupToken = "vk1.a.PnjjMVU5_JxNWE9YSszDAwzTPmwK1wRh-jrfzJl5CEMKkO7IBMcySRzERTulLp_4AAMafqRlt0xhCkleFRVacZXOsf00Zkd5CCfODNZSbAiAJKa1-Fr5qwZPduoIV-yqD525rwSkHRYw0ID0Mhe2xtht4aXkPNDuRBdHkKRzI-d8iiuORPtriCvJDkZR1lPae1nWT5wgdE5jehn2gcuuIw"
session = vk_api.VkApi(token=GroupToken)
vk = session.get_api()
vkGroup = session.get_api()
longpoll = VkBotLongPoll(session, 213443881)

Bot1Token = "vk1.a.1TyfBTt-PlOIqHDzMgxpmQPF6yKw4twJKgAN7FUVc0DPXycyXUhkiu7Fvt1YgibguaLd0-K865qCX5y6T_umnqpbfusQxtbrfh4w8j7rQips4r52kuJd2g78USmefgVQN06lQp0IIUo4-9SuAGrUJPP1fRFgG0qIychD4kWFigL0RrHQx8ktb4Mw0OSQwVIwp_b8P5Rjuc2UBwoQeOorWA"
sessionBot1 = vk_api.VkApi(token=Bot1Token)
vkBot1 = sessionBot1.get_api()
prEvent = None


def main(): # Запуск бота
	global threadCount
	global prEvent
	try:
		for event in longpoll.listen():
			if event.obj != prEvent: 
				prEvent = event.obj
				thr = threading.Thread(target=EventHandler, args=(event, )).start()

	except BaseException as e:
		print(e)
		threading.Thread(target=main).start() 


def EventHandler(event):
	global threadCount
	if event.type == VkBotEventType.MESSAGE_EVENT: # Кнопки
		vk.messages.sendMessageEventAnswer(event_id=event.obj.event_id,  user_id=event.obj.user_id, peer_id=event.obj.peer_id,event_data=json.dumps(event.obj['payload']))
		id = event.obj['user_id']
		pld = event.obj['payload']
		user_get = vk.users.get(user_ids = (id))
		user_get = user_get[0]
		first_name = user_get['first_name']
		last_name = user_get['last_name']
		full_name = first_name + " " + last_name
		name = "@id" + str(id) + "(" + full_name + ")" + ", "
		TodaysDate = (datetime.now()).strftime('%d.%m.%y')

		allId = ''
		try:
			allId = open('data/AllId.txt', encoding='utf-8').read()
		except BaseException:
			pass

		if str(id) not in allId:
			msstart(id, 'Привет, '+full_name+'!👋\nЯ вижу, что ты новый пользователь MutSupp. Чтобы продвигать пост, тебе достаточно отправить мне ССЫЛКУ на него и выполнять всё, что я скажу!\n\n📝Также рекомендую тебе ознакомится с правилами - https://vk.com/topic-213443881_49767270')                           
			open('data/AllId.txt', 'a', encoding='utf-8').write(str(id)+'\n')
			open('data/'+TodaysDate+'AllId.txt', 'a', encoding='utf-8').write(str(id)+'\n')

		if pld == 4: # Назад

			waitYPusrs = ''
			try:
				waitYPusrs = open('data/wait_YPusrs.txt',encoding='utf-8').read()
			except BaseException:
				pass
			open(r'data/wait_YPusrs.txt', 'w',encoding='utf-8').write(waitYPusrs.replace(str(id)+'\n', ''))
			waitLikeOrComm = ''
			try:
				waitLikeOrComm=open(r'data/waitLikeOrComm.txt',encoding='utf-8').read()
			except BaseException:
				pass
			ZapDeleteId = ''
			try:
				ZapDeleteId=open(r'data/ZapDeleteId.txt', encoding='utf-8').read()
			except BaseException:
				pass
			open(r'data/waitLikeOrComm.txt','w',encoding='utf-8').write(waitLikeOrComm.replace(str(id)+'\n',''))
			CommOnUsts = ''
			try:
				CommOnUsts=open(r'data/CommOnUsts.txt',encoding='utf-8').read()
			except BaseException:
				pass
			open('data/CommOnUsts.txt','w',encoding='utf-8').write(CommOnUsts.replace(str(id)+'\n', ''))
			ZapDeleteId = ''
			try:
				ZapDeleteId = open(r'data/ZapDeleteId.txt', encoding='utf-8').read()
			except BaseException:
				print(traceback.format_exc())
			CommClosed = ''
			try:
				CommClosed = open(r'data/CommClosed.txt', encoding='utf-8').read()
			except BaseException:
				print(traceback.format_exc())
			open(r'data/ZapDeleteId.txt', 'w', encoding='utf-8').write(ZapDeleteId.replace(str(id)+'\n', ''))
			open(r'data/CommClosed.txt', 'w', encoding='utf-8').write(CommClosed.replace(str(id)+'\n', ''))
			regAutoLike = ''
			try:
				regAutoLike = open('AL/regAutoLike.txt', encoding='utf-8').read()
			except BaseException:
				pass
			open('AL/regAutoLike.txt', 'w', encoding='utf-8').write(regAutoLike.replace(str(id)+'\n', ''))
			msstart(id, 'Ок')
			

		if pld == 3: # Запись удалена
			try:
				open(r'data/ZapDeleteId.txt', 'a', encoding='utf-8').write(str(id)+'\n')
			except BaseException:
				print(traceback.format_exc())
				open(r'data/ZapDeleteId.txt', 'w', encoding='utf-8').write(str(id)+'\n')
			keyboard = VkKeyboard()
			keyboard.add_callback_button('Назад', VkKeyboardColor.NEGATIVE, payload=4)
			send_message(id, 'Отправь ссылку на удалённую запись', keyboard)


		if pld == '0': # Профиль
			UserInAutoLike = ''
			try:
				UserInAutoLike = open('AL/UserInAutoLike.txt', encoding='utf-8').read()
			except BaseException:
				pass
			TodaysDate = (datetime.now()).strftime('%d.%m.%y')
			LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
			keyboard = VkKeyboard(inline=True)

			if str(id) in UserInAutoLike:
				keyboard.add_button("АвтоЛайк", VkKeyboardColor.NEGATIVE)
			else:
				keyboard.add_button("АвтоЛайк", VkKeyboardColor.POSITIVE)


			keyboard.add_line()
			keyboard.add_button('Удалить пост')

			psts = ''
			try:
				psts += open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read() + '\n'
			except BaseException:
				pass 
			try:
				psts += open('data/Post_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read()
			except BaseException:
				pass

			pstsCom = ''
			try:
				pstsCom += open('data/PostCom_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read() + '\n'
			except BaseException:
				pass 
			try:
				pstsCom += open('data/PostCom_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read()
			except BaseException:
				pass
			vipUs = ''
			try:
				vipUs = open('data/vip.txt', encoding='utf-8').read()
			except BaseException:
				pass

			vipStat = 'Отсутствует'

			if str(id) in vipUs:
				vipStat = 'до '+open('data/vip'+str(id)+'.txt', encoding='utf-8').read()

			

			send_message(id, name+'твой профиль:\n\n🔤 Спец. Айди: '+str(id)+'\n💎VIP-статус: '+vipStat+'\n👥Пользователей MutSupp: '+str(len(allId.split()))+'\n\n📝Твои посты за 2 дня:\n\nДля лайков❤:\n'+psts+'\n\nДля комментариев💬:\n'+pstsCom, keyboard)



		if pld == 1: # Цены
			keyboard = VkKeyboard(inline=True)
			keyboard.add_openlink_button('Купить что-то', 'https://vk.com/id582582218')
			vk.messages.send(user_id=id, message='💸Цены услуг:\n\n• Подписки на группу (на твою группу будут подписываться все пользователи MutSupp) - 39р/день\n• Доп. пост (ты можешь скинуть ещё один пост) - 19р/пост\n• VIP-статус (привелегии - https://vk.com/topic-213443881_49983313) - 99р/мес\n\n@id730993538(*Если кнопка не работает*)', random_id=0, keyboard=keyboard.get_keyboard())  
	if event.type == VkBotEventType.MESSAGE_NEW: # Сообщения    
		if event.from_chat: 
			mid = event.obj['message']['conversation_message_id']
			id = event.obj['message']['peer_id']-2000000000
			text = event.obj['message']['text']
			userid = event.obj['message']['from_id']


			if id == 6: # MS WORK
				user_get = vk.users.get(user_ids = (userid))
				user_get = user_get[0]
				first_name = user_get['first_name']
				last_name = user_get['last_name']
				full_name = first_name + " " + last_name
				name = "@id" + str(id) + "(" + full_name + ")" + ", "
				try:
					os.mkdir('MSW')
				except BaseException:
					pass


				if 'https://vk.com/' in text and len(text.split()) == 1:
					try:
						us = text.split()[0]
						if 'https://vk.com/' in us:
								us = us.replace('https://vk.com/','')
						elif '[' in us:
							us = us.replace('[','').replace(']','').split('|')[0]
						us = vk.users.get(user_ids=us)[0]['id']
						InvitedUsrsID = ''
						try:
							InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						if str(us) not in InvitedUsrsID:
							open('MSW/IvitedUsrs.txt', 'a', encoding='utf-8').write(str(us)+'\n')	
							open('MSW/'+str(userid)+'IvitedUsrs.txt', 'a', encoding='utf-8').write(str(us)+'\n')	
							send_messageCHAT(id, '✅Я записал его - @id' + str(us))

						else:
							send_messageCHAT(id, '⛔Его уже приглашал кто-то!')
					except BaseException as e:
						send_messageCHAT(id, '⛔Ошибка: '+str(e))


				if text == 'key!':
					keyboard = VkKeyboard()
					keyboard.add_button('Проверить', VkKeyboardColor.POSITIVE)
					keyboard.add_button('Удалить', VkKeyboardColor.NEGATIVE)
					keyboard.add_line()
					keyboard.add_button('Получить')
					send_messageCHAT(id, 'ок', keyboard)


				if text == '[club213443881|@mutsupp] Получить' or text == 'Получить':
					try:
						uss = open('pplsForSpam.txt', encoding='utf-8').read().split()
						u = str(random.choice(uss))
						send_messageCHAT(id, '👉 Вот человек, которого можно попробовать пригласить в проект:\n\n@id'+u)
						uss1 = open('pplsForSpam.txt', encoding='utf-8').read()
						open('pplsForSpam.txt', 'w',encoding='utf-8').write(uss1.replace(u+'\n', ''))
					except BaseException as e:
						print(traceback.format_exc())
						send_messageCHAT(id, '⛔Ошибка: ' + str(e))


				if text == '[club213443881|@mutsupp] Проверить' or text == 'Проверить':
					sp = {}
					
					msg = ''
					n = 1
					SendPostsUsrs = []
					try:
						SendPostsUsrs = open('MSW/SendPostsUsrs.txt', encoding='utf-8').read().split()
					except BaseException:
						pass 
					invUsrs = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read().split()
					for c in invUsrs:
						sp[c] = SendPostsUsrs.count(c)
					sorted_users = sorted(sp.items(), key=lambda x: x[1])
					for user_id, num_posts in sorted_users:
						msg += str(n) + '. @id' + str(user_id)+' - ' + str(num_posts) + '\n'
						n += 1	

					send_messageCHAT(id, name+'вот люди, которых ты пригласил:\n\n'+msg)


				if text == '[club213443881|@mutsupp] Удалить' or text == 'Удалить':
					send_messageCHAT(id, 'Чтобы удалить кого-то напиши следующее: \n\n "удалить ЗДЕСЬ_ССЫЛКА" - удалит определённого человека\n"удалить активных" - удалит людей, скинувших 3 и более постов\n"удалить всех" - удалит всех людей, которых ты скинул')


				if 'удалить ' in text.lower() and 'активных' not in text.lower() and 'всех' not in text.lower() and len(text.split()) == 2:
					try:
						us = text.split()[1]
						if 'https://vk.com/' in us:
								us = us.replace('https://vk.com/','')
						elif '[' in us:
							us = us.replace('[','').replace(']','').split('|')[0]
						us = vk.users.get(user_ids=us)[0]['id']
						InvitedUsrsID = ''
						try:
							InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						inv = ''
						try:
							inv = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						open('MSW/IvitedUsrs.txt', 'w', encoding='utf-8').write(InvitedUsrsID.replace(str(us)+'\n', ''))
						open('MSW/'+str(userid)+'IvitedUsrs.txt', 'w', encoding='utf-8').write(inv.replace(str(us)+'\n', ''))	
						send_messageCHAT(id, '✅ Я удалил его - @id' +str(us))
					except BaseException as e:
						send_messageCHAT(id, '⛔Ошибка: '+str(e))


				if 'удалить активных ' in text.lower() and len(text.split()) == 3:
					sp = {}
					dlt = []
					
					msg = ''
					n = 1
					SendPostsUsrs = []
					try:
						SendPostsUsrs = open('MSW/SendPostsUsrs.txt', encoding='utf-8').read().split()
					except BaseException:
						pass 
					invUsrs = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read().split()
					for c in invUsrs:
						sp[c] = SendPostsUsrs.count(c)
					for c in sp:
						q = sp[c]
						if q >= 3:
							dlt.append(c)

					for us in dlt:
						InvitedUsrsID = ''
						try:
							InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						inv = ''
						try:
							inv = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						open('MSW/IvitedUsrs.txt', 'w', encoding='utf-8').write(InvitedUsrsID.replace(str(us)+'\n', ''))
						open('MSW/'+str(userid)+'IvitedUsrs.txt', 'w', encoding='utf-8').write(inv.replace(str(us)+'\n', ''))	
						msg += '@id'+str(us)+'\n'
					send_messageCHAT(id, '✅ Я удалил всех людей, скинувших 3 и более постов:\n\n' + msg)


				if 'удалить всех' in text.lower() and len(text.split()) == 2:
					msg = ''
					invUsrs = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read().split()
					for us in invUsrs:
						InvitedUsrsID = ''
						try:
							InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						inv = ''
						try:
							inv = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read()
						except BaseException:
							pass
						open('MSW/IvitedUsrs.txt', 'w', encoding='utf-8').write(InvitedUsrsID.replace(str(us)+'\n', ''))
						open('MSW/'+str(userid)+'IvitedUsrs.txt', 'w', encoding='utf-8').write(inv.replace(str(us)+'\n', ''))	
						msg += '@id'+str(us)+'\n'
					send_messageCHAT(id, '✅ Я удалил всех людей:\n\n' + msg)


			if id == 3: # MS ADMINS
				TodaysDate = (datetime.now()).strftime('%d.%m.%y')
				LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')


				if '+вип ' in text and len(text.split()) > 2:
					try:
						month = int(text.split()[2])
						us = text.split()[1]
						if 'https://vk.com/' in us:
								us = us.replace('https://vk.com/','')
						elif '[' in us:
							us = us.replace('[','').replace(']','').split('|')[0]
						us = vk.users.get(user_ids=us)[0]['id']


						vipUs = ''
						try:
							vipUs = open('data/vip.txt', encoding='utf-8').read()
						except BaseException:
							pass
						if str(us) in vipUs:
							send_messageCHAT(id, '⛔У него @id'+str(us)+' уже есть VIP-ка!')
						else:
							open('data/vip.txt', 'a', encoding='utf-8').write(str(us)+'\n')
							TodaysDate = (datetime.now()).strftime('%d.%m.%y')
							dt = 31 * month
							DateClear = ((datetime.now()) + timedelta(days=int(dt))).strftime('%d.%m.%y')
							open('data/vip'+str(us)+'.txt', 'w', encoding='utf-8').write(str(DateClear))
							send_messageCHAT(id, '✅Успешно выдан VIP статус @id'+str(us)+' до '+DateClear)  
							try:
								send_message(us, '✅ Тебе выдан VIP-статус до '+DateClear)  
							except BaseException:
								pass


					except BaseException as e:
						send_messageCHAT(id, '⛔Ошибка: '+str(e))


				if text == 'upgkey':
					allUs = []
					uss = open('data/AllId.txt', encoding='utf-8').read().split()
					for c in uss:
						allUs.append(c)
					for i in allUs:
						try:
							msstart(i, '✅Клавиатура обновлена!')
						except BaseException:
							send_messageCHAT(3, 'Заблокал - @id'+str(i))

					
				if '+посты ' in text:
					try:
						us = text.split()[1]
						psts = text.split()[2]
						if 'https://vk.com/' in us:
								us = us.replace('https://vk.com/','')
						elif '[' in us:
							us = us.replace('[','').replace(']','').split('|')[0]
						us = vk.users.get(user_ids=us)[0]['id']
						open('data/addPost'+str(us)+'.txt', 'w', encoding='utf-8').write(str(psts))
						send_messageCHAT(id, '✅Я добавил доп. пост @id'+str(us)+'. Кол-во - '+open('data/addPost'+str(us)+'.txt', encoding='utf-8').read())
					except BaseException as e:
						send_messageCHAT(id, '⛔Ошибка: '+str(e))


				if text == 'dlt':
					DeleteDontActiveUsrs()
					send_messageCHAT(id, 'Завершил')


				if text == "[club213443881|@mutsupp] MutSupp":
					TodaysDate = (datetime.now()).strftime('%d.%m.%y')
					LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
					vipUs = ''
					try:
						vipUs = open('data/vip.txt', encoding='utf-8').read()
					except BaseException:
						pass
					allId = ''
					try:
						allId = open('data/AllId.txt', encoding='utf-8').read()
					except BaseException:
						pass

					pstsT = ''
					try:
						pstsT = open('data/'+TodaysDate+'wall.txt', encoding='utf-8').read()
					except BaseException:
						pass
					pstsL = ''
					try:
						pstsL = open('data/'+LastDate+'wall.txt', encoding='utf-8').read()
					except BaseException:
						pass
					pstsCT = ''
					try:
						pstsCT = open('data/'+TodaysDate+'WallForComm.txt', encoding='utf-8').read()
					except BaseException:
						pass
					pstsCL = ''
					try:
						pstsCL = open('data/'+LastDate+'WallForComm.txt', encoding='utf-8').read()
					except BaseException:
						pass

					UserInAutoLike = ''
					try:
						UserInAutoLike = open('AL/UserInAutoLike.txt', encoding='utf-8').read()
					except BaseException:
						pass
					AllIdToday = ''
					try:
						AllIdToday = open('data/'+TodaysDate+'AllId.txt', encoding='utf-8').read()
					except BaseException:
						pass

					send_messageCHAT(id, "Вот вся информация о MutSupp'е на данный момент📊:\n\n📈Новых пользователей за сегодня: "+str(len(AllIdToday.split()))+"\n👥Пользователей: "+str(len(allId.split()))+"\n💎VIP-пользователей: "+str(len(vipUs.split()))+"\n❤АвтоЛайком пользуются: "+str(len(UserInAutoLike.split()))+"\n\n📝❤Постов за сегодня: "+str(len(pstsT.split()))+"\n📝❤Постов за вчера: "+str(len(pstsL.split()))+"\n📝❤💬Постов за сегодня: "+str(len(pstsCT.split()))+"\n📝❤💬Постов за вчера: "+str(len(pstsCL.split())))


				if text == 'key!!!':
					keyboard = VkKeyboard()
					keyboard.add_button("MutSupp", VkKeyboardColor.POSITIVE)
					send_messageCHAT(id, 'okeey)', keyboard)


				if "!блок " in text:
					try:
						us = text.split()[1]
						com =  text.split()[2]
						UsInJob = []
						try:
							UsInJob=open('data/UsInJob.txt', encoding='utf-8').read().split()
						except BaseException:
							pass
						for j in UsInJob:
							usrsNew=''
							try:
								usrsNew=open('data/'+str(j)+'usrsNew.txt', encoding='utf-8').read()
							except BaseException:
								pass
							for h in usrsNew.split():
								if str(h) == str(us):
									open('data/'+str(j)+'usrsNew.txt','w', encoding='utf-8').write(usrsNew.replace(str(h)+'\n',''))
									send_messageCHAT(6, '@id'+str(j)+', я удалил его, так как он нарушил правило MutSupp - '+us)


						if 'https://vk.com/' in us:
							us = us.replace('https://vk.com/','')
						elif '[' in us:
							us = us.replace('[','').replace(']','').split('|')[0]
						us = vk.users.get(user_ids=us)[0]['id']
						vkG.groups.ban(group_id=213443881, owner_id=us,reason=0,comment=com,comment_visible=1)
						

						AllId = ''
						try:
							AllId = open('data/AllId.txt', encoding='utf-8').read()
						except BaseException:
							pass 
						open('data/AllId.txt','w', encoding='utf-8').write(AllId.replace(str(us)+'\n',''))
						AllId1 = ''
						try:
							AllId1 = open('data/AllId1.txt', encoding='utf-8').read()
						except BaseException:
							pass 
						open('data/AllId1.txt','w', encoding='utf-8').write(AllId1.replace(str(us)+'\n',''))



						send_messageCHAT(3, 'Пользователь @id'+str(us)+' - заблокирован. Причина: '+com)
					except BaseException as e:
						send_messageCHAT(3, str(e))


				if '+слот' in text:
					try:
						textInList = text.split()
						slot = textInList[1]
						group = textInList[2]
						date = textInList[3]        
						if '[' in group and ']' in group:
							group = 'https://vk.com/'+group.replace('[', '').replace(']','').split('|')[0]
						group=group.replace('https://vk.com/','')
							
						group = str(vk.groups.getById(group_id=group)[0]['id'])
						TodaysDate = (datetime.now()).strftime('%d.%m.%y')
						DateClear = ((datetime.now()) + timedelta(days=int(date))).strftime('%d.%m.%y')
						open(r'data/slot'+slot+'.txt', 'w', encoding='utf-8').write(group)
						open(r'data/slotTIme'+slot+'.txt', 'w', encoding='utf-8').write(DateClear)
						vk.messages.send(chat_id=id, message='Группа @club'+group+' записана в слот номер '+slot+' до '+DateClear, random_id=0)
					except BaseException:
						vk.messages.send(chat_id=id, message='Какая-то ошибка', random_id=0)
						print(traceback.format_exc())
				if '-слот' in text:
					textInList = text.split()
					slot = textInList[1]
					open(r'data/slot'+slot+'.txt', 'w', encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme'+slot+'.txt', 'w', encoding='utf-8')
					vk.messages.send(chat_id=id, message='Слот номер '+slot+' очищен', random_id=0)


				if "+сообщение" in text:
					text = text.replace("+сообщение", '')
					AllId = open(r'data/AllId.txt', encoding='utf-8').read()
					AllIdInList = AllId.split()
					threading.Thread(target=SmsSend, args=(AllIdInList, text,)).start()

				if text == '!группы':
					sms = ''
					for i in range(1,6):
						group_id = open(r'data/slot'+str(i)+'.txt', encoding='utf-8').read()
						date = open(r'data/slotTIme'+str(i)+'.txt', encoding='utf-8').read()
						if '.' in date:
							date = ' - до ' + date
						group = vk.groups.getById(group_id=group_id)[0]['screen_name']
						sms += str(i)+'. @'+group+date+'\n'
					vk.messages.send(chat_id=3, message=sms.replace('@mutsupp', '- Пустой Слот - '), random_id=0)

				if text == 'act threads':
					send_messageCHAT(id, str(threading.active_count()))


			if id == 2: # MS CHAT
				getSMS = vk.messages.getById(message_ids=mid)
				try:
					if len(getSMS['items'][0]['attachments']) > 0:
						gr_id = str(getSMS['items'][0]['attachments'][0]['wall']['from_id'])
						it_id = str(getSMS['items'][0]['attachments'][0]['wall']['id'])
						url = 'https://vk.com/wall'+gr_id+'_'+it_id
						text = url
				except BaseException: 
					text=text

				if 'https://vk.com/' in text and userid != 730993538: 
					TodaysDate = (datetime.now()).strftime('%d.%m.%y')
					LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
				# Получение имени и фамилии
					user_get = vk.users.get(user_ids = (userid))
					user_get = user_get[0]
					first_name = user_get['first_name']
					last_name = user_get['last_name']
					full_name = first_name + " " + last_name
					name = "@id" + str(userid) + "(" + full_name + ")" + ", "
					vk.messages.send(chat_id=id, message=name+"саппорт находится в ЛС бота (там же будет инструкция) - https://vk.com/im?sel=-213443881", random_id=0)
					try:
						vk.messages.delete(message_ids=mid, delete_for_all=1, peer_id=2000000000 + 2)
					except BaseException:
						pass


		if event.from_user:
			id = event.obj['message']['from_id']
			mid = event.obj['message']['id']
			text = event.obj['message']['text']
			tp = ''
			try:
				tp = event.obj['message']['attachments'][0]['type']
			except BaseException:
				tp = ''
			if tp == 'wall':
				try:
					link = 'https://vk.com/wall' + str(event.obj['message']['attachments'][0]['wall']['from_id']) + '_' + str(event.obj['message']['attachments'][0]['wall']['id'])
					text = link
				except BaseException:
					text= text
			else: 
				text = text

			
			
			TodaysDate = (datetime.now()).strftime('%d.%m.%y')
			LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
			hour = (datetime.now()).strftime('%H')
			user_get = vk.users.get(user_ids = (id))
			user_get = user_get[0]
			first_name = user_get['first_name']
			last_name = user_get['last_name']
			full_name = first_name + " " + last_name
			name = "@id" + str(id) + "(" + full_name + ")" + ", "
			waitLikeOrComm = ''
			try:
				waitLikeOrComm=open(r'data/waitLikeOrComm.txt',encoding='utf-8').read()
			except BaseException:
				pass
			ZapDeleteId = ''
			try:
				ZapDeleteId=open(r'data/ZapDeleteId.txt', encoding='utf-8').read()
			except BaseException:
				pass
			CommClosed = ''
			try:
				CommClosed=open(r'data/CommClosed.txt', encoding='utf-8').read()
			except BaseException:
				pass
			waitYPusrs = ''
			try:
				waitYPusrs = open('data/wait_YPusrs.txt',encoding='utf-8').read()
			except BaseException:
				pass
			regAutoLike = ''
			try:
				regAutoLike = open('AL/regAutoLike.txt', encoding='utf-8').read()
			except BaseException:
				pass
			UserInAutoLike = ''
			try:
				UserInAutoLike = open('AL/UserInAutoLike.txt', encoding='utf-8').read()
			except BaseException:
				pass
			allId = ''
			try:
				allId = open('data/AllId.txt', encoding='utf-8').read()
			except BaseException:
				pass
			vipUs = ''
			try:
				vipUs = open('data/vip.txt', encoding='utf-8').read()
			except BaseException:
				pass

			# - - - - Проверка на новичков - - - - 
			if str(id) not in allId:
				msstart(id, 'Привет, '+full_name+'!👋\nЯ вижу, что ты новый пользователь MutSupp. Чтобы продвигать пост, тебе достаточно отправить мне ССЫЛКУ на него и выполнять всё, что я скажу!\n\n📝Также рекомендую тебе ознакомится с правилами - https://vk.com/topic-213443881_49767270')                           
				open('data/AllId.txt', 'a', encoding='utf-8').write(str(id)+'\n')
				open('data/'+TodaysDate+'AllId.txt', 'a', encoding='utf-8').write(str(id)+'\n')

			# - - - - Кнопка "подписался" и замена текста на пост - - - - 
			if text == 'Подписался':
				send_message(id, "Сейчас проверю...")
				text = open(r'data/'+str(id)+'postSubs.txt', encoding='utf-8').read()

			# - - - - AutoLike - - - - 
			if str(id) in regAutoLike and text != 'Назад':
				open('AL/regAutoLike.txt', 'w', encoding='utf-8').write(regAutoLike.replace(str(id)+'\n', ''))
				tkn = text[text.find('access_token=')+13:text.find('&')]
				msstart(id, 'Проверяю токен...')
				try:
					session2 = vk_api.VkApi(token=tkn)
					vk2 = session2.get_api()
					longpoll2 = VkLongPoll(session2)

					open(r'AL/tokens.txt', 'a', encoding='utf-8').write(tkn+'\n')
					open(r'AL/'+tkn+'.txt', 'w', encoding='utf-8').write(str(id))
					open(r'AL/'+str(id)+'tkn.txt', 'w', encoding='utf-8').write(tkn)
					open(r'AL/UserInAutoLike.txt', 'a', encoding='utf-8').write(str(id)+'\n')

					msstart(id, '✅Твоя страница успешно подключена к системе АвтоЛайка! Чтобы отключить, нажми на АвтоЛайк в Профиле')
				except BaseException:
					print(traceback.format_exc())
					msstart(id, '⛔Ошибка: неверный токен')
				return
			if text == 'АвтоЛайк':
				if str(id) not in vipUs:
					keyboard = VkKeyboard(inline=True)
					keyboard.add_openlink_button('Купить', 'https://vk.com/id730993538')
					send_message(id, '⛔ Это действие доступно только для обладателей VIP-статуса!', keyboard)
				else:
					if str(id) not in UserInAutoLike:
						open('AL/regAutoLike.txt', 'a', encoding='utf-8').write(str(id)+'\n')
						keyboard = VkKeyboard()
						keyboard.add_button('Назад', VkKeyboardColor.NEGATIVE)
						send_message(id, 'Скинь сюда свой токен. Сайт - https://vkhost.github.io/\n\nИнструкция:\n1. Нажимаешь на "Настройки" (не vk.com)\n2. Выбираешь все пункты (Доступ в любое время, Статус, Стена и т.д. ВСЕ!)\n3. Нажимаешь получить\n4. Разрешаешь доступ\n5. Копируешь ВСЮ адресную строку (Ссылку на веб-страницу)\n6. Отправляешь сюда всё, что скопировал(а)\n\nЕсли ВК блокирует ссылку, то скопируй её, и вставь в любой другой браузер\n\nПодключая АвтоЛайк, ты соглашаешься с условиями пользования: https://vk.com/topic-213443881_50052623', keyboard)
					else:
						try:
							tkn = open(r'AL/'+str(id)+'tkn.txt', encoding='utf-8').read()
							os.remove('AL/'+tkn+'.txt')
							os.remove('AL/'+str(id)+'tkn.txt')
							tkns = ''
							try:
								tkns = open(r'AL/tokens.txt', encoding='utf-8').read()
							except BaseException:
								pass
							open(r'AL/tokens.txt', 'w', encoding='utf-8').write(tkns.replace(tkn+'\n', ''))
							open(r'AL/UserInAutoLike.txt', 'w', encoding='utf-8').write(UserInAutoLike.replace(str(id)+'\n', ''))
							send_message(id, '✅ Я отключил тебя от АвтоЛайка')
						except BaseException as e:
							send_message(id, '⛔Ошибка: '+str(e))

			# - - - - Запуск проверки комментариев - - - -
			if text == 'Прокомментировал':
				if id in threadForCommUs:
					send_message(id, 'Я уже проверяю комментарии!!!')
				if id not in threadForCommUs:
					msstart(id, '🔎Проверяю. Это может занять от 30с до 5 минут...')
					
					if str(id) not in vipUs:
						time.sleep(6)
					threadForCommUs.append(id)
					threading.Thread(target=CommentCheckProcess, args=(id, open(r'data/'+str(id)+'WallsForComm.txt',encoding='utf-8').read().split(), TodaysDate)).start()


			# - - - - Приём постов - - - -
			if 'https://' in text and 'удалить' not in text.lower() and 'жалоба' not in text.lower():
				if "vk" not in text: # не пост вк
					send_message(id, '⛔ Сюда можно кидать только ссылки на ПОСТЫ ВК!')
				else:
					text = PostHandler(text)
					text = text.replace(' ','')
					try:
						ForOwnANdItem = text.replace("https://vk.com/wall", "").split("_")
						int(ForOwnANdItem[0])
						int(ForOwnANdItem[1])
					except BaseException:
						send_message(id, '⛔ Не правильная ссылка! (кинь стандартную ссылку типа: "https://vk.com/wall-123456789_123" или обратись в поддержку)')
						return

					if str(id) in CommClosed:
						TodaysWalls =''
						LastWalls=''
						TodaysWallsm=''
						LastWallsm=''
						open(r'data/CommClosed.txt', 'w', encoding='utf-8').write(CommClosed.replace(str(id)+'\n', ''))
						pstsC1 = ''
						try:
							pstsC1 = open('data/'+TodaysDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass
						pstsC = ''
						try:
							pstsC += open('data/'+LastDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass
						pstsC11 = ''
						try:
							pstsC11 = open('data/'+TodaysDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass
						pstsC111 = ''
						try:
							pstsC111 += open('data/'+LastDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass

						if text not in pstsC1+' '+pstsC+' '+pstsC11+' '+pstsC111:
							msstart(id, '⛔Этой записи нет в базе! (Возможно кто-то уже удалил её или ты случайно нажал на кнопку "Закрытые ком-ии")')
						else:
							ForOwnANdItem = text.replace("https://vk.com/wall", "").split("_")
							owner_id = int(ForOwnANdItem[0])
							item_id = int(ForOwnANdItem[1])
							try:
								idc = vkG.wall.createComment(owner_id=owner_id,post_id=item_id, message='CheckOnCloseComments', from_group=213443881)['comment_id']
								vkG.wall.deleteComment(owner_id=owner_id,comment_id=idc)
								msstart(id, '⛔Запись ' + text + ' с открытыми комментариями!')
							except BaseException:
								open('data/'+TodaysDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC1.replace(text+'\n',''))
								open('data/'+LastDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC.replace(text+'\n',''))
								open('data/'+TodaysDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC11.replace(text+'\n',''))
								open('data/'+LastDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC111.replace(text+'\n',''))
								msstart(id, '✅Комментарии действительно закрыты. Удаляю пост из базы')


					# Пост для удаления
					elif str(id) in ZapDeleteId:
						TodaysWalls =''
						LastWalls=''
						TodaysWallsm=''
						LastWallsm=''
						open(r'data/ZapDeleteId.txt', 'w', encoding='utf-8').write(ZapDeleteId.replace(str(id)+'\n', ''))
						walls=''
						try: 
							TodaysWalls = open(r'data/'+TodaysDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
							walls += TodaysWalls
						except BaseException:
							print(traceback.format_exc())
						try:
							LastWalls = open(r'data/'+LastDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
							walls += LastWalls
						except BaseException:
							print(traceback.format_exc())
						pstsC1 = ''
						try:
							pstsC1 = open('data/'+TodaysDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass
						pstsC = ''
						try:
							pstsC += open('data/'+LastDate+'WallForComm.txt', encoding='utf-8').read()
						except BaseException:
							pass

						if text not in walls and text not in pstsC:
							for i in allId.split():
								postsForLikes = ''
								try:
									postsForLikes = open('data/'+i+'postsForLikes.txt', encoding='utf-8').read()
								except BaseException:
									pass
								open('data/'+i+'postsForLikes.txt', 'w',encoding='utf-8').write(postsForLikes.replace(text+'\n', ''))
							msstart(id, '⛔Этой записи нет в базе! (Возможно кто-то уже удалил её или ты случайно нажал на кнопку "Запись удалена")')
						else:
							ForOwnANdItem = text.replace("https://vk.com/wall", "").split("_")
							owner_id = int(ForOwnANdItem[0])
							item_id = int(ForOwnANdItem[1])
							try:
								vkBot1.likes.add(owner_id=owner_id,item_id=item_id,type='post')
								msstart(id, 'Запись ' + text + ' не удалена!')
							except BaseException:
								open('data/'+TodaysDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC1.replace(text+'\n',''))
								open('data/'+LastDate+'WallForComm.txt','w', encoding='utf-8').write(pstsC.replace(text+'\n',''))
								open(r'data/'+TodaysDate+'wall.txt', 'w', encoding="utf-8").write(TodaysWalls.replace(text+'\n', ''))
								open(r'data/'+LastDate+'wall.txt', 'w', encoding="utf-8").write(LastWalls.replace(text+'\n', ''))
								open(r'data/'+TodaysDate+'wall.txt', 'w', encoding="utf-8").write(TodaysWallsm.replace(text+'\n', ''))
								open(r'data/'+LastDate+'wall.txt', 'w', encoding="utf-8").write(LastWallsm.replace(text+'\n', ''))

								for i in allId.split():
									postsForLikes = ''
									try:
										postsForLikes = open('data/'+i+'postsForLikes.txt', encoding='utf-8').read()
									except BaseException:
										pass
									open('data/'+i+'postsForLikes.txt', 'w',encoding='utf-8').write(postsForLikes.replace(text+'\n', ''))

								msstart(id, '✅Запись удалена. Убираю её из базы')
						
						
					else:
						dltPosts = ''
						try:
							dltPosts = open('data/dltPosts.txt', encoding='utf-8').read()
						except BaseException:
							pass
						if text not in dltPosts:

							group_not_subsc = ''
							if str(id) not in vipUs:
								group_not_subsc = CheckSubscOnGroup(id)

							if group_not_subsc != '':
								keyboard = VkKeyboard(inline=True)
								keyboard.add_openlink_button('Хочу Сюда', 'https://vk.com/id730993538')
								keyboard.add_line()
								keyboard.add_button('Подписался')
								open(r'data/'+str(id)+'postSubs.txt','w',encoding='utf-8').write(text)
								send_message(id, '😎Сначала нужно подписаться на группы, а потом уже скинуть пост:\n\n'+group_not_subsc, keyboard)
							else:	
								keyboard = VkKeyboard()
								keyboard.add_button('❤Лайки', VkKeyboardColor.POSITIVE)
								keyboard.add_button('💬Комментарии', VkKeyboardColor.POSITIVE)
								keyboard.add_button('Назад', VkKeyboardColor.NEGATIVE)
								send_message(id, 'Что ты хочешь получить? (см. кнопки)', keyboard)
								open('data/waitLikeOrComm.txt', 'a', encoding='utf-8').write(str(id)+'\n')
								open(r'data/'+str(id)+'post.txt','w',encoding='utf-8').write(text)
						else:
							send_message(id, '⛔ Этот пост в чёрном списке!')
				

			# - - - - Выбор лайков или комментариев - - - -
			if str(id) in waitLikeOrComm:
				if text == '❤Лайки':
					open('data/waitLikeOrComm.txt', 'w', encoding='utf-8').write(waitLikeOrComm.replace(str(id)+'\n', ''))
					TextToList = open(r'data/'+str(id)+'post.txt',encoding='utf-8').read().split()
					for i in TextToList:
						if "https://vk.com/wall" in i:
							banposts = ''
							try:
								banposts=open('data/banposts.txt',encoding='utf-8').read()
							except BaseException:
								pass
							if i in banposts:
								msstart(id, '⛔Этот пост находится в черном списке!')
							else:
								usSendPostsToday = ''
								try:
									usSendPostsToday = open('data/'+TodaysDate+'peoples.txt',encoding='utf-8').read()
								except BaseException:
									pass
								addPosts = 0
								try:
									addPosts = int(open('data/addPost'+str(id)+'.txt', encoding='utf-8').read().split()[0])
								except BaseException:
									pass

								vipUs = ''
								try:
									vipUs = open('data/vip.txt', encoding='utf-8').read()
								except BaseException:
									pass

								if str(id) in vipUs:
									usSendPostsToday = usSendPostsToday.replace(str(id), '', 1)

								if str(id) not in usSendPostsToday or addPosts > 0:
									if id in threadForId:
										send_message(id, '🕑Подожди, я проверяю лайкаешь ты записи или нет...')
									if id not in threadForId:
										if threadCount <15:
											threadCount+=1
											threadForId.append(id)
											
											threading.Thread(target=WallWriting, args=(id, TodaysDate, LastDate, i, )).start()

										if threadCount >=15:
											
											msstart(id, '🙁Все потоки заполнены. Подожди чуть-чуть...')
								else:
									msstart(id, "⛔Ты сегодня уже кидал пост!")
				if text == '💬Комментарии':
					
					try:
						uss = ''
						try:
							uss = open(r'data/'+TodaysDate+'UsersForComm.txt',encoding='utf-8').read()
						except BaseException:
							pass
						addPosts = 0
						try:
							addPosts = int(open('data/addPost'+str(id)+'.txt', encoding='utf-8').read().split()[0])
						except BaseException:
							pass

						vipUs = ''
						try:
							vipUs = open('data/vip.txt', encoding='utf-8').read()
						except BaseException:
							pass

						if str(id) in vipUs:
							uss = uss.replace(str(id), '', 1)
						
						if str(id) not in uss or addPosts > 0:
							
							msg = ''
							usWallsForComm = 'None'
							try:
								usWallsForComm = msg = open(r'data/'+str(id)+'WallsForComm.txt',encoding='utf-8').read()
							except BaseException:
								pass
							if 'https://vk.com/wall' not in usWallsForComm:
								usWallsForComm = 'None'
							wallsComm = []

							if 'None' in usWallsForComm:

								wallsComm = GetWallsComm(id)

								msg = ''
								for i in wallsComm:
									msg += i+'\n'
								open(r'data/'+str(id)+'WallsForComm.txt', 'w',encoding='utf-8').write(msg)
							if 'None' not in usWallsForComm:
								wallsComm.append('none')
							
							if len(wallsComm) == 0:
								text =open(r'data/'+str(id)+'post.txt',encoding='utf-8').read()
								ForOwnANdItem = text.replace("https://vk.com/wall", "").split("_")
								owner_id = ForOwnANdItem[0]
								item_id = ForOwnANdItem[1]
								open('data/PostCom_From'+str(id)+'_'+TodaysDate+'.txt', 'w', encoding='utf-8').write(str('https://vk.com/wall'+owner_id+'_'+item_id))
								open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', 'w', encoding='utf-8').write(str('https://vk.com/wall'+owner_id+'_'+item_id))
								open('data/wall'+owner_id+'_'+item_id+'COMM.txt', 'w', encoding='utf-8').write(str(id))
								open(r'data/'+str(id)+'WallsForComm.txt', 'w',encoding='utf-8').write('None')
								
								

								open(r'data/'+TodaysDate+'WallForComm.txt','a',encoding='utf-8').write(text+'\n')

								addPosts = 0
								try:
									addPosts = int(open('data/addPost'+str(id)+'.txt', encoding='utf-8').read().split()[0])
								except BaseException:
									pass
								if addPosts > 0:
									open('data/addPost'+str(id)+'.txt', 'w', encoding='utf-8').write(str(addPosts - 1))
								msstart(id, '✅Твоя запись подключена к системе комментариев!')
								open('MSW/SendPostsUsrs.txt', 'a', encoding='utf-8').write(str(id)+'\n')


								vipUs = ''
								try:
									vipUs = open('data/vip.txt', encoding='utf-8').read()
								except BaseException:
									pass

								if str(id) not in vipUs:
									threading.Thread(target=SendPostsAllUs, args=(id,text,'💬 Запрос комментария на пост!\n'+text, 1, )).start()
									
								else:
									open('data/vipPosts.txt', 'a', encoding='utf-8').write(text+'\n')
									threading.Thread(target=SendPostsAllUs, args=(id,text,'💎💬 Запрос комментария на пост!\n'+text, 1, )).start()
									

								
									
							if len(wallsComm) > 0:
								
								keyboard = VkKeyboard(inline=True)
								keyboard.add_button('Прокомментировал')
								keyboard.add_button('Перезапустить')
								keyboard.add_line()
								keyboard.add_button('Жалоба')

								ms = ''
								n=0
								for cc in msg.split():
									n+=1
									vPsts = ''
									try:
										vPsts = open('data/vipPosts.txt',encoding='utf-8').read()
									except BaseException:
										pass
									if cc in vPsts:
										ms += '💎 '+cc+'\n'
									else:	
										ms += str(n)+'. '+cc+'\n'

								send_message(id, '⛔Сначала тебе нужно оставить комментарии на этих записях (по тематике и со своей страницы!):\n\n'+ms+'\n\n@id730993538(*Обратись в поддержку), если у тебя есть проблемы с постами или нажми на кнопку "Перезапустить" для того, чтобы бот прислал тебе другие посты', keyboard)					
						else:
							send_message(id, '⛔Сегодня ты уже подключал запись к системе комментариев! Попробуй завтра!')	

					except BaseException as e:
						print(traceback.format_exc())
						send_message(id,'Ошибка: '+ str(e))


			if text == 'Пролайкал':
				TextToList = open(r'data/'+str(id)+'post.txt',encoding='utf-8').read().split()
				for i in TextToList:
					if "https://vk.com/wall" in i:
						banposts = ''
						try:
							banposts=open('data/banposts.txt',encoding='utf-8').read()
						except BaseException:
							pass
						if i in banposts:
							msstart(id, '⛔Этот пост находится в черном списке!')
						else:
							usSendPostsToday = ''
							try:
								usSendPostsToday = open('data/'+TodaysDate+'peoples.txt',encoding='utf-8').read()
							except BaseException:
								pass
							addPosts = 0
							try:
								addPosts = int(open('data/addPost'+str(id)+'.txt', encoding='utf-8').read().split()[0])
							except BaseException:
								pass

							vipUs = ''
							try:
								vipUs = open('data/vip.txt', encoding='utf-8').read()
							except BaseException:
								pass

							if str(id) in vipUs:
								usSendPostsToday = usSendPostsToday.replace(str(id), '', 1)
								usSendPostsToday = usSendPostsToday.replace(str(id), '', 1)
								usSendPostsToday = usSendPostsToday.replace(str(id), '', 1)

							if str(id) not in usSendPostsToday or addPosts > 0:
								if id in threadForId:
									send_message(id, '🕑Подожди, я проверяю лайкаешь ты записи или нет...')
								if id not in threadForId:
									if threadCount <15:
										threadCount+=1
										threadForId.append(id)
										
										threading.Thread(target=WallWriting, args=(id, TodaysDate, LastDate, i, )).start()

									if threadCount >=15:
										
										msstart(id, '🙁Все потоки заполнены. Подожди чуть-чуть...')
							else:
								msstart(id, "⛔Ты сегодня уже кидал пост!")


			if text == 'Удалить пост':
				send_message(id, '🗑️ Если хочешь удалить какой-то из постов, то напиши сюда след. команду: \n"удалить ЗДЕСЬ_ССЫЛКА"')


			if 'удалить' in text.lower() and 'пост' not in text.lower():
				psts = ''
				try:
					psts += open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read() + '\n'
				except BaseException:
					pass 
				try:
					psts += open('data/Post_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read()
				except BaseException:
					pass
				if text.split()[1] in psts:
					try:
						tdPsts = ''
						try:
							tdPsts = open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read()
						except BaseException:
							pass
						if text.split()[1] in tdPsts:
							try:
								open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', 'w', encoding='utf-8').write(open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read().replace(str(text.split()[1])+'\n', ''))
							except BaseException:
								pass
							try:
								open('data/'+TodaysDate+'peoples.txt','w',encoding='utf-8').write(open('data/'+TodaysDate+'peoples.txt',encoding='utf-8').read().replace(str(id)+'\n', ''))
							except BaseException:
								pass
						else:
							try:
								open('data/Post_From'+str(id)+'_'+LastDate+'.txt', 'w', encoding='utf-8').write(open('data/Post_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read().replace(str(text.split()[1])+'\n', ''))
							except BaseException:
								pass
							try:
								open('data/'+LastDate+'peoples.txt','w',encoding='utf-8').write(open('data/'+LastDate+'peoples.txt',encoding='utf-8').read().replace(str(id)+'\n', ''))
							except BaseException:
								pass
						for i in allId.split():
							postsForLikes = ''
							try:
								postsForLikes = open('data/'+i+'postsForLikes.txt', encoding='utf-8').read()
							except BaseException:
								pass
							open('data/'+i+'postsForLikes.txt', 'w',encoding='utf-8').write(postsForLikes.replace(text.split()[1]+'\n', ''))
						PostDelete(text.split()[1], id)
						send_message(id, "✅Пост удалён!")
					except BaseException:
						send_message(id, '⛔Ошибка')
						print(traceback.format_exc())

				else:
					send_message(id, '⛔ Это не твой пост или ты скинул этот пост позже 2-х дней назад')


			if text == 'Закрытые ком-ии':
				try:
					open(r'data/CommClosed.txt', 'a', encoding='utf-8').write(str(id)+'\n')
				except BaseException:
					open(r'data/CommClosed.txt', 'w', encoding='utf-8').write(str(id)+'\n')
				keyboard = VkKeyboard()
				keyboard.add_callback_button('Назад', VkKeyboardColor.NEGATIVE, payload=4)
				send_message(id, 'Отправь ссылку на запись с закрытыми комментариями', keyboard)


			if text == 'Перезапустить':
				keyboard = VkKeyboard(inline=True)
				keyboard.add_button('Прокомментировал')
				keyboard.add_button('Перезапустить')
				send_message(id, '🕑 Сейчас постараюсь скинуть другие посты...')
				wallsComm = GetWallsComm(id)
				msg = ''
				for i in wallsComm:
					msg += i+'\n'
				open(r'data/'+str(id)+'WallsForComm.txt', 'w',encoding='utf-8').write(msg)

				ms = ''
				n=0
				for cc in msg.split():
					n+=1
					vPsts = ''
					try:
						vPsts = open('data/vipPosts.txt',encoding='utf-8').read()
					except BaseException:
						pass
					if cc in vPsts:
						ms += '💎 '+cc+'\n'
					else:	
						ms += str(n)+'. '+cc+'\n'

				send_message(id, '⛔ Вот другие посты:\n\n'+ms+'\n\n@id730993538(*Обратись в поддержку), если у тебя есть проблемы с постами или нажми на кнопку "Перезапустить" для того, чтобы бот прислал тебе другие посты', keyboard)				


			if text == 'Жалоба':
				send_message(id, '&#128483; Для отправки жалобы напиши следующее:\nжалоба ССЫЛКА_НА_ПОСТ ПРИЧИНА\n\n*Отправка жалобы на пост без причины карается блокировкой')


			if 'жалоба ' in text.lower() and len(text.split()) >= 2:
				try:
					post = text.split()[1]
					ForOwnANdItem = post.replace("https://vk.com/wall", "").split("_")

					owner_id = None
					item_id = None
					try:
						owner_id = ForOwnANdItem[0]
						item_id = ForOwnANdItem[1]
					except BaseException:
						send_message(id, '⛔ Не правильная ссылка!')
						return
					msg = text.replace('жалоба ', '').replace(post, '')
					rprts = ''
					dltPosts = ''
					try:
						dltPosts = open('data/dltPosts.txt', encoding='utf-8').read()
					except BaseException:
						pass
					if post in dltPosts:
						send_message(id, 'Пост уже удалён')
					else:
						try:
							rprts = open('data/reports'+owner_id+'_'+item_id+'.txt', encoding='utf-8').read()
						except BaseException as e:
							pass
						if str(id) not in rprts:
							open('data/reports'+owner_id+'_'+item_id+'.txt', 'a',encoding='utf-8').write(str(id)+'\n')
							rprts += str(id)+'\n'
							send_messageCHAT(3, '&#128483; Жалоба от @id'+str(id)+' на пост '+ post+' с причиной: '+msg+'. Кол-во жалоб на данный момент: '+str(len(rprts.split())) + '\n\nЧтобы удалить пост без ожидания 6 жалоб, нажми на кнопку "🚫Удалить"')
							if len(rprts.split()) >= 6:
								PostDelete(post)
								send_messageCHAT(3, '&#10060; Пост удалён из-за жалоб: '+post)

							send_message(id, '✅ Жалоба отправлена!')
						else:
							send_message(id, '⛔ Ты уже отправлял жалобу на этот пост!')
				except BaseException as e:
					send_message(id, '⛔Ошибка: '+str(e))

			if text == 'Подписался':
				pst = open(r'data/'+str(id)+'postSubs.txt', encoding='utf-8').read()

			# - - - - Клиенты, не поддерживающие Callback кнопки - - - -

			if text == '👤Профиль':
				keyboard = VkKeyboard(inline=True)
				keyboard.add_button('Удалить пост')
				psts = ''
				try:
					psts += open('data/Post_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read() + '\n'
				except BaseException:
					pass 
				try:
					psts += open('data/Post_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read()
				except BaseException:
					pass

				pstsCom = ''
				try:
					pstsCom += open('data/PostCom_From'+str(id)+'_'+TodaysDate+'.txt', encoding='utf-8').read() + '\n'
				except BaseException:
					pass 
				try:
					pstsCom += open('data/PostCom_From'+str(id)+'_'+LastDate+'.txt', encoding='utf-8').read()
				except BaseException:
					pass

				vipStat = 'Отсутствует'

				if str(id) in vipUs:
					vipStat = 'до '+open('data/vip'+str(id)+'.txt', encoding='utf-8').read()

				send_message(id, name+'твой профиль:\n\n🔤 Спец. Айди: '+str(id)+'\n💎VIP-статус: '+vipStat+'\n👥Пользователей MutSupp: '+str(len(allId.split()))+'\n\n📝Твои посты за 2 дня:\n\nДля лайков❤:\n'+psts+'\n\nДля комментариев💬:\n'+pstsCom, keyboard)


			if text == '💸Цены':
				keyboard = VkKeyboard(inline=True)
				keyboard.add_openlink_button('Купить что-то', 'https://vk.com/id730993538')
				vk.messages.send(user_id=id, message='💸Цены услуг:\n\n• Подписки на группу (на твою группу будут подписываться все пользователи MutSupp) - 39р/день\n• Доп. пост (ты можешь скинуть ещё один пост) - 19р/пост\n• VIP-статус (привелегии - https://vk.com/topic-213443881_49983313) - 99р/мес\n\n@id730993538(*Если кнопка не работает*)', random_id=0, keyboard=keyboard.get_keyboard())  


			if text == 'Назад':
				open('AL/regAutoLike.txt', 'w', encoding='utf-8').write(regAutoLike.replace(str(id)+'\n', ''))
				open(r'data/waitLikeOrComm.txt','w',encoding='utf-8').write(waitLikeOrComm.replace(str(id)+'\n',''))
				CommOnUsts = ''
				try:
					CommOnUsts=open(r'data/CommOnUsts.txt',encoding='utf-8').read()
				except BaseException:
					pass
				open('data/CommOnUsts.txt','w',encoding='utf-8').write(CommOnUsts.replace(str(id)+'\n', ''))
				ZapDeleteId = ''
				try:
					ZapDeleteId = open(r'data/ZapDeleteId.txt', encoding='utf-8').read()
				except BaseException:
					print(traceback.format_exc())
				CommClosed = ''
				try:
					CommClosed = open(r'data/CommClosed.txt', encoding='utf-8').read()
				except BaseException:
					print(traceback.format_exc())
				open(r'data/ZapDeleteId.txt', 'w', encoding='utf-8').write(ZapDeleteId.replace(str(id)+'\n', ''))
				open(r'data/CommClosed.txt', 'w', encoding='utf-8').write(CommClosed.replace(str(id)+'\n', ''))
				msstart(id, 'Ок')


			if text == 'Запись удалена':
				try:
					open(r'data/ZapDeleteId.txt', 'a', encoding='utf-8').write(str(id)+'\n')
				except BaseException:
					print(traceback.format_exc())
					open(r'data/ZapDeleteId.txt', 'w', encoding='utf-8').write(str(id)+'\n')
				keyboard = VkKeyboard()
				keyboard.add_callback_button('Назад', VkKeyboardColor.NEGATIVE, payload=4)
				send_message(id, 'Отправь ссылку на удалённую запись', keyboard)


def DeleteDontActiveUsrs111():
	uss = []
	dts = []
	for i in range(1,25):
		dts.append( ((datetime.now()) - timedelta(days=i)).strftime('%d.%m.%y') )
	dts.append( (datetime.now()).strftime('%d.%m.%y') )
	for d in dts:
		ppls = ''
		try:
			ppls = open('data/'+d+'peoples.txt',encoding='utf-8').read()
		except BaseException:
			pass
		for i in ppls.split():
			uss.append(i)
		ppls1 = ''
		try:
			ppls1 = open('data/'+d+'UsersForComm.txt',encoding='utf-8').read()
		except BaseException:
			pass
		for i in ppls1.split():
			uss.append(i)
	allId = ''
	try:
		allId = open('data/AllId.txt', encoding='utf-8').read()
	except BaseException:
		pass
	for i in allId.split():
		allId1 = ''
		try:
			allId1 = open('data/AllId.txt', encoding='utf-8').read()
		except BaseException:
			pass
		if i not in uss:
			try:
				send_message(i, '⛔ Я удаляю тебя из базы, так как ты долгое время не отправлял посты')
			except BaseException:
				pass
			open('data/AllId.txt', 'w',encoding='utf-8').write(allId1.replace(i+'\n', ''))


def PostHandler(text):
    text = text.replace('.ru', '.com').replace('.me', '.com').replace('https://m.vk.com/', 'https://vk.com/').replace('https://m.vk.ru/', 'https://vk.com/').replace('https://m.vk.me/', 'https://vk.com/')
    frgm = ['?w=', '?hash=', '?access_key']
    for i in frgm:
        text = text.split(i)[0]
    return text


def SendingDontLikedAndCommPosts():
	TodaysDate = (datetime.now()).strftime('%d.%m.%y')
	LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
	vipUs = ''
	try:
		vipUs = open('data/vip.txt', encoding='utf-8').read().split()
	except BaseException:
		pass

	for idw in vipUs:
		try:

			walls = ''
			try: 
				walls += open(r'data/'+TodaysDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
			except BaseException:
				pass
			try:
				walls += open(r'data/'+LastDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
			except BaseException:
				pass

			l = walls.split()

			
			checkLiked = CheckLikes(int(idw), l, random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6]))

			if checkLiked == True: # Если человек пролайкал все записи
				send_message(idw, "💾 У тебя пролайканы все посты! :)")

			else: # Человек не пролйкал записи
				keyboard = VkKeyboard(inline=True)
				keyboard.add_callback_button('Запись удалена', VkKeyboardColor.SECONDARY, payload=3)
				keyboard.add_button('Жалоба')

				walls = ''
				n=0
				for w in checkLiked:
					n += 1
					vPsts = ''
					try:
						vPsts = open('data/vipPosts.txt',encoding='utf-8').read()
					except BaseException:
						pass
					if w in vPsts:
						walls += '💎' + ' ' + w + '\n'
					else:
						walls += str(n) + '. ' + w + '\n'


				send_message(idw, "💾 Вот твои не пролайканные посты:\n\n"+walls, keyboard)

		except BaseException as e: 
			print(e)


def AutoLike(post):
	tkns = ''
	try:
		tkns = open(r'AL/tokens.txt', encoding='utf-8').read()
	except BaseException:
		pass
	tkns1 = tkns.split()
	for tkn in tkns1:
		err = False
		v = None
		try:
			v = vk_api.VkApi(token=tkn).get_api()		
			VkLongPoll(vk_api.VkApi(token=tkn))	
		except BaseException:

			id = open('AL/'+tkn+'.txt', encoding='utf-8').read()
			err = True
			os.remove('AL/'+str(id)+'tkn.txt')
			os.remove('AL/'+tkn+'.txt')
			tkns = ''
			try:
				tkns = open(r'AL/tokens.txt', encoding='utf-8').read()
			except BaseException:
				pass
			open(r'AL/tokens.txt', 'w', encoding='utf-8').write(tkns.replace(tkn+'\n', ''))
			open(r'AL/UserInAutoLike.txt', 'w', encoding='utf-8').write(UserInAutoLike.replace(str(id)+'\n', ''))
			send_message(id, '⛔ Я отключил тебя от АвтоЛайка. Причина: ошибка токена')
			
		if err == False:
			ForOwnANdItem = post.replace("https://vk.com/wall", "").split("_")
			owner_id = ForOwnANdItem[0]
			item_id = ForOwnANdItem[1]
			time.sleep(random.randint(3,12))
			v.likes.add(type='post', owner_id=owner_id, item_id=item_id)


def CheckComments(id, posts, vkCheck):
	vk = vkCheck
	chunks = [posts[i:i+8] for i in range(0, len(posts), 8)] # Создание чанков по 8 постов в каждом
	psts = {}
	cmUsers = {}

	for c in chunks:
		script = '''var comments = [];'''
		
		n=0
		for i in c:
			n+=1
			psts[n] = i
			ForOwnANdItem = i.replace("https://vk.com/wall", "").split("_") 
			owner_id = ForOwnANdItem[0]
			post_id = ForOwnANdItem[1]

			# Шаблон скрипта для получения комментариев
			script += '''
				var post_id = %s;
				var max_count = 100;
				var offset = %s;
				 var owner = %s;
				comments = comments + {"https://vk.com/wall%s_%s": "https://vk.com/wall%s_%s"};
				var count = API.wall.getComments({"owner_id": owner, "post_id": post_id, "offset": offset, "count": max_count}).count;
				while(offset < count) {
					comments = comments + API.wall.getComments({"owner_id": owner, "post_id": post_id, "offset": offset, "count": max_count}).items;
					offset = offset + max_count;
					}
			   

			''' % (post_id, 0, owner_id, owner_id,post_id, owner_id,post_id)

		# Отправляем запрос на получение всех комментариев
		script += '''return comments;'''
		cm = vk.execute(code=script)
		n1 = 0
		
		post = None
		for m in cm:
			if 'https://vk.com/wall' in m:
				n1 += 1
				cmUsers[psts[n1]] = []
				post = psts[n1]
			else:
				cmUsers[psts[n1]].append(cm[m]['from_id'])




	# Печатаем все комментарии
	notLikedPsts = []
	for i in cmUsers:
		if id not in cmUsers[i]:
			notLikedPsts.append(i)
	if len(notLikedPsts) == 0:
		return True
	else:
		return notLikedPsts


def CheckLikes(id, posts, vkCheck):
	chunks = [posts[i:i+9] for i in range(0, len(posts), 9)]
	psts = {}
	LkUs = {}
	psts1 = []
	for c in chunks:
		code = '''var likes = [];'''
		n=0
		for p in c:
			if p not in psts1:
				n+=1
				psts[n] = p
				psts1.append(p)
				ForOwnANdItem = p.replace("https://vk.com/wall", "").split("_") 
				owner_id = ForOwnANdItem[0]
				post_id = ForOwnANdItem[1]
				code += '''
					var post_id = %s;
					var max_count = 1000;
					var offset = %s;
					var owner = %s;
					likes = likes + {"https://vk.com/wall%s_%s": "https://vk.com/wall%s_%s"};
					var count = API.likes.getList({"owner_id": owner, "item_id": post_id, "offset": offset, "count": max_count, "type": "post"}).count;
					while(offset < count) {
						likes = likes + API.likes.getList({"owner_id": owner, "item_id": post_id, "offset": offset, "count": max_count, "type": "post"}).items;
						offset = offset + max_count;
						}
				  
				''' % (post_id, 0, owner_id, owner_id,post_id, owner_id,post_id)
		code += '''return likes;'''
		result = vkCheck.execute(code=code)
		vkCheck1 = random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6])
		if vkCheck1 != vkCheck:
			vkCheck = vkCheck1

		n1 = 0
		post = None
		for i in result:
			if 'https://vk.com/wall' in str(result[i]):
				n1 += 1
				post = psts[n1]
				LkUs[post] = []
			else:
				LkUs[post].append(result[i])

	notLikedPsts = []
	for i in LkUs:
		if id not in LkUs[i]:
			notLikedPsts.append(i)
	if len(notLikedPsts) == 0:
		return True
	else:
		return notLikedPsts


def getUsersForMsg(usrs):
	RTRN = {}
	n1 = 1
	n = 1
	uss = []
	for i in usrs: 
		if len(uss) <= 99:
			uss.append(i)
			n+=1
		if len(uss) > 99 or n > len(usrs):
			msg = ''
			for c in uss:
				if len(msg) == 0:
					msg += c
				else:
					msg += ', ' + c
			RTRN[n1] = msg 
			n1 += 1
			uss = []
	return RTRN


def SendAllUsMsg(usrs, message, keyboard=None):
	code = None
	for i in usrs:
		try:
			if keyboard == None:
				req = vk.messages.send(user_ids=usrs[i], message=message, random_id=0)
				try:
					for c in req:
						if c['error']['code'] == 901:
							idb = str(c['peer_id'])
							print('Заблокал!!!!1 - ' + str(c['peer_id']))

							allUs = ''
							try:
								allUs = open('data/AllId.txt', encoding='utf-8').read()
							except BaseException:
								pass

							open('data/AllId.txt', 'w', encoding='utf-8').write(allUs.replace(str(idb)+'\n', ''))

							InvitedUsrsID = ''
							try:
								InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
							except BaseException:
								pass
							if str(idb) in InvitedUsrsID:
								open('MSW/IvitedUsrs.txt', 'w', encoding='utf-8').write(InvitedUsrsID.replace(str(idb)+'\n', ''))
								a = vkG.messages.getChatUsers(chat_id=36)
								for userid in a:
									inv = ''
									try:
										inv = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read()
									except BaseException:
										pass

									if str(idb) in inv:
										open('MSW/'+str(userid)+'IvitedUsrs.txt', 'w', encoding='utf-8').write(inv.replace(str(idb)+'\n', ''))
										spUs = ''
										try:
											spUs = open('MSW/SendPostsUsrs.txt', encoding='utf-8').read()
										except BaseException:
											pass
										open('MSW/SendPostsUsrs.txt', 'w', encoding='utf-8').write(spUs.replace(str(idb)+'\n',''))
										send_messageCHAT(6, '🚫 @id' + userid + 'я удалил его из базы, так как он заблокировал MutSupp - @id'+str(idb))

				except BaseException:
					pass


			else:
				req = vk.messages.send(user_ids=usrs[i], message=message, random_id=0, keyboard=keyboard.get_keyboard())
				try:
					for c in req:
						if c['error']['code'] == 901:
							idb = str(c['peer_id'])
							print('Заблокал!!!!1 - ' + str(c['peer_id']))

							allUs = ''
							try:
								allUs = open('data/AllId.txt', encoding='utf-8').read()
							except BaseException:
								pass

							open('data/AllId.txt', 'w', encoding='utf-8').write(allUs.replace(str(idb)+'\n', ''))

							InvitedUsrsID = ''
							try:
								InvitedUsrsID = open('MSW/IvitedUsrs.txt', encoding='utf-8').read()
							except BaseException:
								pass
							if str(idb) in InvitedUsrsID:
								open('MSW/IvitedUsrs.txt', 'w', encoding='utf-8').write(InvitedUsrsID.replace(str(idb)+'\n', ''))
								a = vkG.messages.getChatUsers(chat_id=36)
								for userid in a:
									inv = ''
									try:
										inv = open('MSW/'+str(userid)+'IvitedUsrs.txt', encoding='utf-8').read()
									except BaseException:
										pass

									if str(idb) in inv:
										open('MSW/'+str(userid)+'IvitedUsrs.txt', 'w', encoding='utf-8').write(inv.replace(str(idb)+'\n', ''))
										spUs = ''
										try:
											spUs = open('MSW/SendPostsUsrs.txt', encoding='utf-8').read()
										except BaseException:
											pass
										open('MSW/SendPostsUsrs.txt', 'w', encoding='utf-8').write(spUs.replace(str(idb)+'\n',''))
										user_get = vk.users.get(user_ids = (userid))
										user_get = user_get[0]
										first_name = user_get['first_name']
										last_name = user_get['last_name']
										full_name = first_name + " " + last_name
										name = "@id" + str(userid) + "(" + full_name + ")" + ", "
										send_messageCHAT(6, '🚫 ' + name + 'я удалил его из базы, так как он заблокировал MutSupp - @id'+str(idb))
				except BaseException:
					pass


		except BaseException:
			print(traceback.format_exc())


def PostDelete(post, id=None): # Удаляет пост (если id ничему не равен, то пост удаляется у всех)

	if id == None: # All
		open('data/dltPosts.txt', 'a', encoding='utf-8').write(post+'\n')
		dates = []
		now = datetime.now()
		for i in range(15):
			i+=1
			dates.append((now - timedelta(days=i)).strftime('%d.%m.%y'))
		dates.append(now.strftime('%d.%m.%y'))
		for dt in dates:

			try:
				usrs = open('data/AllId.txt', encoding='utf-8').read().split()
				for o in usrs:
					psts = ''
					try:
						psts = open('data/'+str(o)+'WallsForComm.txt', encoding='utf-8').read()
					except BaseException:
						pass
					open('data/'+str(o)+'WallsForComm.txt','w', encoding='utf-8').write(psts.replace(post+'\n','')) 
			except BaseException:
				pass

			psts = ''
			try:
				psts = open('data/'+dt+'wall.txt', encoding='utf-8').read()
			except BaseException:
				pass
			pstsC = ''
			try:
				pstsC = open('data/'+dt+'WallForComm.txt', encoding='utf-8').read()
			except BaseException:
				pass
			if post in pstsC:
				open('data/'+dt+'WallForComm.txt','w', encoding='utf-8').write(pstsC.replace(post+'\n',''))

				
			if post in psts:
				open('data/'+dt+'wall.txt','w', encoding='utf-8').write(psts.replace(post+'\n',''))

					
	else: # Not All
		dates = []
		now = datetime.now()
		for i in range(2):
			i+=1
			dates.append((now - timedelta(days=i)).strftime('%d.%m.%y'))
		dates.append(now.strftime('%d.%m.%y'))
		for dt in dates:

			try:
				usrs = open('data/AllId.txt', encoding='utf-8').read().split()
				for o in usrs:
					psts = ''
					try:
						psts = open('data/'+str(o)+'WallsForComm.txt', encoding='utf-8').read()
					except BaseException:
						pass
					open('data/'+str(o)+'WallsForComm.txt','w', encoding='utf-8').write(psts.replace(post+'\n','')) 
			except BaseException:
				pass

			psts = ''
			try:
				psts = open('data/'+dt+'wall.txt', encoding='utf-8').read()
			except BaseException:
				pass
			pstsC = ''
			try:
				pstsC = open('data/'+dt+'WallForComm.txt', encoding='utf-8').read()
			except BaseException:
				pass
			if post in pstsC:
				open('data/'+dt+'WallForComm.txt','w', encoding='utf-8').write(pstsC.replace(post+'\n',''))

				
			if post in psts:
				open('data/'+dt+'wall.txt','w', encoding='utf-8').write(psts.replace(post+'\n',''))


def SmsSend(AllIdInList, text):
	SendAllUsMsg(getUsersForMsg(AllIdInList), '💬 Новое сообщение: '+text)


def SendPostsAllUs(id,i, text, likeOrComm): # Отправляет сообщение всем пользователям 
	AllId = ''
	try:
		AllId+=open('data/AllId.txt', encoding='utf-8').read()
	except BaseException as e:
		print(e)

	AllIdInList = AllId.replace(str(id),'').split()
	AllIdInList1 = []
	try:

		for c in AllIdInList:
			if c not in AllIdInList1:
				AllIdInList1.append(c)

		keyboard = VkKeyboard(inline=True)
		keyboard.add_callback_button('Запись удалена', VkKeyboardColor.SECONDARY, payload=3)

		SendingPostsLike = ''
		try:
			SendingPostsLike = open('data/SendingPostsLike.txt', encoding='utf-8').read()
		except BaseException:
			pass
		SendingPostsComm = ''
		try:
			SendingPostsComm = open('data/SendingPostsComm.txt', encoding='utf-8').read()
		except BaseException:
			pass

		if likeOrComm == 0 and str(i) not in SendingPostsLike: #Лайки
			keyboard.add_button('Жалоба')
			SendAllUsMsg(getUsersForMsg(AllIdInList1), text, keyboard)

		if likeOrComm == 1 and str(i) not in SendingPostsComm: #Комментарии
			keyboard.add_button('Закрытые ком-ии')
			keyboard.add_line()
			keyboard.add_button('Жалоба')
			SendAllUsMsg(getUsersForMsg(AllIdInList1), text, keyboard)

	except BaseException:
		print(traceback.format_exc())


def CheckComment(id, wall): # Проверяет комментарии человека
	elements = wall.replace('https://vk.com/wall','').split('_')
	own = elements[0]
	itm = elements[1]
	n=0
	offset = 0
	usComm = False
	CommCount=None
	RTRN = False
	try:
		CommCount = random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6]).wall.getComments(owner_id=own, post_id=itm)['count']
	except BaseException:
		return True
	count100 = math.ceil(CommCount/100)
	offset = 0
	for i in range(count100):
		i += 1
		try:
			get = random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6]).wall.getComments(owner_id=own, post_id=itm, offset=offset, count=100, sort='desc')
			if len(get['items']) == 0:
				break
			for j in get['items']:
				n+=1
				if j['from_id'] == id:
					RTRN = True
					return RTRN
		except BaseException as e:
			print(e)
		offset += 100
	return RTRN


def CommentCheckProcess(id, walls, Todaysdate): # Записывает пост человека для комментов 
	b = CheckComments(id, walls, random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6]))
	threadForCommUs.remove(id)
	if b == True:
		open(r'data/'+str(id)+'WallsForComm.txt', 'w',encoding='utf-8').write('None')
		WallForComm = ''
		try:
			WallForComm = open(r'data/'+Todaysdate+'WallForComm.txt',encoding='utf-8').read()
		except BaseException:
			pass
		text = open('data/'+str(id)+'post.txt',encoding='utf-8').read()
		if text not in WallForComm:


			open(r'data/'+Todaysdate+'WallForComm.txt','a',encoding='utf-8').write(text+'\n')
			open(r'data/'+Todaysdate+'UsersForComm.txt','a',encoding='utf-8').write(str(id)+'\n')
			ForOwnANdItem = text.replace("https://vk.com/wall", "").split("_")
			owner_id = ForOwnANdItem[0]
			item_id = ForOwnANdItem[1]
			open('data/PostCom_From'+str(id)+'_'+Todaysdate+'.txt', 'w', encoding='utf-8').write(str('https://vk.com/wall'+owner_id+'_'+item_id))
			open('data/Post_From'+str(id)+'_'+Todaysdate+'.txt', 'w', encoding='utf-8').write(str('https://vk.com/wall'+owner_id+'_'+item_id))
			open('data/wall'+owner_id+'_'+item_id+'COMM.txt', 'w', encoding='utf-8').write(str(id))
			addPosts = 0
			try:
				addPosts = int(open('data/addPost'+str(id)+'.txt', encoding='utf-8').read().split()[0])
			except BaseException:
				pass
			if addPosts > 0:
				open('data/addPost'+str(id)+'.txt', 'w', encoding='utf-8').write(str(addPosts - 1))
			
			msstart(id, '✅Твоя запись успешно подключена к системе комментариев!')
			open('MSW/SendPostsUsrs.txt', 'a', encoding='utf-8').write(str(id)+'\n')

			vipUs = ''
			try:
				vipUs = open('data/vip.txt', encoding='utf-8').read()
			except BaseException:
				pass

			if str(id) not in vipUs:
				threading.Thread(target=SendPostsAllUs, args=(id,text,'💬 Запрос комментария на пост!\n'+text, 1,  )).start()
				
			else:
				open('data/vipPosts.txt', 'a', encoding='utf-8').write(text+'\n')
				threading.Thread(target=SendPostsAllUs, args=(id,text,'💎💬 Запрос комментария на пост!\n'+text, 1,  )).start()

		if text in WallForComm:
			msstart(id, '⛔Эта запись уже подключена к системе комментариев!') # Пост для комментариев
	else:

		keyboard = VkKeyboard(inline=True)
		keyboard.add_button('Прокомментировал')
		keyboard.add_button('Перезапустить')
		keyboard.add_line()
		keyboard.add_button('Жалоба')
		ms = ''
		n=0
		for cc in b:
			n+=1
			vPsts = ''
			try:
				vPsts = open('data/vipPosts.txt',encoding='utf-8').read()
			except BaseException:
				pass
			if cc in vPsts:
				ms += '💎 '+cc+'\n'
			else:	
				ms += str(n)+'. '+cc+'\n'
		send_message(id, '⛔Ты не оставил комментарий на этих постах:\n\n'+ms+'\n\n@id730993538(*Обратись в поддержку), если у тебя есть проблемы с постами или нажми на кнопку "Перезапустить" для того, чтобы бот прислал тебе другие посты', keyboard)


def TimerBot():
	try:
		while True:
			time1 = (datetime.now()).strftime('%H:%M:%S')
			Date = (datetime.now()).strftime('%d.%m.%y')


			if time1 == '00:00:00':
				
				# проверка VIP-ок
				try:
					vipUs = ''
					try:
						vipUs = open('data/vip.txt', encoding='utf-8').read()
					except BaseException:
						pass
					vipUs1 = vipUs.split()
					for i in vipUs1:
						dt = open('data/vip'+str(i)+'.txt', encoding='utf-8').read()
						if Date in dt:
							open('data/vip.txt', 'w', encoding='utf-8').write(vipUs.replace(str(us)+'\n',''))
							os.remove('data/vip'+str(i)+'.txt')
							send_messageCHAT(3, '@id'+str(i)+' - снял с него VIP статус')
							try:
								send_message(i, '💎 Срок действия VIP-статуса закончен!')
							except BaseException:
								pass
				except BaseException as e:
					send_messageCHAT(3, 'Ошибка в проверке випок: '+str(e))

				# Очистка слотов
				slot1=''
				slot2=''
				slot3=''
				slot4=''
				slot5=''
				try:
					slot1 = open(r'data/slotTIme1.txt', encoding='utf-8').read()
					slot2 = open(r'data/slotTIme2.txt', encoding='utf-8').read()
					slot3 = open(r'data/slotTIme3.txt', encoding='utf-8').read()
					slot4 = open(r'data/slotTIme4.txt', encoding='utf-8').read()
					slot5 = open(r'data/slotTIme5.txt', encoding='utf-8').read()
				except BaseException:
					open(r'data/slotTIme1.txt','w', encoding='utf-8')
					open(r'data/slotTIme2.txt','w', encoding='utf-8')
					open(r'data/slotTIme3.txt','w', encoding='utf-8')
					open(r'data/slotTIme4.txt','w', encoding='utf-8')
					open(r'data/slotTIme5.txt','w', encoding='utf-8')
				if Date in slot1:
					open(r'data/slot1.txt', 'w',encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme1.txt','w', encoding='utf-8')
					vk.messages.send(chat_id=3, message='Слот номер 1 очищен', random_id=0)
				if Date in slot2:
					open(r'data/slot2.txt', 'w',encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme2.txt','w', encoding='utf-8')
					vk.messages.send(chat_id=3, message='Слот номер 2 очищен', random_id=0)
				if Date in slot3:
					open(r'data/slot3.txt', 'w',encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme3.txt','w', encoding='utf-8')
					vk.messages.send(chat_id=3, message='Слот номер 3 очищен', random_id=0)
				if Date in slot4:
					open(r'data/slot4.txt', 'w',encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme4.txt','w', encoding='utf-8')
					vk.messages.send(chat_id=3, message='Слот номер 4 очищен', random_id=0)
				if Date in slot5:
					open(r'data/slot5.txt', 'w',encoding='utf-8').write('mutsupp')
					open(r'data/slotTIme5.txt','w', encoding='utf-8')
					vk.messages.send(chat_id=3, message='Слот номер 5 очищен', random_id=0)

				SendingDontLikedAndCommPosts()

				# DeleteDontActiveUsrs()


			elif time1 == '12:00:00':
				SendingDontLikedAndCommPosts()


	except BaseException:
		print(traceback.format_exc())
		threading.Thread(target=TimerBot).start()


def GetWallsComm(id): # Получает записи для комментариев
	walls = ''
	try:
		walls += open(r'data/'+(datetime.now()).strftime('%d.%m.%y')+'WallForComm.txt',encoding='utf-8').read()
	except BaseException:
		pass
	try:
		walls += open(r'data/'+((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')+'WallForComm.txt',encoding='utf-8').read()
	except BaseException:
		pass
	walls = walls.split()
	for i in walls:
		n = walls.count(i)
		if n > 1:
			for c in range(n-1):
				walls.remove(i)
	n = 0
	if len(walls) < 15:
		n = len(walls)-1
		if n < 0:
			n = 0
	if len(walls) >= 15:
		n = 15
	wlcm = []
	n -= 1
	if n < 0:
		n+=1
	while len(wlcm)<n:
		wl = random.choice(walls)
		if wl not in wlcm:
			wlcm.append(wl)
	return wlcm


def GetPostsForLikes(id): # Получает записи для лайков
	huh = 'none'
	try:
		huh = open('data/'+str(id)+'postsForLikes.txt', encoding='utf-8').read()
	except BaseException:
		huh = 'none' 
	if 'none' not in huh:
		return huh.split()
	if '' not in huh:
		return huh.split()
	TodaysDate = (datetime.now()).strftime('%d.%m.%y')
	LastDate = ((datetime.now()) - timedelta(days=1)).strftime('%d.%m.%y')
	walls = ''
	try: 
		walls += open(r'data/'+TodaysDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
	except BaseException:
		pass
	try:
		walls += open(r'data/'+LastDate+'wall.txt', encoding="utf-8").read().replace(' ', '')
	except BaseException:
		pass

	l = walls.split()
	wls = []
	rtrn = []
	for i in l:
		if i not in wls:
			wls.append(i)
	open('data/'+str(id)+'postsForLikes.txt', 'w', encoding='utf-8').write('')
	if len(wls) < 51:
		for i in wls:
			open('data/'+str(id)+'postsForLikes.txt', 'a', encoding='utf-8').write(i+'\n')
		return wls 
	else:
		while len(rtrn) < 50:
			rtrn.append(random.choice(wls))
	for i in rtrn:
		open('data/'+str(id)+'postsForLikes.txt', 'a', encoding='utf-8').write(i+'\n')
	return rtrn


def WallWriting(idw,TodaysDate,LastDate, i): # Записывает пост человека
	global threadCount
	try:
		msstart(idw, "🔎Проверяю, лайкаешь ли ты записи...")

		l = GetPostsForLikes(idw)
		checkLiked = CheckLikes(idw, l, random.choice([vkSrv1,vkSrv2,vkSrv3,vkSrv4,vkSrv5,vkSrv6]))

		vipUs = ''
		try:
			vipUs = open('data/vip.txt', encoding='utf-8').read()
		except BaseException:
			pass

		if str(idw) not in vipUs:
			time.sleep(10)

		if checkLiked == True: # Если человек пролайкал все записи
			open('data/'+str(id)+'postsForLikes.txt', 'w', encoding='utf-8').write('none')
			ForOwnANdItem = i.replace("https://vk.com/wall", "").split("_")
			owner_id = ForOwnANdItem[0]
			item_id = ForOwnANdItem[1]

			# Запись поста в базу
			open('data/Post_From'+str(idw)+'_'+TodaysDate+'.txt', 'w', encoding='utf-8').write(str('https://vk.com/wall'+owner_id+'_'+item_id)) # Пост для отображения в профиле
			open('data/wall'+owner_id+'_'+item_id+'LIKE.txt', 'w', encoding='utf-8').write(str(idw)) # Файл для определения по посту того кто его скинул

			with open(f"data/{TodaysDate}wall.txt", "a", encoding="utf-8") as file:
				file.write(i + "\n")

			open('data/'+TodaysDate+'peoples.txt','a',encoding='utf-8').write(str(idw)+'\n') # Файл показывающий всех кто кинул сегодня пост
			open('MSW/SendPostsUsrs.txt', 'a', encoding='utf-8').write(str(idw)+'\n') # MS WORK сколько человек скинул постов

			# Дополнительный пост
			addPosts = 0
			try:
				addPosts = int(open('data/addPost'+str(idw)+'.txt', encoding='utf-8').read().split()[0])
			except BaseException:
				pass
			if addPosts > 0:
				open('data/addPost'+str(idw)+'.txt', 'w', encoding='utf-8').write(str(addPosts - 1))

			# Оповещение о том, что пост записан
			send_message(idw, "✅Твой пост " + i + " записан")
			

			# Оповещение о новом посте
			vipUs = ''
			try:
				vipUs = open('data/vip.txt', encoding='utf-8').read()
			except BaseException:
				pass
			if str(idw) not in vipUs:
				threading.Thread(target=SendPostsAllUs, args=(idw,i,'✏ Появился новый пост!\n'+i, 0, )).start()
			else:
				open('data/vipPosts.txt', 'a', encoding='utf-8').write(i+'\n')
				threading.Thread(target=SendPostsAllUs, args=(idw,i,'💎✏ Появился новый пост!\n'+i, 0, )).start()

			# АвтоЛайк
			threading.Thread(target=AutoLike, args=(i,)).start()

		else: # Человек не пролйкал записи
			keyboard = VkKeyboard(inline=True)
			keyboard.add_callback_button('Запись удалена', VkKeyboardColor.SECONDARY, payload=3)
			keyboard.add_button('Пролайкал', VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Жалоба')

			walls = ''
			n=0
			for w in checkLiked:
				n += 1
				vPsts = ''
				try:
					vPsts = open('data/vipPosts.txt',encoding='utf-8').read()
				except BaseException:
					pass
				if w in vPsts:
					walls += '💎' + ' ' + w + '\n'
				else:
					walls += str(n) + '. ' + w + '\n'


			send_message(idw, "💔Ты не пролайкал эти записи:\n\n"+walls, keyboard)
			open('data/'+str(idw)+'PostsNotLiked.txt', 'w', encoding='utf-8').write(walls)
	except BaseException as e: 
		print(e)

	threadCount-=1
	try:
		threadForId.remove(idw)
	except BaseException:
		vk.messages.send(chat_id=3, message='ошибка в потоке: '+traceback.format_exc())


def msstart(ids, text): # Отправляет основные кнопки
	keyboard = VkKeyboard()
	
	buttons = ['👤Профиль', '💸Цены']
	button_colors = [VkKeyboardColor.POSITIVE, VkKeyboardColor.NEGATIVE]

	n = 0
	for btn, btn_color in zip(buttons, button_colors):
		keyboard.add_callback_button(btn, color=btn_color, payload=n)
		n+=1
	keyboard.add_line()
	keyboard.add_openlink_button('📞Поддержка', 'https://vk.com/id730993538') 

	send_message(ids, text, keyboard)



def send_message(user_id, message, keyboard=None): # Отправляет сообщение в лс
	post = {
		"user_id": user_id,
		"message": message,
		"random_id": 0
		}

	if keyboard != None:
		post["keyboard"] = keyboard.get_keyboard()
	else:
		post=post

	session.method("messages.send", post)


def send_messageCHAT(user_id, message, keyboard=None): # Отправляет сообщение в беседу
	post = {
		"chat_id": user_id,
		"message": message,
		"random_id": 0
		}

	if keyboard != None:
		post["keyboard"] = keyboard.get_keyboard()
	else:
		post=post

	session.method("messages.send", post)


def CheckSubscOnGroup(id): # Проверяет, подписан ли на группы
	group_not_subsc = ""
	for n in range(3):
		try:
			n+=1
			group = open(r'data/slot'+str(n)+'.txt', encoding='utf-8').read().replace(' ','').replace('\n','')
			if group == '' or 'mutsupp' in group:
				subsc_gr = ''
			else:
				groupIsSubs = vk.groups.isMember(group_id=group, user_id=id)
				groupID = vk.groups.getById(group_id=group)[0]['screen_name']
				if groupIsSubs != 1:
					group_not_subsc += '@club'+group+'('+groupID+') \n'
		except BaseException as e:
			if ('No such file or directory:' in traceback.format_exc()):
				open(r'data/slot'+str(n)+'.txt', 'w',encoding='utf-8')
			else:
				print(traceback.format_exc())
				vk.messages.send(chat_id=3, message='@all Ошибка в группах!!!\n\n' + str(e), random_id=0)

	return group_not_subsc

def printvk(text,id=730993538): # print in vk
	vk.messages.send(chat_id=3, message=str(text),random_id=0)


if __name__ == '__main__':
	threading.Thread(target=main).start()
	threading.Thread(target=TimerBot).start()
