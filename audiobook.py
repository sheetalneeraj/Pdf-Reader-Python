import pyttsx3
import PyPDF2
book = open('pythontb.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
#speaker.setProperty('voice','')
voices=speaker.getProperty('voices')
for v in voices:
    print('Voice:')
    print('ID:',v.id)

#speaker.setProperty('Voice','kannada')
for num in range(7, pages): # want to read all pages from 8/7 depending on starting page of your book
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()