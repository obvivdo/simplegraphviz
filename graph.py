import graphviz


FILE = 'bitsadmin.csv'
FILENAME = FILE.split('.')[0]
OUTFILE = FILENAME + '_output' # no .pdf

def get_input(FILE):
    import csv
    rows = []
    nodes = []
    with open(f'./inputs/{FILE}', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
            nodes.extend([row[0],row[1]])
    print(header)
    nodes = set(nodes)

    return nodes, rows


def make_graph(nodes,rows):
    # data is a list ?
    f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')

    # define Nodes
    f.attr('node', shape='doublecircle')
    for n in nodes:
        f.node(n)


    # Define edges 
    f.attr('node', shape='circle')
    for i,e in enumerate(rows):
        label = f'{str(i)}. {e[2]}'
        f.edge(e[0], e[1], label)


    # make it so 
    f.render(f'./outputs/{OUTFILE}')  


if __name__ == '__main__':
     nodes, rows = get_input(FILE)
     make_graph(nodes,rows)

