import numpy as np
from collections import deque
import heapq


class GridWorld:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.height, self.width = self.grid.shape
        # Find start (П) and finish (Ф) positions
        self.start = tuple(np.argwhere(self.grid == 'П')[0])
        self.finish = tuple(np.argwhere(self.grid == 'Ф')[0])

    def get_neighbors(self, pos):
        """Get valid neighboring positions"""
        y, x = pos
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []

        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if (0 <= new_y < self.height and
                0 <= new_x < self.width and
                    self.grid[new_y, new_x] != '∞'):
                neighbors.append((new_y, new_x))
        return neighbors

    def breadth_first_search(self):
        """Implement all-directional (breadth-first) search"""
        # Initialize cost matrix A
        A = np.full(self.grid.shape, self.width * self.height, dtype=int)
        A[self.start] = 0

        # Initialize queue with start position
        queue = deque([self.start])
        visited = {self.start}

        while queue:
            current = queue.popleft()

            if current == self.finish:
                break

            for next_pos in self.get_neighbors(current):
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append(next_pos)
                    A[next_pos] = A[current] + 1

        return A

    def construct_path(self, came_from):
        """Construct path using directional markers based on came_from dictionary."""
        path_grid = np.full(self.grid.shape, ' ', dtype=str)
        current = self.finish

        # Mapping of movement directions for each possible move
        directions = {
            (0, 1): '<',    # left
            (1, 0): '^',    # up
            (0, -1): '>',   # right
            (-1, 0): 'v'    # down
        }

        # Trace back from the finish to the start, marking the path
        while current != self.start:
            prev = came_from.get(current)
            if not prev:  # No path found
                return path_grid

            # Determine the direction from previous cell to current
            dy, dx = current[0] - prev[0], current[1] - prev[1]
            direction = directions[(dy, dx)]
            path_grid[current] = direction

            current = prev

        return path_grid

    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance heuristic"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def a_star_search(self):
        """Implement A* algorithm"""
        # Initialize cost matrices
        G = np.full(self.grid.shape, float('inf'))
        G[self.start] = 0

        # Priority queue for A*: (f_score, position)
        open_set = [(self.manhattan_distance(
            self.start, self.finish), self.start)]
        heapq.heapify(open_set)

        # Keep track of visited nodes and their parents
        closed_set = set()
        came_from = {}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.finish:
                break

            if current in closed_set:
                continue

            closed_set.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue

                tentative_g = G[current] + 1

                if tentative_g < G[neighbor]:
                    came_from[neighbor] = current
                    G[neighbor] = tentative_g
                    f_score = tentative_g + \
                        self.manhattan_distance(neighbor, self.finish)
                    heapq.heappush(open_set, (f_score, neighbor))

        return G, came_from

# Example usage


def create_example_grid():
    grid = [
        ['П', '∞', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '∞', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '∞', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '∞', ' ', ' ', '∞', ' ', '∞', '∞', ' ', ' '],
        [' ', ' ', ' ', ' ', '∞', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '∞', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '∞', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '∞', ' ', ' ', ' ', ' ', 'Ф']
    ]
    return grid


# Create world and run algorithms
world = GridWorld(create_example_grid())

# Run BFS
print("Running Breadth-First Search...")
A = world.breadth_first_search()
print("\nCost matrix A:")
print(A)

# Create world and run A*
world = GridWorld(create_example_grid())
G, came_from = world.a_star_search()
print("\nCost matrix G:")
print(G)

# Construct path using the came_from dictionary from A*
path_grid = world.construct_path(came_from)
print("\nPath with directional markers:")
print(path_grid)

# Compare effectiveness
bfs_explored = np.count_nonzero(A < world.width * world.height)
astar_explored = len(came_from) + 1

print("\nComparison:")
print(f"BFS explored {bfs_explored} cells")
print(f"A* explored {astar_explored} cells")
