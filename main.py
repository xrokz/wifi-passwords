import subprocess
import sys
from os import system, name 
  
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def intro():
	input("press ENTER to continue...")
	clear()
	print("""
Welcome to Wi-Fi Password finder.
Note: this don't give you the password of any network, only saved ones.

Intagram: @9q7p
Discord: @xRokz#0555""")

def get_list(profiles):
	print("\nChoose the number that tags you Wi-Fi to get your password: ")
	j = 0
	for i in profiles:
		j+=1
		print("[{}] {}".format(j, i))

def get_password(index):
	global profiles
	
	i = profiles[index]

	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
	results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

	try:
		print ("The Password you requested is: {:<}".format(results[0]))
		intro()
	except IndexError:
		print ("i coudn't find the password	of {}".format(i))

def input_password():
	global profiles
	get_list(profiles)

	ind = input("\n> ")

	if not ind.isdigit():
		intro() 
		input_password()
	else: 
		ind = int(ind)

	if ind > len(profiles) or ind <= 0:
		intro()
		input_password()
	else:
		get_password(ind-1)
		# get_list(profiles)
		input_password()

try:
	data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
	profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
	intro()
	input_password()

except KeyboardInterrupt as e:
	print("Aborted.")