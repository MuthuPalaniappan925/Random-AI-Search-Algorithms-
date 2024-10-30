from collections import deque, defaultdict
import heapq
import random
from typing import Dict, List, Set, Tuple, Optional

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = {}  # -> A* and  informed search algorithms
        self.weights = {}    # -> weighted edges

    def add_edge(self, u: str, v: str, weight: int = 1):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def set_heuristic(self, node: str, value: float):
        self.heuristic[node] = value

    def print_graph(self):
        print("Graph adjacency list:")
        for node, neighbors in self.graph.items():
            print(f"{node}: {', '.join(neighbors)}")

    def bfs(self, start: str, goal: str) -> List[str]:
        """Breadth-First Search"""
        queue = deque([[start]])
        visited = set([start])
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            print(f"Processing Node: {node}")
            print(f"Current Path: {path}")
            
            if node == goal:
                return path
                
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    print(f"Pushing Path: {new_path}")
        return []

    def british_museum_search(self, start: str, goal: str, max_iterations: int = 1000) -> List[str]:
        """British Museum Search (Random Walk)"""
        best_path = None
        best_length = float('inf')
        
        for _ in range(max_iterations):
            current = start
            path = [current]
            visited = {start}
            
            while current != goal and len(self.graph[current]) > 0:
                neighbors = [n for n in self.graph[current] if n not in visited]
                if not neighbors:
                    break
                    
                current = random.choice(neighbors)
                path.append(current)
                visited.add(current)
                
            if current == goal and len(path) < best_length:
                best_path = path
                best_length = len(path)
                
        return best_path if best_path else []

    def dfs(self, start: str, goal: str) -> List[str]:
        """Depth-First Search"""
        stack = [(start, [start])]
        print(stack)
        visited = set() ##Prevents Cycle
        
        while stack: ##Continues as long as nodes are there to explore
            node, path = stack.pop()
            print(f"Popped: {node}, Current Path: {path}")
            if node not in visited:
                if node == goal:
                    return path
                    
                visited.add(node)
                print(f"Visited: {node}")
                for neighbor in reversed(self.graph[node]): ##to control traversal order
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
                        print(f"Added to stack: {neighbor}, Path will be: {path + [neighbor]}")
        return []

    def hill_climbing(self, start: str, goal: str) -> List[str]:
        """Hill Climbing Search"""
        current = start
        path = [current]
        print(f"Starting search from: {current}")
        
        while current != goal:
            neighbors = self.graph[current]
            print(f"Current node: {current}")
            print(f"Neighbors: {neighbors}")
            if not neighbors:
                break
            next_node = min(neighbors, key=lambda x: self.heuristic.get(x, float('inf')))
            print(f"Selected next node: {next_node} with heuristic value: {self.heuristic.get(next_node, float('inf'))}")
            
            if self.heuristic.get(next_node, float('inf')) >= self.heuristic.get(current, float('inf')):
                print("Reached a local minimum, stopping search.")
                break
                
            current = next_node
            path.append(current)
            
        return path if path[-1] == goal else []

    ##solution space can be divided into branches(sub-problems) and bounds can 
    # be used to eliminate branches that cannot yield better solutions than the current best.
    def branch_and_bound(self, start: str, goal: str) -> List[str]:
        """Branch and Bound Search"""
        queue = [(0, start, [start])]  # (cost, node, path)
        visited = set()
        
        while queue:
            cost, node, path = heapq.heappop(queue) ##node with the lowest cost is extracted from the queue
            print(f"Total Cost: {cost}, Current Node: {node}, Current Path: {path}")
            
            if node == goal:
                return path
                
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + self.weights.get((node, neighbor), 1) ##each unvisited neighbor, the new cost to reach that neighbor is calculated.
                        heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
        return []

    def branch_and_bound_with_heuristic(self, start: str, goal: str) -> List[str]:
        """Branch and Bound with Heuristic Estimation"""
        queue = [(self.heuristic.get(start, 0), 0, start, [start])]  # (estimate, cost, node, path)
        visited = set()
        
        while queue:
            _, cost, node, path = heapq.heappop(queue)
            
            if node == goal:
                return path
                
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + self.weights.get((node, neighbor), 1)
                        estimate = new_cost + self.heuristic.get(neighbor, 0)
                        #print(f"  Processing Neighbor: '{neighbor}'")
                        #print(f"  New Cost to '{neighbor}': {new_cost}, Heuristic: {self.heuristic.get(neighbor, 0)}, Total Estimate: {estimate}")
                        heapq.heappush(queue, (estimate, new_cost, neighbor, path + [neighbor]))
        return []

    def oracle_search(self, start: str, goal: str) -> List[str]:
        """Oracle Search (Assumes perfect knowledge of shortest path)"""
        return self.a_star(start, goal, use_heuristic=False)


def main():
    
    g = Graph()
    
    ##add edges to tthe graph
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'G'), ('E', 'G'), ('F', 'G')
    ]
    
    for edge in edges:
        g.add_edge(*edge)
    
    ## heur will be "how far I am away from the goal"
    heuristics = {
        'A': 4, 'B': 3, 'C': 3,
        'D': 1, 'E': 1, 'F': 1,
        'G': 0
    }
    
    for node, value in heuristics.items():
        g.set_heuristic(node, value)
    
    g.print_graph()
    
    start, goal = 'A', 'G'
    algorithms = [
        #('BFS', g.bfs),
        #('British Museum', g.british_museum_search),
        #('DFS', g.dfs),
        ('Hill Climbing', g.hill_climbing),
        #('Branch & Bound', g.branch_and_bound),
        #('Oracle', g.oracle_search),
        #('Branch & Bound with Heuristic', g.branch_and_bound_with_heuristic),
        #('A*', g.a_star)
    ]
    
    
    for name, algo in algorithms:
        path = algo(start, goal)
        print(f"{name}: {' -> '.join(path)}")

if __name__ == "__main__":
    main()