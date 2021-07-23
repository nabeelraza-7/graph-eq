import numpy as np
import cv2 as cv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
class_names = ['(',')','+','-','0','1','2','3','4','5','6','7','8','9','x','*','^','/']

model = tf.keras.models.load_model("./multiclass_verification_model")
# print(model.summary())
class Rect:
    def __init__(self, t):
        self.x = t[0]
        self.y = t[1]
        self.w = t[2]
        self.h = t[3]

    def checkIntersection(self, B):
        if (self.x <= B.x and self.y <= B.y) and (self.w >= B.w and self.h >= B.h):
            return True
        return False

def remove_some(temp):
    i = 0
    while i < len(temp):
        A = Rect(temp[i])
        j = i+1
        while j < len(temp):
            if A.checkIntersection(Rect(temp[j])):
                temp.remove(temp[j])
            j += 1
        i += 1

def remove_duplicates(lst):
    result = []
    for i in lst:
        if i in result:
            continue
        else:
            result.append(i)
    return result

def predict_ex():
    img = cv.imread("media/image.jpeg")
    src_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    src_gray = cv.blur(src_gray, (3, 3))
    thresh = 127
    canny_output = cv.Canny(src_gray,thresh, thresh*2)
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        boundRect[i] = cv.boundingRect(c)
    boundRect = remove_duplicates(boundRect)
    remove_some(boundRect)
    boundRect = sorted(boundRect)
    white = (255,255,255)
    text = ""
    for i in range(len(boundRect)):
        x = boundRect[i][0] - 5
        y = boundRect[i][1] - 5
        w = boundRect[i][2] + 5*2
        h = boundRect[i][3] + 5*2
        part = img[y:y+h, x:x+w]
        if w > h:
            ww = w
            hh = w
        else:
            ww = h
            hh = h
        ht, wd, cc = part.shape
        result = np.full((hh,ww, cc), white, dtype=np.uint8)
        xx = (ww - wd) // 2
        yy = (hh - ht) // 2
        result[yy:yy+ht, xx:xx+wd] = part
        result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
        n_result = cv.resize(result, (45, 45))
        part = tf.reshape(n_result, [1, 45, 45, 1])
        prediction = model.predict(part)
        text += class_names[prediction.argmax()]
    return text

if __name__ == "__main__":
    print(predict_ex("test_new.jpeg"))