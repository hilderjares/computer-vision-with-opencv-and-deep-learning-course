import cv2

image = cv2.imread('data/0000-horse.jpg')

while True:
    cv2.imshow('Horse', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
