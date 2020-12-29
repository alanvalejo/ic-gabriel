import igraph as ig

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

text_processad = [word.lower().replace('\n', '') for word in text.split(' ') if word.strip() != '' and word.strip() != '\n' and len(word) > 1]
nodes = set(text_processad);

G = ig.Graph();
G.add_vertices(list(nodes));

cont=1;
node_actual = text_processad[0];
node_next = '';

for i in range(1,X+1):
  for node_next in text_processad[i:]:
    try:
      id = G.get_eid(node_actual, node_next);
      G.es[id]['weight'] += W;
    except:
      G.add_edge(node_actual, node_next, weight=W);
    node_actual = text_processad[cont];
    cont+=1;
  cont = 1;
  node_actual = text_processad[0];

def color_vertex(degree):
  if degree < 4:
    return 0;
  if degree < 8:
    return 1;
  return 2;

colors=['#e74c3c', '#c0392b', '#34495e'];
visual_style = {};
visual_style['vertex_shape']='circle';
visual_style['vertex_label_color']='#ffffff';
visual_style['vertex_size']=[degree * 5 for degree in G.degree()];
# visual_style['vertex_label']=G.vs['name'];
visual_style['vertex_color']=[colors[color_vertex(degree)] for degree in G.degree()];
visual_style['edge_width']=[1 + 0.8 * weight for weight in G.es['weight']];
visual_style['margin']=2;
visual_style['layout']=G.layout_auto();

ig.plot(G, **visual_style);