import re

reed_dict = {
	"model" : "reed",
	"base_url" : 'https://www.reed.co.uk',
	"job_sep" : "-",
	"loc_sep" : "+",
	"final_sep" : ["/jobs/jobs-in-","?keywords=", "/jobs?keywords="], #3th sep is for no-loc
	"mod_page_nr" : 2,
	"mod_pages_nr" : 1,
	"my_numberpage_mod" : '&cached=True&pageno=',
	"id_results" : 'server-results',
	"tags_mod" : ['article', 'class', 'job-result ']
}

# offer_info_list = [] 
def count_num_pages_REED(soup):
	checking_1 = soup.findAll("span", { "class" : "count h1 " })
	checking_2 = soup.findAll("span", {"class" : "count h1 is-hidden"})
	check = [str(checking_1), str(checking_1)]
	if "is-hidden" in str(check):
		jobs_number = soup.findAll("span", {"class" : "count h1 is-hidden"})
	else:
		jobs_number = soup.findAll("span", {"class" : "count h1 "})
	jobs_number = int("".join(str(jobs_number).split()[4].split(',')))
	pages_number = round(int(jobs_number)/25)
	return [pages_number, jobs_number]

def REED_get_links_to_all_sub_pages(tags):
	from Init import offer_info_list
	for tag in tags:
		offer_desc = tag.findAll("div", { "class" : "metadata" })
		offer_link = tag.findAll("a")
		offer_link = (re.findall('href="(.*)"></a>', str(offer_link)))[0]
		offer_job = re.findall('/jobs/(.*)/[0-9]', str(offer_link))
		offer_job = (" ".join(str(offer_job[0]).split("-")))
		offer_salary = re.findall('salary">(.*)</li>', str(offer_desc))
		if "-" in str(offer_salary):
			offer_salary_min = str(offer_salary).split("-")[0]
			offer_salary_max = str(offer_salary).split("-")[1]
		else:
			offer_salary_min = str(offer_salary)	
			offer_salary_max = str(offer_salary)
		offer_salary = [(re.sub("\D", "", offer_salary_min)), (re.sub("\D", "", offer_salary_max))]
		offer_location = str(re.findall('location">(.*)', str(offer_desc))[0])
		offer_info = [offer_link, offer_job, offer_location, offer_salary]
		offer_info_list.append(offer_info)