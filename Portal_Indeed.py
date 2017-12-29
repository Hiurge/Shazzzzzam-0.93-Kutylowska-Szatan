import re

indeed_dict = {
	"model" : "indeed",
	"base_url" : 'https://www.indeed.com',
	"job_sep" : "+",
	"loc_sep" : "+",
	"final_sep" : ["/jobs?q=",'%22','&l='], #3th sep is for no-loc
	"mod_page_nr" : 1,
	"mod_pages_nr" : 10,
	"my_numberpage_mod" : '&start=',
	"id_results" : 'resultsCol',
	"tags_mod" : ['a']
}
# offer_info_list = []
def count_num_pages_INDEED(soup):
	if soup.find(id = 'searchCount'):
		jobs_number = soup.find(id = 'searchCount').string.encode('utf-8')
		jobs_number = jobs_number.decode('utf-8') 
		jobs_number = re.findall('\d+', jobs_number) 
		pass
	else:
		print("Zero results on INDEED.")
		return
	if len(jobs_number) > 3: 
		jobs_total = (int(jobs_number[2])*1000) + int(jobs_number[3])
	elif len(jobs_number) == 2: 
		jobs_total = int(jobs_number[1]) 
	elif len(jobs_number) == 0: 
		print("Zero results on INDEED.") 
		return
	else: jobs_total = int(jobs_number[2]) # tu cos jest
	num_pages = round(jobs_total/10)
	return [num_pages, jobs_total]

def INDEED_get_links_to_all_sub_pages(tags,location):
	from Init import offer_info_list
	for tag in tags: 
		scraps = re.findall('/rc/clk\?jk=.*&amp;fccid=.*?.*title=".*">.*</a>', str(tag))
		if scraps: 
			my_job = re.findall('/rc/clk\?jk=.*&amp;fccid=.*?.*title="(.*)">.*</a>', str(scraps))
			my_offer = re.findall('/rc/clk.*?"', str(scraps))
			my_offer = (indeed_dict["base_url"] + str(my_offer[0]))[0:-1]
			offer_salary = [" ", " "]
			if location == None:
				location = "all USA"
			offer_info_list.append([my_offer,my_job[0], location, offer_salary])