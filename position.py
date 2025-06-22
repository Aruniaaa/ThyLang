

class Position:
    def __init__(self, index, line, column, file_name, file_text):
        self.file_name = file_name
        self.file_text = file_text
        self.line = line
        self.index = index
        self.column = column

    def advance(self, current_char=None):
        self.index += 1
        self.column +=1

        if current_char == "\n":
            self.line += 1
            self.column = 0

        return self


    def copy(self):
        return Position(self.index, self.line, self.column, self.file_name, self.file_text)
