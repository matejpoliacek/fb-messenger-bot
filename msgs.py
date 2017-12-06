def check_msg(message_text, sender_id):
	if (message_text == 'register'):
		found = False
		with open("users.txt", "r+") as userlist:
			for line in userlist:
				line = line.rstrip()
				if (line == sender_id):
					send_message(sender_id, "You are already registered!")
					found = True
					break

		if (not found):
			return sender_id
			#with open("users.txt", "a+") as userlist:
			#	userlist.write(sender_id)
			#	send_message(sender_id, "Successfully registered")

	else:
		send_message(sender_id, "roger, that!")
		return ""
