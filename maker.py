from torchvision import datasets
import os
import shutil
import numpy as np
import cv2
import sprite
import camera
from tqdm import tqdm
import toml

def make(root, dataset, actions):
    frame_number = 20
    frame_size = (64, 64)
    fps = 60
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    if os.path.exists(root):
        shutil.rmtree(root)
        os.makedirs(root)
    else:
        os.makedirs(root)
    label_dict = { 'Action label' : {}, 'Video label' : {} }
    camera_ = camera.Camera(frame_size)
    for action_label, action_class in enumerate(actions):
        action = action_class(sprite.Sprite(np.zeros((1, 1))))
        action_name = action.__class__.__name__
        label_dict['Action label'][action_name] = action_label
    video_i = 0
    total = len(dataset) * len(actions)
    progress = tqdm(total=total, desc='Converting')
    for image, label in dataset:
        image = np.array(image, dtype=np.uint8)
        sprite_ = sprite.Sprite(image)
        for action_label, action_class in enumerate(actions):
            action = action_class(sprite_)
            action_name = action.__class__.__name__
            video_i += 1
            
            video_name = f'{video_i}.mp4'
            video_path = f'{root}/{video_name}'
            writer = cv2.VideoWriter(video_path, fmt, fps, frame_size, False)
            action.start(frame_number, frame_size[1], frame_size[0])
            for _ in range(frame_number):
                action.update()
                writer.write(camera_.rendering(sprite_))
            writer.release()
            label_dict['Video label'][video_name] = action_name
            progress.update(1)
    with open(f'{root}/0.toml', mode='w') as f:
        toml.dump(label_dict, f)


if __name__ == '__main__':
    root = 'action_mnist'
    if not os.path.exists(root):
        os.makedirs(root)
    actions = [
        sprite.MoveUp,
        sprite.MoveDown,
        sprite.MoveLeft,
        sprite.MoveRight,
        sprite.MoveUpLeft,
        sprite.MoveUpRight,
        sprite.MoveDownLeft,
        sprite.MoveDownRight,
    ]
    train_root = f'{root}/train'
    train_dataset = datasets.MNIST(root=root, train=True, download=True)
    make(train_root, train_dataset, actions)
    test_root = f'{root}/test'
    test_dataset = datasets.MNIST(root=root, train=False, download=True)
    make(test_root, test_dataset, actions)
    
    
