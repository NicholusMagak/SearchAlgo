from collections import defaultdict
import queue as Q


class Greedy_BfsTraverser:

    # Constructor
    def __init__(self):
        # the path
        self.path = []
        # visited nodes
        self.visited = []
        # ending the code
        self.end_search = False

    def greedy_BFS(self, graph, start_node, goal_node):

        heuristics = {}
        # get file with heuristic distances
        f = open('heuristics.txt')
        for i in graph.nodes():
            node_heuristic_val = f.readline().split()
            heuristics[node_heuristic_val[0]] = node_heuristic_val[1]

        for node in graph:
            # print the graph
            print(heuristics[node], node)
            queue = []
            self.path.append(start_node)
            queue.append(start_node)
            # print(queue)
            # set of visited nodes
            self.visited.append(start_node)
            while queue and not self.end_search:
                # Dequeue a vertex from
                s = queue.pop(0)
                print("Drive to", s, " Estate")

                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                # print(list(graph.neighbors(s)))
                smallest_heuristic_node = ''
                unvisited_neighbors = list(x for x in graph.neighbors(s) if x not in self.visited)
                for i in list(unvisited_neighbors):
                    if i == list(unvisited_neighbors)[0]:
                        smallest_heuristic_node = i
                        # print(smallest_heuristic_node)
                        # print(self.visited)
                    # if i not in self.visited:
                    # print("This is goal node", goal_node, "Current Node", i)
                    if i is goal_node:
                        self.visited.append(i)
                        self.end_search = True
                        # print(self.end_search)
                        print(f"Drive to", goal_node, " and you will have arrived")
                        smallest_heuristic_node = i
                        break
                    else:
                        # print("hapa", self.end_search)
                        if heuristics[i] < heuristics[smallest_heuristic_node]:
                            smallest_heuristic_node = i

                        self.visited.append(i)
                        print(self.visited)
                self.path.append(smallest_heuristic_node)
                queue.append(smallest_heuristic_node)
                # print(queue)
        return self.visited