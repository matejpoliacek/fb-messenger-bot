from db_script import check_fbID, write_fbID, check_post, mute_fbID, unmute_fbID, get_all_users
from weather_script import get_weather
from responses import send_message, log
import re

def clean_msg(text):
	text = ''.join(text.split()).lower()
	text = re.sub(r'[a-zA-Z]', '', text)
	return text

def check_msg(message_text, sender_id):
	message_text = clean_msg(message_text)
	if (message_text == 'register'):
		reg_msg(sender_id)
	elif (message_text == 'unregister'):
		unreg_msg(sender_id)
	elif (message_text == 'help'):
		help_msg(sender_id)
	else:
		send_message(sender_id, "Type 'help' for a list of available commands.")

def weather_msg():
	all_ids = get_all_users()
	for user_id in all_ids:
		send_message(user_id[0], get_weather())

def reg_msg(sender_id):
	found = check_fbID(sender_id)
	if (not found):
		write_fbID(sender_id)
		send_message(sender_id, "Successfully registered")
	else:
		if (check_post(sender_id)):
			send_message(sender_id, "Already registered!")
		else:
			unmute_fbID(sender_id)
			send_message(sender_id, "Successfully registered, welcome back!")
	

def unreg_msg(sender_id):
	found = check_fbID(sender_id)
	reply = "You were not registered at the moment, no need to unregister."	

	if (not found):
		send_message(sender_id, reply)
	else:
		if (check_post(sender_id)):
			mute_fbID(sender_id)
			send_message(sender_id, "You now are unregistered. Feel free to come back using 'register' at any time!")
		else:
			send_message(sender_id, reply)

def help_msg(sender_id):
	send_message(sender_id, "Welcome to ESTEC Bike Weather Bot! Commands currently available:\nregister - add yourself to the list\nunregister - remove yourself from the list\n\nReports are sent out at 5:00 UTC")
