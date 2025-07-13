import tkinter as tk
from tkinter import filedialog
import pyttsx3
import fitz  # PyMuPDF

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to select PDF and extract text
def select_pdf():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        text = extract_text(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

def extract_text(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text.strip()

def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    engine.setProperty('rate', rate_slider.get())
    engine.setProperty('volume', volume_slider.get())
    engine.say(text)
    engine.runAndWait()

def save_mp3():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        print("No text to convert.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")],
        title="Save Audiobook As"
    )
    if save_path:
        engine.setProperty('rate', rate_slider.get())
        engine.setProperty('volume', volume_slider.get())
        engine.save_to_file(text, save_path)
        engine.runAndWait()
        print(f"Audio saved to: {save_path}")

# Tkinter GUI setup
root = tk.Tk()
root.title("PDF to Audiobook Converter")

# PDF Import Button
pdf_btn = tk.Button(root, text="Select PDF", command=select_pdf)
pdf_btn.pack(pady=5)

# Text Box
text_box = tk.Text(root, height=15, width=60)
text_box.pack(padx=10, pady=5)

# Speed Slider
tk.Label(root, text="Speed (Rate)").pack()
rate_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL)
rate_slider.set(150)
rate_slider.pack()

# Volume Slider
tk.Label(root, text="Volume").pack()
volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
volume_slider.set(1.0)
volume_slider.pack()

# Speak Button
speak_btn = tk.Button(root, text="Play Audiobook", command=speak_text)
speak_btn.pack(pady=10)
# Save Butten
save_btn = tk.Button(root, text="Save as MP3", command=save_mp3)
save_btn.pack(pady=5)

root.mainloop()