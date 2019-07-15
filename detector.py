import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import cPickle as c

def load(clf_file):
    with open (clf_file) as fp:
        clf = c.load(fp)
    return (clf)

def make_dict ():
    direc = "emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files]

    words = []
    c = len(emails)
    for email in emails:
        f = open(email)
        blob = f.read()
        words += blob.split(" ")
        print (c)
        c-=1
    for i in range (len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary [""]
    return (dictionary.most_common(3000))

clf = load ("text_classifier.mdl")
d = make_dict()

while True:
    features = []
    inp =""

    inp = raw_input(">").split()
    if inp =="exit":
        break
    for word in d:
        features.append(inp.count(word[0]))

    res = clf.predict([features])

    print ["NOT SPAM", "SPAM"][res[0]]
