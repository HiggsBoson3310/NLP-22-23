import PyPDF2
import re
import csv

# Text Extraction Stuff

pdfFileObj = open('BP-0001.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pageObj = pdfReader.getPage(0)

z = pageObj.extractText()
print(z.replace("\n", " "))

searchString = z.replace("\n", " ")

pdfFileObj.close()

# Parsing Stuff

print("______________________________________________________________________________________\n")
print("Output of RegEx Paragraph 1:")

# Species
species = ["Rat ", "Monkey ", "Dog ", "Cat ", "Rabbit ", "Human "]
# Matrix
matrix = ["Plasma", "Urine", "Serum", "Liver", "Brain"]
# Extraction Method
extraction_method = ["protein precipitation", "liquid liquid extraction", "solid phase extraction", "immunoprecipitation", "solid liquid extraction"]
# Chromatography
chromatography = ["reversed phase", "normal phase"]
# Turbo Ionspray
turbo_ionspray = ["turbo ionspray", "Atmospheric pressure chemical ionization"]
# Polarity
polarity = ["positive", "negative"]
# Regression Model
regression_model = ["linear","quadratic"]
# 1/x^2
equation = ["1/x","1/x2"]
# dilutent
dilutent = ["ACN/H 2O \[50/50\]","MeOH/H 2O \[50/50\]","DMSO"]
# Solution and Sample Storage Temp
storage_temp = ["-70°C","-20°C","\+4°C","room temperature"]
# Anticoagulant
anticoagulant = ["EDTA","Na Heparin"]
# Special Requirments
special_requirments = ["low binding plates","thaw on wet ice instead of room","temp.","peptide needle","additional carryover blanks","shut down method"]

# Method: Sets input to it's match if there is a match
def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

# BP Number
bpNumber = None
bpNumber = re.search("BP-([^\s]+)",searchString, re.I)
bpNumber = noneOrNo(bpNumber)

print(bpNumber)

# MK Number
mkNumber = None
mkNumber = re.search("MK-([^\s]+)",searchString, re.I)
mkNumber = noneOrNo(mkNumber)

print(mkNumber)

# L Number
lNumber = None
lNumber = re.search("L-([^\)]+)",searchString, re.I)
lNumber = noneOrNo(lNumber)

print(lNumber)

# Species
speciesValue = None
for a in species:
	speciesValue = re.search('(' + a + ')', searchString, re.I)
	if(speciesValue != None):
		print(speciesValue.group(1))
		break

# Matrix
matrixValue = None
for b in matrix:
	matrixValue = re.search('(' + b + ')', searchString, re.I)
	if(matrixValue != None):
		print(matrixValue.group(1))
		break

#Extraction Method
extractionValue = None
for c in extraction_method:
	extractionValue = re.search('(' + c + ')', searchString, re.I)
	if(extractionValue != None):
		print(extractionValue.group(1))
		break

# Internal Standard
internalStandard = None
internalStandard = re.search("SIL-MK-([^\)]+)",searchString, re.I)
internalStandard = noneOrNo(internalStandard)

print(internalStandard)

# Chromatography
chromatographyValue = None
for d in chromatography:
	chromatographyValue = re.search('(' + d + ')', searchString, re.I)
	if(chromatographyValue != None):
		print(chromatographyValue.group(1))
		break

# Turbo Ion Spray
turboionsprayValue = None
for e in turbo_ionspray:
	turboionsprayValue = re.search('(' + e + ')', searchString, re.I)
	if(turboionsprayValue != None):
		print(turboionsprayValue.group(1))
		break

# Polarity
polarityValue = None
for f in polarity:
	polarityValue = re.search('(' + f + ')', searchString, re.I)
	if(polarityValue != None):
		print(polarityValue.group(1))
		break

# To m/z
drugMZTo = None
isMZTo = None
mzTo = re.findall("→ ([^\s]+)",searchString, re.I)
drugMZTo = mzTo[0]
isMZTo = mzTo[1]

print(drugMZTo)
print(isMZTo)

# From m/z
drugMZFrom = None
isMZFrom = None
mzFrom = re.findall("([^\s]+) →",searchString, re.I)
drugMZFrom = mzFrom[0]
isMZFrom = mzFrom[1]

print(drugMZFrom)
print(isMZFrom)

# LLOQ; I really dunno how to do this [ng/mL]
LLOQ = None

# Regression Model
regressionModelValue = None
for g in regression_model:
	regressionModelValue = re.search('(' + g + ')', searchString, re.I)
	if(regressionModelValue != None):
		print(regressionModelValue.group(1))
		break

# X to XXX; I really dunno how to do this [ng/mL]
calibrationRangeFrom = None
calibrationRangeTo = None
calibrationPhrase = re.search(r"(\b\S+\b) to (\b\d+) ng/mL", searchString, re.I)
calibrationRangeFrom = calibrationPhrase.group(1)
calibrationRangeTo = calibrationPhrase.group(2)
print(calibrationRangeFrom)
print(calibrationRangeTo)

# X uL matrix sample
matrixSample = None
matrixSample = re.search("([^\s]+) L",searchString, re.I)
matrixSample = noneOrNo(matrixSample)
	
print(matrixSample)

# Dilutent
dilutentValue = None
for h in dilutent:
	dilutentValue = re.search('(' + h + ')', searchString, re.I)
	if(dilutentValue != None):
		print(dilutentValue.group(1))
		break

# Solution Temperature and Matrix Sample
standardSolutionTemperature = None
matrixSampleTemperature = None
counter = 1
tempValueTemperature = None
for i in storage_temp:
	tempValueTemperature = re.search('(' + i + ')', searchString, re.I)
	if tempValueTemperature != None and counter == 1:
		standardSolutionTemperature = tempValueTemperature.group(1)
		tempValueTemperature = None
		counter += 1
	if tempValueTemperature != None and counter == 2:
		matrixSampleTemperature = tempValueTemperature.group(1)
		break
	else:
		tempValueTemperature = None

print(standardSolutionTemperature)
print(matrixSampleTemperature)
	
# Anticoagulant
anticoagulantValue = None
for j in anticoagulant:
	anticoagulantValue = re.search('(' + j + ')', searchString, re.I)
	if(anticoagulantValue != None):
		print(anticoagulantValue.group(1))
		break

#CSV Stuff

header = ['BP_Number','MK_Number','L_Number','Species','Matrix','Extraction Method','Internal Standard','Chromatography','Turbo-Ionspray','Polarity','m/z Drug From', 'm/z Drug To', 'm/z I.S From','m/z I.S To','LLOQ','Regression Model','Calibration Range From','Calibration Range To','Matrix Sample L','Dilutent','Storage Temperature','Anticoagulant','Sample Temperature']

data = [
	[bpNumber, mkNumber, lNumber, speciesValue.group(1), matrixValue.group(1), extractionValue.group(1), internalStandard, chromatographyValue.group(1), turboionsprayValue.group(1), polarityValue.group(1), drugMZFrom, drugMZTo, isMZFrom, isMZTo, LLOQ, calibrationRangeFrom, calibrationRangeTo, matrixSample, dilutentValue.group(1), standardSolutionTemperature, anticoagulantValue.group(1), matrixSampleTemperature]
]

with open('Page1.csv','w', encoding = 'UTF8', newline = '') as f:
 writer = csv.writer(f)
 writer.writerow(header);
 writer.writerows(data);

#This is all for paragraph 1