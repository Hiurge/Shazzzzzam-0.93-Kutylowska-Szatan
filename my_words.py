Cash_universal = {"salary" : 0, "per day" : 0, "per month" : 0, "per annum" : 0, "money" : 0}
Cash_Gold = {"brutto" : 0,"netto" : 0,"pln" : 0}
Cash_Dollars = {"usd" : 0}
Cash_Pounds = {"pound" : 0,}
Cash_Euro = {"euro" : 0}

Data_bases = {
"sql" : 0, "nosql" : 0, "psql" : 0,
"mongodb" : 0, "maria" : 0, "hbase" : 0, "couchdb" : 0, "cassandra" : 0, "druid" : 0, "memcachedb" : 0,
"aws" : 0, "azure" : 0,
"hive" : 0, "spark" : 0, "hadoop" : 0, "flink" : 0, "hbase" : 0, "pytorch" : 0,}
			
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
"spss" : 0, "excel" : 0, "tableau" : 0, "sas" : 0, "d3.js" : 0}
			
Education = {"masters" : 0, "phd" : 0, "bachelor" : 0, "bs in" : 0,"degree" : 0, "certificat" : 0}

Python_libs = {"numpy" : 0, "thenao" : 0, "keras" : 0, "scikit" : 0, "pandas" : 0, "bokken" : 0, "seaborn" : 0, "matplotlib" : 0,
"bs4" : 0, "beautiful soup" : 0, "django" : 0, "puppet" : 0, "flask" : 0,
"tensorflow" : 0, "tf" : 0}

Dev = {
"test" : 0,"debug" : 0, "unit test" : 0, 
"jinja" : 0,"mako" : 0, 
"git" : 0,"mercurial" : 0, "svn" : 0, "jira" : 0, "grunt" : 0,
"html" : 0,"css" : 0, "frontend" : 0,
"orm" : 0,"object relational mapper" : 0, "rest" : 0}

Programming_languages = {
"python" : 0, "r" : 0, "javascript" : 0, "ruby" : 0, "matlab" : 0,
"c++" : 0, "c#" : 0, "java" : 0, ".net" : 0, "scala" : 0, "pearl" : 0}

Other_keywords = {"kaggle" : 0, "scraping" : 0, "metrics" : 0,"consult" : 0, "project management" : 0, 

"blockchain" : 0, "security":0, "vr":0,"ar":0,"augmented":0, "chatbot":0, "automation":0,"conversational interface":0, }

Remote = {"zdalna" : 0, "zdalnie" : 0, "remote" : 0,}

my_words = {**Remote, **Cash_universal, **Cash_Gold, **Cash_Dollars,  **Cash_Pounds, **Cash_Euro, **Data_bases, **Education, **Deep_statistics, **Education, **Python_libs, **Dev, **Programming_languages, **Other_keywords}


