class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        print('graph init')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        print('Button init')
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False

    def toggle(self):
        self.status = not self.status


class SquareButton(Button):
    def __init__(self, pos_x, pos_y, size):
        print('SquareButton init')
        super().__init__(pos_x, pos_y, size, size)

b = SquareButton(10, 20, 200)
print(b.pos_x,b.pos_y, b.size_x, b.size_y)