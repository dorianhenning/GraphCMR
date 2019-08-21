import argparse


def arg_parse():
    """
    Parse arguments

    """

    parser = argparse.ArgumentParser(description="3D Graph CMR powered by YOLOv3")

    parser.add_argument("--images", dest="images", help=
                        "Image / Directory containing images to perform\
                        detection on",
                        default="data/test_imgs", type=str)

    parser.add_argument("--det", dest="det", help=
                        "Image / Directory to store detections to",
                        default="data/detections", type=str)

    parser.add_argument("--bs", dest="bs", help=
                        "Batch size", default=1)

    parser.add_argument("--confidence", dest="confidence", help=
                        "Object confidence to filter predictions", default=0.5)

    parser.add_argument("--nms_thresh", dest="nms_thresh", help=
                        "NMS threshold", default=0.4)

    parser.add_argument("--cfg", dest="cfg_file", help=
                        "Configuration file",
                        default="data/yolov3.cfg", type=str)

    parser.add_argument("--weights", dest="weights_file", help=
                        "Weights file from official YOLO website",
                        default="data/models/yolov3.weights", type=str)

    parser.add_argument("--reso", dest="input_resolution", help=
                        "Input resolution of the network. Increase to increase \
                        accuracy. Decrease to increase speed.",
                        default="416", type=str)

    parser.add_argument('--checkpoint', default=None, help=
                        'Path to pretrained checkpoint')

    parser.add_argument('--img', type=str, required=False, help=
                        'Path to input image')

    parser.add_argument('--outfile', type=str, default=None, help=
                        'Filename of output images. If not set use input \
                        filename.')

    return parser.parse_args()
