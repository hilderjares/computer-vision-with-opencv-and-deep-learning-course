import cv2
import numpy as np

image = np.zeros((500, 500, 3))


def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 100, (0, 255, 0), -1)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 100, (255, 255, 0), -1)


drawing = False
ix = -1
iy = -1


def draw_trinagle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)


cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_trinagle)

while True:
    cv2.imshow("drawing", image)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
