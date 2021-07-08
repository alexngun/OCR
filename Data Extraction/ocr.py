#%%
import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
dir = "Demo Invoices/"
img = cv2.imread(dir+"invoice2.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
processed_img = cv2.adaptiveThreshold(gray_img, 
                                           255, 
                                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                           cv2.THRESH_BINARY, 
                                           91, 
                                           11)

text = pytesseract.image_to_string(processed_img, config="--psm 3")
print(text)

# %%
