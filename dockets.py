## NOTE - I installed the pdfminer package first by following instructions
# at this site: http://euske.github.io/pdfminer/index.html


import requests
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
print "Reading some dockets"

#url = "https://ujsportal.pacourts.us/DocketSheets/CPReport.ashx?docketNumber=CP-51-CR-0000862-2013"
#page = requests.get(url)
open_file = open("/home/selah/Code/dockets/docket_sample.pdf")
# Create a PDF parser object associated with the file object.
parser = PDFParser(open_file)
# Create a PDF document object that stores the document structure.
doc = PDFDocument(parser)
# Connect the parser and document objects.
print parser.nextline()



