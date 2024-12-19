import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.04)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.08)
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = - self.change_y
        if self.bottom < 0:
            self.change_y = - self.change_y


class Game(arcade.Window): # Представление главного окна
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 1.7
        self.ball.center_y = SCREEN_HEIGHT / 2.8


    def on_draw(self): # метод позволяет поменять цвет экрана
        self.clear((255, 255, 255)) # очистка экрана и установка белого фона
        self.bar.draw() # рисуем ракетку
        self.ball.draw() # рисуем мяч

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = - self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        # движение ракетки при нажатии кнопок <право> - <влево>
        if  key == arcade.key.RIGHT:
            self.bar.change_x = 4

        if  key == arcade.key.LEFT:
            self.bar.change_x = -4

    def on_key_release(self, key, modifiers):
        # Остановка ракетки при отпускании кнопок
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()