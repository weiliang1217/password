password = 'a123456'
n = 3
while n > 0 :
	n = n - 1
	pwd = input('請輸入密碼: ')
	if pwd != password:
		print('密碼錯誤')
		if n > 0:
			print('還有' , n , '次機會')
	elif pwd == password:
		print('密碼輸入正確')
		break

