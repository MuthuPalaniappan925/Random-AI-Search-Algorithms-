class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.alpha = float('-inf')
        self.beta = float('inf')
        
    def add_child(self, child):
        self.children.append(child)
        
    def is_terminal(self):
        return len(self.children) == 0

def create_game_tree():
    root = Node(3)
    child1 = Node(5)
    child2 = Node(2)
    child3 = Node(9)
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    
    #L2 - C1
    child1.add_child(Node(1))
    child1.add_child(Node(7))
    child1.add_child(Node(4))
    
    #L2 - C2
    child2.add_child(Node(5))
    
    #L2 - C3
    child3.add_child(Node(2))
    child3.add_child(Node(8))
    child3.add_child(Node(3))
    
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Print the tree structure"""
    print("  " * level + prefix + str(node.value))
    for i, child in enumerate(node.children):
        print_tree(child, level + 1, f"Child {i+1}: ")

def minimax(node, depth, maximizing_player, moves=None):
    if moves is None:
        moves = []
    moves.append((node.value, depth, "MAX" if maximizing_player else "MIN"))
    
    ##BC
    if depth == 0 or node.is_terminal():
        return node.value, moves
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval, child_moves = minimax(child, depth - 1, False, moves)
            max_eval = max(max_eval, eval)
        return max_eval, moves
    else:
        min_eval = float('inf')
        for child in node.children:
            eval, child_moves = minimax(child, depth - 1, True, moves)
            min_eval = min(min_eval, eval)
        return min_eval, moves

def alpha_beta(node, depth, alpha, beta, maximizing_player, moves=None):
    if moves is None:
        moves = []
    moves.append((node.value, depth, "MAX" if maximizing_player else "MIN", alpha, beta))
    
    ##BC
    if depth == 0 or node.is_terminal():
        return node.value, moves
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval, child_moves = alpha_beta(child, depth - 1, alpha, beta, False, moves)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                moves.append(("Pruned", depth, "MAX", alpha, beta))
                break
        return max_eval, moves
    else:
        min_eval = float('inf')
        for child in node.children:
            eval, child_moves = alpha_beta(child, depth - 1, alpha, beta, True, moves)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                moves.append(("Pruned", depth, "MIN", alpha, beta))
                break
        return min_eval, moves

def visualize_moves(moves, algorithm_name):
    print(f"\n{algorithm_name} Algorithm Traversal:")
    print("=" * 50)
    print("Format: (Node Value, Depth, Player Type, Alpha, Beta)")
    print("-" * 50)
    
    for move in moves:
        if len(move) == 3:
            value, depth, player = move
            print(f"Depth {depth}: {player} evaluates node {value}")
        else:
            value, depth, player, alpha, beta = move
            if value == "Pruned":
                print(f"Depth {depth}: {player} pruned branch (α={alpha}, β={beta})")
            else:
                print(f"Depth {depth}: {player} evaluates node {value} (α={alpha}, β={beta})")

if __name__ == "__main__":
    root = create_game_tree()
    print("Game Tree Structure:")
    print_tree(root)
    
    ##MM
    print("\nRunning Minimax...")
    minimax_value, minimax_moves = minimax(root, 3, True)
    visualize_moves(minimax_moves, "Minimax")
    print(f"Minimax Final Value: {minimax_value}")
    
    ##ABR Run
    print("\nRunning Alpha-Beta Pruning...")
    alpha_beta_value, alpha_beta_moves = alpha_beta(root, 3, float('-inf'), float('inf'), True)
    visualize_moves(alpha_beta_moves, "Alpha-Beta")
    print(f"Alpha-Beta Final Value: {alpha_beta_value}")