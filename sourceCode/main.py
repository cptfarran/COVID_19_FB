from scl import recent_posts, get_recorded_ids, get_new_ids, update_ids, save_new_posts
#rom secondary import 
from test_script import reset_ids_savefile, reset_savefile

import facebook_scraper as fs
import json,csv

new_data_file = 'new_data.json'
recorded_ids_file = 'recorded_ids.csv'
saved_posts_file = 'saved_posts.json'


def main():

	#Gets data from most recent posts and saves to new_data.json
	new_posts = recent_posts(save=False) #CANNOT SAVE RECORDED NEW POSTS
	
	#Pulls previously recorded Post IDs
	rec_ids = get_recorded_ids(recorded_ids_file)

	#Pulls new ids from most recent 
	new_ids = get_new_ids(new_posts)

	#Updates recorded ID file and returns new post ids
	new_post_ids = update_ids(rec_ids,new_ids, recorded_ids_file)

	#Save new posts found to the local savefile
		#Added a try/except in case datetime error occurs again
	try:
		save_new_posts(new_posts,new_post_ids,saved_posts_file) 
	except:
		print('ERROR: Unable to save new files to savefile')


main()