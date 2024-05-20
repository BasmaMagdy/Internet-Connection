print("Welcome to our service.")

name = input("please enter your name : ")
date_start = input("please enter your first day of your internet connection : ")
date_end = input("please enter your end day of youe internet connection : ")
phone_number = input("please enter your phone number : ")

service_day = 1

while service_day < 30 :
	print(service_day)
	service_day += 1

else :
	print("Hello Mr./Ms." + name)
	print("Your internet service is end today : " + str(date_end) + "that start in : " + str(date_start))
	print("Your phone number is : " + str(phone_number))

print("Thanks for using our services.")