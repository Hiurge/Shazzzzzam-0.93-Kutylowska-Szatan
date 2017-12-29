from my_words import my_words

def raport_gen(nr_of_positions, df, input_info):
	all_rows_content = []
	html_string_mids = []
	for counter in range(0,nr_of_positions): # tu
		offer_row = df.iloc[counter:(counter+1),:]
	 
		offer_row_job = ((offer_row['Job name'].values)[0]).capitalize()
		offer_row_loc = ((offer_row['Location'].values)[0]).capitalize() 

		offer_row_salary = ((offer_row['Salary min'].values)[0] + " - " + (offer_row["Salary max"].values)[0])
		offer_row_link = str(((offer_row['Link'].values)[0])[1:-1])
		
		key_words_one_offer = []
		for column_name in offer_row.columns:
			if 1 in offer_row[column_name].values:
				key_words_one_offer.append(column_name)

		project_words = {	
		# Project keywords:
		"iot" : 0, "internet of things" : 0,"nlp" : 0, "natural language processing" : 0, "cryptography" : 0, "genetics" : 0, 
		"machine learning" : 0, "deep learning" : 0, "artificial intelligence" : 0,
		"big data" : 0, "social science" : 0, "neuro" : 0, "psychology" : 0,  "neural networks" : 0,
		 "biznes intelligence" : 0, "cnn" : 0,
		#Buissness:
		"consult" : 0, "management" : 0,
		"blockchain" : 0, "security":0, "vr":0,"ar":0,"augmented":0, "chatbot":0, "automation":0,"conversational interface":0,
		
		"numpy" : 0, "thenao" : 0, "keras" : 0, "scikit" : 0, "pandas" : 0, "bokken" : 0, "seaborn" : 0, "matplotlib" : 0,
		"bs4" : 0, "beautiful soup" : 0, "django" : 0, "puppet" : 0, "flask" : 0,
		"tensorflow" : 0, "tf" : 0, "nltk" : 0,
		}

		technology_words_1 = {	
		# Technology keywords:
		"sql" : 0, "nosql" : 0, "psql" : 0,
		"mongodb" : 0, "maria" : 0, "hbase" : 0, "couchdb" : 0, "cassandra" : 0, "druid" : 0, "memcachedb" : 0,
		"aws" : 0, "azure" : 0,
		"hive" : 0, "spark" : 0, "hadoop" : 0, "flink" : 0, "hbase" : 0, "pytorch" : 0,

		"math" : 0, "statistic" : 0,
		 
		"data" : 0, "analysis" : 0, "methodology" : 0,
		"data exploration" : 0, "exploratory" : 0, "data mining" : 0, "unstructured" : 0,"experiment" : 0,
		"large datasets" : 0,"quantitative analysis" : 0, "wrangl" : 0, "engineering" : 0,
		"algebra" : 0, "calculus" : 0, "visualisation" : 0, "presentation":0, "munging" : 0,
		"estimators" : 0, "data processing" : 0, "algorithm" : 0, "predictive" : 0,
		"decision trees" : 0,"information retrival" : 0, "descriptive" : 0, "bayes" : 0,
		"anova" : 0, "regression" : 0, "classification" : 0, "supervised" : 0, "unsupervised" : 0,
		"classifier" : 0, "clustering" : 0, "nltk" : 0, 
		"decision tree" : 0, "data integration" : 0,
		"spss" : 0, "excel" : 0, "tableau" : 0, "sas" : 0, "d3.js" : 0, 


		}

		technology_words_2 = {
		"test" : 0,"debug" : 0, "unit test" : 0, 
		"jinja" : 0,"mako" : 0, 
		"mercurial" : 0, "svn" : 0, "jira" : 0, "grunt" : 0,
		"css" : 0, "frontend" : 0,
		"orm" : 0,"object relational mapper" : 0, "rest" : 0,
		}

		Remote = {"zdalna" : 0, "zdalnie" : 0, "remote" : 0}

		Cash_universal = {"salary" : 0, "per day" : 0, "per month" : 0, "per annum" : 0, "money" : 0}
		Cash_Gold = {"brutto" : 0,"netto" : 0,"pln" : 0}
		Cash_Dollars = {"usd" : 0}
		Cash_Pounds = {"pound" : 0,}
		Cash_Euro = {"euro" : 0}
		Cash_words = {**Cash_universal, **Cash_Gold, **Cash_Dollars,  **Cash_Pounds, **Cash_Euro}
		

		keys_remote = []
		keys_technology_words_1 = [] 
		keys_technology_words_2 = []
		keys_project_words = []
		keys_cash_words = []
		for each in key_words_one_offer:
			if each in Remote:
				keys_remote.append(each) 
			if each in technology_words_1: 
				keys_technology_words_1.append(each) 
			if each in technology_words_2: 
				keys_technology_words_2.append(each) 
			if each in project_words:  
				keys_project_words.append(each) 
			if each in Cash_words:  
				keys_cash_words.append(each) 
		if len(keys_remote) > 0:
	 		is_remote = "yes"
		else:
			is_remote = ""

		keys_project_words_ok = str(", ".join(keys_project_words))
		if len(keys_project_words_ok) > 0:
			keys_project_words_ok += ","
		keys_technology_words_1_ok = str(", ".join(keys_technology_words_1))
		if len(keys_technology_words_1_ok) > 0:
			keys_technology_words_1_ok += ","
		keys_technology_words_2_ok = str(", ".join(keys_technology_words_2))
		if len(keys_technology_words_2_ok) > 0: 
			keys_technology_words_2_ok += "," 

		# Set black words, put aside black words we don't want to see.
		black_dict = {"data" : 0, "engineering" : 0,"metrics" : 0,
			"masters" : 0, "phd" : 0, "bachelor" : 0, "bs in" : 0,
			"degree" : 0, "certificat" : 0, 
			"git" : 0, "report" : 0, 
			"html" : 0, "ruby" : 0, "scala" : 0, "pearl" : 0,
			"excel" : 0, "sas" : 0, "d3.js" : 0, "css" : 0}
		drop_words_list = [keys_project_words, keys_remote, keys_technology_words_1, keys_technology_words_2, Cash_words, black_dict]	
		for each in drop_words_list:
			key_words_one_offer = [item for item in key_words_one_offer if item not in each]	 
		offer_row_keywords_string = (", ".join(key_words_one_offer))
		if len(offer_row_keywords_string) > 0: offer_row_keywords_string += "."

		html_string_mid_temp = '''
				<tr onMouseOver="Context('context1', true)"
	                onMouseOut="Context('context1', false)">
					<td valign="top"><font size="2">''' + str(offer_row_loc) + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font size="2">''' + str(offer_row_salary) + '''</font></td>
					<th valign="top"><font size="2"></font></th> 
					<td valign="top"><font size="2">''' + str(is_remote) + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font color="black" size="2"><a href="''' + str(offer_row_link) + '''">''' + str(offer_row_job) + '''</a></font></td> 
					<th valign="top"<font size="2"></font></th> 
					<td valign="top">
					<font color="green" size="2">''' + str(keys_project_words_ok) + '''</font>
					<font color="blue" size="2">''' + str(keys_technology_words_1_ok) + '''</font>
					<font color="orange" size="2">''' + str(keys_technology_words_2_ok) + '''</font>
					<font size="2">''' + str(offer_row_keywords_string) + '''</font></td>
				</tr>'''

		html_string_mids.append(html_string_mid_temp)
		counter +=1
	for i in range(len(input_info)):	
		if input_info[i][1] == None:
			input_info[i][1] = "no localisation."

	my_search1 = "UK: " + input_info[0][0].capitalize() + " in " + input_info[0][1].capitalize() +"."
	my_search2 = "US: " + input_info[1][0].capitalize() + " in " + input_info[1][1].capitalize() +"."  
	my_search3 = "PL: " + input_info[2][0].capitalize() + " in " + input_info[2][1].capitalize() +"."
	
	html_string_open = '''
	<html>
		<head>
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
			<style>body{ margin:0 100; background:whitesmoke; }</style>
			<style>table>tbody>tr:hover{ padding: 20px; background-color: #ffa !important; border: 1px solid #ccc; border-collapse: collapse;}</style> 
		</head>
		<body onLoad="Context('context1', false); Context('context2', false);">
			<h1>Shazzzzzam!</h1>
			<p><font size="1">''' +"Results for "+my_search1+" "+my_search2+" "+my_search3 + '''</font></p>
			<br>
			<br>
			<table style="width:100%">
				<tr>
					<th style="min-width:90px"><font size="2">Place</font></th> 
					<th style="min-width:5px"><font size="2"></font></th>
					<th style="min-width:90px"><font size="2">Salary</font></th> 
					<th style="min-width:5px"><font size="2"></font></th>
					<th style="min-width:5px"><font size="2">Remote</font></th> 
					<th style="min-width:5px"><font size="2"></font></th>
					<th style="min-width:175px"><font size="2">Position</font></th> 
					<th style="min-width:5px"><font size="2"></font></th>
					<th><font size="2">Keywords</font></th>
				</tr>'''

	html_string_end = '''
			</table>
			<h3>Pozdrawiam.</h3>
		</body>
	</html>'''

	html_string_mid = "".join(html_string_mids)
	html_string = html_string_open + html_string_mid + html_string_end
	f = open('Pulpit/Shazzzzzam/Shazzzzzam_Report.html','w+')
	f.write(html_string)
	f.close()