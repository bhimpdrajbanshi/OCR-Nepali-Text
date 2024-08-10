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