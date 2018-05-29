import cv2
import os
import argparse
import sys

def crop_video(path, x_start, y_start, x_end, y_end):
    fps = int(round((cv2.VideoCapture(path)).get(cv2.CAP_PROP_FPS)))
    os.rename(path, 'old_res_' + path)
    out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (x_end-x_start, y_end-y_start))

    path = 'old_res_' + path
    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        sucess, frame = cap.read()
        if sucess == False:
            break
    
        print("(%d:%d), (%d:%d)" % (y_start, y_end, x_start, x_end))
        crop = frame[y_start:y_end, x_start: x_end]
        cv2.imshow('frame2', crop)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        out.write(crop)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

argp = argparse.ArgumentParser(description='Crop a video')
argp.add_argument("-path", dest='path', type=str, nargs=1, required=True,
                 help='Usage: -path <path_to_video>')
argp.add_argument("-start_point", dest='start_p', type=int, nargs=2, 
                 required=True, help='Usage: -start_point <x_start> <y_start>')
argp.add_argument("-end_point", dest='end_p', type=int, nargs=2, required=True,
                 help='Usage: -end_point <x_end> <y_end>')

print("***********************************************")
print("* Take care with (x, y) format for your video *")
print("***********************************************")
try:
    args = argp.parse_args()
except:
    argp.print_help(sys.stderr)
    exit(1)

crop_video(args.path[0], args.start_p[0], args.start_p[1], args.end_p[0], 
           args.end_p[1])
