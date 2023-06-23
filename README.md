# Emotion-Recognizer
The facial expression recognition project will involve the usage of a Computer Vision, deep learning model and convolutional neural networks.<br>
**Important Libraries:** pip install opencv-python, pip install face-emotion-recognition.<br>
**Necessary Configuration:** ./site-package/torch/serialization.py<br>
**Change:** [None --> 'cpu']<br>
def load(f, map_location=None, pickle_module=pickle, **pickle_load_args): <br> **TO**<br>
def load(f, map_location='cpu', pickle_module=pickle, **pickle_load_args):



