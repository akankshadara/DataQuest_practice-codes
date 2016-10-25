import pandas as pd
import numpy
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
# print (all_ages.head(5))

# summarizing major categories
# All values for Major_category
print(all_ages['Major_category'].value_counts().index)

all_ages_major_categories = dict()
recent_grads_major_categories = dict()

def calculate_totals(file):
	majors_list = file["Major_category"].value_counts().index
	category_count = dict()
	for m in majors_list:
		list_m = file[file["Major_category"] == m]
		total = list_m["Total"].sum(axis = 0)
		category_count[m] = total
	return category_count



all_ages_major_categories = calculate_totals(all_ages)
recent_grads_major_categories = calculate_totals(recent_grads)

print all_ages_major_categories
# using pivot tables
all_ages_major_categories = all_ages.pivot_table(index = "Major_category", values = "Total", aggfunc = sum)
print all_ages_major_categories


recent_grads_major_categories = recent_grads.pivot_table(index = "Major_category", values = "Total", aggfunc = sum)
print recent_grads_major_categories

# Use the Low_wage_jobs and Total columns to calculate the 
# proportion of recent college graduates that worked low wage jobs 
low_wage_percent = 0.0
total_low_wage_jobs = recent_grads["Low_wage_jobs"].sum(axis = 0)
total_jobs = recent_grads["Total"].sum(axis = 0)
low_wage_percent = total_low_wage_jobs/total_jobs

print(low_wage_percent)


# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index
print majors
recent_grads_lower_unemp_count = 0
all_ages_lower_unemp_count = 0

for m in majors:
	x = all_ages[all_ages["Major_category"] == m]
	y = recent_grads[recent_grads["Major_category"] == m]
	a = x['Unemployment_rate'].values[0]
	r = y['Unemployment_rate'].values
	if(a>r):
		all_ages_lower_unemp_count += 1
	elif(a<r):
		recent_grads_lower_unemp_count += 1


# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_unemp_count = 0
all_ages_lower_unemp_count = 0
for m in majors:
    recent_grads_row =  recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    
    recent_grads_unemp_rate = recent_grads_row['Unemployment_rate'].sum()
    all_ages_unemp_rate = all_ages_row['Unemployment_rate'].sum()
    
    if recent_grads_unemp_rate < all_ages_unemp_rate:
        recent_grads_lower_unemp_count += 1
    elif all_ages_unemp_rate < recent_grads_unemp_rate:
        all_ages_lower_unemp_count += 1
	 
print all_ages_lower_unemp_count
print recent_grads_lower_unemp_count
