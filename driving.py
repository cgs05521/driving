country = input('請問您是哪國人')
age = input('請輸入年齡： ')
age = int(age)
if country == '台灣' :
	if age >=18:
		print('你可以考台灣駕照')
	else :
		print('你不能考台灣駕照')
elif country == '美國':
	if age >=16:
		print('你可以考美國駕照')
	else:
		print('你不能考美國駕照')
else:
	print('你只能輸入台灣或美國')