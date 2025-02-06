import os
import re

# Define the directory containing text files
text_dir = r"D:\Gen AI _ Feb Batch\Retail Product Support Chatbot\gen-ai-project\data\processed"

# Function to clean text
def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

# Loop through all text files in the directory
for file_name in os.listdir(text_dir):
    if file_name.endswith(".txt"):
        file_path = os.path.join(text_dir, file_name)

        # Read the text file
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Clean the text
        cleaned_text = clean_text(text)

        # Save the cleaned text back to the same file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print(f"Cleaned text saved: {file_path}")

print("All text files have been cleaned successfully.")


#### Testing git demo and pushing the latest updated file
