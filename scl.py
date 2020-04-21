import facebook_scraper as fs
import json, csv


def recent_posts(save=False):

	print("Getting most recent posts from the group...")
	
	i=0
	data = {}
	data['postsData'] = []
	
	for post in fs.get_posts(group='670932227050506/?sorting_setting=RECENT_ACTIVITY'):
		if post['post_id'] == None:
			print(f'	ERROR: Post ID readings as none - cannot save post {i}')
		else:
			#print(post['post_id'])
			data['postsData'].append(post)
			i+=1
	print(f"Retreived {i} posts from the group.")

	if save is True:
		print(f"Attempting to save retreived {i} posts from the group to file: {new_data_file}")
		with open(new_data_file, 'w') as savefile:
			try:
				json.dump(data['postsData'], savefile)
				print('Saved new posts successfully')
			except:
				print(f'Unable to save new posts to {new_data_file}')
	return(data['postsData'])

def get_recorded_ids(recorded_ids_file):
	#Will return a list of previous Post IDs, including 'None', for crosscheck
	
	print(f'Pulling previously recorded Post IDs from file: {recorded_ids_file}')

	ids = []
	i = 0

	with open(recorded_ids_file, 'r') as records:
		reader = csv.reader(records, delimiter = ',')
		for row in reader:
			ids.append(row[0])
			i+=1

	print(f"Pulled {i} recorded ids, including 'None'")
	return(ids)

def get_new_ids(new_data):
	new_ids = []
	for post in new_data:
		new_ids.append(post['post_id'])
	return(new_ids)

def update_ids(rec_ids, new_ids, recorded_ids_file):
	#Takes in previously recorded ids from file	and new ids from recent update

	#Compares to find actual new posts
	nrec_ids = []

	for id in new_ids:
		if id not in rec_ids:
			nrec_ids.append(id)

	#Updates the recorded ids file by appending not recorded IDs
	if len(nrec_ids) > 1:
		with open(recorded_ids_file, 'a') as file: ###############################CHANGE FOR NOT TESTING
			for id in nrec_ids:
				file.write(id + ',' + '\n')
		
	print(f'Number of new posts found: {len(nrec_ids)}')

	#Returns list of the actual new posts
	return(nrec_ids)

def save_new_posts(new_posts,nrec_ids,saved_posts_file):
	i = 0
	with open(saved_posts_file, 'r') as file:
		data = json.load(file)
		for post in new_posts:
			if post['post_id'] in nrec_ids:
				data['postsData'].append(post)
				i+=1
	with open(saved_posts_file, 'w') as file: 
			json.dump(data,file)		
	print(f'New posts saved: {i}')
