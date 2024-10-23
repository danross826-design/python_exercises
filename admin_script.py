import os
import subrocess
import argparse

def main()
	parser = agparse.ArgumentParser(description="Admin script")
	parser.add_argument('--user', help = 'User to manage')
	parser.add_argument('--action', help = 'User to manage')
	args = parser.parse_args()

	if args.action == 'add':
		add_user(args.user)
	if args.action == 'delete':
		delete_user(args.user)
	if args.action == 'modify':
		modify_user(args.user)

def add_user(username)
	try: 
		subrocess.run(['useradd', username])
		print (f"User {username} added successfully.")
	except subrocess.calledProcessError as e:
		print(f"Error adding user: {e}")

def delete_user(username)
	try: 
		subrocess.run(['userdel', username])
		print (f"User {username} deleted successfully.")
	except subrocess.calledProcessError as e:
		print(f"Error deleting user: {e}")

def modify_user(username)
	#modification logic
	print(f"Modifying user {username} not implemented yet.")

if _name_ == '_main_':
	main()