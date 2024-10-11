import cv2
import os
from utils import preprocess, perform_ocr, postprocess
import numpy as np
from pdf2image import convert_from_path
from doctr.models import ocr_predictor


ocr_model = ocr_predictor(pretrained=True)

def process_image_with_doctr(image):
    # Preprocess the image
    clean_image = preprocess(image)

    # Ensure the image is in RGB format
    if len(clean_image.shape) == 2:  # If grayscale, convert to RGB
        image = cv2.cvtColor(clean_image, cv2.COLOR_GRAY2RGB)
    elif clean_image.shape[2] == 1:  # If single channel, convert to RGB
        image = cv2.cvtColor(clean_image, cv2.COLOR_BGR2RGB)

        # Convert image to a list since doctr expects a list of images
    images_list = [image]

    # Perform OCR
    result = ocr_model(images_list)
    extracted_text = result.render()  # Extract the text in string format
    return extracted_text


def ocr_pipeline(input_folder, output_folder):
    # if image path is not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_text=""
        print(f"file name: {file_name}")
        # check if input is image or pdf
        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):

            print("Processing image file")
            image = cv2.imread(input_path)
            text = process_image_with_doctr(image)
            output_text = postprocess(text)

        elif file_name.lower().endswith((".pdf")):

            print("Processing pdf file")
            images = convert_from_path(input_path)

            for i, page_text in enumerate(images):
                open_cv_image = cv2.cvtColor(np.array(page_text), cv2.COLOR_RGB2BGR)

                print(f"Processing page {i + 1}...")
                # Process each page as an image
                page_text = process_image_with_doctr(open_cv_image)
                output_text += f"Page {i + 1}:\n{page_text}\n\n"

        else:
            print("Invalid input file format.Please provide a valid image or PDF file.")

        # store output in txt file
        # Save the extracted text to a .txt file
        output_file = os.path.join(
            output_folder, f"{os.path.splitext(file_name)[0]}.txt"
        )
        print(f"{output_file=}")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(output_text)

        print(f"Text extracted and saved for: {file_name}")

if __name__ == "__main__":
    input_folder = "/home/fx/Desktop/akash/Study work/Study_work/OCR/input/"
    output_folder = "/home/fx/Desktop/akash/Study work/Study_work/OCR/output/"
    ocr_pipeline(input_folder,output_folder)
