import PyPDF2
import re
import csv

# Text Extraction Stuff

# Camelot Sub-Extraction; did not work

# PyPDF2 Sub-Extraction

pdfFileObj = open('BP-0001.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pageObj = pdfReader.getPage(10)

searchString = pageObj.extractText()
print(searchString)

pdfFileObj.close()

# Parsing Stuff

print("______________________________________________________________________________________\n")
print("Output of RegEx Page 11:")

def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

# MK Number [Table 1 and 2 and Number 2]
mkNumber1 = None
mkNumber2 = None
mkNumber3 = None
mkNumber = re.findall("MK-([^\s]+)",searchString, re.I)
mkNumber1 = mkNumber[0]
mkNumber2 = mkNumber[1]
mkNumber3 = mkNumber[2]

print(mkNumber1)
print(mkNumber2)
print(mkNumber3)

# X [Table 1]
xFirst = None
xValues = re.findall(r"(\b\S+\b) ng/mL", searchString, re.I)
xFirst = xValues[0]

print(xFirst)

# Matrix [Table 1]

# Matrix
matrix = ["Plasma", "Urine", "Serum", "Liver", "Brain"]

matrixValue = None
for b in matrix:
	matrixValue = re.search('(' + b + ')', searchString, re.I)
	if(matrixValue != None):
		print(matrixValue.group(1))
		matrixValue = matrixValue.group(1)
		break

# ≥ XXX [Table 1 and 2]
greaterThanOne = None
greaterThanTwo = None
greaterThan = None
greaterThan = re.findall(r"≥(\b\d\S+)", searchString, re.I)
greaterThanOne = greaterThan[0]
greaterThanTwo = greaterThan[1]

print(greaterThanOne)
print(greaterThanTwo)

# XX ± 0.X [Table 1 and 2]

xxFirst = None
xxSecond = None
pointXFirst = None
pointXSecond = None
plusOrMinus = re.findall(r"(\b\S+\b) ± (\b\d\S+)", searchString, re.I)
xxFirst = plusOrMinus[0][0]
xxSecond = plusOrMinus[1][0]
pointXFirst = plusOrMinus[0][1]
pointXSecond = plusOrMinus[1][1]
print(xxFirst)
print(xxSecond)
print(pointXFirst)
print(pointXSecond)


# Signatures (1,2,3)

signatureOne = None
signatureTwo = None
signatureThree = None
splitLines = re.split("\n", searchString)
numOfLines = len(splitLines)

signatureOne = splitLines[numOfLines - 4]
signatureTwo = splitLines[numOfLines - 3]
signatureThree = splitLines[numOfLines - 2]

print(signatureOne)
print(signatureTwo)
print(signatureThree)

#CSV Stuff

header = ['mk1','mk2','mk3','X','Matrix','GreaterThan1','GreaterThan2','plusOrMinusFirstFirst','plusOrMinusFirstSecond','plusOrMinusSecondFirst','plusOrMinusSecondSecond','Signature1','Signature2','Signature3']

data = [
	[mkNumber1, mkNumber2, mkNumber3, xFirst, greaterThanOne, greaterThanTwo, xxFirst, pointXFirst, xxSecond, pointXSecond, signatureOne, signatureTwo, signatureThree]
]

with open('Page11.csv','w', encoding = 'UTF8', newline = '') as f:
 writer = csv.writer(f)
 writer.writerow(header);
 writer.writerows(data);
