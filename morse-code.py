class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        morse = ""
        for i in pattern:
            if len(pattern)-1 == pattern.index(i)
                if i == ".":
                    morse += "dot"
                elif i == "-":
                    morse += "dash"
        else:
            if len(pattern)-1 == pattern.index(i)
                if i == ".":
                    morse += "dot-"
                elif i == "-":
                    morse += "dash-"
        return morse
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)