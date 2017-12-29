import re

pracuj_dict = {
	"model" : "pracuj",
	"base_url" : 'https://www.pracuj.pl',
	"job_sep" : '%20',
	"loc_sep" : '-x44-%20',
	"final_sep" : ["/praca/", ";kw","/",";wp"], #3th sep is for no-loc
	"mod_page_nr" : 1,
	"mod_pages_nr" : 1,
	"my_numberpage_mod" : '?pn=',
	"id_results" : 'mainOfferList',
	"tags_mod" : ['a', 'class', 'o-list_item_link_name']
}
# offer_info_list = []
def count_num_pages_PRACUJ(soup):
	jobs_number = soup.findAll("span", { "class" : "o__search_results_title_number" })
	jobs_number = re.findall('">(.*).ofert.*</span>', str(jobs_number))
	if (len(str(jobs_number))) == 14:
		jobs_number = int(str(jobs_number)[2:3] + str(jobs_number)[-5:-2])
	elif (len(str(jobs_number))) == 15:
		jobs_number = int(str(jobs_number)[2:4] + str(jobs_number)[-5:-2])
	elif (len(str(jobs_number))) >= 16:
		print("There too much positions, not avaliable in alfa SkillScrapper. Program will break.")
		pass
	else:
		jobs_number = int(str(jobs_number[0]))
	pages_number = round(int(jobs_number)/50)
	return [pages_number, jobs_number] # Bug na 0 pozycji na pracuj

def PRACUJ_get_links_to_all_sub_pages(tags):
	from Init import offer_info_list
	for tag in tags:
		offer_link =  str(re.findall('href="(.*)".itemp', str(tag))[0]) #offer_nr = offer_link[-7:]
		offer_sep = re.findall('/praca/.*,(.*),.*',offer_link)[0]
		offer_job = re.findall("/(.*),oferta,", offer_link[6:])[0].split('-')
		offer_location = (offer_job[-1:])[0]
		offer_job = ' '.join(offer_job[0:-1]) 
		offer_salary = [" ", " "]
		offer_info = [offer_link, offer_job, offer_location, offer_salary]
		offer_info_list.append(offer_info)