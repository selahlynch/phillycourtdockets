## NOTE - I installed the pdfminer package first by following instructions
# at this site: http://euske.github.io/pdfminer/index.html


import requests
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams


##following practices from pdf2txt.py to extract text
#pdf2txt.py

print "Downloading pdf..."
docket_min = 863
docket_max = 867

data_file = "docket_dataz.txt"
fp_data = open(data_file, "w")

for i in range(docket_min, docket_max):
    docket_code = str(i).zfill(7)

    url = "https://ujsportal.pacourts.us/DocketSheets/CPReport.ashx?docketNumber=CP-51-CR-{}-2013".format(docket_code)
    r = requests.get(url, stream=True)
    with open('/tmp/docket.pdf', 'wb') as fd:
        chunk_size = 20000
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


    page = requests.get(url)
    #fname_in = "/home/selah/Code/phillycourtdockets/docket_sample.pdf"
    fname_in = "/tmp/docket.pdf"
    fname_txt = "/tmp/docket.txt"
    #open_file = open(fname)
    fp_in = file(fname_in, 'rb')
    fp_out = open(fname_txt, 'w')

    ##ATTEMPT 1
    # Create a PDF parser object associated with the file object.
    #parser = PDFParser(open_file)
    # Create a PDF document object that stores the document structure.
    #doc = PDFDocument(parser)
    # Connect the parser and document objects.
    #print parser.nextline()
    #print parser.nextline()
    #print parser.nextline()


    ##ATTEMPT 2
    #Code from pdf2txt.py
    laparams = LAParams()
    laparams.char_margin = 2.0
    laparams.line_margin=0.5
    laparams.word_margin=0.1
    laparams.all_texts=False

    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, fp_out, codec='utf-8', laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pdf_pages = PDFPage.get_pages(fp_in, set())
    pagenum = 0
    pagelim = 3
    for page in pdf_pages:
        pagenum += 1
        if pagenum > pagelim:
            continue
        print "Transcribing page " + str(pagenum) + " from PDF to text"
        interpreter.process_page(page)
    fp_in.close()
    fp_out.close()
    device.close()

    fp_in = open(fname_txt, "r")
    docket_num_recorded = False
    name_recorded = False
    for line in fp_in:

        if "Docket Number:" in line and not docket_num_recorded :
            print line.rstrip()
            docket_num_recorded = True
        if "v." in line and not name_recorded :
            line = fp_in.next()
            line = fp_in.next().rstrip()
            print line
            name = line
            name_recorded = True
        if "CHARGES" in line :
            charge_lines = []
            for i in range(1,4):
                line = fp_in.next().rstrip()
                print line
                if i > 1:
                    charge_lines.append(line)
            charges = " ".join(charge_lines)
    fp_data.write(name + ", " + charges + "\n")
    fp_in.close()
fp_data.close()