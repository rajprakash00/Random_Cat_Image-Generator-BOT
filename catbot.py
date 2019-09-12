from telegram.ext import Updater, CommandHandler
import requests
import re


def get_url():
	data = requests.get('http://aws.random.cat/meow').json()
	url =data['file']
	return url

def start(update, context):
	context.message.reply_text('''Hello!!
     I'm a BOT and I will show you a very interesting thing...For that type /boc''')


def boc(bot,update):
	url= get_url()
	chat_id= update.message.chat.id
	bot.send_photo(chat_id=chat_id, photo=url)
	update.message.reply_text('''For more images you can type /boc multiple no. of times..!!
			

                 And yes! Send ur love to cats.. 
''')


def main():
	updater = Updater('your token')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('boc',boc))
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	main()
