from imutils import paths
import numpy as np
import imutils
import cv2

class OCV:

    def __init__(self, src_file_path, out_file_path=None):

        if not src_file_path:
            raise KeyError("Need to pass in a image source")

        self.src_file_path = src_file_path
        self.out_file_path = out_file_path

        self.flags = {}
        self.flags["image_loaded"] = False
        self.flags["image_stitched"] = False
        self.flags["image_reshaped"] = False
        self.flags["operation_success"] = False

        self.images = []

        imageList = sorted(list(paths.list_images(self.src_file_path)))
        for imagePath in imageList:
            image = cv2.imread(imagePath)
            # resize here for fast process
           # image = imutils.resize(image, width=640, height=480)
            self.images.append(image)

        self.flags["image_loaded"] = True

    def stitch_images(self):
        if self.flags["image_loaded"]:
            # call the cv2 stitcher class and use
            stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
            (status, self.stitched) = stitcher.stitch(self.images)
        
        if status == 0:
            self.flags["image_stitched"] = True

    def disp_images(self):
        # another resize here?
        frame = cv2.resize(self.stitched,(960,520))
        cv2.imshow("Stitched", frame)
        cv2.imwrite('stitched.png', frame)
        cv2.waitKey(0)
    

