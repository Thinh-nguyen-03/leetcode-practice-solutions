class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)