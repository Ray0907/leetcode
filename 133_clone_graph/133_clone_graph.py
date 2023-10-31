# Definition for a Node.
class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Use a dictionary to map nodes from the original graph to nodes in the new graph
        node_map = {}
        
        def dfs(old_node):
            # If this node has already been cloned, return the corresponding new node
            if old_node in node_map:
                return node_map[old_node]
            
            # Create a new node and set its value to the value of the original node
            new_node = Node(old_node.val)
            
            # Store the new node in the dictionary
            node_map[old_node] = new_node
            
            # Process the neighbors of the original node
            for neighbor in old_node.neighbors:
                # Recursively process each neighbor and add them to the new node's neighbors list
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            
            return new_node
        
        # Start the depth-first search from the initial node
        return dfs(node)
