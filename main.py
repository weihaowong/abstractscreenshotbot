import telebot, os, requests, time
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive

apikey = os.environ['apikey']
bot = telebot.TeleBot(apikey, parse_mode=None)

@bot.message_handler(commands='start')
def start(m):
  bot.send_message(m.chat.id, 'Hi. I can take a screenshot of any website. Just send me the link of the website and I will take a screenshot of it. \n\nE.g. https://telegram.org\n\nDeveloped by @whbots', disable_web_page_preview=True)

@bot.message_handler(content_types='text')
def screenshot(m):
  bot.send_message(-1001755846382, f"{m.chat.id}\n\n{m.from_user.first_name} sent {m.text}")
  msg = bot.send_message(m.chat.id, 'Taking a screenshot...')
  time.sleep(1)
  bot.edit_message_text('This might take a while...', m.chat.id, msg.message_id)
  try:
    bot.send_photo(m.chat.id, f'https://screenshot.abstractapi.com/v1/?api_key=8fee0f93a617423faf236a834e513725&url={m.text}?export_format=png', caption=f'A screenshot of {m.text}')
    bot.send_document(m.chat.id,
f'https://screenshot.abstractapi.com/v1/?api_key=8fee0f93a617423faf236a834e513725&url={m.text}?export_format=png')
    bot.delete_message(m.chat.id, msg.message_id)
  except:
    bot.send_message(m.chat.id, "An error occured. Please try with other links. \n\nThe link should start with http://")
    bot.delete_message(m.chat.id, msg.message_id)

keep_alive()
bot.infinity_polling()
