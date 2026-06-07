print('Welcome to Cash Flow')
print('Please indicate your age')
age = int(input())

if age >= 18:
	print("Eligible for application")
	print('we require additional details')
	print ('email address')
	email_address = input()
	print('phone number')
	Phone_number = input()
	
	is_valid=True 
	
	if '@g' not in email_address or "." not in email_address 
		print('Invalid email address')
		is_valid=False
		
	if len(phone number) < 10 or not phone_number.isdigit():
		print('Invalid phone number')
		is_valid=False
		
	if is_valid:
		print('Application successful')
		
else:
	print('Too young to apply')
