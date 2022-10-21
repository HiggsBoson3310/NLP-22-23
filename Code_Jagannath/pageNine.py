from PyPDF2 import PdfReader
import re
import csv

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
#Loops
loops = ["Partial Loop"]
#Elution
elution = ["Gradient, Isocratic"]
#Mobile_Phase_A
mobile_phase_a = []
#Mobile_Phase_B
mobile_phase_b = []

reader = PdfReader("BP-0001.pdf")
doc_length = len(reader.pages)
page = reader.pages[8]
t = page.extract_text()
text = str(t)

print(t)

def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

bpNumber = None
bpNumber = re.search("BP-([^\s]+)",t, re.I)
bpNumber = noneOrNo(bpNumber)

print(bpNumber)

# MK Number
mkNumber = None
mkNumber = re.search("MK-([^\s]+)",t, re.I)
mkNumber = noneOrNo(mkNumber)

print(mkNumber)

# L Number
lNumber = None
lNumber = re.search("L-([^\)]+)",t, re.I)
lNumber = noneOrNo(lNumber)

print(lNumber)

# Species
speciesValue = None
for a in species:
	speciesValue = re.search('(' + a + ')', t, re.I)
	if(speciesValue != None):
		print(speciesValue.group(1))
		break

# Matrix
matrixValue = None
for b in matrix:
	matrixValue = re.search('(' + b + ')', t, re.I)
	if(matrixValue != None):
		print(matrixValue.group(1))
		break

#Extraction Method
extractionValue = None
for c in extraction_method:
	extractionValue = re.search('(' + c + ')', t, re.I)
	if(extractionValue != None):
		print(extractionValue.group(1))
		break

# Internal Standard
internalStandard = None
internalStandard = re.search("SIL-MK-([^\)]+)",t, re.I)
internalStandard = noneOrNo(internalStandard)

print(internalStandard)

# Chromatography
chromatographyValue = None
for d in chromatography:
	chromatographyValue = re.search('(' + d + ')', t, re.I)
	if(chromatographyValue != None):
		print(chromatographyValue.group(1))
		break

# Turbo Ion Spray
turboionsprayValue = None
for e in turbo_ionspray:
	turboionsprayValue = re.search('(' + e + ')', t, re.I)
	if(turboionsprayValue != None):
		print(turboionsprayValue.group(1))
		break

# Polarity
polarityValue = None
for f in polarity:
	polarityValue = re.search('(' + f + ')', t, re.I)
	if(polarityValue != None):
		print(polarityValue.group(1))
		break

#Loops
loopValue = None
for g in loops:
    loopValue = re.search('(' + g + ')', t, re.I)
    if(loopValue != None):
        print(loopValue.group(1))
        break

mobile_phase_a = None
mobile_phase_a = re.search("Mobile Phase A (.*)", t, re.I)
mobile_phase_a = noneOrNo(mobile_phase_a)
print(mobile_phase_a)

mobile_phase_b = None
mobile_phase_b = re.search("Mobile Phase B (.*)", t, re.I)
mobile_phase_b = noneOrNo(mobile_phase_b)
print(mobile_phase_b)
