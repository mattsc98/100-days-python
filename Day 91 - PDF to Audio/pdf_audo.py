import PyPDF2
import pyttsx3

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()
    return text

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    pdf_file_path = "your_pdf_file.pdf"  # Replace with the path to your PDF file
    try:
        pdf_text = extract_text_from_pdf(pdf_file_path)
        text_to_speech(pdf_text)
    except Exception as e:
        print("An error occurred:", str(e))
