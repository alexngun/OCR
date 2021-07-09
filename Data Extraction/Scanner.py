#%%
try:
    import pytesseract
except ImportError:
    raise ImportError('pytesseract is not installed.')

try:
    import pdf2image
except ImportError:
    raise ImportError('pdftoimage is not installed')

import cv2
import numpy as np
from PIL import Image
import os

from pdf2image.pdf2image import convert_from_path

#%%
class pdfScanner:

    def __init__(self, directory:str) -> None:

        self.dir = directory
        self.pics = []
        self.__load_pdf()

    def __load_pdf(self):

        for file in os.listdir(self.dir):
            if file.endswith('.pdf'):

                pic = []
                doc = convert_from_path(self.dir + '/' + file, dpi=300)

                for page in doc:
                    pic.append(page)
                
                self.pics.append(pic)

            



# %%
