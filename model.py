import sys
from PIL import Image

import torch
from torchvision import models
from torchvision import transforms
import json


class Model:
    def __init__(self):
        torch.hub.set_dir('.')
        self.model = models.googlenet(pretrained=True)
        self.model.eval()
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        with open('imagenet_class_index.json') as file:
            self.labels = json.load(file)

    def predict(self, image):
        input_tensor = self.preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = self.model(input_batch)

        return self.labels[str(torch.argmax(torch.nn.functional.softmax(output[0], dim=0)).item())][1]


if __name__ == '__main__':
    image = Image.open(sys.argv[1])
    model = Model()
    print(model.predict(image))
