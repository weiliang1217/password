n = 3 # 次數
n = int(n)
while n >= 0:
	password = input('請輸入密碼: ')
	if password != 'a123456':
		print ('密碼錯誤! 還有',n,'次機會')
		n = n -1
	elif password == 'a123456':
		print('登入成功')
		raise SystemExit
print('超過嘗試次數')
raise SystemExit