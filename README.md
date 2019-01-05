# tex2csv
Python script for convert LaTeX to TSV. By set the converted TSV file into Google Spreadsheet, you can check per one sentence.

## Environment
- Python 3.6.5

## Usage
1. Install requirements.
```
pip install -r requirements.txt
```

2. Convert LaTeX file to TSV file.
```
python tex2tsv.py input_file.tex output_file.tsv
```

3. Import output.tsv Google Spread Sheet. Set Column D `=GOOGLETRANSLATE(B*,"en","ja")` and set Column E `=COUNTA(SPLIT(B*, " "))`. Check translated sentences in your native language. Fix sentences.
![GoogleSpreadSheet](https://github.com/chike0905/tex2tsv/blob/images/google.png)

4. Download fixed spread sheet as TSV file. Convert TSV file to LaTeX file.
```
python tex2tsv.py fixed_tsv.tsv output_file.tex
```
