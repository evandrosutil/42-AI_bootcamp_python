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
        elif isinstance(vector, list):
            self._values = vector
        elif isinstance(vector, tuple):
            values = list(map(float, list(range(vector[0], vector[1]))))
            self._values = values
        elif isinstance(vector, range):
            values = list(map(float, vector))
            self._values = values
        else:
            raise TypeError

    def __add__(self, element):
        try:
            if isinstance(element, Vector):
                if len(self.values) != len(element.values):
                    raise ValueError
                numbers = list(zip(self.values, element.values))
                vector_sum = [sum(elem) for elem in numbers]
                return Vector(vector_sum)
            return Vector([c + float(element) for c in self._values])
        except ValueError:
            print('Cannot add vectors with different sizes')
        except TypeError:
            print('Unsupported operand type for +: {type(element)}')

    def __radd__(self, element):
        return (element + self)

    def __sub__(self, element):
        try:
            if isinstance(element, Vector):
                if len(self.values) != len(element.values):
                    raise ValueError
                numbers = list(zip(self.values, element.values))
                vector_sub = [elem[0] - elem[1] for elem in numbers]
                return Vector(vector_sub)
            return Vector([c - float(element) for c in self._values])
        except ValueError:
            print(
                'Cannot perform substraction between vectors with '
                'different sizes')
        except TypeError:
            print('Unsupported operand type for -: {type(element)')

    def __rsub__(self, element):
        try:
            if isinstance(element, Vector):
                if len(self.values) != len(element.values):
                    raise ValueError
                numbers = list(zip(self.values, element.values))
                vector_rsub = [elem[1] - elem[0] for elem in numbers]
                return Vector(vector_rsub)
        except ValueError:
            print(
                'Cannot perform substraction between vectors with '
                'different sizes.')
        except TypeError:
            print('Unsupported operand type for -: {type(element)}')

    def __truediv__(self, element):
        if isinstance(element, Vector):
            if len(self.values) != len(element.values):
                raise ValueError
            numbers = list(zip(self.values, element.values))
            try:
                vector_div = [elem[0] - elem[1] for elem in numbers]
                return Vector(vector_div)
            except ZeroDivisionError:
                print('You cannot divide by zero!')
        return Vector([c / element for c in self.values])

    def __rtruediv__(self, element):
        if isinstance(element, Vector):
            if len(self.values) != len(element.values):
                raise ValueError
            numbers = list(zip(self.values, element.values))
            try:
                vector_div = [elem[1] - elem[0] for elem in numbers]
                return Vector(vector_div)
            except ZeroDivisionError:
                print('You cannot divide by zero!')
        return Vector([element / c for c in self.values])

    def __mul__(self, element):
        if isinstance(element, Vector):
            if len(self.values) != len(element.values):
                raise ValueError
            numbers = list(zip(self.values, element.values))
            vector_mul = [elem[0] + elem[1] for elem in numbers]
            return Vector(vector_mul)
        return Vector([c * element for c in self._values])

    def __rmul__(self, element):
        return (self * element)

    def __str__(self):
        return f"(Vector {self.values})"

    def __repr__(self):
        return f"{self.__class__} {self.__dict__}"
