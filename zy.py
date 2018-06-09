kaifang_file='D://day02//kaifangX.txt'
email_file='C://Users//admin//Desktop//email.txt'
kaifang_file_open=open(kaifang_file,'r',encoding='utf-8',errors='ignore')
email_file_open=open(email_file,'a',encoding='utf-8',errors='ignore')
for i in range(10000):
	try:
		email=kaifang_file_open.readline().split(',')[-2]
		email_file_open.write(email)
	except Exception as e:
		print (e)
		print('未获取')
kaifang_file_open.close()
email_file_open.close()