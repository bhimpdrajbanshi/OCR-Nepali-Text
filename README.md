

1.How to Use
Upload Your Image:

Upload the image from which you want to extract text. For example, an image named nagirikta.png.

Script to Extract Text:

Use the following script to extract text from the image:

Below is the image (nagirikta.png) used for OCR:















# Nepali OCR with EasyOCR

This project provides a simple script to extract text from images using EasyOCR, specifically designed for the Nepali language.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Output](#Output)

## Introduction

This project provides a simple script to extract text from images using EasyOCR, specifically designed for the Nepali language.

## Getting Started

### Prerequisites

To get started, ensure you have the following installed:

- pip install easyocr
- import matplotlib.pyplot as plt
- import cv2
- from pylab import rcParams
- from IPython.display import Image

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bhimpdrajbanshi/OCR-Nepali-Text.git
    ```


2. script:

    ```bash
    import easyocr
    import matplotlib.pyplot as plt
    from PIL import Image

    # Initialize the EasyOCR reader with Nepali language
    reader = easyocr.Reader(['ne'])

    # Read the text from the image
    result = reader.readtext('nagirikta.png')

    # Extract the text into a simple list
    extracted_text = [item[1] for item in result]

    # Print the result as a list of texts
    print(extracted_text)

    # Optionally, display the image
    img = Image.open('nagirikta.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    ```


## Sample documents in Nepali
1. Output
After running the script, the extracted text will be printed as a list of strings.

Example output:
['नेपाली नागरिकता प्रमाणपत्र', 'नाम: राम बहादुर', 'ठेगाना: काठमाण्डौ']


## sample image
https://nagarikapp.gov.np/img/citizenship.ec93c799.png