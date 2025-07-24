from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
import pymupdf

def select_file():
    # Create a hidden Tkinter root window
    root = tk.Tk()
    root.withdraw() 

    # Open the file dialog and get the selected file path
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*"), ("Text files", "*.txt"), ("Python files", "*.py")]
    )

    # Check if a file was selected
    if file_path:
        print(f"Selected file: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None

# Call the function to open the file dialog
selected_file = select_file() 



def extract_text_from_pdf_pymupdf(selected_file):
    """
    Extracts all text from a PDF file using PyMuPDF (fitz).
    """
    doc = pymupdf.open(selected_file)
    extracted_text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        extracted_text += page.get_text()
    doc.close()
    return extracted_text

# Example usage:
# pdf_file = "your_document.pdf"
text = extract_text_from_pdf_pymupdf(selected_file)
# print(text)


language = "en"

obj = gTTS(text=text, lang=language, slow=False)

obj.save("sample.mp3")

#os.system("start sample.mp3")
