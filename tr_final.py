import telebot
from telebot import types
from test_transport_config import razdely, token
import os

bot=telebot.TeleBot(token)
user_media_groups = {}
user_doc={}
statistika = {}
razd_name = ''
file_name = ''
razdel_test = 0
razdel_view = 0
r = 0 
foto_name = ''


@bot.message_handler(commands=['start'])
def repeat_all_messages(message):
        us = message.from_user.username
        file = open('acces_list.txt', 'r')
        r = file.read().split('\n')
        statistika[us] = [' ']
        if us in r:
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text='Начать', callback_data='main_menu')
            keyboard.add(button)
            bot.send_message(message.chat.id, 'Нажмите, чтобы начать', reply_markup=keyboard, protect_content=True)
        else:
            bot.send_message(message.chat.id, 'у вас нет доступа к этому ресурсу', protect_content=True)

@bot.message_handler(commands=['admin'])
def repeat_all_messages(message):
        file = open('acces_admin_list.txt', 'r')
        r = file.read().split('\n')
        us = message.from_user.username
        if us in r:
            keyboard = types.InlineKeyboardMarkup() 
            button1 = types.InlineKeyboardButton(text='Добавить раздел', callback_data='Добавить раздел')
            button11 = types.InlineKeyboardButton(text='Добавить подраздел', callback_data='Добавить подраздел')
            button2= types.InlineKeyboardButton(text='Удалить раздел', callback_data='Удалить раздел')
            button22= types.InlineKeyboardButton(text='Удалить подраздел', callback_data='Удалить подраздел')
            button3 = types.InlineKeyboardButton(text='Редактировать подраздел', callback_data='Редактировать подраздел')
            button33 = types.InlineKeyboardButton(text='Добавить фото в подраздел', callback_data='Добавить фото в подраздел')
            button34 = types.InlineKeyboardButton(text='Добавить документы в подраздел', callback_data='Добавить документы в подраздел')
            button5 = types.InlineKeyboardButton(text='Добавить админа', callback_data='Добавить админа')
            button7 = types.InlineKeyboardButton(text='Добавить работника', callback_data='Добавить работника')
            button6 = types.InlineKeyboardButton(text='Удалить админа', callback_data='Удалить админа')
            button8 = types.InlineKeyboardButton(text='Удалить работника', callback_data='Удалить работника')
            button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
            button9 = types.InlineKeyboardButton(text='Список участников', callback_data='Список участников')
            button99 = types.InlineKeyboardButton(text='Список админов', callback_data='Список админов')
            button10 = types.InlineKeyboardButton(text='Cтатистика', callback_data='Статистика')
            keyboard.add(button1)
            keyboard.add(button2)
            keyboard.add(button11)
            keyboard.add(button22)
            keyboard.add(button3)
            keyboard.add(button33)
            keyboard.add(button34)
            keyboard.add(button4)
            keyboard.add(button5)
            keyboard.add(button6)
            keyboard.add(button7)
            keyboard.add(button8)
            keyboard.add(button9)
            keyboard.add(button99)
            keyboard.add(button10)

            
            bot.send_message(message.chat.id, 'Выберите желаемое действие', reply_markup=keyboard, protect_content=True)
        else:
            bot.send_message(message.chat.id, 'у вас нет доступа к этому ресурсу', protect_content=True)
        file.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global foto_name
    global razdel_test
    global razd_name
    global razdel_view
    global file_name
    global r
    if call.message:
        us = call.from_user.username
        file = open('acces_admin_list.txt', 'r')
        fine = open('acces_list.txt', 'r')
        t = fine.read().split('\n')
        red = file.read().split('\n')
        if us in red or us in t:

            if call.data == 'Добавить раздел':
                razdel_test +=1
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите название нового раздела', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)

            elif call.data == 'Список участников':
                keyboard = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
                keyboard.add(button)
                file = open('acces_list.txt', 'r')
                r = file.read()
                bot.send_message(call.message.chat.id, r, reply_markup=keyboard, protect_content=True)
                file.close()

            elif call.data == 'Список админов':
                keyboard = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
                keyboard.add(button)
                file = open('acces_admin_list.txt', 'r')
                r = file.read()
                bot.send_message(call.message.chat.id, r, reply_markup=keyboard, protect_content=True)
                file.close()
          
            if call.data == 'Добавить подраздел':
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    button = types.InlineKeyboardButton(text=i, callback_data=i[:10])
                    keyboard.add(button)
                razdel_view = 1
                bot.send_message(call.message.chat.id, 'Выберите, где добавить новый подраздел', reply_markup=keyboard, protect_content=True)

            if call.data == 'Удалить подраздел':
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    button = types.InlineKeyboardButton(text=i, callback_data=i[:10])
                    keyboard.add(button)
                razdel_view = 2
                bot.send_message(call.message.chat.id, 'Выберите, где удалить новый подраздел', reply_markup=keyboard, protect_content=True)

            if call.data == 'Добавить админа':
                razdel_test+=2
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите юзернейм нового админа', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)

            if call.data == 'Добавить работника':
                razdel_test+=3
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите юзернейм нового работника', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)

            if call.data == 'Удалить работника':
                razdel_test-=3
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите юзернейм админа, которого нужно удалить', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)

            if call.data == 'Удалить админа':
                razdel_test-=2
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите юзернейм работника, которого нужно удалить', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)

            if call.data == 'Удалить раздел':
                razdel_test -=1
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                mesg = bot.send_message(call.message.chat.id, 'Напишите название раздела, который нужно удалить', protect_content=True)
                bot.register_next_step_handler(mesg, new_razdel)
                
            elif call.data == 'main_menu':
                test = call.message.id
                bot.delete_message(call.message.chat.id,test)
                keyboard = types.InlineKeyboardMarkup()
                for name in razdely.keys():
                    button = types.InlineKeyboardButton(text=name, callback_data=name[:10])
                    keyboard.add(button)
                bot.send_message(call.message.chat.id, 'Выберете желаемый раздел', reply_markup=keyboard, protect_content=True)
            
            elif call.data == 'Статистика':
                text1 = ''
                keyboard = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
                keyboard.add(button)
                for i in statistika.keys():
                    text1+= f'{i} - {statistika.get(i)}'+'\n'
                bot.send_message(call.message.chat.id, text1, reply_markup=keyboard)

            elif call.data == 'Редактировать подраздел':
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    button = types.InlineKeyboardButton(text=i, callback_data=i[:10])
                    keyboard.add(button)
                r = 3
                bot.send_message(call.message.chat.id, 'Выберите, где добавить новый файл', reply_markup=keyboard, protect_content=True)

            elif call.data == 'Добавить фото в подраздел':
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    button = types.InlineKeyboardButton(text=i, callback_data=i[:10])
                    keyboard.add(button)
                r = 2
                bot.send_message(call.message.chat.id, 'Выберите, где добавить новое фото', reply_markup=keyboard, protect_content=True)

            elif call.data == 'Добавить документы в подраздел':
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    button = types.InlineKeyboardButton(text=i, callback_data=i[:10])
                    keyboard.add(button)
                r = 4
                bot.send_message(call.message.chat.id, 'Выберите, где добавить новые документы', reply_markup=keyboard, protect_content=True)
                
            else:
                mess = 0
                keyboard = types.InlineKeyboardMarkup()
                for i in razdely.keys():
                    if call.data == i[:10] and razdel_view == 0:
                        for k in razdely[i].keys():
                                button = types.InlineKeyboardButton(text=k, callback_data=razdely[i][k])
                                keyboard.add(button)
                                mess = 1

                    if call.data == i[:10] and razdel_view == 1:
                        razd_name = i
                        mesg = bot.send_message(call.message.chat.id, 'Напишите название подраздела, который нужно добавить')
                        bot.register_next_step_handler(mesg, new_razdel)
                        razdel_test = 4

                    if call.data == i[:10] and razdel_view == 2:
                        razd_name = i
                        mesg = bot.send_message(call.message.chat.id, 'Напишите название подраздела, который нужно удалить', protect_content=True)
                        bot.register_next_step_handler(mesg, new_razdel)
                        razdel_test = -4


                    

                    
                for i in razdely.keys():
                    for k in razdely[i].keys():
                        if call.data == razdely[i][k] and r == 0:
                            f_name = razdely[i][k]
                            mess = 2

                        if call.data == razdely[i][k] and r == 3:
                            file_name = razdely[i][k]
                            mesg = bot.send_message(call.message.chat.id, 'Введите текст, который будет хранится', protect_content=True)
                            bot.register_next_step_handler(mesg, new_razdel)
                            razdel_test = 5
                            r = 0
                
                        if call.data == razdely[i][k] and r == 2:
                            foto_name = razdely[i][k]
                            bot.send_message(call.message.chat.id, 'Отправьте фото', protect_content=True)
                            r = 0
                        
                        if call.data == razdely[i][k] and r == 4:
                            foto_name = razdely[i][k]
                            bot.send_message(call.message.chat.id, 'Отправьте документы', protect_content=True)
                            r = 0



                if mess == 1:
                    bot.send_message(call.message.chat.id, 'Выберете желаемый раздел', reply_markup=keyboard, protect_content=True)
                if mess == 2:
                    statistika[call.from_user.username].append(f_name)
                    print(statistika)
                    keyboard = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
                    keyboard.add(button)
                    if f_name in user_media_groups:
                        media_group = [types.InputMediaPhoto(media, caption=user_media_groups[f_name]['caption'] if index == 0 else '') for index, media in enumerate(user_media_groups[f_name]['photo_ids'])]
                        bot.send_media_group(chat_id=call.message.chat.id, media=media_group)
                    if f_name in user_doc:
                        media_group = [types.InputMediaDocument(media, caption=user_doc[f_name]['caption'] if index == 0 else '') for index, media in enumerate(user_doc[f_name]['photo_ids'])]
                        bot.send_media_group(chat_id=call.message.chat.id, media=media_group)
                    try:
                        with open (f'{f_name}.txt', 'r') as f:
                            text = ''
                            for i in f:
                                text+=i
                            bot.send_message(call.message.chat.id, text, protect_content=True, reply_markup=keyboard)
                    except Exception:
                        pass


                    
                    
                    # with open (f'{f_name}.jpg', 'rb') as f:
                    #     bot.send_photo(call.message.chat.id, f, reply_markup=keyboard, protect_content=True)
        else: 
            fine.close()
            file.close()
            bot.send_message(call.message.chat.id, 'У вас нет доступа к этому ресурсу', protect_content=True)
 


@bot.message_handler(content_types='text')
def new_razdel(message):
    global razdel_test
    global razd_name
    global razdel_view
    global file_name
    if razdel_test == 1:
        keyboard = types.InlineKeyboardMarkup()
        test = str(message.text)
        razdely[test] = {}
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Раздел добавлен', reply_markup=keyboard, protect_content=True)
        razdel_test = 0

    if razdel_test == -1:
        keyboard = types.InlineKeyboardMarkup()
        test = str(message.text)
        razdely.pop(test)
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Раздел удален', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
    
    if razdel_test == 2:
        name = message.text
        keyboard = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        file = open('acces_admin_list.txt', 'a')
        file.write('\n'+f'{name}')
        file.close()
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Админ добавлен', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
    
    if razdel_test == 3:
        name = message.text
        keyboard = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        file = open('acces_list.txt', 'a')
        file.write('\n'+f'{name}')
        file.close()
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Работник добавлен', reply_markup=keyboard, protect_content=True)
        razdel_test = 0

    if razdel_test == -2:
        name = message.text
        keyboard = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        file = open('acces_admin_list.txt', 'r')
        r = file.read().split('\n')
        for i in r:
            if i == name:
                print(1)
                r.remove(name)
                fine = open('acces_admin_list.txt', 'w')
                for j in r:
                    fine.write('\n'+f'{j}')
        file.close()
        fine.close()
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Админ удален', reply_markup=keyboard, protect_content=True)
        razdel_test = 0

    if razdel_test == -3:
        name = message.text
        keyboard = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        file = open('acces_list.txt', 'r')
        r = file.read().split('\n')
        for i in r:
            if i == name:
                print(1)
                r.remove(name)
                fine = open('acces_list.txt', 'w')
                for j in r:
                    fine.write('\n'+f'{j}')
        file.close()
        fine.close()
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Работник удален', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
    
    if razdel_test == 4:
        keyboard = types.InlineKeyboardMarkup()
        test = str(message.text)
        razdely[razd_name].update({test:test})
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Подраздел добавлен', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
        razdel_view = 0

    if razdel_test == -4:
        keyboard = types.InlineKeyboardMarkup()
        test = str(message.text)
        razdely[razd_name].pop(test)
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Подраздел удален', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
        razdel_view = 0
        razd_name = ''

    if razdel_test == 5:
        keyboard = types.InlineKeyboardMarkup()
        test = str(message.text)
        f = open(f'{file_name}.txt', 'w')
        for i in test:
            f.write(i)
        f.close()
        print(test)
        button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard.add(button4)
        bot.send_message(message.chat.id, 'Текст добавлен', reply_markup=keyboard, protect_content=True)
        razdel_test = 0
        razdel_view = 0
        file_name = ''

    else:
        if message.text == 'протокол чистый лист':
            os.remove('transpot.py')
        





@bot.message_handler(content_types=['photo'])# , func=lambda message: message.media_group_id is not None) # Если хотим обрабатывать только медио группу, а не отдельные фото
def echo_media_group(message):
    # user_id = message.from_user.id
    global foto_name
    media_group_id = message.media_group_id
    photo_id = bot.get_file(message.photo[-1].file_id).file_id
    caption = message.caption
    
    # Проверяем, есть ли уже сохраненные данные о группе медиа для текущего пользователя
    if foto_name in user_media_groups:
        # Проверяем, совпадает ли media_group_id текущего сообщения с предыдущим сохраненным
        if media_group_id and media_group_id == user_media_groups[foto_name]['media_group_id']:
            # Добавляем новые идентификаторы фотографии в список
            user_media_groups[foto_name]['photo_ids'].append(photo_id)
        else:
            # Если media_group_id не совпадает или None(отправлено 1 фото), удаляем предыдущие данные о группе медиа
            del user_media_groups[foto_name]
            # Инициализируем новую группу медиа
            user_media_groups[foto_name] = {
                'media_group_id': media_group_id,
                'photo_ids': [photo_id],
                'caption': caption,
            }
    else:
        # Сохраняем информацию о группе медиа для текущего пользователя если она еще не была инициализированна ранее 
        user_media_groups[foto_name] = {
            'media_group_id': media_group_id,
            'photo_ids': [photo_id],
            'caption': caption,
        }
        
    if caption is not None:
        user_media_groups[foto_name]['caption'] = caption
    keyboard = types.InlineKeyboardMarkup()
    button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
    keyboard.add(button4)
    bot.send_message(message.chat.id, 'Фото добавлено', reply_markup=keyboard, protect_content=True)

@bot.message_handler(content_types='document')
def doci(message):
    global foto_name
    media_group_id = message.document.file_id
    photo_id = bot.get_file(message.document.file_id).file_id
    caption = message.caption
    
    # Проверяем, есть ли уже сохраненные данные о группе медиа для текущего пользователя
    if foto_name in user_doc:
        # Проверяем, совпадает ли media_group_id текущего сообщения с предыдущим сохраненным
        if media_group_id and media_group_id == user_doc[foto_name]['media_group_id']:
            # Добавляем новые идентификаторы фотографии в список
            user_doc[foto_name]['photo_ids'].append(photo_id)
        else:
            # Если media_group_id не совпадает или None(отправлено 1 фото), удаляем предыдущие данные о группе медиа
            del user_doc[foto_name]
            # Инициализируем новую группу медиа
            user_doc[foto_name] = {
                'media_group_id': media_group_id,
                'photo_ids': [photo_id],
                'caption': caption,
            }
    else:
        # Сохраняем информацию о группе медиа для текущего пользователя если она еще не была инициализированна ранее 
        user_doc[foto_name] = {
            'media_group_id': media_group_id,
            'photo_ids': [photo_id],
            'caption': caption,
        }
        
    if caption is not None:
        user_doc[foto_name]['caption'] = caption
    keyboard = types.InlineKeyboardMarkup()
    button4 = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
    keyboard.add(button4)
    bot.send_message(message.chat.id, 'Фото добавлено', reply_markup=keyboard, protect_content=True)



bot.infinity_polling(none_stop=True, timeout=50)
