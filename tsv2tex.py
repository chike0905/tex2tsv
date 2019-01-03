from nltk.tokenize import sent_tokenize
import sys
import pandas as pd
import math

args = sys.argv

tsv_data = pd.read_csv(args[1], delimiter='\t')

out = ""
for row in tsv_data["source"]:
        if row != row:
            out = out[:-1]
            out += "\n\n"
        else:
            out += row + " "
            if row[-1] == "}":
                out += "\n"

output_tex = open(args[2], mode="a")
output_tex.write(out)
output_tex.close()
