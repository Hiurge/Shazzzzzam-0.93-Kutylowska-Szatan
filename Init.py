from bs4 import BeautifulSoup 
import urllib.request, urllib.parse, urllib.error 
import re 
import pandas as pd
import sys 

from my_words import my_words
from Harvester import *
from Portal_Pracuj import pracuj_dict
from Portal_Reed import reed_dict
from Portal_Indeed import indeed_dict 
from Raport_gen import *

OFFER_LIMIT = 20 # Per each website, so 100 = 300 for 3 sites. Set to 9999999 for no limit, but for now it can take long might crash here and there.

us_job = "python remote"	#'deep learning python'
us_location = "Texas"

uk_job = 'python remote'
uk_location = "London"

pl_job = 'python'
pl_location = "Wroclaw"


input_info = [[uk_job, uk_location], [us_job, us_location], [pl_job, pl_location]]
dict_list = [reed_dict,indeed_dict, pracuj_dict]


offer_info_list = [] 
magic_number = 0
for portal_dict in dict_list:
	job = input_info[magic_number][0]
	location = input_info[magic_number][1]
	final_url = set_url_info(location, job, portal_dict)
	soup = get_into_portal(final_url)
	My_words = my_words # 100 + words
	My_fixed_columns = ["Job name","Link","Location", "Salary min", "Salary max", "Portal"]
	df, my_columns = create_dataframe(My_words, My_fixed_columns)
	if portal_dict["model"] == "indeed": pages_jobs = count_num_pages_INDEED(soup)
	if portal_dict["model"] == "reed": pages_jobs = count_num_pages_REED(soup)
	if portal_dict["model"] == "pracuj": pages_jobs = count_num_pages_PRACUJ(soup)
	main_get_links_to_all_sub_pages(pages_jobs, final_url, portal_dict, OFFER_LIMIT, location)
	offer_cleaner_and_loader(offer_info_list, df, portal_dict, OFFER_LIMIT)
	offer_info_list = []
	magic_number += 1

for each in offer_with_full_data_list:
	df = df.append(pd.Series(each, index=my_columns), ignore_index=True)

df.to_csv('Pulpit/Shazzzzzam/Shazzzzzam_data.csv', sep=",")
print(df)


nr_of_positions = len(df.index)
raport_gen(nr_of_positions, df, input_info)