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
