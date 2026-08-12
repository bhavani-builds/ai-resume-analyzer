import fitz


# PDF file location
pdf_path = "resume.pdf"


# Open the PDF
document = fitz.open(pdf_path)


# Extract text from every page
full_text = ""

for page in document:
    text = page.get_text()
    full_text += text


# Close the PDF
document.close()


# Display extracted text
print("=" * 60)
print("EXTRACTED RESUME TEXT")
print("=" * 60)

print(full_text)


# Save the extracted text
with open(
    "resume_text.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(full_text)


print("\nText extraction completed!")
print("Saved as: resume_text.txt")
