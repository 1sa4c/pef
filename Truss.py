import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Joint import Joint
from Support import Support
from SupportType import SupportType


class Truss:
    def __init__(self):
        self.graph = nx.Graph()
        self.bar_count = 0

    def add_joint(self, joint: Joint, **kwargs) -> None:
        self.graph.add_node(joint, **kwargs)

    def add_bar(self, from_joint: Joint, to_joint: Joint, **kwargs) -> None:
        angle = np.arctan2(to_joint.y - from_joint.y, to_joint.x - from_joint.x)
        self.graph.add_edge(from_joint, to_joint, bar_id=self.bar_count, bar_angle=angle, **kwargs)
        self.bar_count += 1

    def show(self) -> None:
        pos = {}
        reaction_pos = {}
        node_labels = {}
        edge_labels = {e: round(self.graph.edges[e]['weight'], 2) for e in self.graph.edges}
        for node in self.graph:
            pos[node] = (node.x, node.y)
            reaction_pos[node] = (node.x, node.y - 0.5)
            if node.support:
                label = ''
                if node.support.reaction_force[0] is not None:
                    label += f'\nRX: {node.support.reaction_force[0]}'
                if node.support.reaction_force[1] is not None:
                    label += f'\nRY: {node.support.reaction_force[1]}'
                node_labels[node] = label

        nx.draw_networkx(self.graph, pos=pos, with_labels=True, width=3, node_size=700, font_size=22, font_color='whitesmoke')
        nx.draw_networkx_labels(self.graph, reaction_pos, labels=node_labels)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

    def solve(self) -> None:
        coefficients = list()
        constants = list()

        reaction_id = 0

        for joint in self.graph.nodes():
            x_bars = list()
            y_bars = list()

            x_reactions = [0] * Support._total_number_of_reactions
            y_reactions = [0] * Support._total_number_of_reactions

            for e in self.graph.edges():
                angle = self.graph.get_edge_data(*e)['bar_angle']

                if e in self.graph.edges(joint):
                    if e[1] is joint:
                        x_bars.append(-np.cos(angle))
                        y_bars.append(-np.sin(angle))
                    else:
                        x_bars.append(np.cos(angle))
                        y_bars.append(np.sin(angle))
                else:
                    x_bars.append(0)
                    y_bars.append(0)

            if joint.support:
                if joint.support.support_type != SupportType.ROLLER:
                    x_reactions[reaction_id] = 1
                    reaction_id += 1

                y_reactions[reaction_id] = 1
                reaction_id += 1

            coefficients.append(x_bars + x_reactions)
            coefficients.append(y_bars + y_reactions)

            constants.append(-joint.get_total_load()[0])
            constants.append(-joint.get_total_load()[1])


        m, b = np.array(coefficients), np.array(constants)

        result = np.linalg.solve(m, b)

        for i, e in enumerate(self.graph.edges()):
            self.graph[e[0]][e[1]]['weight'] = result[i]
            

        reaction_id = len(self.graph.edges())
        for joint in self.graph.nodes():
            if joint.support:
                if joint.support.support_type != SupportType.ROLLER:
                    joint.support.reaction_force[0] = result[reaction_id]
                    reaction_id += 1

                joint.support.reaction_force[1] = result[reaction_id]
                reaction_id += 1
