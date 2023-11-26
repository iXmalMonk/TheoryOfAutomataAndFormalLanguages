import matplotlib.pyplot as plt
import networkx as nx
import threading
import time
from tkinter import ttk
import tkinter as tk

graph = nx.DiGraph()

graph.add_nodes_from(range(11))

graph.add_weighted_edges_from(
    [
        (0, 1, 3), (0, 3, 5), (0, 5, 1), (1, 2, 1),
        (2, 3, 4), (2, 3, 7),
        (3, 4, 0), (3, 10, 4), (4, 10, 3), (4, 0, 7),
        (5, 6, 0), (5, 6, 5),
        (5, 9, 6), (6, 7, 5), (7, 8, 1), (8, 10, 0),
        (9, 8, 3)
    ]
)

node_colors = ['grey'] * len(graph.nodes)

node_positions = {
    0: (0, 0),
    1: (1, 1),
    2: (2, 1),
    3: (2, 0),
    4: (3, 1),
    5: (0, -1),
    6: (1, -1),
    7: (2, -1),
    8: (3, -1),
    9: (1, -2),
    10: (4, 0)
}

def function():
    flag = False
    def change_node_color(node, color, flag):
        node_colors[node] = color
        draw_graph()
        if flag:
            time.sleep(0.5)
    def draw_graph():
        nonlocal flag
        if not flag:
            flag = True
            nx.draw_networkx_edges(graph, node_positions, arrows=True, arrowsize=30, arrowstyle='->', edge_color='grey', width=1)
            nx.draw_networkx_edge_labels(graph, node_positions, edge_labels=nx.get_edge_attributes(graph, 'weight'))
            nx.draw_networkx_labels(graph, node_positions, font_color='black', font_size=7)
            nx.draw_networkx_nodes(graph, node_positions, node_color=node_colors, node_size=800)
            plt.annotate('', xy=(2.1, 0.13), xytext=(2.2, 1), arrowprops=dict(arrowstyle='->', color='grey'))
            plt.annotate('4', xy=(2.185, 0.575))
            plt.annotate('', xy=(0.9, -0.85), xytext=(0.1, -0.85), arrowprops=dict(arrowstyle='->', color='grey'))
            plt.annotate('0', xy=(0.5, -0.8))
        else:
            nx.draw_networkx_nodes(graph, node_positions, node_color=node_colors, node_size=800)
        plt.show()
    return change_node_color, draw_graph

change_node_color, draw_graph = function()

thread_graph = threading.Thread(target=draw_graph)

thread_graph.daemon = True

thread_graph.start()

def button_change_node_color(value):
    label['text'] = ''
    if value == '31403.' or value == '31703.':
        change_node_color(0, 'green', True)
        change_node_color(1, 'green', True)
        change_node_color(2, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(4, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(1, 'grey', False)
        change_node_color(2, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(4, 'grey', False)
        change_node_color(10, 'grey', False)
    elif value == '31407' or value == '31707':
        change_node_color(0, 'green', True)
        change_node_color(1, 'green', True)
        change_node_color(2, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(4, 'green', True)
        change_node_color(0, 'red', True)
        label['text'] = 'Ошибочная цепочка'
        change_node_color(0, 'grey', False)
        change_node_color(1, 'grey', False)
        change_node_color(2, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(4, 'grey', False)
        change_node_color(0, 'grey', False)
    elif value == '3144.' or value == '3174.':
        change_node_color(0, 'green', True)
        change_node_color(1, 'green', True)
        change_node_color(2, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(1, 'grey', False)
        change_node_color(2, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(10, 'grey', False)
    elif value == '503.':
        change_node_color(0, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(4, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(4, 'grey', False)
        change_node_color(10, 'grey', False)
    elif value == '507':
        change_node_color(0, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(4, 'green', True)
        change_node_color(0, 'red', True)
        label['text'] = 'Ошибочная цепочка'
        change_node_color(0, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(4, 'grey', False)
        change_node_color(0, 'grey', False)
    elif value == '54.':
        change_node_color(0, 'green', True)
        change_node_color(3, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(3, 'grey', False)
        change_node_color(10, 'grey', False)
    elif value == '10510.' or value == '15510.':
        change_node_color(0, 'green', True)
        change_node_color(5, 'green', True)
        change_node_color(6, 'green', True)
        change_node_color(7, 'green', True)
        change_node_color(8, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(5, 'grey', False)
        change_node_color(6, 'grey', False)
        change_node_color(7, 'grey', False)
        change_node_color(8, 'grey', False)
        change_node_color(10, 'grey', False)
    elif value == '1630.':
        change_node_color(0, 'green', True)
        change_node_color(5, 'green', True)
        change_node_color(9, 'green', True)
        change_node_color(8, 'green', True)
        change_node_color(10, 'green', True)
        label['text'] = 'Цепочка распознана'
        change_node_color(0, 'grey', False)
        change_node_color(5, 'grey', False)
        change_node_color(9, 'grey', False)
        change_node_color(8, 'grey', False)
        change_node_color(10, 'grey', False)
    else:
        change_node_color(0, 'red', True)
        label['text'] = 'Ошибочная цепочка'
        change_node_color(0, 'grey', False)

window = tk.Tk()

window.geometry('250x100')

window.title('Window')

combobox_data = [
    '31403.',
    '31407',
    '3144.',
    '31703.',
    '31707',
    '3174.',
    '503.',
    '507',
    '54.',
    '10510.',
    '15510.',
    '1630.',
]

combobox = ttk.Combobox(window, state='readonly', values=combobox_data)

combobox.pack()

button = ttk.Button(window, command=lambda: button_change_node_color(combobox.get()), text='---')

button.pack()

label = tk.Label(window)

label.pack()

window.mainloop()