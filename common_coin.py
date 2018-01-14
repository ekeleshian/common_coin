
from pdb import set_trace
from pprint import pprint as pp


def add_player(player_num):
	
	return {'id': 'default', 'admin': False, 'credits': 10}

def get_admin(users):

	for player in users:			#to delete prior admins
		if player['admin'] == True:
			player['admin'] = False

	admin = input("Who wants to be the admin? ")

	for player in users:
		if player['id'] == admin:
			player['admin'] = True
			update_users = get_request(player, users)

	return update_users

def get_request(player, users):

	will_request = input("{}, Do you want to connect with someone (y/n)? ".format(player['id']))

	if will_request == 'n'.strip().lower():
		admin = get_admin(users)
		resume_game = get_request(admin, users)
	else:
		potential_connection = 'edgar'
		potential_connection = input("Who do you want to connect with? ")
		is_connection = input("{}, do you want to connect with {} (y/n)?".format(potential_connection, player['id']))
		if is_connection == 'y'.strip().lower():
			player['credits'] += 10
			for player in users:
				if player['id'] == potential_connection:
					player['credits'] += 10

	return users

def gather_players():
	users = []
	player = {}
	all_users = False
	all_names = False

	while not all_users:
		add_players = input("How many players are in this game? ")
		for num in range(int(add_players)):
				player = add_player(num)
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














