# Optical Character Recognition - An OCR invoice reader

## Description
The process is powered by `pdf2image` and `pytesseract`. We load pdf file as an image data and feed in to `pytesseract`. 
`pytesseract` would recognize the text and then we can use regular expression to extract the key info from the text.
The regular expression template is stored in a `YAML` file.

## Simple invoice template

Here is a sample of a valid template

    issuer: ABC Company
    keywords:
      - ABC Company
    exclude_keywords:
      - Paid
    fields:
      amount: (?<=TOTAL\s\$)\d+?\.\d+\b
      date: (?<=DUE\sDATE\s)20[0-9][0-9]\/[0-1][0-9]\/[0-3][0-9]\b
      invoice_number: (?<=INVOICE\s\#\s)[A-Z]{3}\-[0-9]{4}
      
`issuer`, `keywords`, `exclude_keywords` and `fields` are required attributes of a valid template. 
`issuer` is defined at the time where the template is specifically written for a company.
`keywords` and `exclude_keywords` are also defined by users to help the computer to read the right invoices.
`fields` is the data that we want to extract. This should be written in a regular expression.

## Simple Demo

###### Import the modules
```
from DataExtraction.Regex import fieldExtractor
from DataExtraction.Scanner import pdfScanner
```

###### Set the directory where invoices and templates are located
```
pdf_dir = 'Demo Invoices/'
template_dir = 'DataExtraction/Templates/'
```

###### Convert pdf to text
```
ocr = pdfScanner(pdf_dir)
texts = ocr.extract_text()
```

###### Extract data from the text and save it as a `json` file
```
worker = fieldExtractor(template_dir, texts)
data = worker.fetch()
worker.save(data)
```

## Result `data.json`

    [
      {
        "invoice_number": [
          "TWA-1190"
        ],
        "amount": [
          "204.75"
        ],
        "date": [
          "2021/07/23"
        ]
      }
    ]
