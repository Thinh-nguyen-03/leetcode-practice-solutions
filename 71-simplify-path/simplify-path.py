class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        directories = path.split('/')
        
        for directory in directories:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

            print(stack)
        
        return '/' + '/'.join(stack)
