import nltk
import sys
import pandas as pd

args = sys.argv

tex_data = open(args[1], "r")

output = pd.DataFrame()

tmp_sentence = []
tmp_verbs = []
for line in tex_data:
    sentences = nltk.sent_tokenize(line)
    if sentences == []:
        tmp_sentence.append(None)
        tmp_verbs.append(None)
    else:
        for sentence in sentences:
            tmp_sentence.append(sentence)
            words = nltk.word_tokenize(sentence)
            words = nltk.pos_tag(words)
            verbs = ""
            for word in words:
                if word[1][:2] == "VB":
                    verbs += word[0] + ", "
            tmp_verbs.append(verbs)

output["source"] = tmp_sentence
output["verbs"] = tmp_verbs
output["translate"] = [None for a in range(0,len(tmp_sentence))]

output.to_csv(args[2], sep='\t')

tex_data.close()
