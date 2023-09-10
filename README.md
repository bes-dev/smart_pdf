# SmartPDF

A simple python library for AI-powered PDF documents processing.

## Requirements

* Linux, Windows, MacOS
* Python 3.8.+
* OpenAI API Key

## Install package

```bash
pip install smart_pdf
```

## Install the latest version

```bash
git clone https://github.com/bes-dev/random_face.git
cd random_face
pip install -r requirements.txt
python download_model.py
pip install .
```

## Demo

```bash
python -m smart_pdf.smart_pdf --help
```

## Example

```python
from smart_pdf import SmartPDF
smart_doc = SmartPDF(
    path=<path_to_pdf>,
    openai_api_key=<openai_api_key>
)
print(smart_doc)
print(f"Summary: {smart_doc.summary()}")
print("Press q! to exit")
while True:
    request = input("> ")
    if request == "q!":
        break
    print(smart_doc.smart_search(request))
```
