print('Welcome to Cash Flow')
print('Please indicate your age')
age = int(input())

if age >= 18:
	print("Eligible for application")
	print('we require additional details')
	print ('email address')
	email_address = input()
	print('Phone number')
	Phone_number = input()
	
	is_valid=True 
	
	if '@gmail.com' not in email_address:
		print('Invalid email address')
		is_valid=False
		
	if '0' not in Phone_number:
		print('Invalid phone number')
		is_valid=False
		
	if is_valid:
		print('Application successful')
		
else:
	print('Too young to apply')
