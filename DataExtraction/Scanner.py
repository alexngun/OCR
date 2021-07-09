#%%
import pytesseract
import numpy as np
import os
from pdf2image.pdf2image import convert_from_path

#%%
""""
pdfScanner: Scan all files with extension '.pdf' in a given directory.
"""
class pdfScanner:

    def __init__(self, directory:str) -> None:

        self.dir = directory
        self.invoices = []
        self.__load_pdf()

    def __load_pdf(self) -> None:

        """""
        Load all pdf invoices from a directory
        mulitple pages of invoice is allowed
        """

        for file in os.listdir(self.dir):
            if file.endswith('.pdf'):

                pages = []
                doc = convert_from_path(self.dir + '/' + file, dpi=350)

                for page in doc:
                    pages.append(page)
                
                self.invoices.append(pages)

    def extract_text(self) -> list:

        """""
        Pytesseract Guide 

        --psm N
           Set Tesseract to only run a subset of layout analysis and assume a certain form of
           image. The options for N are:

               0 = Orientation and script detection (OSD) only.
               1 = Automatic page segmentation with OSD.
               2 = Automatic page segmentation, but no OSD, or OCR.
               3 = Fully automatic page segmentation, but no OSD. (Default)
               4 = Assume a single column of text of variable sizes.
               5 = Assume a single uniform block of vertically aligned text.
               6 = Assume a single uniform block of text.
               7 = Treat the image as a single text line.
               8 = Treat the image as a single word.
               9 = Treat the image as a single word in a circle.
               10 = Treat the image as a single character.

       --oem N
           Specify OCR Engine mode. The options for N are:

               0 = Original Tesseract only.
               1 = Neural nets LSTM only.
               2 = Tesseract + LSTM.
               3 = Default, based on what is available.

        """

        texts = []

        for invoice in self.invoices:
            text = ''
            for page in invoice:
                img = np.array(page)
                custom_config = r'--oem 3 --psm 4'
                text += pytesseract.image_to_string(img, config=custom_config)
            texts.append(text)

        return texts
