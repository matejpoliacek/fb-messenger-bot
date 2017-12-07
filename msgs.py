import db
import weather

weather_report = "Hey! Today is a good day to bike to ESTEC!"

def check_msg(message_text, sender_id):
	if (message_text == 'register'):
		found = check_fbID(sender_id)

		if (not found):
			write_fbID(sender_id)
			send_message(sender_id, "Successfully registered")

		else:
			send_message(sender_id, "Already registered!")

	else:
		send_message(sender_id, "roger, that!")

def weather_msg():
	if not get_weather():
		all_ids = get_all_users()
		for user_id in all_ids:
			send_message(user_id, weather_report)
	
