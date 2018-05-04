import Dict_creator
def first_word_hyp_existing (hashtag, my_dict):
	word_hyp = []

	if hashtag[0] in my_dict.keys():
		dict_branch = my_dict[hashtag[0]]
	else:
		return []
	substring = ''
	for i in hashtag:
		substring += i
		if substring in dict_branch:
			word_hyp.append(substring)
	stems = word_hyp[:]
	for i in range (0,len(stems)) :
		stem = stems[i]
		flag = False
		endings = []
		if stem in dict_branch.keys():
			endings = dict_branch[stem]
		else:
			flag = True
			
		if not(endings == []):
			ending = ''
			if ending in endings:
				flag = True
			
			for it in hashtag[len(stem):]:
				ending += it
				if ending in endings:
					if not (flag):
						word_hyp[i]+=ending
						flag = True
					else:
						word_hyp.append(stem)
						word_hyp[len(word_hyp)-1] +=ending
		
		if not (flag):
			word_hyp[i] = ''
	
	i = 0
	while (i<len(word_hyp)):
		if word_hyp[i] == '':
			word_hyp.remove(word_hyp[i])
			#print('Удалено!')
		else:
			i +=1
			
	return word_hyp



def Make_hyp (hashtag, my_dict):
	word_hyp = first_word_hyp_existing(hashtag, my_dict)
	unknown_finish = 0 #iterator of the end of substring with unknown word
	alphabet =  ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','.',',','!','?']

	if word_hyp == []:
		if not (hashtag[0] in alphabet):
			symb_seq = 0
			notinalph = True
			while notinalph and (not (len(hashtag) == symb_seq)):
				notinalph = (not (hashtag[symb_seq] in alphabet))
				symb_seq+=1
			if (not (len(hashtag) == symb_seq)):
				symb_seq-=1
			word_hyp.append(hashtag[:symb_seq])
	
	unknown_count = [0 for i in range (0, len(word_hyp))]
	if word_hyp == []:
			if len(hashtag) >= 1:
				for i in range (0, len(hashtag)):
					substring = hashtag[i:]
					if not (first_word_hyp_existing(substring, my_dict) == []):

						word_hyp.append(hashtag[:unknown_finish])
						unknown_count.append(1)
					unknown_finish = i+1
					
	for i in range (0,len(word_hyp)):
		word_hyp[i] = [word_hyp[i]]
	
	flag = True

	while (flag):
		flag = False 
		it = 0

		while it < len(word_hyp):			
			if (len(word_hyp[it])>6) or (unknown_count[it] > 3):
				word_hyp.pop(it)
				unknown_count.pop(it)
				it-=1
				flag = True
			else:
				ibegin = 0 #iterator on begin of the unslited part
				unknown_finish = 0
				for j in range (0, len(word_hyp[it])):
					ibegin += len(word_hyp[it][j])
					
				if ibegin < len(hashtag):
					substring = hashtag[ibegin:]
					if unknown_count[it] == 0:
						boof = word_hyp[it][:]
						boof.append(substring)
						if not (boof in word_hyp):
							word_hyp.append(boof)
							unknown_count.append(0)
							flag = True

					unknown_finish = 0
					if first_word_hyp_existing(substring, my_dict) == []:
						if not (substring[0] in alphabet):
							symb_seq = 0
							notinalph = True
							while notinalph  and (not (len(substring) == symb_seq)):
								notinalph = not(substring[symb_seq] in alphabet)
								symb_seq+=1
							if not (notinalph):
								symb_seq-=1
							word_hyp[it].append(substring[:symb_seq])
							substring = substring[symb_seq:]
							flag = True
		
						else:
							
							first_variant = True
							digit_started = False
							if len(substring) >= 1:
								for i in range (0, len(substring)):
										subsubstring = substring[i:]
										if digit_started and subsubstring[0] in alphabet:
											digit_started = False
										
										if not (first_word_hyp_existing(subsubstring, my_dict) == []) or (not(subsubstring[0] in alphabet) and not digit_started):
											if not(subsubstring[0] in alphabet) and not digit_started:
												digit_started = True

											if (first_variant):
												
												mem = word_hyp[it][:]
												check = mem[:]
												check.append(substring[:unknown_finish])
												if not (check in word_hyp):
													word_hyp[it].append(substring[:unknown_finish])
													first_variant = False
													unknown_count[it]+=1
											else:
												boof2 = mem[:]
												boof2.append(substring[:unknown_finish])
												if not(boof2 in word_hyp):
													word_hyp.append(boof2)
													unknown_count.append(unknown_count[it]+1)
											flag = True

										unknown_finish = i+1

								boof = word_hyp[it][:]
								boof.append(substring)
								if len(substring) == unknown_finish and first_variant and not (boof in word_hyp):
									word_hyp[it].append(substring)
									unknown_count.append(unknown_count[it]+1)
								elif (boof in word_hyp):
									word_hyp.pop(it)
									it-=1 		
										
							substring = substring[unknown_finish:]
					else:			
								
						if not (ibegin+unknown_finish >= len(hashtag)):
							flag = True
							boof = first_word_hyp_existing(substring, my_dict)
							f = False
							for word in boof:
								if not f:
									mem = word_hyp[it][:]
									check = mem[:]
									check.append(word)
									if not (check in word_hyp):
										word_hyp[it].append(word)
										f = True
								else:
									boof2 = mem[:]
									boof2.append(word)
									if not(boof2 in word_hyp):
										word_hyp.append(boof2)
										unknown_count.append(unknown_count[it])

			it+=1
						
	segmentation = []
	for sublist in word_hyp:
		segmentation.append('')
		for word in sublist:
			segmentation[len(segmentation)-1] += word + ' '
		segmentation[len(segmentation)-1] = segmentation[len(segmentation)-1][:len(segmentation[len(segmentation)-1])-1]
	return segmentation

# li = Dict_creator.Dict_form('/home/corra/Documents/VKR/zaliznjak.txt')
# h = Make_hyp('мамамылараму', li)
# print( Methrics.methric_count(h), h )




# segmentation_test('/home/corra/Documents/VKR/splittedHashtagsTest.txt', '/home/corra/Documents/VKR/joinedHashtagsTest.txt')

	
