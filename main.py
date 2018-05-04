
from Dict_creator import*
from Segment import*
from Methrics import*

my_dict = Dict_form('/home/corra/Documents/VKR/zaliznjak.txt')
print('Dictionary was successfuly formed!')

src  = open ('/home/corra/Documents/VKR/GP_test/joined/5j.txt')
chck = open ('/home/corra/Documents/VKR/GP_test/splitted/5.txt')
res  = open ('/home/corra/Documents/VKR/result.txt', 'w')
count = 0
success = 0
for hashtag in src:
	count +=1

	hypothesis = Make_hyp(hashtag, my_dict)
	print(hypothesis)
	#[link_rate, unknown_words, (number_of_words - functional_words)/number_of_words]	
	if not hypothesis == []:
		metric_list = methric_count(hypothesis)
		
		l = []
		for i in metric_list:
			l.append(i[0])
		minimal_link_rate = min(l)
		boof_h = []
		boof_m = []
		for i in range (0, len(hypothesis)):
			if metric_list[i][0] == minimal_link_rate:
				boof_h.append(hypothesis[i])
				boof_m.append(metric_list[i])

		hypothesis = boof_h
		metric_list = boof_m
		boof_h = []
		boof_m = []
		l = [] 
		for i in metric_list:
			l.append(i[2])
		maximum_part_not_func = max(l)
		for i in range (0, len(hypothesis)):
			if metric_list[i][2] == maximum_part_not_func:
				boof_h.append(hypothesis[i])
				boof_m.append(metric_list[i])

		hypothesis = boof_h
		metric_list = boof_m
		boof_h = []
		boof_m = []
		l = [] 
		for i in metric_list:
			l.append(i[3])
		maximum_length_of_unfunc = max(l)
		for i in range (0, len(hypothesis)):
			if metric_list[i][3] == maximum_length_of_unfunc:
				boof_h.append(hypothesis[i])
				boof_m.append(metric_list[i])

		hypothesis = boof_h
		metric_list = boof_m
		boof_h = []
		boof_m = []
		l = [] 
		for i in metric_list:
			l.append(i[1])
		minimum_unknown = min(l)
		for i in range (0, len(hypothesis)):
			if metric_list[i][1] == minimum_unknown:
				boof_h.append(hypothesis[i])
				boof_m.append(metric_list[i])

		hypothesis = boof_h
		print(hypothesis)
		res.write(hypothesis[0])
		line = chck.readline()
		if hypothesis[0] == line[:len(line)-1]:
			success+=1


	else:
		res.write(hashtag)


		hypothesis = boof_h
		metric_list = boof_m
		boof_h = []
		boof_m = []
		l = []


