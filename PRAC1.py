import telepot

token ='1208283437:AAEysyY40C_RJ-49FSG-pgCbz9p0UxTMHjc'
bot = telepot.Bot(token)
print (bot.getMe())

def handle(msg):
  content_type = telepot.glance(msg)
  chat_type=telepot.glance(msg)
  chat_id=telepot.glance(msg)
  print(content_type, chat_type, chat_id)

  if content_type == 'text':
    bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
    
bot.message_loop(handle)
