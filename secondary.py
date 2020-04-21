import csv

def update_rec_ids(new_ids):
	with open(recorded_ids_file, 'w') as records:
		for id in new_ids:
			records.write(id + ',' + '\n')

def check_nrec(rec_ids,new_ids):
	#Will return an updated list of recorded ids  and a list of added ids given a list of new ids
	nrec_ids = []

	for id in new_ids:
		if id not in rec_ids:
			rec_ids.append(id)
			nrec_ids.append(id)
	return(rec_ids,nrec_ids)

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