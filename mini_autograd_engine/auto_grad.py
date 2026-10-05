class Value:
    
    def __init__(self, data):
        self.data = data
        self.grad = 0.0
        self._prev = set()
        self._op = ''

    def __add__(self, other):
        out_data = self.data + other.data
        out = Value(out_data)
        out._prev = {self, other}
        out._op = "+"

        return out

    def __mul__(self, other):
        out_data = self.data * other.data
        out = Value(out_data)
        out._prev = {self, other}
        out._op = "*"

        return out

    def backward(self):
        self.grad = 1
        topo_list = []
        visited = set()

        #custom function
        def build_topo(node):
                if node in visited:
                    return
                visited.add(node)

                for neighbour in node._prev:
                    build_topo(neighbour)
                topo_list.insert(0, node)

        build_topo(self)

        #loop on topo_list and update gradient
        for node in topo_list:
            if node._op == "+":
                child = list(node._prev)
                if child:
                    child[0].grad += 1.0 * node.grad
                    if len(child)>1:
                        child[1].grad += 1.0 * node.grad
            elif node._op == "*":
                child = list(node._prev)
                if len(child) == 2:
                    child[0].grad += child[1].data * node.grad
                    child[1].grad += child[0].data * node.grad
            else:
                continue




if __name__ == "__main__":

    a = Value(2.0)
    b = Value(3.0)
    c = Value(4.0)
    d = Value(5.0)

    y = a * b + c + d
    y.backward()

    print(f"y.data (expected 15.0): {y.data}")
    print(f"a.grad (expected 3.0): {a.grad}")
    print(f"d.grad (expected): {d.grad}")
