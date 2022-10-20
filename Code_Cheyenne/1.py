#!/usr/bin/env python
# coding: utf-8

# Questions:
# 1.) Should csv be separated by page or tables?
# 2.) Should we assign values to the category and category_val variables first then put into csv row by row or 
#     assign values to category and category_val variables and input into csv row by row
#     as we loop through the minor lists?

# In[1]:


from PyPDF2 import PdfReader
import re
import csv


# In[2]:


#pre-determined lists

#Minor lists
bp_num = ["bpNum", "BP-0001", "BP-0326"] #exact word
mk_num = ["mkNum", "MK-1234", "MK-0002"] #exact word
species = ["species", "Rat", "Monkey", "Dog", "Cat", "Rabbit", "Human"] #exact word
matrix = ["matrix", "Plasma", "Urine", "Serum", "Liver", "Brain"] #exact word
extraction_method = ["extractionMethod", "Protein Precipitation ", "Liquid Liquid Extraction", "Solid Phase Extraction", "Immunoprecipitation", "Solid Liquid Extraction"] #substrings
internal_standard = ["internalStandard", "SIL-MK-1234", "SIL-MK-0159"] #exact word
chromatography = ["chromatography", "reverse phase", "normal phase"] #substring
turbo_ionspray = ["turboIonspray","ionization", "ionspray", "Atmospheric pressure chemical"] #substring
stored_temp = []
polarity = ["polarity","positive", "negative"] #exact word

#Main list
main_list = [bp_num, mk_num, species, matrix, extraction_method, internal_standard, 
             chromatography, turbo_ionspray, polarity]

fields = ['category', 'value']
rows = []


# In[3]:


#get document from front-end and convert to pdf
reader = PdfReader("example_docs/BP-0001.pdf")
doc_length = len(reader.pages)
page = reader.pages[0]
t = page.extract_text()
text = str(t)


# In[4]:


print(text)


# In[5]:


#Search document for variables using pre-determined lists
for i in main_list:
    for j in i[1:]:
        a = re.search('(.+)' + j + '(.+)', text, re.I)
        if a:
            name_category = i[0]
            val_category = j.capitalize()
            rows.append([name_category, val_category])
            #print(i[0] + ": " + j)
print(rows)


# In[6]:


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


# In[3]:





# In[ ]:




