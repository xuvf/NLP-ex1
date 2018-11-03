import json, nltk, re, time
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.util import ngrams
from collections import Counter



nltk.data.path.append('/modules/cs918/nltk_data/')
f = open("signal-news1.jsonl", 'r')

s = time.time()
#Read data into a list
data = []
data_string = ''
count = 0
with open('signal-news1.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line)["content"].lower())


def get_pos_tag(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag == "VBP" or tag == "VBZ":
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.ADJ

def check_pos(e):
    return e in pos_wordlist

def check_neg(e):
    return e in neg_wordlist

lemmatiser = WordNetLemmatizer()


data_list = []
trigram =[]
pos_wordlist = open("opinion-lexicon-English/positive-words.txt" , 'r').read().split('\n')
neg_wordlist = open("opinion-lexicon-English/negative-words.txt", 'r').read().split('\n')
pos_list = []
neg_list = []

for i in range(len(data)):

    #Question 1d: Remove all URLs
    data[i] =  re.sub(r'(http(s)?:\/\/)?[a-z0-9]+\.\S+', '', data[i])
    #Question 1a: Remove all non-alphanumeric characters(except spaces)
    data[i] = re.sub(r'[^A-Za-z0-9]+', ' ', data[i])

    #Question 1b: Remove character with size 1
    data[i] = re.sub(r'\W*\b\D{1}\b', ' ', data[i])

    #Question 1c: Remove digit only character
    data[i] = re.sub(r'\b[\d]*\b', '', data[i])


    #Question 2: Lemmatise all words
    data[i] = list(map(lambda x: lemmatiser.lemmatize(x[0], get_pos_tag(x[1])),pos_tag(word_tokenize(data[i]))))

    #Part B
    #Question 1: Compute N number of tokens and V vocabulary size
    data_list.extend(data[i])
    
    
    #Question 2: Find the top 25 Trigrams
    trigram.extend(list(ngrams(data[i], 3)))

    #Question 3: Find the number of positive words list and negative words list
    pos_count = 0
    neg_count = 0
    for n in data[i]:
        if n in pos_wordlist:
            pos_count += 1
        elif n in neg_wordlist:
            neg_count += 1
        else:
            continue
    pos_list.append(pos_count)
    neg_list.append(neg_count)


N = len(data_list)
V = len(set(data_list))
trigram_top25 = []
for i in Counter(trigram).most_common(25):
    trigram_top25.append(i[0])
pos_count = sum(pos_list)
neg_count = sum(neg_list)
#Question 4: Compute the number of news stories with positve and negative words
more = 0
less = 0
for i in range(len(data)):
    if (pos_list[i] > neg_list[i]):
        more += 1
    elif (pos_list[i] < neg_list[i]):
        less += 1
    else:
        continue

#Part C
# Question 1: Training data and find the 10 most likely word
trigram_base = []
for i in range(16000):
    trigram_base,extend(list(ngrams(data[i], 3)))

snetence = ['is', 'this']
for i in range(10):
    trigram_list = []
    for t in trigram_base:
        if t[0] == sentence[-2] and t[1] == sentence[-1]:
            trigram_list.append(t)
        sentence.append(Counter(trigram_list).most_common()[0][0][-1])
sentence = ' '.join(sentence)

#Question 2: Compute perplexity

        
e = time.time()
print(e-s)


