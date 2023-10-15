import pytesseract
import cv2

# Read the image
image = cv2.imread("card.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save the image to disk
cv2.imwrite('preprocessed_card.jpg', thresh)

# Perform OCR
text = pytesseract.image_to_string('preprocessed_card.jpg')

# Print extracted text
print(text)

# Split text into lines and then words
lines = text.strip().split('\n')
words = [line.split() for line in lines]

print(words)

