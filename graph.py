import graphviz
# pip3 install graphviz 

FILE = 'basic_vr_patterns.csv'
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
    f.attr(rankdir='LR', size='12,9')

    # define Nodes
    f.attr('node', shape='egg')
    for n in nodes:
        f.node(n)
        

    table_str =  '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    '''
    # Define edges 
    
    for i,e in enumerate(rows):
        label = f'{str(i)}. {e[2]}'
        f.edge(e[0], e[1], label)

        table_str += f'''<TR>
        <TD COLSPAN="3">{label}</TD>
        </TR>
        '''
    table_str += '''</TABLE>>'''

    if table:
        f.attr('node', shape='plaintext')
        f.node('struct1', table_str)

    # make it so 
    f.render(f'./outputs/{OUTFILE}')  


if __name__ == '__main__':
    table = False
    nodes, rows = get_input(FILE)
    make_graph(nodes,rows)
    #make_table()

