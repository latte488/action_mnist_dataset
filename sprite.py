import random

class Sprite:

    def __init__(self, image):
        self.image = image
        self.width, self.height = image.shape
        self.x = 0
        self.y = 0

class Action:

    def __init__(self, sprite):
        self.sprite = sprite

    @property
    def width(self):
        return self.sprite.width

    @property
    def height(self):
        return self.sprite.height

    @property
    def x(self):
        return self.sprite.x

    @x.setter
    def x(self, value):
        self.sprite.x = value

    @property
    def y(self):
        return self.sprite.y

    @y.setter
    def y(self, value):
        self.sprite.y = value

    def x_random_reset(self, frame_number, frame_width):
        self.x = random.randint(0, frame_width - self.width - 1)

    def y_random_reset(self, frame_number, frame_height):
        self.y = random.randint(0, frame_height - self.height - 1)

    def start(self, frame_number, frame_width, frame_height):
        self.x_random_reset(frame_number, frame_width)
        self.y_random_reset(frame_number, frame_height)

    def update(self):
        raise NotImplementedError

class MoveUp(Action):
    
    def __init__(self, sprite):
        super(MoveUp, self).__init__(sprite)

    def y_random_reset(self, frame_number, frame_height):
        self.y = random.randint(frame_number, frame_height - self.height - 1)

    def update(self):
        self.y -= 1

class MoveDown(Action):

    def __init__(self, sprite):
        super(MoveDown, self).__init__(sprite)

    def y_random_reset(self, frame_number, frame_height):
        self.y = random.randint(0, frame_height - self.height - frame_number - 1)

    def update(self):
        self.y += 1

class MoveLeft(Action):

    def __init__(self, sprite):
        super(MoveLeft, self).__init__(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.x = random.randint(frame_number, frame_width - self.width - 1)

    def update(self):
        self.x -= 1

class MoveRight(Action):

    def __init__(self, sprite):
        super(MoveRight, self).__init__(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.x = random.randint(0, frame_width - self.width - frame_number - 1)

    def update(self):
        self.x += 1

class MoveUpLeft(Action):

    def __init__(self, sprite):
        super(MoveUpLeft, self).__init__(sprite)
        self.move_up = MoveUp(sprite)
        self.move_left = MoveLeft(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.move_left.x_random_reset(frame_number, frame_width)

    def y_random_reset(self, frame_number, frame_height):
        self.move_up.y_random_reset(frame_number, frame_height)

    def update(self):
        self.move_up.update()
        self.move_left.update()

class MoveUpRight(Action):

    def __init__(self, sprite):
        super(MoveUpRight, self).__init__(sprite)
        self.move_up = MoveUp(sprite)
        self.move_right = MoveRight(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.move_right.x_random_reset(frame_number, frame_width)

    def y_random_reset(self, frame_number, frame_height):
        self.move_up.y_random_reset(frame_number, frame_height)

    def update(self):
        self.move_up.update()
        self.move_right.update()


class MoveDownLeft(Action):

    def __init__(self, sprite):
        super(MoveDownLeft, self).__init__(sprite)
        self.move_down = MoveDown(sprite)
        self.move_left = MoveLeft(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.move_left.x_random_reset(frame_number, frame_width)

    def y_random_reset(self, frame_number, frame_height):
        self.move_down.y_random_reset(frame_number, frame_height)

    def update(self):
        self.move_down.update()
        self.move_left.update()

class MoveDownRight(Action):

    def __init__(self, sprite):
        super(MoveDownRight, self).__init__(sprite)
        self.move_down = MoveDown(sprite)
        self.move_right = MoveRight(sprite)

    def x_random_reset(self, frame_number, frame_width):
        self.move_right.x_random_reset(frame_number, frame_width)

    def y_random_reset(self, frame_number, frame_height):
        self.move_down.y_random_reset(frame_number, frame_height)

    def update(self):
        self.move_down.update()
        self.move_right.update()
