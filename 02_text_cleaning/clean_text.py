import re
from pathlib import Path


# Find the project folder
project_folder = Path(__file__).resolve().parent.parent


# Location of extracted resume text
input_file = (
    project_folder
    / "01_pdf_text_extraction"
    / "resume_text.txt"
)


# Read the extracted text
with open(
    input_file,
    "r",
    encoding="utf-8"
) as file:

    text = file.read()


print("=" * 60)
print("ORIGINAL RESUME TEXT")
print("=" * 60)

print(text)


# ------------------------------------------
# Clean the text
# ------------------------------------------

# Convert everything to lowercase
clean_text = text.lower()


# Remove email addresses
clean_text = re.sub(
    r'\S+@\S+',
    ' ',
    clean_text
)


# Remove website links
clean_text = re.sub(
    r'https?://\S+|www\.\S+',
    ' ',
    clean_text
)


# Remove special characters
clean_text = re.sub(
    r'[^a-z0-9\s]',
    ' ',
    clean_text
)


# Remove extra spaces
clean_text = re.sub(
    r'\s+',
    ' ',
    clean_text
).strip()


# ------------------------------------------
# Display cleaned text
# ------------------------------------------

print("\n" + "=" * 60)
print("CLEANED RESUME TEXT")
print("=" * 60)

print(clean_text)


# ------------------------------------------
# Save cleaned text
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "cleaned_resume.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(clean_text)


print("\n" + "=" * 60)
print("TEXT CLEANING COMPLETED")
print("=" * 60)

print(
    "Saved to:",
    output_file
)
