"""
Programing Language Class

"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        '''Store flied from table.'''
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """returns no parameters other than self"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)