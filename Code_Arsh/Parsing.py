import PyPDF2
import re
import csv
import camelot

# Text Extraction Stuff

pdfFileObj = open('BP-0001.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

searchString = ""
numOfPages = pdfReader.numPages
for i in range(numOfPages):
	pageObj = pdfReader.getPage(i)
	z = pageObj.extractText()
	document = z.replace("\n", " ").replace(",","")
	document = re.sub(' +',' ', document)
	searchString = searchString + document

# print(searchString)

pdfFileObj.close()

# Parsing Stuff

tables = camelot.read_pdf('BP-0001.pdf')

print("______________________________________________________________________________________\n")
print("Output of RegEx BP Document:")

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
# special_requirments = ["low binding plates","thaw on wet ice instead of room","temp.","peptide needle","additional carryover blanks","shut down method"]

# Method: Sets input to it's match if there is a match
def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

# BP Number
bpNumber = None
bpNumber = re.search("BP-([^\s]+)",searchString, re.I)
bpNumber = noneOrNo(bpNumber)

print("BP Number:")
print(bpNumber)

# MK Number
mkNumber = None
mkNumber = re.search("MK-([^\s]+)",searchString, re.I)
mkNumber = noneOrNo(mkNumber)

print("MK Number:")
print(mkNumber)

# L Number
lNumber = None
lNumber = re.search("L-([^\)]+)",searchString, re.I)
lNumber = noneOrNo(lNumber)

print("L Number:")
print(lNumber)

# Species
speciesValue = None
for a in species:
	speciesValue = re.search('(' + a + ')', searchString, re.I)
	if(speciesValue != None):
		print("Species Value:")
		print(speciesValue.group(1))
		break

# Matrix
matrixValue = None
for b in matrix:
	matrixValue = re.search('(' + b + ')', searchString, re.I)
	if(matrixValue != None):
		print("Matrix Value:")
		print(matrixValue.group(1))
		break

#Extraction Method
extractionValue = None
for c in extraction_method:
	extractionValue = re.search('(' + c + ')', searchString, re.I)
	if(extractionValue != None):
		print("Extraction Value:")
		print(extractionValue.group(1))
		break

# Internal Standard
internalStandard = None
internalStandard = re.search("SIL-MK-([^\)]+)",searchString, re.I)
print("Internal Standard Number:")
internalStandard = noneOrNo(internalStandard)

print(internalStandard)

# Chromatography
chromatographyValue = None
for d in chromatography:
	chromatographyValue = re.search('(' + d + ')', searchString, re.I)
	if(chromatographyValue != None):
		print("Chromatography Value:")
		print(chromatographyValue.group(1))
		break

# Turbo Ion Spray
turboionsprayValue = None
for e in turbo_ionspray:
	turboionsprayValue = re.search('(' + e + ')', searchString, re.I)
	if(turboionsprayValue != None):
		print("Turboionspray Value:")
		print(turboionsprayValue.group(1))
		break

# Polarity
polarityValue = None
for f in polarity:
	polarityValue = re.search('(' + f + ')', searchString, re.I)
	if(polarityValue != None):
		print("Polarity Value:")
		print(polarityValue.group(1))
		break

# To m/z
drugMZTo = None
isMZTo = None
mzTo = re.findall("→ ([^\s]+)",searchString, re.I)
drugMZTo = mzTo[0]
isMZTo = mzTo[1]

print("M/Z for To Values: [drug/I.S]:")
print(drugMZTo)
print(isMZTo)

# From m/z
drugMZFrom = None
isMZFrom = None
mzFrom = re.findall("([^\s]+) →",searchString, re.I)
drugMZFrom = mzFrom[0]
isMZFrom = mzFrom[1]

print("M/Z for From Values: [drug/I.S]:")
print(drugMZFrom)
print(isMZFrom)

# LLOQ; I really dunno how to do this [ng/mL]
lloq = None
lloq = re.search(r" for this method is (.*?) ng/mL", searchString, re.I)
lloq = noneOrNo(lloq)

print("LLOQ Value:")
print(lloq)

# Regression Model
regressionModelValue = None
for g in regression_model:
	regressionModelValue = re.search('(' + g + ')', searchString, re.I)
	if(regressionModelValue != None):
		print("Regression Value:")
		print(regressionModelValue.group(1))
		break

# X to XXX; I really dunno how to do this [ng/mL]
calibrationRangeFrom = None
calibrationRangeTo = None
calibrationPhrase = re.search(r"(\b\S+\b) to (\b\d+) ng/mL", searchString, re.I)
calibrationRangeFrom = calibrationPhrase.group(1)
calibrationRangeTo = calibrationPhrase.group(2)

print("Calibration Range Values: [From/To]")
print(calibrationRangeFrom)
print(calibrationRangeTo)

# X uL matrix sample
matrixSample = None
matrixSample = re.search("([^\s]+) L",searchString, re.I)
matrixSample = noneOrNo(matrixSample)

print("Matrix Sample 'X' uL Value:")
print(matrixSample)

# Dilutent
dilutentValue = None
for h in dilutent:
	dilutentValue = re.search('(' + h + ')', searchString, re.I)
	if(dilutentValue != None):
		print("Dilutent Value:")
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

print("Storage Temperature Values: [standard solution/matrix sample]")
print(standardSolutionTemperature)
print(matrixSampleTemperature)
	
# Anticoagulant
anticoagulantValue = None
for j in anticoagulant:
	anticoagulantValue = re.search('(' + j + ')', searchString, re.I)
	if(anticoagulantValue != None):
		print("Anticoagulant Value:")
		print(anticoagulantValue.group(1))
		break

# End of Paragraph 1

# Special Requirments
specialRequirments = None
specialRequirments = re.search(r"Special Requirements:", searchString, re.I)
specialRequirmentsActual = None
if specialRequirments != None:
	specialRequirments = re.search(r"Special Requirements: (.*?) 1 INSTRUMENTATION", searchString, re.I)
	specialRequirmentsActual = specialRequirments.group(1).replace("• ","\n")
	print("Special Requirment Value:")
	print(specialRequirmentsActual)

tables = camelot.read_pdf('BP-0001.pdf',pages = "1,2,3,4,5,6,7,8,9,10,11,12,13,14")

#Table 1

first_table = tables[0]
print_table = first_table.df

a = print_table.at[1,2]
massSpecModel = a[0:-5]
print("Mass Spec Model Value:")
print(massSpecModel)

liquidHandlingComponents = print_table.at[3,2]
print("Liquid Handling Components Value:")
print(liquidHandlingComponents)

#SECTION 2

#Table 2

columnList = []
tableToUsed = tables[1].df
c = len(tableToUsed.columns)
canAdd = False
counter = 0
positions = 0
for a in tableToUsed[0]:
  if a == "Tweezers":
    canAdd = True 
  elif canAdd == True: 
    columnList.append(a)
    positions = counter
  counter = counter + 1

supplier = tableToUsed[1][positions]

print("Column Values:")
print(columnList)
print("Column Supplier Values:")
print(supplier)

#Third Table

third_table = tables[2]

third_table.df

print_table_three = third_table.df

microbalance = print_table_three.at[1,1]
print("Micro Balance Value:")
print(microbalance)

analyticalBalance = print_table_three.at[2,1]
print("Analytical Balance Value:")
print(analyticalBalance)

refrigeratedCentrifuge = []
tableToUsed3 = tables[2].df
c = len(tableToUsed3.columns)
canAdd = False
counter = 0
positions = 0
for a in tableToUsed3[0]:
  if a == "Microplate De-Froster" or a == "Refrigerated centrifuge - 96-well":
    canAdd = True 
  elif canAdd == True: 
    refrigeratedCentrifuge.append(a)
    positions = counter
    break
  counter = counter + 1

refrigeratedCentrifuge = tableToUsed3[1][positions]

print("Refrigerated Centrifuge Values: ")
print(refrigeratedCentrifuge)

phMeter = []
tableToUsed3 = tables[2].df
c = len(tableToUsed3.columns)
canAdd = False
counter = 0
positions = 0
for a in tableToUsed3[0]:
  if a == "External Column Heater":
    canAdd = True 
  elif canAdd == True: 
    phMeter.append(a)
    positions = counter
    break
    phMeter = tableToUsed3[1][positions]
  elif (counter == (len(tableToUsed3)-1)):
      phMeter = "None"
      break
  counter = counter + 1


print("pH Meter Values: ")
print(phMeter)

plateSealer = print_table_three.at[(c-1),1]
print("Plate Sealer Values: ")
print(plateSealer)

#Fourth Table

fourth_table = tables[3]

fourth_table.df

print_table_four = fourth_table.df

adjustablePipes = print_table_four.at[3,1]
print("Adjustable Pipes Values: ")
print(adjustablePipes)

pipetteTips = print_table_four.at[4,1]
print("Pipette Tips Values: ")
print(pipetteTips)

#Fifth Table
#Camelot failed to detect the table so will be using Regex

def noneOrNo(searchInput): 
	if searchInput != None:
		return searchInput.group(1)
	return searchInput

reagentTroughs = None
reagentTroughs = re.search("Troughs ([^\s]+)",searchString, re.I)
reagentTroughs = noneOrNo(reagentTroughs)
print("Reagent Troughs Values: ")
print(reagentTroughs)

fifth_table = tables[4]

fifth_table.df

print_table_five = fifth_table.df

analyteLNumber = print_table_five.at[1,1]
print("Analyte L Number Values: ")
print(analyteLNumber)
analyte = analyteLNumber[3:7]
lNumber = analyteLNumber[12:22]
print("Analyte Values: ")
print(analyte)
print("L Number Values: ")
print(lNumber)

internalStandard = print_table_five.at[1,2]
print("Internal Standard Values: ")
print(internalStandard)

analyteForm = print_table_five.at[2,1]
print("Analyte Form Values: ")
print(analyteForm)

ISForm = print_table_five.at[2,2]
print("IS Form Values: ")
print(ISForm)

analyteMolecularWeight = print_table_five.at[3,1]
print("Analyte Molecular Weight Values: ")
print(analyteMolecularWeight)

ISMolecularWeight = print_table_five.at[3,2]
print("Internal Standard Molecular Weight Values: ")
print(ISMolecularWeight)

analyteWatsonID = print_table_five.at[4,1]
print("Analyte Watson ID Values: ")
print(analyteWatsonID)

ISWatsonID = print_table_five.at[4,2]
print("Internal Standard Watson ID Values: ")
print(ISWatsonID)

matrix = None
matrix = re.search("Supplier \n([^\s]+)",searchString, re.I)
matrix = noneOrNo(matrix)
print("Matrix Values:")
print(matrix)

# Section 5; N/A [nothing to extract from this section]

# Section 6; N/A [nothing to extract from this section]

# Note:
# 1. 7, 8, and 9 do not have regEx expressions for everything in red since some [a lot] of the values are just repeats that can be found in paragraph 1
# Section 7, 8, 9 completed @ 6:42 10/25/22
# Camelot does not work with tables that aren't a certain width

# Section 7; Arsh [DONE]

# Section 8; Arsh [DONE]

# Section 9; Arsh [DONE]

# Free Form Stock [these all occur in sections 7,8 so we use findall; get 2 values and put them for each respective section]

freeStockStandard = None
freeStockQualityControl = None
freeStock = None
freeStock = re.findall(r"([^\s]+) mg/mL free form stock", searchString, re.I)
if freeStock != None:
	freeStockStandard = freeStock[0]
	freeStockQualityControl = freeStock[1]

print("Free Stock Standard Values: ")
print(freeStockStandard)
print("Free Stock Quality Control Values: ")
print(freeStockQualityControl)

# Instructions after Mix Well [these all occur in sections 7,8,9 so we use findall; get 3 values and put them for each respective section]

mixWellInstructionsStandardA = None
mixWellInstructionStandardB = None
mixWellInstructionQualityA = None
mixWellInstructionQualityB = None
mixWellInstructionISA = None
mixWellInstructionISB = None
mixWell = None
mixWell = re.findall(r"Mix well(.*?)Store", searchString, re.I)
if mixWell != None:
	mixWellInstructionsStandardA = mixWell[0].replace(".","")
	mixWellInstructionStandardB = mixWell[1].replace(".","")
	mixWellInstructionQualityA = mixWell[2].replace(".","")
	mixWellInstructionQualityB = mixWell[3].replace(".","")
	mixWellInstructionISA = mixWell[4].replace(".","")
	mixWellInstructionISB = mixWell[5].replace(".","")

print("Mix Well Instructions Section 7 Part A Values: ")
print(mixWellInstructionsStandardA)
print("Mix Well Instructions Section 7 Part B Values: ")
print(mixWellInstructionStandardB)
print("Mix Well Instructions Section 8 Part A Values: ")
print(mixWellInstructionQualityA)
print("Mix Well Instructions Section 8 Part B Values: ")
print(mixWellInstructionQualityB)
print("Mix Well Instructions Section 9 Part A Values: ")
print(mixWellInstructionISA)
print("Mix Well Instructions Section 9 Part B Values: ")
print(mixWellInstructionISB)

# Cap the tube and briefly vortex [1 occurence - Section 8]

capTubeInstructions = None
capTubeInstructions = re.search(r"Cap the tube and briefly vortex(.*?).Aliquot",searchString, re.I)
capTubeInstructions = noneOrNo(capTubeInstructions)
print("Cap the Tube Instruction Values: ")
print(capTubeInstructions)

# Aliquot [1 occurence - Section 8]

aliquot = None
aliquot = re.search(r"Aliquot ([^\s]+) mL",searchString, re.I)
aliquot = noneOrNo(aliquot)
print("Aliquot Values: ")
print(aliquot)

# Superscript a Values {2} [1 occurence - Section 7]
superscriptValueA = None
superScriptValueB = None
superScriptValue = re.search(r"a A (.*?) µL spike of the working standards into (.*?) µL", searchString, re.I)
if superScriptValue != None:
	superscriptValueA = superScriptValue.group(1)
	superScriptValueB = superScriptValue.group(2)
print("Measurment Value Superscript a 1: ")
print(superscriptValueA)
print("Measurment Value Superscript a 2: ")
print(superScriptValueB)

# X.XX mg/mL SIL-MK-XXXX stock solution)
stockSolutionXXXSection8 = None
stockSection8 = re.search(r"([^\s]+) mg/mL SIL-MK-", searchString, re.I)
if stockSection8 != None:
	stockSolutionXXXSection8 = stockSection8.group(1).replace("(","")
print("Internal Standard Stock Solution Value:")
print(stockSolutionXXXSection8)

# Section 10; Arsh [I'll hold off on this one since it needs some more thought]

# Section 11; Arsh

# UPLC/Settings

uplcSettingList = ["Elution", "Mobile Phase A", "Mobile Phase B"]
positionUPLCSetting = []
table16 = tables[15].df
counter = 0
for uplcSettings in table16[0]:
	for stuff in uplcSettingList:
		if uplcSettings == stuff:
			positionUPLCSetting.append(counter)
	counter = counter + 1

for stuff1 in positionUPLCSetting:
	print(table16[0][stuff1])
	print(table16[0][stuff1 + 1])

# UPLC Profile; can just get this directly

table17 = tables[16].df

#[0,3] and [0,4]

mobilePhaseA = table17.at[0,3].replace("\n"," ").replace("% A ","")
mobilePhaseB = table17.at[0,4].replace("\n"," ").replace("% B ","")
print(mobilePhaseA)
print(mobilePhaseB)

# MS/Settings

msSettingList = ["Ion Source","Ion Mode","Ionization potential (IS)", "Temperature", "Curtain Gas - N2* ","MR pause between mass range", "MR settling time"]
positionsMSSetting = []
table19 = tables[18].df
counter1 = 0
for msSettings in table19[0]:
	for stuff2 in msSettingList:
		if msSettings == stuff2:
			positionsMSSetting.append(counter1)
	counter1 = counter1 + 1

for stuff3 in positionUPLCSetting:
	print(table16[0][stuff3])
	print(table16[1][stuff3])

# Should be fine; just getting the tables

# Section 12; Arsh [DONE]

# Signal; noise ratio 
signalStuff = None
signalStuff = re.search = re.search(r"e\.g\. signal : (.*?) BP", searchString, re.I)
signalStuff = noneOrNo(signalStuff)
print("Signal Noise Ratio Values: ")
print(signalStuff)

# Table 22 and 23 Data; use regex instead of camelot

# Analyte; X [Table 1]
xFirst = None
xValues = re.findall(r"(\b\S+\b) ng/mL", searchString, re.I)
xFirst = xValues[5]
print("Analyte X Table A Section 12: ")
print(xFirst)

# Peak Height

greaterThanOne = None
greaterThanTwo = None
greaterThan = None
greaterThan = re.findall(r"≥(\b\d\S+)", searchString, re.I)
greaterThanOne = greaterThan[1]
greaterThanTwo = greaterThan[2]

print("Greater than X Table A Section 12: ")
print(greaterThanOne)
print("Greater than X Table B Section 12: ")
print(greaterThanTwo)

# Retention Time; XX ± 0.X

xxFirst = None
xxSecond = None
pointXFirst = None
pointXSecond = None
plusOrMinus = re.findall(r"(\b\S+\b) ± (\b\d\S+)", searchString, re.I)
xxFirst = plusOrMinus[0][0]
xxSecond = plusOrMinus[1][0]
pointXFirst = plusOrMinus[0][1]
pointXSecond = plusOrMinus[1][1]
print("Plus/Minus Table A Section 12 Value 1: ")
print(xxFirst)
print("Plus/Minus Table A Section 12 Value 2: ")
print(xxSecond)
print("Plus/Minus Table B Section 12 Value 1: ")
print(pointXFirst)
print("Plus/Minus Table B Section 12 Value 2: ")
print(pointXSecond)

# Section 13; Arsh [just get the names]

namesOfPeople = None
namesOfPeople = re.findall(r"((?:\S+\s+){0,6}\bJames Schiller)", searchString, re.I)
namesOfPeople = namesOfPeople[0].replace("James Schiller","")
print("Signature Values:")
print(namesOfPeople)

# Final Notes:
# 1. The Camelot implementation will only work for BP-0001; however we do have a plan to get BP-002/BP-003 up to speed
# 2. BP-0003 will take a bit longer so it has two L numbers

# CSV Writing
	# Is not going to be too hard