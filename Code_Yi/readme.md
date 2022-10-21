# Fall 2022 MerckNLP: Database Team
This repository contains the scripts, schema and data files associated with the creation of the Merck BP file graph database.

## File Structure
```
neo4j
│   README.md
│
└── old (archived files)
│   │   Merck_gdb.csv (data file)
│   │   neo4j_create.py (generate cypher script)
│   └── output.txt (output of neo4j_create.py)
│   
└── resources
└── schema
    │   BP_triple.csv (graph data model of BP template in RDF/triple format)
    │   schema_visualizer.py (visualize BP_triple.csv)
    └── schema.html (generated interactive graph)
```