import json


USERS_FILE_PATH = 'data/users.json'


def login(username, password):
	'''Load all users from the json file.
	If a user is found with a matching username AND password,
	return True. Otherwise, return False.'''
	with open('data/users.json') as f:
		users = json.load(f)

		for user in users:
			# dict_user_name = user["username"]
			# dict_pasword = user["password"]
			if username == user["username"] and password == user["password"]:
				return True
		else:
			return False

		# 	if user
		# # # is_logged_in()
		# show_messages(username, password)
	# else:
		# return redirect
		return render_template('login.html')


			# 	with open('data/game-state.json') as f:
			# game = json.load(f)


# How do you get the value from a dictiony
# when you have them check if they match if yes then return true
		# upload json file. with for loop find to find the user

