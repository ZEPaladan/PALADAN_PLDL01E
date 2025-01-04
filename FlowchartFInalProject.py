import pydotplus
from IPython.display import Image

try:
    # Create a directed graph
    graph = pydotplus.Dot(graph_type='digraph')

    # Adding nodes (shapes)
    graph.add_node(pydotplus.Node('START', shape='ellipse'))
    graph.add_node(pydotplus.Node('SETUP Main Application', shape='rectangle'))
    graph.add_node(pydotplus.Node('CREATE Separate GUI Class Files', shape='rectangle'))
    graph.add_node(pydotplus.Node('IMPORT Classes into Specific GUI Files', shape='rectangle'))
    graph.add_node(pydotplus.Node('DESIGN GUI Pages', shape='rectangle'))
    graph.add_node(pydotplus.Node('RUN Main Application', shape='rectangle'))
    graph.add_node(pydotplus.Node('END', shape='ellipse'))

    # Adding edges (connections between nodes)
    graph.add_edge(pydotplus.Edge('START', 'SETUP Main Application'))
    graph.add_edge(pydotplus.Edge('SETUP Main Application', 'CREATE Separate GUI Class Files'))
    graph.add_edge(pydotplus.Edge('CREATE Separate GUI Class Files', 'IMPORT Classes into Specific GUI Files'))
    graph.add_edge(pydotplus.Edge('IMPORT Classes into Specific GUI Files', 'DESIGN GUI Pages'))
    graph.add_edge(pydotplus.Edge('DESIGN GUI Pages', 'RUN Main Application'))
    graph.add_edge(pydotplus.Edge('RUN Main Application', 'END'))

    # Save the graph as a PNG image
    graph.write_png('flowchart_visualization.png')

    # Display the flowchart image
    Image(filename='flowchart_visualization.png')

except Exception as e:
    print(f"An error occurred: {e}")
