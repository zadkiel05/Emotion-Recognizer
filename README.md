# Emotion-Recognizer
The facial expression recognition project will involve the usage of a Computer Vision, deep learning model and convolutional neural networks.
**Important Libraries:** pip install opencv-python, pip install face-emotion-recognition.

**Necessary Configuration:** ./site-package/torch/serialization.py

**Change:** [None --> 'cpu']

def load(f, map_location=None, pickle_module=pickle, **pickle_load_args): **TO**
def load(f, map_location='cpu', pickle_module=pickle, **pickle_load_args):



