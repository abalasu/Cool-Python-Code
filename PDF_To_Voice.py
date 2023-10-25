import pyttsx3
import PyPDF2

pdfReader = PyPDF2.PdfReader(open("d:/pythondata/sample.pdf", 'rb'))
reader = pyttsx3.init()

for page in range(len(pdfReader.pages)):
    text = pdfReader.pages[page].extract_text()
    readable_text = text.strip().replace('\n',' ')
    print(readable_text)
    reader.say(readable_text)
    reader.save_to_file(readable_text, 'sample.mp3')
    reader.runAndWait()

reader.stop()

