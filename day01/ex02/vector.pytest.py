class Vector():

    def __init__(self, vector):
        self.values = vector
        self.size = len(self.values)

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, vector):
        if isinstance(vector, int):
            values = list(map(float, list(range(vector))))
            self._values = values
        if isinstance(vector, list):
            self._values = vector
        if isinstance(vector, tuple):
            values = list(map(float, list(range(vector[0],vector[1]))))
            self._values = values
        if isinstance(vector, range):
            values = list(map(float, vector))
            self._values = values

    def __add__(self, value):
        self._values = [c + value for c in self._values]

        return self

    def __rad__(self, value):
        pass

    def __sub__(self, value):

        self._values = [c - value for c in self._values]

        return self

    def __rsub__(self, value):
        pass

    def __truediv__(self, value):
        self._values = [c / value for c in self.values]

        return self

    def __rtruediv__(self, value):
        pass

    def __mul__(self, value):
        self._values = [c * value for c in self._values]

        return self

    def __rmul__(self, value):
        pass

    def __str__(self):
        return f"(Vector {self.values})"

    def __repr__(self):
        return '%s (%r)' % (self.__class__, self.__dict__)
        #return f"{self.__class__} {self.__dict__[_values]}" 

