import json
from scl import get_recorded_ids, get_saved_posts

def reset_ids_savefile(recorded_ids_file):
	blank = []
	with open(recorded_ids_file, 'w') as file:
		for point in blank:
			file.write(point + ',' + '\n')

def reset_savefile(saved_posts_file):
	savepoint = '{"postsData": [{"post_id": "1234567890", "text": "This is a test entry -PG"}]}'
	with open(saved_posts_file, 'w') as file:
		file.write(savepoint)

def check_json(file):
	with open(file,'r') as savefile:
		data = json.load(savefile)
		for post in data['postsData']:
			print(str(post['post_id']) + ',')
			#print('____________________________________________________')
#		print(len(data['posts']))

def check_duplicate_ids(file,recorded_ids):
	checked_ids = []
	duplicates=0
	with open(file,'r') as savefile:
		data = json.load(savefile)
		for post in data['postsData']:
			if post['post_id'] in checked_ids:
				print(f'Duplicate ID found: ' + str(post['post_id']))
				duplicates+=1
			elif post['post_id'] in recorded_ids:
				checked_ids.append(post['post_id'])
	print(f'Total duplicate IDs found: {duplicates}')

def check_recordsVposts(recorded_ids_file, saved_posts_file):

	recorded_ids = get_recorded_ids(recorded_ids_file)
	saved_posts = get_saved_posts(saved_posts_file)

	len_rec = len(recorded_ids)
	len_posts = len(saved_posts)

	if len_rec == len_posts:
		print('Same number of posts and records found.')
	else:
		print(f'ERROR: {len_posts} posts found and {len_rec} recorded IDs found. ')