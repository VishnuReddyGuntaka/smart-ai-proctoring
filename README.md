# Smart AI Based Online Proctoring System

An AI-powered online exam proctoring system that detects 
cheating in real-time using Computer Vision and Deep Learning.

## Features
- Real-time face detection
- Emotion detection (Happy, Sad, Angry, etc.)
- Head pose tracking (Left/Right)
- Mobile phone & book detection
- CNN model with 97% accuracy

## Technologies Used
- Python
- OpenCV
- TensorFlow & Keras
- YOLO (Darknet)
- Tkinter

## How to Run

1. Clone the repo
2. Download model files (see below)
3. Place model files in `model/` folder
4. Run `run.bat`

## Required Model Files
| File | Download From |
|------|--------------|
| model.cfg | YOLO Darknet |
| model.weights | YOLO Darknet |
| modellabels | Create manually |
| haarcascade_frontalface_default.xml | OpenCV GitHub |

## Author
G. Vishnu Vardhan Reddy 
P.B. Siddhartha College, Vijayawada
# Model Files

Place the following files in this folder:

| File | Source |
|---|---|
| `model.cfg` | YOLO config — download from darknet |
| `model.weights` | YOLO weights — download separately (large file) |
| `modellabels` | Text file with one label per line (person, cell phone, book...) |
| `haarcascade_frontalface_default.xml` | Download from OpenCV GitHub |
| `X.txt.npy` | Training feature data |
| `Y.txt.npy` | Training label data |

## Download Links

- Haar Cascade: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
- YOLO Darknet: https://pjreddie.com/darknet/yolo/

## modellabels format (example)

```
person
bicycle
car
...
cell phone
book
```
