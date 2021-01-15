# extract_doc_info.py

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    
    return information

def text_extractor(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        # get the first page
        
        for i in range(number_of_pages):
            page = pdf.getPage(i)
            print(page)
            print('Page type: {}'.format(str(type(page))))
            text = page.extractText()
            print(text)
            
            if i == 0:
                stream_type = "w"
            else:
                stream_type = "a"
                
            with open("demofile1.txt", stream_type, encoding='utf-8') as f:
                f.write(text)
                f.write("\n\n")
                f.close()
        
if __name__ == '__main__':
    path = '/path/to/pdffile.pdf'
    
    info = extract_information(path)
    text_extractor(path)
    