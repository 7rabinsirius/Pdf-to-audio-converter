# Pdf-to-audio-converter
```markdown
# 📚 PDF to Audiobook Converter

Transform any PDF into spoken audio using customizable voices, speed, and volume. This user-friendly GUI application is built with `Tkinter`, `PyMuPDF`, and `pyttsx3`, and allows users to play or export audiobook versions of PDF documents.

---

## 🎯 Features

- 🗂️ **Import PDF** via interactive file dialog
- 🔎 **Extract and display text** from all pages
- 🔊 **Convert text to speech** with customizable voice settings
- 🎙️ **Voice selection** (choose from system voices)
- 🚀 **Adjust speed and volume** using real-time sliders
- 💾 **Save audio as MP3** with auto-suggested filename
- ✅ **Confirmation popup** after successful export
- 🖥️ Intuitive, cross-platform **GUI built with Tkinter**

---

## 🛠️ Tech Stack

| Tool         | Purpose                      |
|--------------|------------------------------|
| Tkinter      | GUI framework                |
| PyMuPDF (`fitz`) | PDF text extraction        |
| pyttsx3      | Text-to-speech (offline)     |
| os           | File naming and handling     |

---

## ▶️ Usage

1. **Install dependencies:**

```bash
pip install pyttsx3 pymupdf
```

2. **Run the application:**

```bash
python audiobook_converter.py
```

3. **Steps in the GUI:**

- Click **"Select PDF"** to import your document
- Choose a **voice** from the dropdown
- Adjust **speed** and **volume** sliders
- Click **"Play Audiobook"** for instant playback
- Click **"Save as MP3"** to export the audio

---

