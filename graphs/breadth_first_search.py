import unittest

# Runtime = O(V + E)



#    A
#  /   \
# C     B
# |   /   \
# |  D     E 
# |        |
#  \      /
#    F _/ 


def bfs_1(graph, start):
    '''Returns all nodes in graph'''
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_2(graph, start):
    '''Returns all nodes in a graph'''
    # keep track of all visited nodes
    explored = set()
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.add(node)
            neighbours = graph[node]
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def bfs_paths(graph, start, goal):
    '''Returns all possible paths between starting node and goal node'''
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    '''Returns shortest_path in between 2 nodes'''
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def bfs_shortest_path(graph, start, goal):
    '''Returns shortest_path in between 2 nodes'''
    # keep track of explored nodes
    explored = set()
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    if start == goal:
        return 'That was easy! Start = goal'
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.add(node)
 
    # in case there's no path between the 2 nodes
    return 'No connecting path exists :('


class Test(unittest.TestCase):

    def test_bfs_1(self):
        actual = bfs_1({'A': set(['B', 'C']),
                      'B': set(['A', 'D', 'E']),
                      'C': set(['A', 'F']),
                      'D': set(['B']),
                      'E': set(['B', 'F']),
                      'F': set(['C', 'E'])}, 'A')
        expected = ({'B', 'C', 'A', 'F', 'D', 'E'})
        self.assertEqual(actual, expected)

    def test_bfs_2(self):
        actual = bfs_2({'A': set(['B', 'C']),
                      'B': set(['A', 'D', 'E']),
                      'C': set(['A', 'F']),
                      'D': set(['B']),
                      'E': set(['B', 'F']),
                      'F': set(['C', 'E'])}, 'A')
        expected = ({'B', 'C', 'A', 'F', 'D', 'E'})
        self.assertEqual(actual, expected)

    def test_bfs_paths(self):
        input_graph = ({'A': set(['B', 'C']),
                        'B': set(['A', 'D', 'E']),
                        'C': set(['A', 'F']),
                        'D': set(['B']),
                        'E': set(['B', 'F']),
                        'F': set(['C', 'E'])})
        expected_result = ([['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        result = list(bfs_paths(input_graph, 'A', 'F'))
        self.assertEqual(expected_result, result)

    def test_shortest_path_1(self):
        actual = shortest_path({'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}, 'A', 'F')
        expected = (['A', 'C', 'F'])
        self.assertEqual(actual, expected)

    def test_shortest_path_2(self):
        actual = bfs_shortest_path({'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}, 'A', 'F')
        expected = (['A', 'C', 'F'])
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)

