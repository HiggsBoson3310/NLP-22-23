import tabula

#run "pip install tabula-py" in terminal. Requires java as dependency. Check using "java -version" 

pdf_path = "BP-0001.pdf" #can be changed accordingly

dfs = tabula.read_pdf(pdf_path, pages='all')

#dfs[0].to_csv("first_table.csv")

print(len(dfs))

for i in range(len(dfs)):
    dfs[i].to_csv(f"all_pages_table{i}.csv")



