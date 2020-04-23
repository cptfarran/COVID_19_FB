import facebook_scraper as fs
import json, csv


def recent_posts(save=False):
#REPLACED WITH NEW FUNCTION pull_all_posts()
#Save arguement does not currently work - keep as FALSE
	print("Getting most recent posts from the group...")
	
	i=0
	data = {}
	data['postsData'] = []
	
	for post in fs.get_posts(group='670932227050506/?sorting_setting=CHRONOLOGICAL'):
		if post['post_id'] == None:
			print(f'	Post ID readings as none - cannot save post {i}')
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
	print(type(data['postsData']))
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

	print(f"Pulled {i} recorded ids")
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
	temp_rec_ids = rec_ids
	for id in new_ids:
		if id not in temp_rec_ids:
			nrec_ids.append(id)
			temp_rec_ids.append(id)
	
	#Updates the recorded ids file by appending not recorded IDs
	if len(nrec_ids) > 0:
		with open(recorded_ids_file, 'a') as file: ###############################CHANGE FOR NOT TESTING
			for id in nrec_ids:
				file.write(id + ',' + '\n')
		
	print(f'Number of new posts found: {len(nrec_ids)}')

	#Returns list of the actual new post ids
	return(nrec_ids)

def save_new_posts(new_posts,nrec_ids,saved_posts_file):
	i = 0
	temp_nrec_ids = nrec_ids
	with open(saved_posts_file, 'r') as file:
		data = json.load(file)
		for post in new_posts:
			if post['post_id'] in nrec_ids:
				data['postsData'].append(post)
				while(post['post_id'] in nrec_ids):
					nrec_ids.remove(post['post_id'])
				i+=1
	with open(saved_posts_file, 'w') as file: 
		json.dump(data,file)
	print(f'New posts saved: {i}')

def get_saved_posts(saved_posts_file):

	with open(saved_posts_file, 'r') as file:
		data = json.load(file)

	return(data['postsData'])

def get_group_links(group_links_file):
	links = []
	with open(group_links_file, 'r') as file:
		reader = csv.reader(file, delimiter = ',')
		for link in reader:
			links.append(link[0])
	return(links)

def pull_all_posts(group_links_file):
	
	links = get_group_links(group_links_file)

	recordedPosts=0
	groupRecordedPosts=0
	cannotread=0
	noPostID=0

	posts = []
	groupsNotRead=[]
	
	for link in links:
		print(' ')
		print('Getting posts for Group: ' + link)
		try:
			retreived_posts = fs.get_posts(group=link)
			for post in retreived_posts:
				if post['post_id'] == None:
					noPostID+=1
				else:
					posts.append(post)
					recordedPosts+=1
					groupRecordedPosts+=1
			print(f'Retreived {groupRecordedPosts} posts')
			groupRecordedPosts=0
		except TypeError:
			print('Unable to read something for group: ' + link)
			cannotread+=1
			groupsNotRead.append(link)
	
	print(f'Retreived posts: {recordedPosts}')
	print(f'Groups unable to be read: {cannotread}')
	print(f'	Unread Groups: {groupsNotRead}')
	print(f'Posts with no ID: {noPostID}')

	return(posts)
	
#Need new way to save posts - check save_new_posts()

def clear_datetime(posts):
	for post in posts:
		if post['time'] != None:
			post['time'] = None
	return(posts)