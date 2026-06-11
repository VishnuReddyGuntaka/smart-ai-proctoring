import cv2
import numpy as np


def detectObject(cnn_model, cnn_layer_names, frame_height, frame_width, frame, label_colors, class_labels):
    """
    Detect objects in a video frame using YOLO CNN model.
    Returns processed frame with bounding boxes and detection details.
    """
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    cnn_model.setInput(blob)
    layer_outputs = cnn_model.forward(cnn_layer_names)

    Boundingboxes = []
    confidence_value = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                box = detection[0:4] * np.array([frame_width, frame_height, frame_width, frame_height])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                Boundingboxes.append([x, y, int(width), int(height)])
                confidence_value.append(float(confidence))
                class_ids.append(class_id)

    # Non-maxima suppression to remove duplicate boxes
    ids = cv2.dnn.NMSBoxes(Boundingboxes, confidence_value, 0.5, 0.3)

    frames = frame.copy()
    cls = []

    if len(ids) > 0:
        for i in ids.flatten():
            (x, y) = (Boundingboxes[i][0], Boundingboxes[i][1])
            (w, h) = (Boundingboxes[i][2], Boundingboxes[i][3])

            cv2.rectangle(frames, (x, y), (x + w, y + h), label_colors, 2)

            label = class_labels[class_ids[i]] if class_ids[i] < len(class_labels) else "Unknown"
            conf_text = "{}: {:.4f}".format(label, confidence_value[i])
            cv2.putText(frames, conf_text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_colors, 2)
            cls.append(label)

    return frames, cls, Boundingboxes, confidence_value, class_ids, ids


def displayImage(title, image):
    """Display an image in a named window."""
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
