import json
import nltk
import re
import datetime

#Start Timer
start_time = datetime.datetime.now()

f = open("signal-news1.jsonl","r")

data = []

for line in f :
    temp = json.loads(line).get("content")
    
    # Lower the characters
    temp = temp.lower()
    
    
    #Q4 remove all URLs
    rule = re.compile(r"http(s)?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]")
    temp = rule.sub('', temp)
    
    #Q1 remove all non-alphacharacters except spaces
    rule = re.compile("[^a-z0-9 ]")
    temp = rule.sub('',temp)
    
    #Q2 remove all words within 3 characters
    rule = re.compile(r"\b\w{1,3}\b")
    temp = rule.sub('', temp)
    
    #Q3 remove numbers that are fully made of digits
    rule = re.compile(r"([0-9]+ )")
    temp = rule.sub('', temp)
    
    temp = nltk.word_tokenize(temp)
    
    temp = nltk.pos_tag(temp)
    
    data.append(temp)

end_time = datetime.datetime.now()
interval = (end_time-start_time).seconds

print (interval)

print(data[6])