import vk_api

f = open('test_hashtags.txt', 'a')
login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)

try:
	vk_session.auth()
except vk_api.AuthError as error_msg:
	print(error_msg)

vk = vk_session.get_api()

from random import *

split_ht = []

while len(split_ht) < 2000:
	randId = randint(1, 1000000000)
	try:
		response = vk.wall.get(owner_id=randId, count=20, extended = 1)
	except vk_api.exceptions.ApiError:
		continue
	if response['items']:
		for j in range(len(response['items'])):
			if '#' in response['items'][j]['text']:
				for i in response['items'][j]['text'].split():
					i = i.strip()[0]
					if i == '#': 
						if (re.search(r'[а-яА-Я]', i) and not (re.search(r'[a-zA-Z]', i))):
							if (len(re.findall('_', i)) > 0 and len(re.findall(r'[А-Я]', i))>1):
								L =  [x for x in i.split('_') if len(x) > 12]
								if (len(L)) == 0:
									split_ht.append(i)
							if (len(re.findall(r'[А-Я]', i)) > 1 and len(re.findall(r'[а-я]', i)) < 25 and len(re.findall(r'[а-я]', i)) > 8): 
								split_ht.append(i)

f.close()
