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

reader = PdfReader("example_docs/BP-0001.pdf")
doc_length = len(reader.pages)
page = reader.pages[9]
t = page.extract_text()
text = str(t)

print(t)

def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

ml = None
ml = re.search("Initial  ([^\s]+)(.*)", t, re.I)
ml = noneOrNo(ml)

ionSource = None
ionSource = re.search("Ion Source. (([^\s]+)(.*))", t, re.I)
ionSource = noneOrNo(ionSource)
print(ionSource)

ionMode = None
ionMode = re.search("Ion Mode. (([^\s]+)(.*))", t, re.I)
ionMode = noneOrNo(ionMode)
print(ionMode)

ionizationPotential = None
ionizationPotential = re.search("IS. (([^\s]+)(.*))", t, re.I)
ionizationPotential = noneOrNo(ionizationPotential)
print(ionizationPotential)

temperature = None
tempreature = re.search("Temperature  (([^\s]+)(.*))", t, re.I)
tempreature = noneOrNo(tempreature)
print(tempreature)

curtainGas = None
curtainGas = re.search("Curtain Gas – ((.*)+[^\s])", t, re.I)
curtainGas = noneOrNo(curtainGas)
curtainGas = curtainGas[4:6]
print(curtainGas)

MRPause = None
MRPause = re.search("range  ([^\s]+ (.*))", t, re.I)
MRPause = noneOrNo(MRPause)
print(MRPause)

MSSettling = None
MSSettling = re.search("time  ([^\s]+ (.*))", t, re.I)
MSSettling = noneOrNo(MSSettling)
print(MSSettling)

bpNumber = None
bpNumber = re.search("BP-([^\s]+)",t, re.I)
bpNumber = noneOrNo(bpNumber)

print(bpNumber)
