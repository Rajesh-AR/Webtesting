from translate import Translator
translator = Translator(to_lang='ja')
try:
	with open('welcome.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as e:
	print('File path is not corrct')
else:
	print('Something else happened')