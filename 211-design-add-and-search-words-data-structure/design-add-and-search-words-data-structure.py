class TrieNode:
    
    def __init__(self):
        # Initialize children as an empty dictionary
        self.children = {}
        
        # Boolean flag to mark the end of a word
        self.isEndOfWord = False

class WordDictionary:
    
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()

    def addWord(self, word):
        # Start from the root node
        currentNode = self.root
        
        # Iterate over each character in the word
        for char in word:
            
            # If the character is not in the current node's children, add it
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            
            # Move to the child node
            currentNode = currentNode.children[char]
        
        # Mark the end of the word
        currentNode.isEndOfWord = True

    def search(self, word):
        
        # Define a recursive DFS function
        def dfs(index, node):
            
            # If we reach the end of the word
            if index == len(word):
                return node.isEndOfWord
            
            # Get the current character
            char = word[index]
            
            # If the character is a '.', check all possible nodes at this level
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            
            # If the character is in the children, continue the search
            if char in node.children:
                return dfs(index + 1, node.children[char])
            
            # If the character is not found, return False
            return False
        
        # Start DFS from the root node
        return dfs(0, self.root)