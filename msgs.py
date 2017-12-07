import db

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
