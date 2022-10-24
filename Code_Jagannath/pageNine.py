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

reader = PdfReader("BP-0001.pdf")
doc_length = len(reader.pages)
page = reader.pages[8]
t = page.extract_text()
text = str(t)



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


#Loops
loopValue = None
for g in loops:
    loopValue = re.search('(' + g + ')', t, re.I)
    if(loopValue != None):
        print(loopValue.group(1))
        loops = loopValue.group(1)
        break

#Mobile Phase A
mobile_phase_a = None
mobile_phase_a = re.search("Mobile Phase A (.*)", t, re.I)
mobile_phase_a = noneOrNo(mobile_phase_a)
print(mobile_phase_a)

#Mobile Phase B
mobile_phase_b = None
mobile_phase_b = re.search("Mobile Phase B (.*)", t, re.I)
mobile_phase_b = noneOrNo(mobile_phase_b)
print(mobile_phase_b)


#CSV code
header = ['BP-number, MK-number, Loops, Mobile-Phase-A, Mobile-Phase-B']

data = [
	[bpNumber, mkNumber, loops, mobile_phase_a, mobile_phase_b ]
]

with open('Page9.csv','w', encoding = 'UTF8', newline = '') as f:
 writer = csv.writer(f)
 writer.writerow(header);
 writer.writerows(data);
