#!/usr/bin/env python
# coding: utf-8

# Questions:
# 1.) Should csv be separated by page or tables?
# 2.) Should we assign values to the category and category_val variables first then put into csv row by row or 
#     assign values to category and category_val variables and input into csv row by row
#     as we loop through the minor lists?




from PyPDF2 import PdfReader
import re
import csv
import tabula




#pre-determined lists

#Minor lists
bp_num = ["bpNum", "BP-0001", "BP-0326"] #exact word
mk_num = ["mkNum", "MK-1234", "MK-0002"] #exact word
species = ["species", "Rat", "Monkey", "Dog", "Cat", "Rabbit", "Human"] #exact word
matrix = ["matrix", "Plasma", "Urine", "Serum", "Liver", "Brain"] #exact word
extraction_method = ["extractionMethod", "Protein Precipitation ", "Liquid Liquid Extraction", "Solid Phase Extraction", "Immunoprecipitation", "Solid Liquid Extraction"] #substrings
internal_standard = ["internalStandard", "SIL-MK-1234", "SIL-MK-0159"] #exact word
chromatography = ["chromatography", "reversed phase", "normal phase"] #substring
turbo_ionspray = ["turboIonspray","ionization", "ionspray", "Atmospheric pressure chemical"] #substring
storage_temp = ["storageTemperature", "-70°C","-20°C","\+4°C","room temperature"]
polarity = ["polarity","positive", "negative"] #exact word
regression_model = ["regressionModel","linear","quadratic"]
dilutent = ["dilutent", "ACN/H 2O \[50/50\]","MeOH/H 2O \[50/50\]","DMSO"]
anticoagulant = ["anticoagulent", "EDTA","Na Heparin"]
special_requirements = ["specialRequirements", "low binding plates","thaw on wet ice instead of room","temp.","peptide needle","additional carryover blanks","shut down method"]

#Main list
main_list = [bp_num, mk_num, species, matrix, extraction_method, internal_standard, 
             chromatography, turbo_ionspray, storage_temp, polarity, regression_model, dilutent, anticoagulant, special_requirements]

fields = ['category', 'value']
rows = []


# In[18]:


#get document from front-end and convert to pdf
document = ""
reader = PdfReader("example_docs/BP-0001.pdf")
doc_length = len(reader.pages)
pages = [0,1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13]
for i in pages:
    page = reader.pages[i]
    t = page.extract_text()
    text = str(t)
    document = document + text
print(document)




rows = []





#Search document for variables using pre-determined lists. 
#Note: Make this a function and when loading in pdf call this for each page
for i in main_list:
    count = 0;
    for j in i[1:]:
        count = count + 1;
        #print(count)
        a = re.search('(.+)' + j + '(.+)', document, re.I)
        if a:
            name_category = i[0]
            val_category = j
            rows.append([name_category, val_category])
            #print(i[0] + ": " + j)
            break
        elif count == len(i) - 1:
            name_category = i[0]
            val_category = "N/A"
            rows.append([name_category, val_category])
print(rows)





#write to csv
file_name = 'output.csv'
with open(file_name, 'w', encoding="UTF-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

rows=[]

#code to read 
pdf_path = "example_docs/BP-0001.pdf" #can be changed accordingly

dfs = tabula.read_pdf(pdf_path, pages='all')

#dfs[0].to_csv("first_table.csv")

#print(len(dfs))

for i in range(len(dfs)):
    dfs[i].to_csv(f"all_pages_table{i}.csv")



