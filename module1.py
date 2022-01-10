import random
def avtoparol()->str:
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() 
	str4 = str0+str1+str2+str3
	ls = list(str4) 
	random.shuffle(ls) 
	psword = ''.join([random.choice(ls) for x in range(12)])		
	print(psword)	
	return psword #пароль готов

def paskontroll(psword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True #есть ли в пароле цифры
		if e.isalpha(): a=True #есть ли в пароле буквы
		if e.isupper(): u=True #есть ли в пароле заглавные буквы
		if e.islower(): l=True #есть ли в пароле маленькие буквы
		if d==True and a==True and u==True and l==True and s==True:
			t=True
		else:
			t=False	