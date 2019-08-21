from __future__ import division
from __future__ import print_function

import torch
from torchvision.transforms import Normalize
import numpy as np
import cv2
import json

from yolov3 import Darknet

from utils import Mesh
from models import GraphCNN
from opt import arg_parse


if __name__ == "__main___":
    args = arg_parse()

    num_layers = 5
    num_channels = 256

    mesh = Mesh()
    graph_cnn = GraphCNN(mesh.adjmat, mesh.ref_vertices.t(),
                         num_layers, num_channels)

    print("Loading network...")
    detection_net = Darknet('data/yolov3.cfg')
    print("Loading pretrained weights...")
    detection_net.load_weights('data/models/yolov3.weights')
    print("Network successfully loaded!")
