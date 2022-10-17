import PyPDF2
import re

# Open the MerckSamplePDF.pdf in binary mode and save it to a pdfFileObj
pdfFileObj = open('MerckSamplePDF.pdf','rb')

# Create an object of PdfFileReader of class PyPDF2 and pass the file object and get a pdf reader object [file I/O]
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# Print's the number of pages
print(pdfReader.numPages)

# Returns PageObject object from class PyPDF2; page number as argument and returns object with given page information
pageObj = pdfReader.getPage(0)

# Prints the text from object above
# print(pageObj.extractText())

# Putting those values into a String so that 
z = pageObj.extractText()
print(z.replace("\n", " "))

searchString = z.replace("\n", " ")

pdfFileObj.close()

print("______________________________")
print("Output of RegEx:")

# Now we start with the regular expression

# Extraction Method
a = re.search('format (.*) of drug', searchString ).group(1)
print("Extraction Method: " + a)

# Species Matrix 
b = re.search('of drug from (.*) . MK-', searchString ).group(1)
print("Species Matrix: " + b)

# Internal Standard

# Chromatography

# Turbo Ionspray (TIS)

# Polarity

# Lower m/z XXX XXX Drug

# Upper m/z XXX XXX Drug

# X ng/mL

# Regression Model

# X

# XXX ng/mL

# X L

# Matrix Sample

# Dilutent

# Temperature °C

# Anticoagulant

# Matrix

# Temperature