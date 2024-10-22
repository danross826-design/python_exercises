import argparse

admin_users = ["admin", "root"];

def is_admin(username)
	return username in admin_users;

def add_user(username)
	if(is_admin(username))
	#code to add new user
	print("user added successfully")
	else:
	print("Unauthorized Access")

parser = argparse.ArgumentParser(description="Admin Script")
parser.add_argument("command", help="The command to execute")
parser.add_argument("username", help="The username of the admin")
args = parser.parse_args()

if is_admin(args.username):
    if args.command == "add_user":
        add_user("newuser")  # Replace with actual user creation logic
    # ... other commands
else:
    print("Unauthorized access.")


