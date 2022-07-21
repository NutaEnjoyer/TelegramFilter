from config import *

from pyrogram import Client, filters


app = Client('session', api_id, api_hash)

@app.on_message(filters.private)
async def message_handler(client, message):
	username = message.chat.username
	if message.from_user.username in username_exception:
		print('SWAP')
		return
	if username in usernames:
		if message.caption:
			txt = message.caption
		else:
			txt = message.text
		for word in strict_filter:
			if word == txt:
				print(f'DELETE STRICT --- {word}')
				print(txt)
				await message.delete()
		for word in lax_filter:
			if word in txt.lower():
				print(f'DELETE LAX --- {word}')
				print(txt)
				await message.delete()


if __name__ == '__main__':
	app.run()
