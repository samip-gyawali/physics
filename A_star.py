from maze import maze

class Node():
    def __init__(self, state, action, parent) -> None:
        self.state = state # (x,y)
        self.action = action
        self.parent = parent


class Frontier():
    def __init__(self):
        self.frontier = []
    
    def add_nodes(self, nodes: list[Node]):
        self.frontier.extend(nodes)
    
    def remove_node(self, node):
        return self.frontier.remove(node)

    def empty(self):
        return self.frontier == []


class Maze():
    i = 0
    def __init__(self, file) -> None:
        self.file = file
        self.frontier = Frontier()
        self.walls = []
        with open(file) as maze_file:
            line_no = 0
            content = maze_file.readlines()
            self.height = len(content) - 1
            self.width = len(content[0]) - 1
        
        with open(file) as maze_file:
            for l in maze_file:
                for col, c in enumerate(l.strip('\n')):
                    if c == '#':
                        self.walls.append((col, line_no))
                    elif c == 'A':
                        self.start = (col, line_no)
                    elif c == 'B':
                        self.goal = (col, line_no)
                line_no += 1



    def heuristic(self, node: Node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1]))  # Manhattan Distance

    def plot(self, path, clear=False):
        maze(self.file, f'./images/maze/{Maze.i:06}', path, clear=clear)
        Maze.i += 1
    
    def possible_moves(self, state, explored, parent: Node):
        x, y = state
        all_moves = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ] 
        possible_moves = []

        for move in all_moves:
            if (move not in self.walls) and (move not in explored) and (0 <= move[0] <= self.width) and (0 <= move[1] <= self.height):
                act = (x - parent.state[0], y - parent.state[1])
                possible_moves.append(Node(move, act, parent))

        return possible_moves
    
    def get_current_path(self, current_node):
        path_to_goal = []
        this_node = current_node

        while this_node.parent != None:
            path_to_goal.append(this_node.state)
            this_node = this_node.parent

        return path_to_goal[::-1]

    def solve(self):
        explored = []
        current_node = Node(self.start, None, None)
        self.frontier.add_nodes([current_node])
        explored.append(current_node.state)

        while current_node.state != self.goal:
            self.plot(self.get_current_path(current_node))
            self.frontier.remove_node(current_node)
            self.frontier.add_nodes(self.possible_moves(current_node.state, explored, current_node))
            next_node = self.frontier.frontier[0]

            for node in self.frontier.frontier:
                if self.heuristic(node) < self.heuristic(next_node):
                    next_node = node

            explored.append(current_node.state)
            current_node = next_node
        
        return (self.get_current_path(current_node), explored)


mymaze = Maze('maze.txt')
path_to_goal, explored = mymaze.solve()
mymaze.plot(path_to_goal, clear=True)