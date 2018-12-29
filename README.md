# tex2csv
Python script for convert LaTeX to TSV. By set the converted TSV file into Google Spread sheet, you can use translate function per one sentence.

## Enviroment
- Python 3.6.5

## Usage
1. Install requirements.
```
pip install -r requirements.txt
```

2. Convert LaTeX file to TSV file.
```
python tex2tsv.py input_file.tex
```

3. Import output.tsv Google Spread Sheet. Set 3rd Column `GOOGLETRANSLATE` function. Check translate your native language. Fix sentences.
![GoogleSpreadSheet](https://github.com/chike0905/tex2tsv/blob/images/google.png)

4. Download fixed spread sheet as TSV file. Convert TSV file to LaTeX file.
```
python tex2tsv.py fixed_tsv.tsv
```
