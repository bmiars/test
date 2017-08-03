class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        return '-'.join(['dot' if param == '.' else 'dash' for param in self.pattern])
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
        