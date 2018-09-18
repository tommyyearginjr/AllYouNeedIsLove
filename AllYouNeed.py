a=4

john='. All you need is love.'
paul='. Love is all you need.'

for i in range(0,a):
	katniss=i+1
	lex=str(katniss)
	if a<10:
		if katniss<a:
			print('0'+lex+john)
		else:
			print('0'+lex+paul)
	else:
		if katniss<10:
			print('0'+lex+john)
		elif katniss<a:
			print(lex+john)
		else:
			print(lex+paul)
		
