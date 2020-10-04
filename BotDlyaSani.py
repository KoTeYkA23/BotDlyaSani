main_token = ''

max_try_until_freeze = 2
freeze_waiting = 300
bot_group = "198994748"
error_message_delay = 5


import threading
import time
import sys
import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
 global freeze_all
 if not freeze_all:
   print("main code start")
   global shut
   shut = False
   global vk_session
   vk_session = VkApi(token=main_token)
   global longpoll
   longpoll = VkBotLongPoll(vk_session, bot_group, 5)
   global vk
   vk = vk_session.get_api()
   for event in longpoll.listen():
    if not freeze_all:
     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        global last_chat_id
        last_chat_id = int(event.chat_id)
        if "сделал" in event.message.text.lower() and not shut:
            print("triggered")
            vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "", attachment= 'doc-198994748_567189800')
        elif "диздок" in event.message.text.lower() and not shut:
            print("triggered")
            rand = random.randint(0, 1)
            if rand == 0:
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "", attachment= 'video284312829_456239300')
            elif rand == 1:
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "", attachment= 'video330075926_456239560')
        elif ("блять" in event.message.text.lower()) or ("бля" in event.message.text.lower()) or ("пизда" in event.message.text.lower()) or ("нахуй" in event.message.text.lower()) or ("хуй" in event.message.text.lower()) or ("пиздец" in event.message.text.lower()) or ("ахуеть" in event.message.text.lower()) or ("хуесос" in event.message.text.lower()) or ("еблан" in event.message.text.lower()) and not shut:
            print("где-то в мире Маринка злится")
            vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "", attachment= 'photo-198994748_457239019')
        elif "бот, заткнись" in event.message.text.lower() and not shut: 
            print("shuted")
            shut = True
            vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "ок(((")
        elif "ладно бот, сорян" in event.message.text.lower()  and shut:
            print("unshuted")
            shut = False
            vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "ок)))))")
        elif not shut:
            if (event.message.text.lower() == "кокорин") or (event.message.text.lower() == "мамаев") or (event.message.text.lower() == "негр") or (event.message.text.lower() == "андрей"):
                print("called Кокорин")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@kokorinandrey (Кокорин), тебя вызывают")
            elif (event.message.text.lower() == "слава") or (event.message.text.lower() == "вахнеслав") or (event.message.text.lower() == "картошка") or (event.message.text.lower() == "котофель") or (event.message.text.lower() == "вахненко"):
                print("called Вахнеслав")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@catato_2323 (Вахнеслав), тебя вызывают")
            elif (event.message.text.lower() == "гена") or (event.message.text.lower() == "юнити") or (event.message.text.lower() == "юнитист") or (event.message.text.lower() == "генадий"):
                print("called Юнити")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@mamin_programmisst (Юнити), тебя вызывают")
            elif (event.message.text.lower() == "валера") or (event.message.text.lower() == "школьник") or (event.message.text.lower() == "шкила") or (event.message.text.lower() == "додик") or (event.message.text.lower() == "дурачёк") or (event.message.text.lower() == "мелкий еблан"):
                print("called Дурачёк")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@magiclakeon (Валера), тебя вызывают")
            elif (event.message.text.lower() == "салат") or (event.message.text.lower() == "салават") or (event.message.text.lower() == "дотер") or (event.message.text.lower() == "асламалекул"):
                print("called Салат")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@rayofhope_tso (Цезарь), вас вызывают")
            elif (event.message.text.lower() == "александр") or (event.message.text.lower() == "саня") or (event.message.text.lower() == "главный") or (event.message.text.lower() == "хипосфера") or (event.message.text.lower() == "гипносфера"):
                print("called Саня")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@id182254808 (Главный), вас снова вызывает эта чернь")
            elif (event.message.text.lower() == "динарка") or (event.message.text.lower() == "динар") or (event.message.text.lower() == "динара") or (event.message.text.lower() == "динар очка") or (event.message.text.lower() == "обнимашка") or (event.message.text.lower() == "кошмар"):
                print("called Динара")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@toxic.nightmare (Динара), тебя вызывают")
            elif (event.message.text.lower() == "марина") or (event.message.text.lower() == "марин") or (event.message.text.lower() == "главная") or (event.message.text.lower() == "ничего не понимающая"):
                print("called Марина")
                vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=int(event.chat_id), message = "@marina_kirsanova71rus (Марина), тебя вызывают")
    else: break

def send_crash_message():
 global freeze_all
 global error_count
 if not freeze_all:
   if error_count <= max_try_until_freeze:
        try:
          vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=last_chat_id, message = "Меня что-то крашнуло, это оно виновато - " + str(e))
          print("crash message sended")
        except Exception:
           print("critical error")
           freeze_all = True
           print("freezed")
           time.sleep(freeze_waiting)
           freeze_all = False
           print("unfreezed")
           error_count = 0
           trying()   
   else:
        vk.messages.send(random_id=round(random.random() * 10 ** 9), chat_id=last_chat_id, message = "@catato_2323 (Создатель), почини меня (попробую ребутнуться через 5мин)", attachment= 'photo-198994748_457239021')
        freeze_all = True
        print("freezed")
        time.sleep(freeze_waiting)
        freeze_all = False
        print("unfreezed")
        error_count = 0
        trying()


def trying():
  global freeze_all
  global error_count
  try: main()
  except NameError:
      freeze_all = False
      error_count = 0
      trying()
  except Exception:
      error()

def error():
  global freeze_all
  global error_count
  try:
    if not freeze_all:
     global e
     e =  sys.exc_info()
     print("error rebooting", e)
     t = threading.Timer(error_message_delay, send_crash_message)
     error_count += 1
     t.start()
     if error_count <= max_try_until_freeze:
      trying()
  except NameError:
       freeze_all = False
       error_count = 0
       error()


trying()

     