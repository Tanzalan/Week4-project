import json


MESSAGE_FILE_PATH = 'data/messages.json'


def get_all_messages():
	with open ('data/messages.json') as f:
		messages = json.load(f)
		return messages

		# for message in messages:
		# 	.append
	# for message in messages:
	#     if yyyyyy == yyyyyy

	'''Get a list of all the messages, loaded from the json file.'''
	# pass


def save_messages(messages):
	'''Save the given messages (list) to the json file.'''
	pass


def get_messages(username):
	'''Get a list of all messages which are addressed to the given user.'''
	messages_to_users = []
	messages = get_all_messages()
	for message in messages:
		if message['to'] == username:
			messages_to_users.append(message)
	return	messages_to_users


		# else:



		# 	return yyyyy
		# else:
		# 	return yyyyy






def get_message(id):
# Unfinished. run try debugging and then ask for help
	messages = get_all_messages()
	found_message = ''
	for message in messages:
		if message['id'] == id:
			found_message = message
			return found_message
		else:
			return None
	# pass
	'''Get the message with the given id.
	Return it if found, otherwise return None.'''



def get_max_id(messages):
	max_id = 0
	for message in messages:
		if message['id'] > max_id:
			max_id = message['id']
	return max_id


def add(message):
	'''Add the given message to the list of all messages.
	Then save the updated list of messages to the json file.
	Be sure that the new message also includes an id!'''
	





	pass