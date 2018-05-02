from pymystem3 import Mystem
from linkgrammar import Sentence, ParseOptions, Dictionary, Clinkgrammar as clg

def methric_count(segmentation_list):
	stemmer = Mystem()
	methric_list = []
	functional_list = ['CONJ','COM','PR','PART','INTJ']
	methric = []
	po = ParseOptions(verbosity=1)
	po = ParseOptions(min_null_count=0, max_null_count=999)
	for line in segmentation_list:

		unknown_words = 0
		functional_words = 0
		number_of_words = 0
		link_rate = 0
		
		number_of_words = len(line.split())

		grammar_information = stemmer.analyze(line)
		grammar_information = grammar_information[:len(grammar_information)-1]
		
		sent = Sentence(line, Dictionary('ru'), po)
		sent.parse()

		link_rate = sent.null_count()
 
		while {'text' : ' '} in grammar_information:
			grammar_information.pop(grammar_information.index({'text' : ' '}))
		for info in grammar_information:
			if 'analysis' in info.keys():
				if len( info['analysis'])==0:
					unknown_words+=1
				else:
					if 'qual' in info['analysis'][0]:
						if info['analysis'][0]['qual'] == 'bastard':
							unknown_words+=1
					grammar =  info['analysis'][0]['gr']
					for f in functional_list:
						if grammar.find(f+'=', 0,  5) > -1 or grammar.find(f+',', 0, 5) > -1:
							functional_words+=1
							break
							

		methric_list.append([link_rate, unknown_words, (number_of_words - functional_words)/number_of_words])

	return methric_list 

