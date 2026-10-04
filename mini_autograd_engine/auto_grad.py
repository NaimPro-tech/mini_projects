class Value:
    
    def __init__(self, data):
        self.data = data
        self.grad = 0
        self._prev = set()

    def __add__(self, other):
        out_data = self.data + other.data
        out = Value(out_data)
        out._prev = {self, other}

        return out

    def __mul__(self, other):
        out_data = self.data * other.data
        out = Value(out_data)
        out._prev = {self, other}

        return out

    def backward(self):
        self.grad = 1

        topo_list = []
        