
from pdb import set_trace
from pprint import pprint as pp


def add_player():
	
	return {'id': 'default', 'admin': False, 'credits': 10, 'in_game':True}

def get_admin(users):

	for player in users:			#to delete prior admins
		if player['admin'] == True:
			player['admin'] = False
	user_check = False
	while not user_check:
		admin = input("Who wants to be the admin? ")
		for player in users:
			if player['id'] == admin:
				user_check = True
				break

	for player in users:
		if player['id'] == admin:
			player['admin'] = True
			update_users = get_request(player, users)

	return update_users

def get_request(player, users):
	#set_trace()
	will_request = input("{}, do you want to connect with someone (y/n)? ".format(player['id']))

	if will_request == 'n'.strip().lower():
		admin = get_admin(users)
		resume_game = get_request(admin, users)
	else:
		user_check = False
		while not user_check:
			potential_connection = input("Who do you want to connect with? ")
			for user in users:
				if user['id'] == potential_connection and potential_connection != player['id']:
					user_check = True
					break
			if potential_connection == player['id']:
				print("You can't connect with yourself! ")
		is_connection = input("{}, do you want to connect with {} (y/n)?".format(potential_connection, player['id']))
		if is_connection == 'y'.strip().lower():
			player['credits'] += 10
			for user_dict in users:
				if user_dict['id'] == potential_connection:
					user_dict['credits'] += 10
		else:
			stolen_creds = player['credits']
			player['credits'] = 0
			player['in_game'] = False
			for user_dict in users:
				if user_dict['id'] == potential_connection:
					user_dict['credits'] += stolen_creds

	return users

def gather_players():
	users = []
	player = {}
	all_users = False
	all_names = False

	while not all_users:
		add_players = input("How many players are in this game? ")
		for num in range(int(add_players)):
				player = add_player()
				users.append(player)
		all_users = True

	while not all_names:
		for player in users:
			name = input("What is your name? ")
			player['id'] = name
		all_names = True

	return get_admin(users)

all_players = gather_players()

pp(all_players)














