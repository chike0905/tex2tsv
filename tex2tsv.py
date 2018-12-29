from nltk.tokenize import sent_tokenize
import sys
import pandas as pd

args = sys.argv

tex_data = open(args[1], "r")

output = pd.DataFrame()

tmp_sentence = []
for line in tex_data:
    sentences = sent_tokenize(line)
    if sentences == []:
        tmp_sentence.append(None)
    for sentence in sentences:
        tmp_sentence.append(sentence)

output["source"] = tmp_sentence
output["translate"] = [None for a in range(0,len(tmp_sentence))]

output.to_csv(args[2], sep='\t')

tex_data.close()
