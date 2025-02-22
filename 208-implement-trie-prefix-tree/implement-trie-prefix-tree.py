class TrieNode:
    
    def __init__(self):
        
        # Initialize a dictionary to store children nodes
        self.children = {}
        
        # Boolean flag to mark the end of a word
        self.isEndOfWord = False

class Trie:
    
    def __init__(self):
        
        # Initialize the root of the Trie
        self.root = TrieNode()

    def insert(self, word):
        
        # Start from the root node
        currentNode = self.root
        
        # Traverse each character in the word
        for char in word:
            
            # If the character is not in the children, add a new TrieNode
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            
            # Move to the child node
            currentNode = currentNode.children[char]
        
        # Mark the end of the word
        currentNode.isEndOfWord = True

    def search(self, word):
        
        # Start from the root node
        currentNode = self.root
        
        # Traverse each character in the word
        for char in word:
            
            # If the character is not found, return False
            if char not in currentNode.children:
                return False
            
            # Move to the child node
            currentNode = currentNode.children[char]
        
        # Return True if the current node marks the end of a word
        return currentNode.isEndOfWord

    def startsWith(self, prefix):
        
        # Start from the root node
        currentNode = self.root
        
        # Traverse each character in the prefix
        for char in prefix:
            
            # If the character is not found, return False
            if char not in currentNode.children:
                return False
            
            # Move to the child node
            currentNode = currentNode.children[char]
        
        # Return True if all characters in the prefix are found
        return True