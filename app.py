from flask import Flask
from flask import render_template, request, url_for, session, redirect

import auth
import messages
# import json

app = Flask(__name__)
app.secret_key = b'aj(>,m&*@#NxmaiOxH23Kkmlb128($'

def is_logged_in():
	'''If 'username' is in the session as a key, return True.
	Otherwise, return False.'''

	return "username" in session
	# if username in session:
	# 	return True
	# else:
	# 	return False
	# if True:
	# 	show_messages()
	# else:
	# 	return redirect(url_for('login.html'))


@app.route("/")
@app.route("/messages/")
def show_messages():
	'''To do: If the user is logged in, render the 'messages.html' template
	together with the user's messages ('inbox').
	If the user is NOT logged in, redirect to the login page.'''

	if is_logged_in(): 
		username = session['username']
		all_messages = messages.get_messages(username)
		return render_template('messages.html', messages=all_messages)
	else:
		return redirect(url_for('login'))


@app.route("/login/", methods=["POST", "GET"])
def login():
	if request.method == 'POST':
		username = request.form.get('username', None)
		password = request.form.get('password', None)
		# Login was successful:
		if auth.login(username, password):
			session['username'] = username
			return redirect(url_for('show_messages'))
		else:
			return render_template('login.html')
	else:
		print('login with GET')
		return render_template('login.html')


@app.route("/logout/")
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))


@app.route("/message/<int:id>/")
def show_message(id):
	# this is the cup that catches the juice
	message = messages.get_message(id)
	return render_template('message.html', message = message)
# ask why you have to put message = message... seems a little redundant
	'''To do: find the given message by its id.
	Then display it in a rendered template.'''
	# pass


@app.route("/message/compose/", methods=["GET", "POST"])
def compose():
	if request.method == 'GET':
		# To do: render the relevant page with no data
		# request.form.get('key') why did you type this?
		return render_template('compose.html')
	# 	username = session['username']
	# 	all_messages = messages.get_messages(username)
	# 	return render_template('messages.html', messages=all_messages)
	# else:
	# 	return redirect(url_for('zzzzzzzzz'))

		
	elif request.method == 'POST':
		# create new dict populate with form data from to sub body. once created you want to send in to messages.add and redirect to mesages page.
		'''To do: 'unpack' the form data, and process it:
		1. Prepare the data in an appropriate data structure
		2. Save the data to your data store (Make use of existing functions
			you may have)
		3. Once the data is saved to file, redirect to the /messages/ page.'''
	username = request.form.get('username', None)
	password = request.form.get('password', None)
		# Login was successful:
	if auth.compose(username, password):
		session['username'] = username
		return redirect(url_for('show_message'(id)))
	else:
		return render_template('show_messages')






















		pass
