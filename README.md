# PyCollocation
Python module to do simple collocation analysis of a corpus.

## Requirements
Since we have implemented some tokenizer from `nltk.tokenize`, one needs to install the corresponding packages first.

```Python
import nltk
nltk.download('punkt')
```

# Tutorial

## CLI

You can use `PyCollocation` as via CLI. Example:

```bash
python3 analysis.py FOLDER SEARCH_TERM L_WINDOW R_WINDOW STATISTIC DOC_TYPE OUTPUT_FORMAT
```

```bash
python3 analysis.py /corpora "test" 3 3 freq folder print
```

### FOLDER

The relative path to the folder including the files to be analyzed.

### SEARCH_TERM

The search term. Can be a string or a regular expression.

### L_WINDOW

Window size left of the search term.

### R_WINDOW

Window size right of the search term.

### STATISTIC
The statistical measure for the analysis. Currently implemented:

- frequency
- MU
- z-score

### DOC_TYPE

The document type. Can be:

- a folder with documents (`folder`)
- a single document (`single`)
- some sort of iterable (`iterable`)

### OUTPUT_FORMAT
Can be:

- print to screen (`print`)
- create a csv `results.csv` (`csv`)

