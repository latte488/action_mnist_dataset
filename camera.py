import numpy as np

class Camera:

    def __init__(self, frame_size):
        self.frame_size = frame_size
        self.reset()
    
    def reset(self):
        self.frame = np.zeros(self.frame_size, dtype=np.uint8)

    def rendering(self, sprite):
        self.reset()
        top = sprite.y
        bottom = sprite.y + sprite.height
        left = sprite.x
        right = sprite.x + sprite.width
        self.frame[top:bottom, left:right] = sprite.image
        return self.frame
