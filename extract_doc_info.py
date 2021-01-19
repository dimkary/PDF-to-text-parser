import sys
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
    output = pdf_path.split(".")[-2]+".txt"
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        # get the first page
        
        for i in range(number_of_pages):
            page = pdf.getPage(i)
            text = page.extractText()
            
            if i == 0:
                stream_type = "w"
            else:
                stream_type = "a"
                
            with open(output, stream_type, encoding='utf-8') as f:
                f.write("######### PAGE {} #########\n".format(i))
                f.write(text.strip())
                f.write("\n##########################\n\n")
                f.close()
        
if __name__ == '__main__':
    args = sys.argv
    print(args[1])
    path = args[1]
    
    info = extract_information(path)
    text_extractor(path)
    
    source = args[2]
    
    with open(source, 'rb') as f:
        source_text = f.readlines()
    print(source_text)
    