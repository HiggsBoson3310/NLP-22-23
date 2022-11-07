import csv

'''
Read the csv file and generate neo4j database creation script in cypher

How to use it?
1. Open the terminal at directory of this script and make sure 'Merck_gdb.csv' is at this directory as well
2. Run ```python neo4j_create.py > output.txt``` in your terminal
3. Copy the cypher code in output.txt
4. Paste the code into neo4j terminal
'''

node_list = set()
db = list()

# Merck_gdb.csv is the input file
with open('Merck_gdb.csv', 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(file):
        if i == 0:
            continue
        node_list.add(row[0])
        node_list.add(row[1])
        db.append([row[0].split(':')[0], row[0].split(':')[1],
                  row[1].split(':')[0], row[1].split(':')[1], row[2]])

for i in node_list:
    print(
        f'CREATE (n:{i.split(":")[0].replace(" ", "_")} {{name: "{i.split(":")[1]}"}});')

for i in db:
    print(f'MATCH (a:{i[0].replace(" ", "_")}), (b:{i[2].replace(" ", "_")})')
    print(f'WHERE a.name = "{i[1]}" AND b.name = "{i[3]}"')
    print(f'CREATE (a)-[r:{i[4].upper()}]->(b);')
