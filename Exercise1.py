import json, nltk, re, time
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag


nltk.data.path.append('/modules/cs918/nltk_data/')
f = open("1.json", 'r')

s = time.time()
#Read data into a list
data = []
for line in f:
    data.append(json.loads(line))

def get_pos_tag(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

lemmatiser = WordNetLemmatizer()

for  i in range(len(data)):
#Convert data to readable json
#Lowecasing all text
    data[i] = data[i]["content"].lower()

	
#PART A

#Question 1d: Remove all URLs
    data[i] = re.sub(r'(www\.|http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?', ' ', data[i])

#Question 1a: Remove all non-alphanumeric characters(except spaces)
    data[i] = re.sub(r'[^A-Za-z0-9]+', ' ', data[i])

#Question 1b: Remove character with size 1
    data[i] = re.sub(r'\W*\b\w{1}\b', '', data[i])

#Question 1c: Remove digit only character
    data[i] = re.sub(r'\b[\d]*\b', '', data[i])

#Question 2: Lemmatise all words	
    data[i] = ' '.join(list(map(lambda x: lemmatiser.lemmatize(x[0], get_pos_tag(x[1])),pos_tag(word_tokenize(data[i])))))


#Part B

#Question 1: compute N number of tokens and V vocabulary size
N = sum(list(map(lambda x: len(word_tokenize(x)),data)))

v_list = list(map(lambda x: word_tokenize(x),data))

v =[]

for i in v_list:
    v.extend(i)
v = set(v)
v = len(v)

print(N)
print(v)
e = time.time()
print(e-s)


