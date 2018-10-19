import json
import nltk
import re

f = open("1.json","r")

data = []

for line in f :
    data.append(json.loads(line).get("content"))

# Lower the characters
data[0] = data[0].lower()


#Q1 remove all non-alphacharacters except spaces
rule = re.compile("[^a-z ]")
data[0] = rule.sub('',data[0])

#Q2 remove all words within 3 characters
rule = re.compile(r"\b\w{1,3}\b")
data[0] = rule.sub('', data[0])

#Q3 remove numbers that are fully made of digits
#rule = re.compile(r"")
print(data[0])
