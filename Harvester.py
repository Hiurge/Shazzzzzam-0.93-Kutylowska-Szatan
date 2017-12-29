from bs4 import BeautifulSoup 
import urllib.request, urllib.parse, urllib.error 
import re 
import pandas as pd
import sys 
from my_words import my_words 
from Portal_Pracuj import *
from Portal_Reed import *
from Portal_Indeed import *

def set_url_info(location, job, portal_dict):
	job = job.split()
	job = portal_dict["job_sep"].join(word for word in job)
	base_url = portal_dict["base_url"] + portal_dict["final_sep"][0]
	if location is not None:
		location = location.split()
		location = portal_dict["loc_sep"].join(word for word in location)
		if portal_dict["model"] == "reed": final_url = base_url + location + portal_dict["final_sep"][1] + job
		if portal_dict["model"] == "pracuj": final_url = base_url + job + portal_dict["final_sep"][1] + portal_dict["final_sep"][2]  + location + portal_dict["final_sep"][3]
		if portal_dict["model"] == "indeed": final_url = base_url + portal_dict["final_sep"][1] + job + portal_dict["final_sep"][1] + portal_dict["final_sep"][2] + location
	else:
		if portal_dict["model"] == "reed": final_url = base_url + job
		if portal_dict["model"] == "pracuj": final_url = base_url + job + portal_dict["final_sep"][1]
		if portal_dict["model"] == "indeed": final_url = base_url + job + portal_dict["final_sep"][2]
	return final_url

def get_into_portal(final_url):
	html = urllib.request.urlopen(final_url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

# For info from portals get_links_to_all_sub_pages:
# offer_info_list = []
def main_get_links_to_all_sub_pages(pages_jobs, final_url, portal_dict, OFFER_LIMIT, location):
	for nr in range(0,pages_jobs[0]+portal_dict["mod_page_nr"]): #doreguluj. bazowo: 1,+1. nie lapie jak jest 1 job, 1 page, pytanie co jak zero itp
		if nr > OFFER_LIMIT:
			break
		else:
			nr += 1
			my_page = ''.join([final_url, portal_dict["my_numberpage_mod"], str(nr*portal_dict["mod_pages_nr"])])
			html_page = urllib.request.urlopen(my_page).read()
			tags = BeautifulSoup(html_page, 'html.parser') 
			tags = tags.find(id=portal_dict["id_results"])
			if len(portal_dict["tags_mod"]) <= 1:
				tags = tags(portal_dict["tags_mod"][0]) 
			else: 
				tags = tags.findAll(portal_dict["tags_mod"][0], {portal_dict["tags_mod"][1] : portal_dict["tags_mod"][2]})
			if portal_dict["model"] == "reed": REED_get_links_to_all_sub_pages(tags)
			if portal_dict["model"] == "pracuj": PRACUJ_get_links_to_all_sub_pages(tags)
			if portal_dict["model"] == "indeed": INDEED_get_links_to_all_sub_pages(tags,location)

def create_dataframe(My_words, My_fixed_columns):
	my_columns = []
	for key, value in My_words.items() :
		my_columns.append(key)
	my_columns = My_fixed_columns + my_columns
	df = pd.DataFrame(columns=my_columns)
	return df, my_columns

# For info from offer_cleaner_and_loader:
offer_with_full_data_list = []
def offer_cleaner_and_loader(offer_info_list, df, portal_dict,OFFER_LIMIT):
	greedy_count = 0
	for number in range(len(offer_info_list)):
		if greedy_count > OFFER_LIMIT:
			break
		else:
			greedy_count += 1
			offer_url = portal_dict["base_url"] + offer_info_list[number][0]
			if portal_dict["model"] == "indeed":
				offer_url = offer_info_list[number][0]
			My_infos = {"Job name" : offer_info_list[number][1],
						"Link" : offer_url,
						"Location" : offer_info_list[number][2],
						"Salary min": offer_info_list[number][3][0],
						"Salary max": offer_info_list[number][3][1],
						"Portal" : portal_dict["model"]}		
			Cash_universal = {
			"salary" : 0, "per day" : 0, "per month" : 0, "per annum" : 0, "money" : 0,
			}

			Cash_Gold = {
			#PolskieStawki
			"brutto" : 0,"netto" : 0,"pln" : 0,
			}

			Cash_Dollars = {
			#Amerykanskie stawki:
			"usd" : 0
			}

			Cash_Pounds = {
			#Amerykanskie stawki:
			"pound" : 0,
			}

			Cash_Euro = {
			#Amerykanskie stawki:
			"euro" : 0
			}

			Data_bases = {
			"sql" : 0, "nosql" : 0, "psql" : 0,
			"mongodb" : 0, "maria" : 0, "hbase" : 0, "couchdb" : 0, "cassandra" : 0, "druid" : 0, "memcachedb" : 0,
			"aws" : 0, "azure" : 0,
			"hive" : 0, "spark" : 0, "hadoop" : 0, "flink" : 0, "hbase" : 0, "pytorch" : 0,
			}
			
			Deep_statistics = {
			#Stata, matma, machine learning, analiza danych
			"math" : 0, "statistic" : 0,
			"machine learning" : 0, "deep learning" : 0, "neural networks" : 0,
			"data" : 0, "analysis" : 0, "big data" : 0, "methodology" : 0,
			"data exploration" : 0, "exploratory" : 0, "data mining" : 0, "unstructured" : 0,"experiment" : 0,
			"large datasets" : 0,"quantitative analysis" : 0, "wrangl" : 0, "engineering" : 0,
			"algebra" : 0, "calculus" : 0, "visualisation" : 0, "presentation":0, "munging" : 0,
			"estimators" : 0, "data processing" : 0, "algorithm" : 0, "predictive" : 0,
			"decision trees" : 0,"information retrival" : 0, "descriptive" : 0, "bayes" : 0,
			"anova" : 0, "regression" : 0, "classification" : 0, "supervised" : 0, "unsupervised" : 0,
			"classifier" : 0, "clustering" : 0, "nltk" : 0, "nlp" : 0, "natural language" : 0,
			"decision tree" : 0, "data integration" : 0,
			"spss" : 0, "excel" : 0, "tableau" : 0, "sas" : 0, "d3.js" : 0, 
			}
			
			Education = {
			#Education:
			"masters" : 0, "phd" : 0, "bachelor" : 0, "bs in" : 0,
			"degree" : 0, "certificat" : 0,
			}

			Python_libs = {
			"numpy" : 0, "thenao" : 0, "keras" : 0, "scikit" : 0, "pandas" : 0, "bokken" : 0, "seaborn" : 0, "matplotlib" : 0,
			"bs4" : 0, "beautiful soup" : 0, "django" : 0, "puppet" : 0, "flask" : 0,
			"tensorflow" : 0, "tf" : 0,
			}

			Dev = {
			#Dev:
			"test" : 0,"debug" : 0, "unit test" : 0, 
			"jinja" : 0,"mako" : 0, 
			"git" : 0,"mercurial" : 0, "svn" : 0, "jira" : 0, "grunt" : 0,
			"html" : 0,"css" : 0, "frontend" : 0,
			"orm" : 0,"object relational mapper" : 0, "rest" : 0,
			}

			Programming_languages = {
			"python" : 0, "r" : 0, "javascript" : 0, "ruby" : 0, "matlab" : 0,
			"c++" : 0, "c#" : 0, "java" : 0, ".net" : 0, "scala" : 0, "pearl" : 0,
			}

			Other_keywords = {	
			#Others
			"kaggle" : 0, "scraping" : 0, "metrics" : 0,

			#Buissness:
			"consult" : 0, "documenting" : 0, "report" : 0, "project management" : 0
			}
			
			Remote = {	
			#Others
			"zdalna" : 0, "zdalnie" : 0, "remote" : 0,
			}
			Cash_words = {**Cash_universal, **Cash_Gold, **Cash_Dollars,  **Cash_Pounds, **Cash_Euro}
			my_words = {**Remote, **Cash_words, **Data_bases, **Education, **Deep_statistics, **Education, **Python_libs, **Dev, **Programming_languages, **Other_keywords}
			get_words_from_offer(offer_url, my_words, number, My_infos, portal_dict)

def get_words_from_offer(offer_url, my_words, number, My_infos, portal_dict):
	try: offer_html = urllib.request.urlopen(offer_url).read()
	except: return

	offer_soup = BeautifulSoup(offer_html, 'html.parser')
	for script in offer_soup(["script", "style"]):
		script.extract()
	text = offer_soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	def chunk_space(chunk):
		chunk_out = chunk + ' '
		return chunk_out
	text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line
	text = text.decode('utf-8')
	text = re.sub("[^A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ.+3]"," ", text)
	clean_offer_text = text.lower().split()
	List_words = set(clean_offer_text)
	for each in List_words:
		if each in my_words:
			my_words[each] = 1 
	My_infos['Link'] = '"' + My_infos['Link'] + '"'			# 	<3
	My_full_info = {**my_words, **My_infos}
	my_words = {}
	all_data_one_offer = pd.Series(My_full_info, name=("Offer_" + portal_dict["model"] + str(number)))
	offer_with_full_data_list.append(all_data_one_offer)
