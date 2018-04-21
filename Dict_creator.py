def Dict_form(dict_file):
	f = open(dict_file)
	my_dict = {}
	#counter = 0
	for line in f:
		
		line = line[line.find('#')+1:len(line)-1]
		line.replace('-,- ','')
		line.replace('-,','')
		line.replace('`','')
		boof = line.split(',')
		#counter +=1
		for lemm in boof:
			#print(counter)
			lemm = lemm.split('\'')
			if len(lemm) > 0: 
				if len(lemm) == 1 :
					lemm.append('')
				# lemm = [stem, ending]
				my_dict = add_too_dict(my_dict, lemm)
	f.close()
	return my_dict			

def add_too_dict(my_dict, lemm):
	if not(lemm[0][0] in my_dict.keys()):
		leaf = {lemm[0][0] : {}}
		my_dict.update(leaf)
	if my_dict[lemm[0][0]] == {}:
		leaf = {lemm[0] : [lemm[1]]}
		my_dict[lemm[0][0]] = leaf
	else:
		if lemm[0] in my_dict[lemm[0][0]].keys():
			if not(lemm[1] in my_dict[lemm[0][0]][lemm[0]]):
				my_dict[lemm[0][0]][lemm[0]].append(lemm[1])
		else:
			leaf = {lemm[0] : [lemm[1]]}
			my_dict[lemm[0][0]].update(leaf)
	return my_dict
