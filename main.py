from Dict_creator import*
from Segment import*
from Methrics import*

def segmentation_test(splitted, joined):

	my_dict = Dict_creator.Dict_form('/home/corra/Documents/VKR/zaliznjak.txt')
	print('Dictionary was successfuly formed!')
	
	s = open(splitted)
	j = open(joined)
	b = open ('/home/corra/Documents/VKR/bad.txt', 'w')
	g_s = open ('/home/corra/Documents/VKR/goodSegmented.txt', 'w')
	g_j = open ('/home/corra/Documents/VKR/goodJoined.txt', 'w')
	total = 0
	success = 0
	
	for j_line in j:
		s_line = s.readline()
		total+=1
		print(total)
		j_line = j_line[:len(j_line)-1]
		s_line = s_line[:len(s_line)-1]

		if s_line in Make_hyp(j_line, my_dict):
			success+=1
			g_s.write(s_line +'\n')
			g_j.write(j_line +'\n')

		else:
			b.write(s_line + '\n')
	g_s.close()
	g_j.close()
	b.close()
	print("hashtags processed: ",total, " \n hashtags splitted correctly: ", success, "\n occurancy: ", (success/total)*100, "% \n")

# segmentation_test('/home/corra/Documents/VKR/splittedHashtagsTest.txt', '/home/corra/Documents/VKR/joinedHashtagsTest.txt')

my_dict = Dict_form('/home/corra/Documents/VKR/zaliznjak.txt')
print('Dictionary was successfuly formed!')

src  = open ('/home/corra/Documents/VKR/goodJoined.txt')
chck = open ('/home/corra/Documents/VKR/goodSegmented.txt')
res  = open ('/home/corra/Documents/VKR/result.txt', 'w')
count = 0
success = 0
for hashtag in src:
	count +=1

	hypothesis = Make_hyp(hashtag, my_dict)
	print(hypothesis)
	#[link_rate, unknown_words, (number_of_words - functional_words)/number_of_words]	
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
		l.append(i[1])
	minimum_unknown = min(l)
	for i in range (0, len(hypothesis)):
		if metric_list[i][1] == minimum_unknown:
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
	print(hypothesis)
	res.write(hypothesis[0])
	line = chck.readline()
	if hypothesis[0] == line[:len(line)-1]:
		success+=1

	print(count)


	print((success/count)*100)


