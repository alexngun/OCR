#%%
from DataExtraction.Regex import fieldExtractor
from DataExtraction.Scanner import pdfScanner

# %%
pdf_dir = 'Demo Invoices/'
template_dir = 'DataExtraction/Templates/'

ocr = pdfScanner(pdf_dir)
texts = ocr.extract_text()

#%%
worker = fieldExtractor(template_dir, texts)
data = worker.fetch()
worker.save(data)
# %%
