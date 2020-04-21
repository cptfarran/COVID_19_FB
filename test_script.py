import json



def reset_ids_savefile(recorded_ids_file):
	blank = []
	with open(recorded_ids_file, 'w') as file:
		for point in blank:
			file.write(point + ',' + '\n')

def reset_savefile(saved_posts_file):
	savepoint = '{"postsData": [{"post_id": "700608134082915", "link": null}]}'
	with open(saved_posts_file, 'w') as file:
		file.write(savepoint)

def check_json(file):
	with open(file,'r') as savefile:
		data = json.load(savefile)
		for post in data['postsData']:
			print(str(post['post_id']) + ',')
			#print('____________________________________________________')
#		print(len(data['posts']))