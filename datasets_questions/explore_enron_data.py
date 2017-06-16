#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# key = next(iter(enron_data))
# features = 0
# for value in enron_data[key]:
# 	features+=1
# print("Features = ",features)
# poi = 0
sal=0
total=0
for key in enron_data:
	
	if enron_data[key]['poi']:
		total+=1
		if enron_data[key]['total_payments'] == 'NaN':
			sal+=1	
	# if enron_data[key]['email_address'] != 'NaN':
	# 	email+=1	
# percentage = float(sal)/total
#total+=10
#sal+=10
#print('Sal =',sal)
#print('total =',total)
#percentage = round(percentage*100,2)

# print('Percentage =',percentage )
# print('Email =',email)

print enron_data['LAY KENNETH L']
