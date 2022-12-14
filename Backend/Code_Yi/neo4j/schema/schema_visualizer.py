from pyvis.network import Network
import pandas as pd
import argparse

def visualization(input: str, output: str):
    """Visualize RDF graph structure using PyVis

    Args:
        input_file:
            A csv file path input
        output_file: 
            A path for output html file  generated by PyVis
    """
    G = Network(height="750px", width="100%", directed=True)

    # read the csv
    data = pd.read_csv(input)

    edge_data = zip(data['node1'], data['node2'], data['relation'])

    for e in edge_data:
        src, dst, edge = e[0], e[1], e[2]

        G.add_node(src, src, size=50, title=src, shape="box")
        G.add_node(dst, dst, size=50, title=dst, shape="box")
        G.add_edge(src, dst, title=edge)

    G.show(output)
    print("File saved")

def main():

    parser = argparse.ArgumentParser(description='Process pdf input')
    parser.add_argument('-i', '--input_path', type=str, default="BP_triple.csv", 
                        help='The input path to the source csv file. REQUIRED')
    parser.add_argument('-o', '--output_path', type=str, default="schema.html", 
                        help='The output path to the resulting html file. REQUIRED')
    args = parser.parse_args()

    visualization(args.input_path, args.output_path)


if __name__ == '__main__':
    main()
