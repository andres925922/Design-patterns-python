class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        response = ['class %s:' % self.name]
        if not self.fields:
            response.append('  pass')
        else:
            response.append('  def __init__(self):')
            for f in self.fields:
                response.append('    %s' % f)
        return '\n'.join(response)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()