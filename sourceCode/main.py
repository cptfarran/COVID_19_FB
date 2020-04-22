from scl import recent_posts, get_recorded_ids, get_new_ids, update_ids, save_new_posts
#rom secondary import 
from test_script import reset_ids_savefile, reset_savefile, check_json, check_duplicate_ids, check_recordsVposts

import facebook_scraper as fs
import json,csv

new_data_file = 'C:/Users/patri/OneDrive/Documents/Scripts/COVID_19_FB/data/new_data.json'
recorded_ids_file = 'C:/Users/patri/OneDrive/Documents/Scripts/COVID_19_FB/data/recorded_ids.csv'
saved_posts_file = 'C:/Users/patri/OneDrive/Documents/Scripts/COVID_19_FB/data/saved_posts.json'
fake_saved_posts = 'C:/Users/patri/OneDrive/Documents/Scripts/COVID_19_FB/data/working_saved_posts.json'


def main():

	#reset_ids_savefile(recorded_ids_file)
	#reset_savefile(saved_posts_file)
	#Gets data from most recent posts and saves to new_data.json
	new_posts = recent_posts(save=False) 
	
	#Pulls previously recorded Post IDs
	rec_ids = get_recorded_ids(recorded_ids_file)

	#Pulls new ids from most recent 
	new_ids = get_new_ids(new_posts)

	#Updates recorded ID file and returns new post ids
	new_post_ids = update_ids(rec_ids,new_ids, recorded_ids_file)

	#Save new posts found to the local savefile
	save_new_posts(new_posts,new_post_ids,saved_posts_file) 

	#Testing code
	testing_code(rec_ids)

	print('===============ENDING===============')

def testing_code(rec_ids):

	print('')
	print('==========RUNNING TESTING CODE==========')
	
	#Looks at saved posts and cross checks with the recorded ID file
	print('Checking saved posts for duplicates')
	check_duplicate_ids(saved_posts_file, rec_ids)

	#Checks that number of saved IDs is the same as number of saved posts
	check_recordsVposts(recorded_ids_file, saved_posts_file)


main()