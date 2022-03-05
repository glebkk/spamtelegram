from pyrogram import Client, filters
from time import sleep

api_id = int(input('api_id '))
api_hash = input('api_hash ')

app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash
)

i = 0

with app:
	while True:
		n = int(input("kol-vo iteraciu: "))
		data = input('data(url_photo or text): ')
		man = input('chel_id: ')
		types = input('photo/text: ')
		try:
			while i<n:
				if types == 'text':
					app.send_message(man, data)
					sleep(0.1)
				elif types == 'photo':
					app.send_photo(man, data)
					sleep(0.1)
				else:
					break	
				i+=1

		except:
			print('error')
			man = input('chel_id: ')
		que = input('retry y/n: ')
		if que in ('N', 'n'):
			break
		else:
			i=0
