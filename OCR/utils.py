# Build a pipeline for OCR

import cv2 
import pytesseract
import numpy as np

from PIL import Image
from doctr.io import DocumentFile



def preprocess(image):
    # Apply grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # save image
    # cv2.imwrite('gray.jpg', gray)

    # # Apply thresholding to convert the image to black and white
    # _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # # Noise Removal
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))

    # cleaned_image = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # # cv2.imwrite("cleaned_image.jpg", cleaned_image)

    # Apply adaptive thresholding to binarize the image (making text more distinct)
    binary_image = cv2.adaptiveThreshold(
        gray, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    # cv2.imwrite("binary_image.jpg", binary_image)
    # Sharpening the image (to enhance black letters)
    # Create a sharpening kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                [-1,  9, -1],
                                [-1, -1, -1]])

    sharpened_image = cv2.filter2D(binary_image, -1, sharpening_kernel)
    # cv2.imwrite("sharpened_image.jpg", sharpened_image)
    # Optionally, apply dilation to make the text thicker and more prominent
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    dilated_image = cv2.dilate(sharpened_image, kernel, iterations=1)

    # cv2.imwrite("dilated_image.jpg", dilated_image)

    return gray

def perform_ocr(image):
    # perform ocr on the image
    # text = pytesseract.image_to_string(image)
    predictor = ocr_predictor(pretrained=True)
    text = DocumentFile.from_images(image).predict(
        predictor
    )
    return text                     


def postprocess(text):
    
    #remove noise
    cleaned_text = text.replace('\n', ' ').strip()

    return cleaned_text
