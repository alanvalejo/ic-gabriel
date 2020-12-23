# -*- coding: utf-8 -*-
"""modelagem_inicial_networkx.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-444vAQCjJ0JNAoIDtyP9nTVFzrFU8It
"""

import networkx as nx
import matplotlib.pyplot as plt

"""#### **Informações**"""

text = """Lorem ipsum dolor sit amet consectetur adipiscing elit cras aliquet eget dolor sed venenatis aliquam
          commodo lectus ac arcu fermentum iaculis nec sed nibh ut nulla lacus mattis a dapibus cursus varius 
          eu elit Pellentesque venenatis eget sapien eget sapien eget sapien nibh sit amet purus dapibus luctus amet Nulla Pellentesque ipsum mi dictum nec 
          eros eget condimentum scelerisque odi amet Nulla eget sapien Duis a malesuada arcu Aliquam vestibulum eros lacus Quisque 
          faucibus diam in pretium scelerisque Aliquam  scelerisque odi dignissim blandit tellus eu molestie augue hendrerit 
          sit amet Nulla eu arcu quam Aenean et est imperdiet efficitur sapien efficitur sapien efficitur sapien eget lacinia lorem Curabitur 
          pulvinar dolor  consectetur adipiscing nulla vel porttitor urna interdum quis Pellentesque imperdiet efficitur imperdiet efficiturin orci augue Maecenas molestie 
          finibus auctor Quisque at libero euismod aliquam magna sed tempus dapibus cursus lorem Integer accumsan mi vitae 
          lorem sollicitudin imperdiet efficitur tincidunt Donec tempus mollis nisl eget aliquet dapibus cursus diam facilisis et Quisque rhoncus 
          nibh sed blandit fringilla Etiam enim imperdiet efficitur sapien volutpat eget sapien vel pharetra commodo turpis Nulla facilisi
          Nunc convallis posuere nibh et pellentesque turpis suscipit nec"""

adj=1;
W=1.0;
X=1;

"""#### **Processamento do texto**
* Etapa responsável por remover todos os caracteres especiais e duplicatas*
"""

text_processad = [word.lower().replace('\n', '') for word in text.split(' ') if word.strip() != '' and word.strip() != '\n' and len(word) > 1]
nodes = set(text_processad);

"""#### **Modelagem do Grafo**
* Etapa resposável por modelar o grafo de acordo com o critério de uma aresta para cada node (palavras) separados por um espaço de X*
"""

G = nx.Graph();
G.add_nodes_from(nodes);

cont=0;
node_actual = text_processad[cont];
cont+=1;
node_next = '';

for i in range(1,X+1):
  for node_next in text_processad[i:]:
    if G.has_edge(node_actual, node_next):
      G[node_actual][node_next]['weight'] = G[node_actual][node_next]['weight']+W;
    else:
      G.add_edge(node_actual, node_next, weight=W);
    node_actual = text_processad[cont];
    cont+=1;
  cont = 1;
  node_actual = text_processad[0];

"""#### **Plotagem do grafo**"""

nx.draw(G, with_labels=True);
plt.show();