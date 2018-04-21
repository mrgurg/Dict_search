import vk_api

f = open('train_text', 'w')
login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)

try:
	vk_session.auth()
except vk_api.AuthError as error_msg:
	print(error_msg)

vk = vk_session.get_api()

from random import *

while len(split_ht) < 2000:
	randId = randint(1, 1000000000)
	try:
		response = vk.wall.get(owner_id=randId, count=20, extended = 1)
	except vk_api.exceptions.ApiError:
		continue
	if response['items']:
		for j in range(len(response['items'])):
			i =  response['items'][j]['text']:
			if (re.search(r'[а-яА-Я]', i) and not (re.search(r'[a-zA-Z]', i))):	
				f.write(i + '\n')
				
f.close()
