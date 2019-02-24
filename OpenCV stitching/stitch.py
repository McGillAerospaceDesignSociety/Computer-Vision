import ocv, os.path as osp

current_path = osp.abspath(osp.realpath("."))
image_path = osp.join(current_path, r"To be Processed")

cv = ocv.OCV(src_file_path=image_path)
cv.stitch_images()
cv.disp_images()