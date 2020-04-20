import facebook_scraper as fs
import json, csv

# (1) Currently not saving the datatime variable from python to json data format

new_data_file = 'new_data.json'
recorded_ids_file = 'recorded_ids.csv'
saved_posts_file = 'saved_posts.json'

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

def check_json(file):
	with open(file,'r') as savefile:
		data = json.load(savefile)
		for post in data['postsData']:
			print(str(post['post_id']) + ',')
			#print('____________________________________________________')
#		print(len(data['posts']))

def check_rec_ids():
	i = 0
	j = 0
	ids = []
	with open(recorded_ids_file, 'r') as records:
		reader = csv.reader(records, delimiter = ',')
		reader2 = reader
		for row in reader:
			ids.append(row[0])
		for id in ids:
			curr_id = id
			for id in ids:
				if id == curr_id:
					i+=1
	print(f'Matches: {i}')
	print(f'Total: {len(ids)}')


def get_recorded_ids():
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


def check_nrec(rec_ids,new_ids):
	#Will return an updated list of recorded ids  and a list of added ids given a list of new ids
	nrec_ids = []

	for id in new_ids:
		if id not in rec_ids:
			rec_ids.append(id)
			nrec_ids.append(id)
	return(rec_ids,nrec_ids)

def update_rec_ids(new_ids):
	with open(recorded_ids_file, 'w') as records:
		for id in new_ids:
			records.write(id + ',' + '\n')

def get_new_ids(new_data):
	new_ids = []
	for post in new_data:
		new_ids.append(post['post_id'])
	return(new_ids)

def save_new_posts(new_posts,nrec_ids):
	i = 0
	with open(saved_posts_file, 'r') as file:
		data = json.load(file)
		print(data['postsData'])
		for post in new_posts:
			if post['post_id'] in nrec_ids:
				data['postsData'].append(post)
				i+=1
	
	with open(saved_posts_file, 'w') as file: 
			json.dump(data,file)		
	print(f'New posts saved: {i}')
			
def update_ids(rec_ids, new_ids):
	#Takes in previously recorded ids from file	and new ids from recent update

	#Compares to find actual new posts
	nrec_ids = []

	for id in new_ids:
		if id not in rec_ids:
			nrec_ids.append(id)

	#Updates the recorded ids file by appending not recorded IDs
	with open(recorded_ids_file, 'w') as file: ###############################CHANGE FOR NOT TESTING
		for id in nrec_ids:
			file.write(id + ',' + '\n')
	
	print(f'Number of new posts found: {len(nrec_ids)}')

	#Returns list of the actual new posts
	return(nrec_ids)

def reset_ids_savefile():
	blank = []
	with open(recorded_ids_file, 'w') as file:
		for point in blank:
			file.write(point + ',' + '\n')

def main():

	####FOR TESTING PURPOSES ONLY
	reset_ids_savefile()

	#Gets data from most recent posts and saves to new_data.json
	new_posts = recent_posts(save=True)
	
	#Pulls previously recorded Post IDs
	rec_ids = get_recorded_ids()

	#Pulls new ids from most recent 
	new_ids = get_new_ids(new_posts)

	#Updates recorded ID file and returns new post ids
	new_post_ids = update_ids(rec_ids,new_ids)

	save_new_posts(new_posts,new_post_ids) 

	#INSERT CODE TO PULL NEW ID POSTS AND SAVE THEM TO MAIN SAVEFILE

	

#check_json('old_data.json')
main()