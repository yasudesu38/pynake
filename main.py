import pyxel

TILE_SIZE = 8
TILE_NUM = 20
WINDOW_SIZE = TILE_SIZE*TILE_NUM

FLAME = 20

class SnakeHead:
    def __init__(self, x, y, direction, color):
        """

        :param x:
        :param y:
        :param direction: 蛇の向き 0:上 1:右 2:下 3:左
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.length = 3
        self.color = color
        self.body = None

    def update(self, key_input):
        if key_input != 0:
            self.direction = (self.direction + key_input) % 4

        self.body = SnakeBody(self.x, self.y, self.length, self.body, self.color)

        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        else:
            self.x -= 1

        if self.body:
            self.body.update()

    def draw(self):
        pyxel.rect(self.x*TILE_SIZE, self.y*TILE_SIZE, TILE_SIZE, TILE_SIZE, self.color)
        if self.body:
            self.body.draw()


class SnakeBody:
    def __init__(self, x, y, length, next_body, color):
        self.x = x
        self.y = y
        self.remain_time = length
        self.next_body = next_body
        self.color = color

    def update(self):
        self.remain_time -= 1

        if self.next_body:
            if self.next_body.remain_time < 0:
                self.next_body = None
            else:
                self.next_body.update()

    def draw(self):
        pyxel.rect(self.x*TILE_SIZE, self.y*TILE_SIZE, TILE_SIZE, TILE_SIZE, self.color)
        if self.next_body:
            self.next_body.draw()


class App:
    def __init__(self):
        pyxel.init(WINDOW_SIZE, WINDOW_SIZE)
        self.snake = SnakeHead(3, 0, 2, 5)
        self.step = 0
        self.key_left = 0
        self.key_right = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.key_left = 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.key_right = 1

        if self.step < FLAME:
            self.step += 1
        else:
            self.snake.update(self.key_right - self.key_left)
            self.step = 0
            self.key_left = 0
            self.key_right = 0


    def draw(self):
        pyxel.cls(0)
        self.snake.draw()

App()