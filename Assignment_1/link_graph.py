import networkx as nx
import matplotlib.pyplot as plt
import pickle

fnames = ['angelinajolie.html', 'bradpitt.html', 'jenniferaniston.html',
           'jonvoight.html','martinscorcese.html', 'robertdeniro.html']

def get_links(fnames):
    links = {}
    for file in fnames:
        links[file] = []
        f = open('pages/'+file)

        for line in f.readlines():
            while True:
                p = line.partition('<a href="http://')[2]
                if p == '':
                    break
                url, _, line = p.partition('">')
                links[file].append(url)
        f.close()
    return links


DG = nx.DiGraph()
DG.add_nodes_from(fnames)
edges = []
links = get_links(fnames)
for key, values in links.items():
    eweight = {}
    for v in values:
        if v in eweight:
            eweight[v] += 1
        else:
            eweight[v] = 1
    for succ, weight in eweight.items():
        edges.append([key, succ, {'weight':weight}])
DG.add_edges_from(edges)
print(DG.graph)

plt.figure(figsize=(9,9))
pos = nx.spring_layout(DG,iterations=10)
nx.draw(DG,pos,node_size=50,alpha=0.8,edge_color='r', font_size=16, with_labels=True)
plt.show()
pickle.dump(DG, open('DG_new.pkl',"wb"))

