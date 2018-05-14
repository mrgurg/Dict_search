import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import re



ftest2 = open('splittedHashtags.txt', 'r')
splitted = ftest2.readlines()
splitted_raw = ['_'.join([a.strip('_') for a in x.split('_') if len(a) > 0]) for x in splitted]
splitted_raw = [re.sub("[^а-яА-Я_]","",x) for x in splitted]
joined, splitted = [], []
splitted_raw = list(set(splitted_raw))
splitted_raw = ['_'.join([a.strip('_') for a in x.split('_') if len(a) > 0]) for x in splitted_raw]
for i in range(len(splitted_raw)):
    if (len(splitted_raw[i]) >= 5 and '_' in splitted_raw[i]):
        splitted.append(splitted_raw[i].strip('_'))
        joined.append(splitted_raw[i].replace('_', ''))

#s = "простименямоялюбовь"
counter = 0

hp_one = open('GP_test/splitted/2.txt', 'r')
splitted_one = hp_one.readlines()
hp_two = open('GP_test/splitted/3.txt', 'r')
splitted_two = hp_two.readlines()
hp_more = open('GP_test/splitted/4.txt', 'r')
splitted_more = hp_more.readlines()

ftest2.close()
hp_one.close()
hp_two.close()
hp_more.close()

splitted_one = [x.replace(' ','_') for x in splitted_one]
splitted_one = [re.sub("[^а-яА-Я_]","",x) for x in splitted_one]
splitted_two = [x.replace(' ','_') for x in splitted_two]
splitted_two = [re.sub("[^а-яА-Я_]","",x) for x in splitted_two]
splitted_more = [x.replace(' ','_') for x in splitted_more]
splitted_more = [re.sub("[^а-яА-Я_]","",x) for x in splitted_more]
joined_one = [x.replace('_','') for x in splitted_one]
joined_two = [x.replace('_','') for x in splitted_two]
joined_more = [x.replace('_','') for x in splitted_more]

for num, s in enumerate(joined[:1000]):
	L = []
	win_size = len(s)
	all_words = {}


	while (win_size > 0):
		curr = []
		for i in range(len(s) - win_size + 1):
			#print(s[i:win_size+i])
			p = morph.parse(s[i:win_size+i])[0]
			#print(len(p.methods_stack), str(p.methods_stack[0][0]))
			if (len(p.methods_stack) == 1 and str(p.methods_stack[0][0]) == "<DictionaryAnalyzer>") or (len(p.methods_stack) == 2 and str(p.methods_stack[0][0]) == "<DictionaryAnalyzer>" and str(p.methods_stack[1][0]) == "<KnownPrefixAnalyzer>"):
				if (len(s[i:win_size+i]) == 1 and p.tag.POS not in ["NPRO", "PREP", "CONJ", "PRCL"]):
						continue
				curr.append(s[i:win_size+i])
		all_words[win_size] = curr 

		win_size -= 1

	#print(all_words)

	all_tokens = sorted([x for y in list(all_words.values()) for x in y], key = len, reverse = True)

	n = 0
	odd = ''
	while True:
		parts = []
		ht = s
		for k, w in all_words.items():
			for token in w:
				if (ht.find(token) != -1 and token != odd):
					parts.append(token)
					ht = ht.replace(token, '_')
		odd = all_tokens[n]
		n += 1
		#print(parts)
		if (len(''.join(parts)) == len(s) or n == len(all_tokens)-1):
			break
		
	if (len(s) != len(''.join(parts))):
		L = []
		while True:
			for i in range(len(s)):
				p = morph.parse(s[i:])[0]
				if (len(p.methods_stack) == 1 and str(p.methods_stack[0][0]) == "<DictionaryAnalyzer>") or (len(p.methods_stack) == 2 and str(p.methods_stack[0][0]) == "<DictionaryAnalyzer>" and str(p.methods_stack[1][0]) == "<KnownPrefixAnalyzer>"):
					L.append(s[i:])
					s = s[:i]
					break
			if (i == (len(s)-1)):
				L.append(s)
			if (i == 0 or i == (len(s)-1)):
				break
		result = '_'.join(L[::-1])
	else:
		result = ''
		c = s 
		while (len(result.replace('_','')) != len(c)):
			for i in parts:
				if (s.find(i) == 0):
					result += i + '_'
					s = s[len(i):]
					break
		result = result.strip('_')
	if (result == splitted[num]):
		counter += 1
	else:
		print(splitted[num], result, parts)
	
print(counter, "из", 1000)
	
